import os
import json
import uuid
import httpx
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=str(Path.home() / "member-system" / ".env"))

import sys
sys.path.insert(0, str(Path.home() / "member-system"))
from db import get_conn

GAS_URL = os.getenv("GAS_URL", "")


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
