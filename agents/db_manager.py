import os
import json
import sqlite3
import subprocess
import uuid
import hashlib
import secrets
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
TELEGRAM_NOTIFY_ENABLED = os.getenv("TELEGRAM_NOTIFY_ENABLED", "").lower() in {"1", "true", "yes", "on"}
TELEGRAM_BOOKING_NOTIFY_ENABLED = os.getenv(
    "TELEGRAM_BOOKING_NOTIFY_ENABLED",
    os.getenv("TELEGRAM_NOTIFY_ENABLED", ""),
).lower() in {"1", "true", "yes", "on"}
TELEGRAM_APPLICATION_NOTIFY_ENABLED = os.getenv(
    "TELEGRAM_APPLICATION_NOTIFY_ENABLED",
    os.getenv("TELEGRAM_BOOKING_NOTIFY_ENABLED", os.getenv("TELEGRAM_NOTIFY_ENABLED", "")),
).lower() in {"1", "true", "yes", "on"}

MACPRO_BACKUP_HOST = os.getenv("MACPRO_BACKUP_HOST", "macpro")
MACPRO_BACKUP_DIR = os.getenv("MACPRO_BACKUP_DIR", "/Users/sanguk/member-system/backups")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _configured_value(value: str | None) -> bool:
    text = (value or "").strip()
    if not text:
        return False
    lowered = text.lower()
    placeholders = (
        "your_",
        "placeholder",
        "token_here",
        "chat_id_here",
        "telegram_bot_token",
        "telegram_admin_chat_id",
        "telegram_chat_id",
    )
    return not any(marker in lowered for marker in placeholders)


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
            available_time_slots, region, main_device, can_code, can_present, skills, contribution,
            participation_grade,
            consent_personal, consent_marketing, consent_at, consent_version,
            status, created_at
        ) VALUES (
            ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
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
        json.dumps(data.get("available_time_slots", []), ensure_ascii=False) if isinstance(data.get("available_time_slots"), list) else data.get("available_time_slots"),
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


def get_latest_member_by_phone_hash(phone_hash: str) -> dict | None:
    conn = get_conn()
    cur = conn.cursor()
    row = cur.execute(
        """
        SELECT *
        FROM members
        WHERE phone_hash=?
        ORDER BY created_at DESC
        LIMIT 1
        """,
        (phone_hash,),
    ).fetchone()
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


def erase_member_personal_data(member_id: str, *, cancel_bookings: bool = True) -> dict | None:
    """Anonymize a member and optionally cancel linked active bookings.

    This keeps operational/audit rows intact while removing reusable contact
    data from member and booking surfaces.
    """
    from agents.encryptor import encrypt_email, encrypt_phone

    if not get_member(member_id):
        return None

    now = _now()
    erased_name = "삭제된 신청자"
    erased_text = "삭제됨"
    encrypted_phone = encrypt_phone("")
    encrypted_email = encrypt_email("")
    conn = get_conn()
    try:
        session_rows = conn.execute(
            """
            SELECT DISTINCT session_id
            FROM bookings
            WHERE member_id=?
              AND session_id IS NOT NULL
            """,
            (member_id,),
        ).fetchall()
        active_count = conn.execute(
            """
            SELECT COUNT(*)
            FROM bookings
            WHERE member_id=?
              AND status NOT IN ('canceled', 'rejected', 'no_show')
            """,
            (member_id,),
        ).fetchone()[0]

        conn.execute(
            """
            UPDATE members
            SET
                name=?,
                email_encrypted=?,
                email_hash=NULL,
                phone_hash=NULL,
                phone_masked=?,
                phone_encrypted=?,
                gender=?,
                age=?,
                job=?,
                referral_source=?,
                reason=?,
                ai_level=?,
                plan_type=?,
                ai_tools=NULL,
                ai_subscription=NULL,
                ai_weekly_hours=NULL,
                ai_use_cases=NULL,
                group_goals=NULL,
                short_term_goal=NULL,
                participation_type=NULL,
                preferred_schedule=NULL,
                available_time_slots=NULL,
                region=NULL,
                main_device=NULL,
                can_code=0,
                can_present=0,
                skills=NULL,
                contribution=NULL,
                participation_grade=?,
                consent_marketing=0,
                status=?,
                rejection_reason=?,
                access_code=NULL,
                code_expires_at=NULL,
                code_issued_at=NULL,
                code_fail_count=0,
                code_locked_until=NULL,
                approved_at=NULL
            WHERE id=?
            """,
            (
                erased_name,
                encrypted_email,
                erased_text,
                encrypted_phone,
                "-",
                0,
                erased_text,
                erased_text,
                erased_text,
                erased_text,
                "erased",
                erased_text,
                "erased",
                "개인정보 삭제 처리",
                member_id,
            ),
        )

        if cancel_bookings:
            cur = conn.execute(
                """
                UPDATE bookings
                SET
                    applicant_name=?,
                    phone_masked=?,
                    desired_outcome='',
                    preparedness='',
                    status=CASE
                        WHEN status IN ('canceled', 'rejected', 'no_show') THEN status
                        ELSE 'canceled'
                    END,
                    payment_note='개인정보 삭제로 예약 취소',
                    canceled_at=CASE
                        WHEN canceled_at IS NULL OR canceled_at='' THEN ?
                        ELSE canceled_at
                    END,
                    updated_at=?
                WHERE member_id=?
                """,
                (erased_name, erased_text, now, now, member_id),
            )
        else:
            cur = conn.execute(
                """
                UPDATE bookings
                SET
                    applicant_name=?,
                    phone_masked=?,
                    desired_outcome='',
                    preparedness='',
                    payment_note='개인정보 삭제 처리',
                    updated_at=?
                WHERE member_id=?
                """,
                (erased_name, erased_text, now, member_id),
            )

        conn.commit()
        return {
            "member_id": member_id,
            "cancel_bookings": cancel_bookings,
            "bookings_updated": int(cur.rowcount or 0),
            "bookings_canceled": int(active_count or 0) if cancel_bookings else 0,
            "session_ids": [row["session_id"] for row in session_rows if row["session_id"]],
        }
    finally:
        conn.close()


def get_stats() -> dict:
    conn = get_conn()
    cur = conn.cursor()
    total = cur.execute("SELECT COUNT(*) FROM members WHERE status!='erased'").fetchone()[0]
    pending = cur.execute("SELECT COUNT(*) FROM members WHERE status='pending'").fetchone()[0]
    approved = cur.execute("SELECT COUNT(*) FROM members WHERE status='approved'").fetchone()[0]
    rejected = cur.execute("SELECT COUNT(*) FROM members WHERE status='rejected'").fetchone()[0]
    blacklist = cur.execute("SELECT COUNT(*) FROM members WHERE status='blacklist'").fetchone()[0]
    erased = cur.execute("SELECT COUNT(*) FROM members WHERE status='erased'").fetchone()[0]
    basic = cur.execute("SELECT COUNT(*) FROM members WHERE plan_type='basic' AND status!='erased'").fetchone()[0]
    full = cur.execute("SELECT COUNT(*) FROM members WHERE plan_type='full' AND status!='erased'").fetchone()[0]

    grade_rows = cur.execute(
        """
        SELECT participation_grade, COUNT(*) as cnt
        FROM members
        WHERE status!='erased'
        GROUP BY participation_grade
        """
    ).fetchall()
    grade_stats = {r["participation_grade"]: r["cnt"] for r in grade_rows}

    conn.close()
    return {
        "total": total,
        "pending": pending,
        "approved": approved,
        "rejected": rejected,
        "blacklist": blacklist,
        "erased": erased,
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


_CODE_LOG_ACTIONS = ("approve", "code_issued", "code_viewed", "code_delivered")


def get_code_delivery_logs(member_id: str, limit: int = 20) -> list:
    conn = get_conn()
    placeholders = ",".join("?" * len(_CODE_LOG_ACTIONS))
    rows = conn.execute(
        f"SELECT id, action, detail, ip, created_at FROM member_logs "
        f"WHERE member_id=? AND action IN ({placeholders}) "
        f"ORDER BY created_at DESC LIMIT ?",
        (member_id, *_CODE_LOG_ACTIONS, limit),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


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

    summary = {
        "reason": reason,
        "created_at": _now(),
        "source": str(DB_PATH),
        "filename": filename,
        "ok_count": sum(1 for item in results if item["status"] == "ok"),
        "failed_count": sum(1 for item in results if item["status"] == "failed"),
        "targets": results,
    }
    log_action(
        "system",
        "db_backup",
        json.dumps(
            {
                "reason": reason,
                "ok_count": summary["ok_count"],
                "failed_count": summary["failed_count"],
                "targets": [
                    {"name": item.get("name"), "status": item.get("status")}
                    for item in results
                ],
            },
            ensure_ascii=False,
        ),
    )
    return summary


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


def _hermes_channel_mode(configured: bool, enabled: bool) -> str:
    if not configured:
        return "not_configured"
    if not enabled:
        return "disabled"
    return "telegram_sendMessage"


def get_hermes_status() -> dict:
    """Return operator-safe Telegram/Hermes readiness without credential values."""
    configured = _configured_value(TELEGRAM_BOT_TOKEN) and _configured_value(TELEGRAM_ADMIN_CHAT_ID)
    active_application = configured and TELEGRAM_APPLICATION_NOTIFY_ENABLED
    active_booking = configured and TELEGRAM_BOOKING_NOTIFY_ENABLED
    active_any = active_application or active_booking
    return {
        "configured": configured,
        "global_enabled": TELEGRAM_NOTIFY_ENABLED,
        "application_enabled": TELEGRAM_APPLICATION_NOTIFY_ENABLED,
        "booking_enabled": TELEGRAM_BOOKING_NOTIFY_ENABLED,
        "active_application": active_application,
        "active_booking": active_booking,
        "status": "ON" if active_any else "OFF",
        "mode": "telegram_sendMessage" if active_any else ("disabled" if configured else "not_configured"),
        "global_mode": "global_switch_on" if TELEGRAM_NOTIFY_ENABLED else "global_switch_off",
        "application_mode": _hermes_channel_mode(configured, TELEGRAM_APPLICATION_NOTIFY_ENABLED),
        "booking_mode": _hermes_channel_mode(configured, TELEGRAM_BOOKING_NOTIFY_ENABLED),
        # Backward-compatible aliases for older admin UI code.
        "enabled": TELEGRAM_NOTIFY_ENABLED,
        "active": active_any,
    }


def get_storage_status(limit: int = 10) -> dict:
    """Return operator-safe persistence status without exposing secrets or raw PII."""
    hermes_status = get_hermes_status()
    conn = get_conn()
    members = conn.execute(
        """
        SELECT id, name, phone_masked, plan_type, status, created_at
        FROM members
        WHERE status != 'erased'
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
              AND action IN ('apply', 'sheets_sync', 'hermes_notify', 'booking_requested', 'booking_requested_public', 'db_backup')
            ORDER BY created_at DESC
            """,
            (member["id"],),
        ).fetchall()
        sheet_log = next((dict(log) for log in logs if log["action"] == "sheets_sync"), None)
        hermes_log = next((dict(log) for log in logs if log["action"] == "hermes_notify"), None)
        booking_log = next((dict(log) for log in logs if log["action"] in {"booking_requested", "booking_requested_public"}), None)
        backup_log = next((dict(log) for log in logs if log["action"] == "db_backup"), None)
        member["name"] = _mask_name(member.get("name"))
        member["phone_masked"] = _mask_phone(member.get("phone_masked"))
        member["db_saved"] = True
        member["sheets_status"] = sheet_log["detail"] if sheet_log else "unknown"
        member["sheets_checked_at"] = sheet_log["created_at"] if sheet_log else None
        member["hermes_status"] = hermes_log["detail"] if hermes_log else "unknown"
        member["hermes_checked_at"] = hermes_log["created_at"] if hermes_log else None
        member["booking_status"] = booking_log["detail"] if booking_log else "not_requested"
        member["backup_status"] = _backup_status_summary(backup_log["detail"]) if backup_log else "unknown"
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
        latest_detail = _safe_backup_detail(latest_backup_log["detail"])
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
        "hermes": hermes_status,
        "backup": backup_status,
        "counts": counts,
        "recent": recent,
    }


def _mask_name(value: str | None) -> str:
    if not value:
        return "-"
    text = str(value).strip()
    if len(text) <= 1:
        return "*"
    if len(text) == 2:
        return f"{text[0]}*"
    return f"{text[0]}{'*' * (len(text) - 2)}{text[-1]}"


def _mask_phone(value: str | None) -> str:
    if not value:
        return "-"
    text = str(value).strip()
    digits = "".join(ch for ch in text if ch.isdigit())
    if text.startswith("010") and len(digits) >= 7:
        return f"010-****-{digits[-4:]}"
    if len(digits) >= 11 and digits.startswith("010"):
        return f"010-****-{digits[-4:]}"
    if len(digits) >= 10:
        return f"***-****-{digits[-4:]}"
    if len(digits) >= 4:
        return f"***-****-{digits[-4:]}"
    return "***-****-****"


def _safe_backup_detail(detail: str | None) -> dict:
    if not detail:
        return {}
    try:
        parsed = json.loads(detail)
    except Exception:
        return {"status": "recorded"}
    if not isinstance(parsed, dict):
        return {}

    safe = {}
    for key in ("ok_count", "failed_count", "skipped_count"):
        if key in parsed:
            safe[key] = parsed.get(key)
    targets = parsed.get("targets")
    if isinstance(targets, list):
        known_target_names = {"local", "icloud", "onedrive", "macpro"}
        known_statuses = {"ok", "failed", "skipped", "unknown"}
        safe["targets"] = [
            {
                "name": str(target.get("name")) if target.get("name") in known_target_names else "custom",
                "status": str(target.get("status")) if target.get("status") in known_statuses else "unknown",
            }
            for target in targets
            if isinstance(target, dict)
        ]
    return safe


def _backup_status_summary(detail: str | None) -> str:
    safe = _safe_backup_detail(detail)
    if not safe:
        return "unknown"
    if "status" in safe:
        return safe["status"]
    ok_count = int(safe.get("ok_count") or 0)
    failed_count = int(safe.get("failed_count") or 0)
    if ok_count > 0 and failed_count == 0:
        return "ok"
    if ok_count > 0:
        return "partial"
    if failed_count > 0:
        return "failed"
    return "unknown"


def get_storage_snapshot(limit: int = 50) -> dict:
    """Return a read-only, masked snapshot for storage visibility/export."""
    limit = max(1, min(int(limit or 50), 200))
    conn = get_conn()
    recent_members = conn.execute(
        """
        SELECT
            m.id,
            m.name,
            m.phone_masked,
            m.plan_type,
            m.participation_grade,
            m.status,
            m.created_at,
            b.id AS booking_id,
            b.status AS booking_status,
            b.payment_status AS payment_status,
            b.created_at AS booking_created_at,
            s.starts_at AS session_starts_at,
            s.location AS session_location
        FROM members m
        LEFT JOIN bookings b ON b.member_id=m.id
        LEFT JOIN sessions s ON s.id=b.session_id
        WHERE m.status != 'erased'
        ORDER BY m.created_at DESC
        LIMIT ?
        """,
        (limit,),
    ).fetchall()
    counts = {
        "members": conn.execute("SELECT COUNT(*) FROM members").fetchone()[0],
        "bookings": conn.execute("SELECT COUNT(*) FROM bookings").fetchone()[0],
        "sessions": conn.execute("SELECT COUNT(*) FROM sessions").fetchone()[0],
        "logs": conn.execute("SELECT COUNT(*) FROM member_logs").fetchone()[0],
    }
    booking_status_rows = conn.execute(
        "SELECT status, COUNT(*) AS count FROM bookings GROUP BY status ORDER BY status"
    ).fetchall()
    latest_member = conn.execute(
        "SELECT created_at FROM members ORDER BY created_at DESC LIMIT 1"
    ).fetchone()
    latest_booking = conn.execute(
        "SELECT created_at FROM bookings ORDER BY created_at DESC LIMIT 1"
    ).fetchone()
    conn.close()

    rows = []
    for row in recent_members:
        item = dict(row)
        rows.append({
            "member_id": item["id"],
            "applicant": _mask_name(item.get("name")),
            "phone_masked": _mask_phone(item.get("phone_masked")),
            "plan_type": item.get("plan_type") or "-",
            "participation_grade": item.get("participation_grade") or "-",
            "member_status": item.get("status") or "-",
            "member_created_at": item.get("created_at"),
            "booking_id": item.get("booking_id"),
            "booking_status": item.get("booking_status") or "not_requested",
            "payment_status": item.get("payment_status") or "-",
            "booking_created_at": item.get("booking_created_at"),
            "session_starts_at": item.get("session_starts_at"),
            "session_location": item.get("session_location") or "-",
        })

    db_stat = DB_PATH.stat() if DB_PATH.exists() else None
    return {
        "storage": {
            "mode": "sqlite_file",
            "path": str(DB_PATH),
            "exists": DB_PATH.exists(),
            "size_bytes": db_stat.st_size if db_stat else 0,
            "tables": ["members", "bookings", "sessions", "member_logs"],
            "pii_policy": "masked_summary_only",
        },
        "counts": counts,
        "booking_status_counts": {row["status"]: row["count"] for row in booking_status_rows},
        "latest": {
            "member_created_at": latest_member["created_at"] if latest_member else None,
            "booking_created_at": latest_booking["created_at"] if latest_booking else None,
        },
        "recent": rows,
    }


def _json_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    text = str(value).strip()
    if not text:
        return []
    if text.startswith("[") and text.endswith("]"):
        try:
            parsed = json.loads(text)
            if isinstance(parsed, list):
                return [str(item).strip() for item in parsed if str(item).strip()]
        except Exception:
            pass
    return [item.strip() for item in text.replace("\r", "\n").replace(",", "\n").split("\n") if item.strip()]


def _json_list_text(value) -> str:
    return json.dumps(_json_list(value), ensure_ascii=False)


def _review_instructor_row(row) -> dict:
    item = dict(row)
    item["specialties"] = _json_list(item.get("specialties"))
    item["sort_order"] = int(item.get("sort_order") or 0)
    return item


def _review_entry_row(row) -> dict:
    item = dict(row)
    item["tags"] = _json_list(item.get("tags"))
    item["image_urls"] = _json_list(item.get("image_urls"))
    item["privacy_checked"] = bool(item.get("privacy_checked"))
    item["featured"] = bool(item.get("featured"))
    return item


def _review_instructor_status(value) -> str:
    status = str(value or "active").strip().lower()
    return status if status in {"active", "inactive"} else "active"


def _review_entry_status(value) -> str:
    status = str(value or "draft").strip().lower()
    return status if status in {"draft", "public", "hidden"} else "draft"


def _review_invite_status(value) -> str:
    status = str(value or "active").strip().lower()
    return status if status in {"active", "revoked"} else "active"


def _review_token_hash(token: str) -> str:
    return hashlib.sha256(str(token or "").encode("utf-8")).hexdigest()


def _review_invite_row(row) -> dict | None:
    if not row:
        return None
    data = dict(row)
    data["max_submissions"] = int(data.get("max_submissions") or 0)
    data["submitted_count"] = int(data.get("submitted_count") or 0)
    data["is_open"] = (
        data.get("status") == "active"
        and (not data.get("expires_at") or str(data.get("expires_at")) >= _now())
        and (not data["max_submissions"] or data["submitted_count"] < data["max_submissions"])
    )
    data.pop("token_hash", None)
    return data


def list_review_invites() -> list[dict]:
    conn = get_conn()
    try:
        rows = conn.execute(
            """
            SELECT ri.*, i.name AS instructor_name, i.role AS instructor_role
            FROM review_invites ri
            LEFT JOIN review_instructors i ON i.id=ri.instructor_id
            ORDER BY ri.created_at DESC
            """
        ).fetchall()
        return [_review_invite_row(row) for row in rows]
    finally:
        conn.close()


def create_review_invite(data: dict) -> dict:
    invite_id = str(uuid.uuid4())
    token = secrets.token_urlsafe(24)
    now = _now()
    conn = get_conn()
    try:
        conn.execute(
            """
            INSERT INTO review_invites (
                id, token_hash, label, instructor_id, class_title, class_date, status,
                max_submissions, submitted_count, expires_at, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?, ?)
            """,
            (
                invite_id,
                _review_token_hash(token),
                str(data.get("label") or "").strip(),
                data.get("instructor_id") or None,
                str(data.get("class_title") or "").strip(),
                str(data.get("class_date") or "").strip(),
                _review_invite_status(data.get("status")),
                max(0, int(data.get("max_submissions") or 0)),
                str(data.get("expires_at") or "").strip(),
                now,
                now,
            ),
        )
        conn.commit()
        invite = get_review_invite(invite_id)
        invite["token"] = token
        return invite
    finally:
        conn.close()


def get_review_invite(invite_id: str) -> dict | None:
    conn = get_conn()
    try:
        row = conn.execute(
            """
            SELECT ri.*, i.name AS instructor_name, i.role AS instructor_role
            FROM review_invites ri
            LEFT JOIN review_instructors i ON i.id=ri.instructor_id
            WHERE ri.id=?
            """,
            (invite_id,),
        ).fetchone()
        return _review_invite_row(row)
    finally:
        conn.close()


def get_review_invite_by_token(token: str) -> dict | None:
    token_hash = _review_token_hash(token)
    conn = get_conn()
    try:
        row = conn.execute(
            """
            SELECT ri.*, i.name AS instructor_name, i.role AS instructor_role
            FROM review_invites ri
            LEFT JOIN review_instructors i ON i.id=ri.instructor_id
            WHERE ri.token_hash=?
            """,
            (token_hash,),
        ).fetchone()
        return _review_invite_row(row)
    finally:
        conn.close()


def revoke_review_invite(invite_id: str) -> bool:
    conn = get_conn()
    try:
        cur = conn.execute(
            "UPDATE review_invites SET status='revoked', updated_at=? WHERE id=?",
            (_now(), invite_id),
        )
        conn.commit()
        return cur.rowcount > 0
    finally:
        conn.close()


def submit_review_from_invite(token: str, data: dict) -> dict:
    token_hash = _review_token_hash(token)
    display_name = str(data.get("display_name") or "수강생").strip()[:80] or "수강생"
    class_title = str(data.get("class_title") or "").strip()[:160]
    title = str(data.get("title") or "").strip()[:160]
    summary = str(data.get("summary") or "").strip()[:500]
    body = str(data.get("body") or "").strip()[:4000]
    if not summary and not body:
        raise ValueError("후기 내용을 입력하세요.")
    if not data.get("consent_public_review"):
        raise ValueError("후기 검수와 공개 후보 등록에 동의해야 합니다.")

    conn = get_conn()
    try:
        invite_row = conn.execute(
            """
            SELECT *
            FROM review_invites
            WHERE token_hash=?
            """,
            (token_hash,),
        ).fetchone()
        invite = _review_invite_row(invite_row)
        if not invite:
            raise ValueError("유효하지 않은 후기 작성 링크입니다.")
        if not invite["is_open"]:
            raise ValueError("현재 사용할 수 없는 후기 작성 링크입니다.")
        final_class_title = class_title or invite.get("class_title") or "ARSEN 수업"
        final_title = title or f"{display_name}님의 수업 후기"
        try:
            rating = max(1, min(5, int(data.get("rating") or 5)))
        except (TypeError, ValueError):
            rating = 5
        tags = _json_list_text(
            ["수강생 제출", f"평점 {rating}점", *reviewListFromData(data.get("tags"))]
        )
        body_parts = [
            f"작성자 공개명: {display_name}",
            f"평점: {rating}점",
        ]
        if body:
            body_parts.append("")
            body_parts.append(body)
        entry_id = str(uuid.uuid4())
        now = _now()
        conn.execute(
            """
            INSERT INTO review_entries (
                id, instructor_id, class_title, class_date, title, summary, body, tags, image_urls,
                status, source, privacy_checked, featured, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'draft', ?, 0, 0, ?, ?)
            """,
            (
                entry_id,
                data.get("instructor_id") or invite.get("instructor_id") or None,
                final_class_title,
                str(data.get("class_date") or invite.get("class_date") or "").strip(),
                final_title,
                summary,
                "\n".join(body_parts).strip(),
                tags,
                _json_list_text(data.get("image_urls")),
                f"student_link:{invite['id']}",
                now,
                now,
            ),
        )
        conn.execute(
            "UPDATE review_invites SET submitted_count=submitted_count+1, updated_at=? WHERE id=?",
            (now, invite["id"]),
        )
        conn.commit()
        return get_review_entry(entry_id)
    finally:
        conn.close()


def reviewListFromData(value) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if not value:
        return []
    return [
        item.strip()
        for item in str(value).replace("\r", "\n").replace(",", "\n").split("\n")
        if item.strip()
    ]


def list_review_board(public_only: bool = False) -> dict:
    conn = get_conn()
    try:
        instructor_where = "WHERE status='active'" if public_only else ""
        instructors = [
            _review_instructor_row(row)
            for row in conn.execute(
                f"""
                SELECT *
                FROM review_instructors
                {instructor_where}
                ORDER BY sort_order ASC, created_at DESC
                """
            ).fetchall()
        ]
        if public_only:
            entry_rows = conn.execute(
                """
                SELECT e.*, i.name AS instructor_name, i.role AS instructor_role
                FROM review_entries e
                LEFT JOIN review_instructors i ON i.id=e.instructor_id
                WHERE e.status='public'
                  AND e.privacy_checked=1
                  AND (i.status='active' OR i.id IS NULL)
                ORDER BY e.featured DESC, COALESCE(e.class_date, e.created_at) DESC, e.created_at DESC
                """
            ).fetchall()
        else:
            entry_rows = conn.execute(
                """
                SELECT e.*, i.name AS instructor_name, i.role AS instructor_role
                FROM review_entries e
                LEFT JOIN review_instructors i ON i.id=e.instructor_id
                ORDER BY e.created_at DESC
                """
            ).fetchall()
        entries = [_review_entry_row(row) for row in entry_rows]
        return {
            "instructors": instructors,
            "entries": entries,
            "invites": [] if public_only else list_review_invites(),
            "stats": {
                "instructors": len(instructors),
                "entries": len(entries),
                "public_entries": sum(1 for item in entries if item.get("status") == "public"),
                "featured_entries": sum(1 for item in entries if item.get("featured")),
            },
        }
    finally:
        conn.close()


def get_review_instructor(instructor_id: str) -> dict | None:
    conn = get_conn()
    try:
        row = conn.execute("SELECT * FROM review_instructors WHERE id=?", (instructor_id,)).fetchone()
        return _review_instructor_row(row) if row else None
    finally:
        conn.close()


def get_review_entry(entry_id: str) -> dict | None:
    conn = get_conn()
    try:
        row = conn.execute(
            """
            SELECT e.*, i.name AS instructor_name, i.role AS instructor_role
            FROM review_entries e
            LEFT JOIN review_instructors i ON i.id=e.instructor_id
            WHERE e.id=?
            """,
            (entry_id,),
        ).fetchone()
        return _review_entry_row(row) if row else None
    finally:
        conn.close()


def create_review_instructor(data: dict) -> str:
    name = str(data.get("name") or "").strip()
    if not name:
        raise ValueError("강사 이름이 필요합니다.")
    instructor_id = str(uuid.uuid4())
    now = _now()
    conn = get_conn()
    try:
        conn.execute(
            """
            INSERT INTO review_instructors (
                id, name, role, bio, specialties, status, sort_order, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                instructor_id,
                name,
                str(data.get("role") or "").strip(),
                str(data.get("bio") or "").strip(),
                _json_list_text(data.get("specialties")),
                _review_instructor_status(data.get("status")),
                int(data.get("sort_order") or 0),
                now,
                now,
            ),
        )
        conn.commit()
        return instructor_id
    finally:
        conn.close()


def update_review_instructor(instructor_id: str, updates: dict) -> bool:
    allowed = {
        "name": lambda value: str(value or "").strip(),
        "role": lambda value: str(value or "").strip(),
        "bio": lambda value: str(value or "").strip(),
        "specialties": _json_list_text,
        "status": _review_instructor_status,
        "sort_order": lambda value: int(value or 0),
    }
    fields = []
    params = []
    for key, normalizer in allowed.items():
        if key in updates and updates[key] is not None:
            fields.append(f"{key}=?")
            params.append(normalizer(updates[key]))
    if not fields:
        return False
    fields.append("updated_at=?")
    params.append(_now())
    params.append(instructor_id)
    conn = get_conn()
    try:
        cur = conn.execute(
            f"UPDATE review_instructors SET {', '.join(fields)} WHERE id=?",
            params,
        )
        conn.commit()
        return cur.rowcount > 0
    finally:
        conn.close()


def delete_review_instructor(instructor_id: str) -> bool:
    conn = get_conn()
    try:
        cur = conn.execute("DELETE FROM review_instructors WHERE id=?", (instructor_id,))
        conn.commit()
        return cur.rowcount > 0
    finally:
        conn.close()


def create_review_entry(data: dict) -> str:
    class_title = str(data.get("class_title") or data.get("title") or "").strip()
    title = str(data.get("title") or class_title).strip()
    if not class_title or not title:
        raise ValueError("수업명과 후기 제목이 필요합니다.")
    entry_id = str(uuid.uuid4())
    now = _now()
    conn = get_conn()
    try:
        conn.execute(
            """
            INSERT INTO review_entries (
                id, instructor_id, class_title, class_date, title, summary, body, tags, image_urls,
                status, source, privacy_checked, featured, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                entry_id,
                data.get("instructor_id") or None,
                class_title,
                str(data.get("class_date") or "").strip(),
                title,
                str(data.get("summary") or "").strip(),
                str(data.get("body") or "").strip(),
                _json_list_text(data.get("tags")),
                _json_list_text(data.get("image_urls")),
                _review_entry_status(data.get("status")),
                str(data.get("source") or "manual").strip() or "manual",
                1 if data.get("privacy_checked") else 0,
                1 if data.get("featured") else 0,
                now,
                now,
            ),
        )
        conn.commit()
        return entry_id
    finally:
        conn.close()


def update_review_entry(entry_id: str, updates: dict) -> bool:
    allowed = {
        "instructor_id": lambda value: str(value).strip() or None,
        "class_title": lambda value: str(value or "").strip(),
        "class_date": lambda value: str(value or "").strip(),
        "title": lambda value: str(value or "").strip(),
        "summary": lambda value: str(value or "").strip(),
        "body": lambda value: str(value or "").strip(),
        "tags": _json_list_text,
        "image_urls": _json_list_text,
        "status": _review_entry_status,
        "source": lambda value: str(value or "manual").strip() or "manual",
        "privacy_checked": lambda value: 1 if value else 0,
        "featured": lambda value: 1 if value else 0,
    }
    fields = []
    params = []
    for key, normalizer in allowed.items():
        if key in updates and updates[key] is not None:
            fields.append(f"{key}=?")
            params.append(normalizer(updates[key]))
    if not fields:
        return False
    fields.append("updated_at=?")
    params.append(_now())
    params.append(entry_id)
    conn = get_conn()
    try:
        cur = conn.execute(f"UPDATE review_entries SET {', '.join(fields)} WHERE id=?", params)
        conn.commit()
        return cur.rowcount > 0
    finally:
        conn.close()


def delete_review_entry(entry_id: str) -> bool:
    conn = get_conn()
    try:
        cur = conn.execute("DELETE FROM review_entries WHERE id=?", (entry_id,))
        conn.commit()
        return cur.rowcount > 0
    finally:
        conn.close()


def get_operator_health() -> dict:
    """Return public, read-only service health without secrets or personal data."""
    hermes_status = get_hermes_status()
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
        "hermes": hermes_status,
        "backup": backup,
    }


def cleanup_expired_codes() -> dict:
    """초대코드는 운영자가 폐기할 때까지 유지한다."""
    return {"cleaned": 0, "ids": []}


def get_expiring_soon(days: int = 7) -> list:
    """초대코드는 만료 경고 대상이 아니다."""
    return []


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
