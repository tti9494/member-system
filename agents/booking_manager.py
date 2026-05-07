import uuid
from datetime import datetime, timezone, timedelta

import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / "member-system"))
from db import get_conn


DEFAULT_TITLE = "AI 기초 셋팅 및 컨설팅 강의 1:4"
DEFAULT_DESCRIPTION = (
    "AI 기초 설정, 유료 구독 점검, 구현하고 싶은 업무 자동화 방향 설계까지 함께 진행합니다."
)
DEFAULT_MATERIALS = "노트북, 필기구, GPT/Claude 유료 구독, 구현하고 싶은 내용"
DEFAULT_PRICE = 50000
DEFAULT_CAPACITY_MIN = 4
DEFAULT_CAPACITY_MAX = 5


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _row_to_dict(row) -> dict | None:
    return dict(row) if row else None


def create_session(data: dict) -> str:
    session_id = str(uuid.uuid4())
    now = _now()
    conn = get_conn()
    conn.execute(
        """
        INSERT INTO sessions (
            id, title, description, program_type, audience_level, starts_at, ends_at,
            timezone, capacity_min, capacity_max, confirmed_count, price_krw,
            location, materials, status, payment_guide, created_at, updated_at
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        (
            session_id,
            data.get("title") or DEFAULT_TITLE,
            data.get("description") or DEFAULT_DESCRIPTION,
            data.get("program_type") or "ai_basic_setup",
            data.get("audience_level") or "all",
            data["starts_at"],
            data["ends_at"],
            data.get("timezone") or "Asia/Seoul",
            int(data.get("capacity_min") or DEFAULT_CAPACITY_MIN),
            int(data.get("capacity_max") or DEFAULT_CAPACITY_MAX),
            0,
            int(data.get("price_krw") or DEFAULT_PRICE),
            data["location"],
            data.get("materials") or DEFAULT_MATERIALS,
            data.get("status") or "open",
            data.get("payment_guide") or "",
            now,
            now,
        ),
    )
    conn.commit()
    conn.close()
    return session_id


def update_session(session_id: str, data: dict) -> bool:
    allowed = {
        "title",
        "description",
        "program_type",
        "audience_level",
        "starts_at",
        "ends_at",
        "timezone",
        "capacity_min",
        "capacity_max",
        "price_krw",
        "location",
        "materials",
        "status",
        "payment_guide",
    }
    fields = [key for key in data if key in allowed]
    if not fields:
        return False
    values = [data[key] for key in fields]
    values.append(_now())
    values.append(session_id)
    sql = ", ".join(f"{key}=?" for key in fields)
    conn = get_conn()
    cur = conn.execute(
        f"UPDATE sessions SET {sql}, updated_at=? WHERE id=?",
        values,
    )
    conn.commit()
    changed = cur.rowcount > 0
    conn.close()
    return changed


def list_sessions(status: str | None = None, include_closed: bool = False) -> list[dict]:
    conn = get_conn()
    query = "SELECT * FROM sessions WHERE 1=1"
    params: list = []
    if status:
        query += " AND status=?"
        params.append(status)
    elif not include_closed:
        query += " AND status IN ('open', 'full')"
    query += " ORDER BY starts_at ASC"
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_session(session_id: str) -> dict | None:
    conn = get_conn()
    row = conn.execute("SELECT * FROM sessions WHERE id=?", (session_id,)).fetchone()
    conn.close()
    return _row_to_dict(row)


def create_booking(data: dict) -> str:
    booking_id = str(uuid.uuid4())
    now = _now()
    amount = int(data.get("payment_amount_krw") or DEFAULT_PRICE)
    conn = get_conn()
    conn.execute(
        """
        INSERT INTO bookings (
            id, session_id, member_id, applicant_name, phone_masked, desired_outcome,
            preparedness, status, payment_status, payment_amount_krw, payment_note,
            confirmed_at, canceled_at, created_at, updated_at
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        (
            booking_id,
            data.get("session_id") or None,
            data.get("member_id") or None,
            data["applicant_name"],
            data["phone_masked"],
            data.get("desired_outcome") or "",
            data.get("preparedness") or "",
            data.get("status") or "requested",
            data.get("payment_status") or "not_sent",
            amount,
            data.get("payment_note") or "",
            data.get("confirmed_at"),
            data.get("canceled_at"),
            now,
            now,
        ),
    )
    conn.commit()
    conn.close()
    return booking_id


def list_bookings(status: str | None = None, session_id: str | None = None) -> list[dict]:
    conn = get_conn()
    query = """
        SELECT
            b.*,
            s.title AS session_title,
            s.starts_at AS session_starts_at,
            s.ends_at AS session_ends_at,
            s.location AS session_location,
            s.capacity_max AS session_capacity_max,
            m.name AS member_name,
            m.ai_level AS member_ai_level,
            m.plan_type AS member_plan_type
        FROM bookings b
        LEFT JOIN sessions s ON s.id = b.session_id
        LEFT JOIN members m ON m.id = b.member_id
        WHERE 1=1
    """
    params: list = []
    if status:
        query += " AND b.status=?"
        params.append(status)
    if session_id:
        query += " AND b.session_id=?"
        params.append(session_id)
    query += " ORDER BY b.created_at DESC"
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_booking(booking_id: str) -> dict | None:
    conn = get_conn()
    row = conn.execute("SELECT * FROM bookings WHERE id=?", (booking_id,)).fetchone()
    conn.close()
    return _row_to_dict(row)


def update_booking(booking_id: str, data: dict) -> bool:
    allowed = {"status", "payment_status", "payment_note", "confirmed_at", "canceled_at"}
    fields = [key for key in data if key in allowed]
    if not fields:
        return False
    values = [data[key] for key in fields]
    values.append(_now())
    values.append(booking_id)
    sql = ", ".join(f"{key}=?" for key in fields)
    conn = get_conn()
    cur = conn.execute(f"UPDATE bookings SET {sql}, updated_at=? WHERE id=?", values)
    conn.commit()
    changed = cur.rowcount > 0
    conn.close()
    return changed


def refresh_session_counts(session_id: str | None) -> None:
    if not session_id:
        return
    conn = get_conn()
    count = conn.execute(
        "SELECT COUNT(*) FROM bookings WHERE session_id=? AND status='confirmed'",
        (session_id,),
    ).fetchone()[0]
    row = conn.execute("SELECT capacity_max FROM sessions WHERE id=?", (session_id,)).fetchone()
    status = None
    if row:
        status = "full" if count >= int(row["capacity_max"]) else "open"
    if status:
        conn.execute(
            "UPDATE sessions SET confirmed_count=?, status=?, updated_at=? WHERE id=? AND status IN ('open', 'full')",
            (count, status, _now(), session_id),
        )
    else:
        conn.execute(
            "UPDATE sessions SET confirmed_count=?, updated_at=? WHERE id=?",
            (count, _now(), session_id),
        )
    conn.commit()
    conn.close()


def set_booking_state(
    booking_id: str,
    *,
    status: str | None = None,
    payment_status: str | None = None,
    payment_note: str | None = None,
) -> bool:
    booking = get_booking(booking_id)
    if not booking:
        return False
    updates: dict = {}
    if status:
        updates["status"] = status
        if status == "confirmed":
            updates["confirmed_at"] = _now()
        if status in {"canceled", "rejected"}:
            updates["canceled_at"] = _now()
    if payment_status:
        updates["payment_status"] = payment_status
    if payment_note is not None:
        updates["payment_note"] = payment_note
    changed = update_booking(booking_id, updates)
    refresh_session_counts(booking.get("session_id"))
    return changed


def seed_default_sunday_sessions(weeks: int = 4) -> list[str]:
    """Create Sunday sample sessions from next Sunday for local MVP testing."""
    weeks = max(1, min(int(weeks), 12))
    locations = ["영등포시장역 사무실", "서울 공유오피스", "안양 공유오피스"]
    now_local = datetime.now()
    days_until_sunday = (6 - now_local.weekday()) % 7
    if days_until_sunday == 0:
        days_until_sunday = 7
    first = now_local + timedelta(days=days_until_sunday)
    slots = [(10, 12), (13, 15), (16, 18)]
    created: list[str] = []
    existing = list_sessions(include_closed=True)
    existing_keys = {(s["starts_at"], s["location"]) for s in existing}
    for week in range(weeks):
        day = first + timedelta(days=7 * week)
        for idx, (start_h, end_h) in enumerate(slots):
            start = day.replace(hour=start_h, minute=0, second=0, microsecond=0)
            end = day.replace(hour=end_h, minute=0, second=0, microsecond=0)
            data = {
                "title": DEFAULT_TITLE,
                "description": DEFAULT_DESCRIPTION,
                "starts_at": start.isoformat(),
                "ends_at": end.isoformat(),
                "location": locations[idx % len(locations)],
                "materials": DEFAULT_MATERIALS,
                "price_krw": DEFAULT_PRICE,
                "status": "open",
            }
            key = (data["starts_at"], data["location"])
            if key in existing_keys:
                continue
            created.append(create_session(data))
            existing_keys.add(key)
    return created
