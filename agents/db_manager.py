import os
import json
import sqlite3
import subprocess
import uuid
import httpx
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=str(Path.home() / "member-system" / ".env"))

import sys
sys.path.insert(0, str(Path.home() / "member-system"))
from db import DB_PATH, get_conn

GAS_URL = os.getenv("GAS_URL", "")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_ADMIN_CHAT_ID = os.getenv("TELEGRAM_ADMIN_CHAT_ID", "")

MACPRO_BACKUP_HOST = os.getenv("MACPRO_BACKUP_HOST", "macpro")
MACPRO_BACKUP_DIR = os.getenv("MACPRO_BACKUP_DIR", "/Users/sanguk/member-system/backups")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def create_member(data: dict) -> str:
    member_id = str(uuid.uuid4())
    conn = get_conn()
    cur = conn.cursor()

    grade = data.get("participation_grade", "🌱 새싹")

    cur.execute("""
        INSERT INTO members (
            id, name, email_encrypted, email_hash, phone_masked, phone_encrypted, phone_hash,
            gender, age, job, referral_source, reason, ai_level, plan_type,
            ai_tools, ai_subscription, ai_weekly_hours, ai_use_cases,
            group_goals, short_term_goal, participation_type, preferred_schedule,
            region, main_device, can_code, can_present, skills, contribution,
            participation_grade,
            consent_personal, consent_marketing, consent_at, consent_version,
            status, created_at
        ) VALUES (
            ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
        )
    """, (
        member_id,
        data["name"],
        data["email_encrypted"],
        data.get("email_hash"),
        data["phone_masked"],
        data["phone_encrypted"],
        data.get("phone_hash"),
        data["gender"],
        int(data["age"]),
        data["job"],
        data["referral_source"],
        data["reason"],
        data["ai_level"],
        data["plan_type"],
        # 선택
        json.dumps(data.get("ai_tools", []), ensure_ascii=False) if isinstance(data.get("ai_tools"), list) else data.get("ai_tools"),
        data.get("ai_subscription"),
        data.get("ai_weekly_hours"),
        json.dumps(data.get("ai_use_cases", []), ensure_ascii=False) if isinstance(data.get("ai_use_cases"), list) else data.get("ai_use_cases"),
        json.dumps(data.get("group_goals", []), ensure_ascii=False) if isinstance(data.get("group_goals"), list) else data.get("group_goals"),
        data.get("short_term_goal"),
        data.get("participation_type"),
        data.get("preferred_schedule"),
        data.get("region"),
        data.get("main_device"),
        1 if data.get("can_code") else 0,
        1 if data.get("can_present") else 0,
        data.get("skills"),
        data.get("contribution"),
        grade,
        # 동의
        1 if data.get("consent_personal") else 0,
        1 if data.get("consent_marketing") else 0,
        data.get("consent_at", _now()),
        data.get("consent_version", "1.0"),
        "pending",
        _now(),
    ))
    conn.commit()
    conn.close()
    return member_id


