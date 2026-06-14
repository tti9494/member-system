import os
import secrets
import base64
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path
from dotenv import load_dotenv
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

load_dotenv(dotenv_path=str(Path.home() / "member-system" / ".env"))

import sys
sys.path.insert(0, str(Path.home() / "member-system"))
from db import get_conn

CODE_MAX_FAIL = int(os.getenv("CODE_MAX_FAIL", "5"))
CODE_LOCK_HOURS = int(os.getenv("CODE_LOCK_HOURS", "24"))
CODE_PREFIX = os.getenv("CODE_PREFIX", "").strip().upper()
CODE_RANDOM_LENGTH = int(os.getenv("CODE_RANDOM_LENGTH", "8"))
CODE_ALPHABET = os.getenv("CODE_ALPHABET", "0123456789")
CODE_LEDGER_PATH = Path(
    os.getenv(
        "CODE_LEDGER_PATH",
        str(Path.home() / "member-system" / "private" / "code_ledger.jsonl"),
    )
)


def _get_key() -> bytes:
    raw = os.getenv("CODE_SECRET_KEY", "")
    key = raw.encode("utf-8")
    return (key + b"\x00" * 32)[:32]


def _encrypt_code(code: str) -> str:
    key = _get_key()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    enc = cipher.encryptor()
    data = code.encode("utf-8")
    pad_len = 16 - (len(data) % 16)
    data += bytes([pad_len] * pad_len)
    ct = enc.update(data) + enc.finalize()
    return base64.b64encode(iv + ct).decode("utf-8")


