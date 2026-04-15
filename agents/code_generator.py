import os
import secrets
import string
import base64
from datetime import datetime, timezone, timedelta
from pathlib import Path
from dotenv import load_dotenv
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

load_dotenv(dotenv_path=str(Path.home() / "member-system" / ".env"))

import sys
sys.path.insert(0, str(Path.home() / "member-system"))
from db import get_conn

CODE_EXPIRE_DAYS = int(os.getenv("CODE_EXPIRE_DAYS", "30"))
CODE_MAX_FAIL = int(os.getenv("CODE_MAX_FAIL", "5"))
CODE_LOCK_HOURS = int(os.getenv("CODE_LOCK_HOURS", "24"))


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


def generate_code(member_id: str) -> str:
    alphabet = string.ascii_uppercase + string.digits
    code = "".join(secrets.choice(alphabet) for _ in range(8))
    encrypted = _encrypt_code(code)
    expires_at = (_now() + timedelta(days=CODE_EXPIRE_DAYS)).isoformat()
    issued_at = _now().isoformat()

    conn = get_conn()
    conn.execute(
        "UPDATE members SET access_code=?, code_expires_at=?, code_issued_at=?, code_fail_count=0, code_locked_until=NULL WHERE id=?",
        (encrypted, expires_at, issued_at, member_id)
    )
    conn.commit()
    conn.close()
    return code


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
    row = conn.execute(
        "SELECT access_code, code_expires_at FROM members WHERE id=?", (member_id,)
    ).fetchone()
    conn.close()

    if not row or not row["access_code"]:
        return {"ok": False, "error": "발급된 코드가 없습니다."}

    expires = datetime.fromisoformat(row["code_expires_at"])
    if _now() > expires:
        return {"ok": False, "error": "코드가 만료되었습니다."}

    stored = _decrypt_code(row["access_code"])
    if secrets.compare_digest(input_code.upper(), stored):
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


def regenerate_code(member_id: str) -> str:
    revoke_code(member_id)
    return generate_code(member_id)