def get_member(member_id: str) -> dict | None:
    conn = get_conn()
    cur = conn.cursor()
    row = cur.execute("SELECT * FROM members WHERE id=?", (member_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def list_members(status: str = None, grade: str = None) -> list:
    conn = get_conn()
    cur = conn.cursor()
    query = "SELECT * FROM members WHERE 1=1"
    params = []
    if status:
        query += " AND status=?"
        params.append(status)
    if grade:
        query += " AND participation_grade=?"
        params.append(grade)
    query += " ORDER BY created_at DESC"
    rows = cur.execute(query, params).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def update_status(member_id: str, status: str, reason: str = None):
    conn = get_conn()
    cur = conn.cursor()
    if status == "approved":
        cur.execute(
            "UPDATE members SET status=?, approved_at=? WHERE id=?",
            (status, _now(), member_id)
        )
    elif reason:
        cur.execute(
            "UPDATE members SET status=?, rejection_reason=? WHERE id=?",
            (status, reason, member_id)
        )
    else:
        cur.execute("UPDATE members SET status=? WHERE id=?", (status, member_id))
    conn.commit()
    conn.close()


def blacklist_member(member_id: str):
    update_status(member_id, "blacklist")


def get_stats() -> dict:
    conn = get_conn()
    cur = conn.cursor()
    total = cur.execute("SELECT COUNT(*) FROM members").fetchone()[0]
    pending = cur.execute("SELECT COUNT(*) FROM members WHERE status='pending'").fetchone()[0]
    approved = cur.execute("SELECT COUNT(*) FROM members WHERE status='approved'").fetchone()[0]
    rejected = cur.execute("SELECT COUNT(*) FROM members WHERE status='rejected'").fetchone()[0]
    blacklist = cur.execute("SELECT COUNT(*) FROM members WHERE status='blacklist'").fetchone()[0]
    basic = cur.execute("SELECT COUNT(*) FROM members WHERE plan_type='basic'").fetchone()[0]
    full = cur.execute("SELECT COUNT(*) FROM members WHERE plan_type='full'").fetchone()[0]

    grade_rows = cur.execute(
        "SELECT participation_grade, COUNT(*) as cnt FROM members GROUP BY participation_grade"
    ).fetchall()
    grade_stats = {r["participation_grade"]: r["cnt"] for r in grade_rows}

    conn.close()
    return {
        "total": total,
        "pending": pending,
        "approved": approved,
        "rejected": rejected,
        "blacklist": blacklist,
        "basic": basic,
        "full": full,
        "grades": grade_stats,
    }


def save_to_sheets(data: dict) -> bool:
    if not GAS_URL or "YOUR_SCRIPT_ID" in GAS_URL:
        return False
    try:
        resp = httpx.post(GAS_URL, json=data, timeout=10)
        return resp.status_code == 200
    except Exception:
        return False


def log_action(member_id: str, action: str, detail: str = None, ip: str = None):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO member_logs (id, member_id, action, detail, ip, created_at) VALUES (?,?,?,?,?,?)",
        (str(uuid.uuid4()), member_id, action, detail, ip, _now())
    )
    conn.commit()
    conn.close()


def _backup_targets() -> list[dict]:
    home = Path.home()
    return [
        {
            "name": "local",
            "label": "Mac Air local",
            "path": home / "member-system" / "backups",
            "available": True,
        },
        {
            "name": "icloud",
            "label": "iCloud Drive",
            "path": home / "Library/Mobile Documents/com~apple~CloudDocs/Arsen/member-system/backups",
            "available": (home / "Library/Mobile Documents/com~apple~CloudDocs").exists(),
        },
        {
            "name": "onedrive",
            "label": "OneDrive",
            "path": home / "OneDrive/Arsen/member-system/backups",
            "available": (home / "OneDrive").exists(),
        },
    ]


def _latest_backup_info(path: Path) -> dict | None:
    if not path.exists():
        return None
    files = sorted(path.glob("members-*.db"), key=lambda item: item.stat().st_mtime, reverse=True)
    if not files:
        return None
    latest = files[0]
    stat = latest.stat()
    return {
        "path": str(latest),
        "size_bytes": stat.st_size,
        "modified_at": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
    }


def _sqlite_backup(dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    source = sqlite3.connect(str(DB_PATH))
    target = sqlite3.connect(str(dest))
    try:
        source.backup(target)
    finally:
        target.close()
        source.close()


def _run_quiet(args: list[str], timeout: int = 8) -> tuple[bool, str]:
    try:
        completed = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except Exception as exc:
        return False, exc.__class__.__name__
    if completed.returncode == 0:
        return True, "ok"
    detail = (completed.stderr or completed.stdout or "").strip().splitlines()
    return False, detail[-1][:160] if detail else f"exit={completed.returncode}"


def backup_database(reason: str = "manual") -> dict:
    """Create encrypted SQLite backups in operator-visible mirror locations."""
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    filename = f"members-{stamp}.db"
    results = []
    first_ok_path = None

    for target in _backup_targets():
        result = {
            "name": target["name"],
            "label": target["label"],
            "path": str(target["path"]),
            "status": "skipped",
            "detail": "not_available",
        }
        if target["available"]:
            dest = target["path"] / filename
            try:
                _sqlite_backup(dest)
                result.update({
                    "status": "ok",
                    "detail": "encrypted_sqlite_backup",
                    "file": str(dest),
                    "size_bytes": dest.stat().st_size,
                })
                first_ok_path = first_ok_path or dest
            except Exception as exc:
                result.update({"status": "failed", "detail": exc.__class__.__name__})
        results.append(result)

    remote = {
        "name": "macpro",
        "label": "Mac Pro",
        "path": MACPRO_BACKUP_DIR,
        "host": MACPRO_BACKUP_HOST,
        "status": "skipped",
        "detail": "no_local_backup",
    }
    if first_ok_path:
        ok, detail = _run_quiet([
            "ssh",
            "-o",
            "BatchMode=yes",
            "-o",
            "ConnectTimeout=5",
            MACPRO_BACKUP_HOST,
            f"mkdir -p {MACPRO_BACKUP_DIR}",
        ])
        if ok:
            ok, detail = _run_quiet([
                "scp",
                "-q",
                "-o",
                "BatchMode=yes",
                "-o",
                "ConnectTimeout=5",
                str(first_ok_path),
                f"{MACPRO_BACKUP_HOST}:{MACPRO_BACKUP_DIR}/{filename}",
            ], timeout=12)
        remote.update({
            "status": "ok" if ok else "failed",
            "detail": detail,
            "file": f"{MACPRO_BACKUP_DIR}/{filename}" if ok else None,
        })
    results.append(remote)

    return {
        "reason": reason,
        "created_at": _now(),
        "source": str(DB_PATH),
        "filename": filename,
        "ok_count": sum(1 for item in results if item["status"] == "ok"),
        "failed_count": sum(1 for item in results if item["status"] == "failed"),
        "targets": results,
    }


def get_backup_status() -> dict:
    targets = []
    for target in _backup_targets():
        targets.append({
            "name": target["name"],
            "label": target["label"],
            "path": str(target["path"]),
            "available": target["available"],
            "latest": _latest_backup_info(target["path"]),
        })
    targets.append({
        "name": "macpro",
        "label": "Mac Pro",
        "path": MACPRO_BACKUP_DIR,
        "available": True,
        "latest": None,
        "mode": "scp_on_backup",
    })
    return {"targets": targets}


def get_storage_status(limit: int = 10) -> dict:
    """Return operator-safe persistence status without exposing secrets or raw PII."""
    hermes_configured = bool(
        TELEGRAM_BOT_TOKEN
        and TELEGRAM_BOT_TOKEN != "your_bot_token_here"
        and TELEGRAM_ADMIN_CHAT_ID
        and TELEGRAM_ADMIN_CHAT_ID != "your_chat_id_here"
    )
    conn = get_conn()
    members = conn.execute(
        """
        SELECT id, name, phone_masked, plan_type, status, created_at
        FROM members
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (limit,),
    ).fetchall()
    recent = []
    for row in members:
        member = dict(row)
        logs = conn.execute(
            """
            SELECT action, detail, created_at
            FROM member_logs
            WHERE member_id=?
              AND action IN ('apply', 'sheets_sync', 'hermes_notify', 'booking_requested', 'db_backup')
            ORDER BY created_at DESC
            """,
            (member["id"],),
        ).fetchall()
        sheet_log = next((dict(log) for log in logs if log["action"] == "sheets_sync"), None)
        hermes_log = next((dict(log) for log in logs if log["action"] == "hermes_notify"), None)
        booking_log = next((dict(log) for log in logs if log["action"] == "booking_requested"), None)
        backup_log = next((dict(log) for log in logs if log["action"] == "db_backup"), None)
        member["db_saved"] = True
        member["sheets_status"] = sheet_log["detail"] if sheet_log else "unknown"
        member["sheets_checked_at"] = sheet_log["created_at"] if sheet_log else None
        member["hermes_status"] = hermes_log["detail"] if hermes_log else "unknown"
        member["hermes_checked_at"] = hermes_log["created_at"] if hermes_log else None
        member["booking_status"] = booking_log["detail"] if booking_log else "not_requested"
        member["backup_status"] = backup_log["detail"] if backup_log else "unknown"
        recent.append(member)

    counts = {
        "members": conn.execute("SELECT COUNT(*) FROM members").fetchone()[0],
        "bookings": conn.execute("SELECT COUNT(*) FROM bookings").fetchone()[0],
        "sessions": conn.execute("SELECT COUNT(*) FROM sessions").fetchone()[0],
    }
    latest_backup_log = conn.execute(
        """
        SELECT detail, created_at
        FROM member_logs
        WHERE action='db_backup'
        ORDER BY created_at DESC
        LIMIT 1
        """
    ).fetchone()
    conn.close()
    db_path = DB_PATH
    backup_status = get_backup_status()
    if latest_backup_log:
        latest_detail = latest_backup_log["detail"]
        try:
            latest_detail = json.loads(latest_detail)
        except Exception:
            pass
        backup_status["last_run"] = {
            "detail": latest_detail,
            "created_at": latest_backup_log["created_at"],
        }
    return {
        "db": {
            "path": str(db_path),
            "exists": db_path.exists(),
            "size_bytes": db_path.stat().st_size if db_path.exists() else 0,
        },
        "sheets": {
            "configured": bool(GAS_URL and "YOUR_SCRIPT_ID" not in GAS_URL),
            "mode": "google_sheets_append" if GAS_URL and "YOUR_SCRIPT_ID" not in GAS_URL else "not_configured",
        },
        "hermes": {
            "configured": hermes_configured,
            "mode": "telegram_sendMessage" if hermes_configured else "not_configured",
        },
        "backup": backup_status,
        "counts": counts,
        "recent": recent,
    }


def get_operator_health() -> dict:
    """Return public, read-only service health without secrets or personal data."""
    conn = get_conn()
    public_session_count = conn.execute(
        "SELECT COUNT(*) FROM sessions WHERE status IN ('open', 'full')"
    ).fetchone()[0]
    open_session_count = conn.execute(
        "SELECT COUNT(*) FROM sessions WHERE status='open'"
    ).fetchone()[0]
    requested_booking_count = conn.execute(
        "SELECT COUNT(*) FROM bookings WHERE status='requested'"
    ).fetchone()[0]
    active_booking_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM bookings
        WHERE status NOT IN ('canceled', 'rejected', 'no_show')
        """
    ).fetchone()[0]
    latest_backup_log = conn.execute(
        """
        SELECT detail, created_at
        FROM member_logs
        WHERE action='db_backup'
        ORDER BY created_at DESC
        LIMIT 1
        """
    ).fetchone()
    conn.close()

    backup = {
        "last_success": False,
        "status": "unknown",
        "checked_at": None,
    }
    if latest_backup_log:
        detail = latest_backup_log["detail"]
        try:
            detail = json.loads(detail)
        except Exception:
            detail = {}
        ok_count = int(detail.get("ok_count") or 0) if isinstance(detail, dict) else 0
        failed_count = int(detail.get("failed_count") or 0) if isinstance(detail, dict) else 0
        if ok_count > 0 and failed_count == 0:
            status = "ok"
        elif ok_count > 0:
            status = "partial"
        else:
            status = "failed"
        backup = {
            "last_success": ok_count > 0,
            "status": status,
            "checked_at": latest_backup_log["created_at"],
        }

    accepting = open_session_count > 0
    return {
        "server": {
            "alive": True,
        },
        "public_sessions": {
            "count": public_session_count,
            "open_count": open_session_count,
        },
        "application_system": {
            "status": "accepting" if accepting else "no_open_sessions",
            "accepting_applications": accepting,
            "requested_booking_count": requested_booking_count,
            "active_booking_count": active_booking_count,
        },
        "backup": backup,
    }


def cleanup_expired_codes() -> dict:
    """만료된 코드 무효화 (매일 자정 실행)"""
    from datetime import datetime, timezone
    now = _now()
    conn = get_conn()
    cur = conn.cursor()
    rows = cur.execute(
        "SELECT id FROM members WHERE access_code IS NOT NULL AND code_expires_at < ?",
        (now,)
    ).fetchall()
    ids = [r["id"] for r in rows]
    if ids:
        cur.executemany(
            "UPDATE members SET access_code=NULL, code_expires_at=NULL, code_fail_count=0, code_locked_until=NULL WHERE id=?",
            [(mid,) for mid in ids]
        )
        conn.commit()
        for mid in ids:
            log_action(mid, "code_expired", "자동 만료 처리")
    conn.close()
    return {"cleaned": len(ids), "ids": ids}


def get_expiring_soon(days: int = 7) -> list:
    """n일 내 만료 예정 코드 목록 반환"""
    from datetime import datetime, timezone, timedelta
    now = _now()
    deadline = (datetime.now(timezone.utc) + timedelta(days=days)).isoformat()
    conn = get_conn()
    rows = conn.execute(
        "SELECT id, name, phone_masked, code_expires_at FROM members "
        "WHERE access_code IS NOT NULL AND code_expires_at > ? AND code_expires_at < ?",
        (now, deadline)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def release_expired_locks() -> dict:
    """시간 지난 코드 잠금 자동 해제 (1시간마다 실행)"""
    now = _now()
    conn = get_conn()
    rows = conn.execute(
        "SELECT id FROM members WHERE code_locked_until IS NOT NULL AND code_locked_until < ?",
        (now,)
    ).fetchall()
    ids = [r["id"] for r in rows]
    if ids:
        conn.executemany(
            "UPDATE members SET code_locked_until=NULL, code_fail_count=0 WHERE id=?",
            [(mid,) for mid in ids]
        )
        conn.commit()
        for mid in ids:
            log_action(mid, "unlocked", "잠금 자동 해제")
    conn.close()
    return {"released": len(ids), "ids": ids}