def _decrypt_code(encrypted: str) -> str:
    key = _get_key()
    raw = base64.b64decode(encrypted)
    iv, ct = raw[:16], raw[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    dec = cipher.decryptor()
    data = dec.update(ct) + dec.finalize()
    pad_len = data[-1]
    return data[:-pad_len].decode("utf-8")


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _generate_invite_code() -> str:
    alphabet = CODE_ALPHABET or "0123456789"
    body = "".join(secrets.choice(alphabet) for _ in range(CODE_RANDOM_LENGTH))
    return f"{CODE_PREFIX}-{body}" if CODE_PREFIX else body


def _canonical_code(code: str) -> str:
    return "".join(ch for ch in (code or "").upper() if ch.isalnum())


def _code_hint(code: str) -> str:
    canonical = _canonical_code(code)
    return f"***{canonical[-4:]}" if canonical else ""


def _ledger_path() -> Path:
    return CODE_LEDGER_PATH


def _write_ledger(event: dict) -> None:
    path = _ledger_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        path.parent.chmod(0o700)
    except OSError:
        pass
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
    try:
        path.chmod(0o600)
    except OSError:
        pass


def _ledger_events(member_id: str) -> list[dict]:
    path = _ledger_path()
    if not path.exists():
        return []
    events: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if event.get("member_id") == member_id:
                events.append(event)
    return events


def _latest_ledger_code(member_id: str) -> dict | None:
    active: dict | None = None
    for event in _ledger_events(member_id):
        action = event.get("action")
        if action == "code_issued" and event.get("encrypted_code"):
            active = event
        elif action == "code_revoked":
            active = None
    if not active:
        return None
    try:
        code = _decrypt_code(active["encrypted_code"])
    except Exception:
        return None
    return {
        "code": code,
        "issued_at": active.get("created_at"),
        "expires_at": None,
        "source": "ledger",
    }


def _record_issue(member_id: str, code: str, issued_at: str, encrypted: str) -> None:
    _write_ledger(
        {
            "action": "code_issued",
            "member_id": member_id,
            "created_at": issued_at,
            "encrypted_code": encrypted,
            "code_hint": _code_hint(code),
            "expires_at": None,
            "source": "member-system",
        }
    )


def _record_revoke(member_id: str, reason: str = "manual") -> None:
    _write_ledger(
        {
            "action": "code_revoked",
            "member_id": member_id,
            "created_at": _now().isoformat(),
            "reason": reason,
            "source": "member-system",
        }
    )


def generate_code(member_id: str) -> str:
    code = _generate_invite_code()
    encrypted = _encrypt_code(code)
    issued_at = _now().isoformat()

    conn = get_conn()
    conn.execute(
        "UPDATE members SET access_code=?, code_expires_at=?, code_issued_at=?, code_fail_count=0, code_locked_until=NULL WHERE id=?",
        (encrypted, None, issued_at, member_id)
    )
    conn.commit()
    conn.close()
    _record_issue(member_id, code, issued_at, encrypted)
    return code


def get_current_code(member_id: str) -> dict:
    conn = get_conn()
    row = conn.execute(
        "SELECT access_code, code_issued_at FROM members WHERE id=?", (member_id,)
    ).fetchone()
    conn.close()

    if row and row["access_code"]:
        return {
            "ok": True,
            "code": _decrypt_code(row["access_code"]),
            "issued_at": row["code_issued_at"],
            "expires_at": None,
            "source": "members",
        }

    ledger = _latest_ledger_code(member_id)
    if ledger:
        return {"ok": True, **ledger}
    return {"ok": False, "error": "발급된 코드가 없습니다."}


def check_lock(member_id: str) -> dict:
    conn = get_conn()
    row = conn.execute(
        "SELECT code_locked_until, code_fail_count FROM members WHERE id=?", (member_id,)
    ).fetchone()
    conn.close()
    if not row:
        return {"locked": False}
    locked_until = row["code_locked_until"]
    if locked_until:
        locked_dt = datetime.fromisoformat(locked_until)
        if _now() < locked_dt:
            return {"locked": True, "until": locked_until}
    return {"locked": False, "fail_count": row["code_fail_count"]}


def increment_fail(member_id: str) -> int:
    conn = get_conn()
    row = conn.execute("SELECT code_fail_count FROM members WHERE id=?", (member_id,)).fetchone()
    if not row:
        conn.close()
        return 0
    new_count = (row["code_fail_count"] or 0) + 1
    if new_count >= CODE_MAX_FAIL:
        locked_until = (_now() + timedelta(hours=CODE_LOCK_HOURS)).isoformat()
        conn.execute(
            "UPDATE members SET code_fail_count=?, code_locked_until=? WHERE id=?",
            (new_count, locked_until, member_id)
        )
    else:
        conn.execute("UPDATE members SET code_fail_count=? WHERE id=?", (new_count, member_id))
    conn.commit()
    conn.close()
    return new_count


def verify_code(input_code: str, member_id: str) -> dict:
    lock = check_lock(member_id)
    if lock.get("locked"):
        return {"ok": False, "error": f"코드가 잠겨 있습니다. 잠금 해제: {lock.get('until')}"}

    conn = get_conn()
    row = conn.execute("SELECT id FROM members WHERE id=?", (member_id,)).fetchone()
    conn.close()

    current = get_current_code(member_id) if row else {"ok": False}
    if not current.get("ok"):
        return {"ok": False, "error": "발급된 코드가 없습니다."}

    stored = current["code"]
    if secrets.compare_digest(_canonical_code(input_code), _canonical_code(stored)):
        # 성공: fail_count 초기화
        conn = get_conn()
        conn.execute("UPDATE members SET code_fail_count=0, code_locked_until=NULL WHERE id=?", (member_id,))
        conn.commit()
        conn.close()
        return {"ok": True}
    else:
        fail_count = increment_fail(member_id)
        remaining = max(0, CODE_MAX_FAIL - fail_count)
        return {"ok": False, "error": f"코드가 올바르지 않습니다. 남은 시도: {remaining}회"}


def revoke_code(member_id: str):
    conn = get_conn()
    conn.execute(
        "UPDATE members SET access_code=NULL, code_expires_at=NULL, code_issued_at=NULL WHERE id=?",
        (member_id,)
    )
    conn.commit()
    conn.close()
    _record_revoke(member_id)


def regenerate_code(member_id: str) -> str:
    revoke_code(member_id)
    return generate_code(member_id)
