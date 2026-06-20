import uuid
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

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
DEFAULT_LOCATION = "영등포시장역 사무실"
PENDING_BOOKING_STATUSES = ("requested", "payment_guide_sent", "payment_pending", "payment_confirmed")
INACTIVE_BOOKING_STATUSES = ("canceled", "rejected", "no_show")
NON_MOVABLE_BOOKING_STATUSES = ("canceled", "rejected", "no_show", "completed")
KST = ZoneInfo("Asia/Seoul")


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
            int(DEFAULT_PRICE if data.get("price_krw") in (None, "") else data.get("price_krw")),
            data.get("location") or DEFAULT_LOCATION,
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


def delete_session(session_id: str) -> tuple[bool, str]:
    """Delete a session when no active booking remains.

    Canceled/rejected/no-show bookings are kept as audit records, but detached
    from the deleted session so the old schedule no longer blocks the calendar.
    """
    conn = get_conn()
    row = conn.execute("SELECT id FROM sessions WHERE id=?", (session_id,)).fetchone()
    if not row:
        conn.close()
        return False, "세션을 찾을 수 없습니다."
    total_count = conn.execute(
        "SELECT COUNT(*) FROM bookings WHERE session_id=?",
        (session_id,),
    ).fetchone()[0]
    active_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM bookings
        WHERE session_id=?
          AND status NOT IN ('canceled', 'rejected', 'no_show')
        """,
        (session_id,),
    ).fetchone()[0]
    if int(active_count or 0) > 0:
        conn.close()
        return False, "신청 또는 확정 예약이 남은 일정은 삭제할 수 없습니다. 먼저 예약을 취소하세요."
    detached = int(total_count or 0)
    if detached:
        conn.execute(
            """
            UPDATE bookings
            SET session_id=NULL, updated_at=?
            WHERE session_id=?
              AND status IN ('canceled', 'rejected', 'no_show')
            """,
            (_now(), session_id),
        )
    conn.execute("DELETE FROM sessions WHERE id=?", (session_id,))
    conn.commit()
    conn.close()
    if detached:
        return True, f"일정을 삭제했습니다. 취소된 예약 기록 {detached}건은 보관했습니다."
    return True, "일정을 삭제했습니다."


def delete_booking(booking_id: str) -> tuple[bool, str, dict | None]:
    """Permanently remove an inactive booking from operator views."""
    booking = get_booking(booking_id)
    if not booking:
        return False, "예약 신청을 찾을 수 없습니다.", None
    if booking.get("status") not in INACTIVE_BOOKING_STATUSES:
        return False, "활성 예약은 먼저 취소한 뒤 삭제하세요.", booking

    session_id = booking.get("session_id")
    conn = get_conn()
    conn.execute("DELETE FROM bookings WHERE id=?", (booking_id,))
    conn.commit()
    conn.close()
    refresh_session_counts(session_id)
    return True, "예약 신청 기록을 삭제했습니다.", {
        "booking_id": booking_id,
        "session_id": session_id,
        "status": booking.get("status"),
    }


def list_sessions(status: str | None = None, include_closed: bool = False) -> list[dict]:
    conn = get_conn()
    query = """
        SELECT
            s.*,
            (
                SELECT COUNT(*)
                FROM bookings b
                WHERE b.session_id=s.id
                  AND b.status NOT IN ('canceled', 'rejected', 'no_show')
            ) AS active_booking_count,
            (
                SELECT COUNT(*)
                FROM bookings b
                WHERE b.session_id=s.id
                  AND b.status IN ('requested', 'payment_guide_sent', 'payment_pending', 'payment_confirmed')
            ) AS requested_count,
            (
                SELECT COUNT(*)
                FROM bookings b
                WHERE b.session_id=s.id
                  AND b.status='confirmed'
            ) AS confirmed_booking_count
        FROM sessions s
        WHERE 1=1
    """
    params: list = []
    if status:
        query += " AND s.status=?"
        params.append(status)
    elif not include_closed:
        query += " AND s.status IN ('open', 'full')"
    query += " ORDER BY s.starts_at ASC"
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return [_with_capacity_fields(dict(row)) for row in rows]


def get_session(session_id: str) -> dict | None:
    conn = get_conn()
    row = conn.execute(
        """
        SELECT
            s.*,
            (
                SELECT COUNT(*)
                FROM bookings b
                WHERE b.session_id=s.id
                  AND b.status NOT IN ('canceled', 'rejected', 'no_show')
            ) AS active_booking_count,
            (
                SELECT COUNT(*)
                FROM bookings b
                WHERE b.session_id=s.id
                  AND b.status IN ('requested', 'payment_guide_sent', 'payment_pending', 'payment_confirmed')
            ) AS requested_count,
            (
                SELECT COUNT(*)
                FROM bookings b
                WHERE b.session_id=s.id
                  AND b.status='confirmed'
            ) AS confirmed_booking_count
        FROM sessions s
        WHERE s.id=?
        """,
        (session_id,),
    ).fetchone()
    conn.close()
    data = _row_to_dict(row)
    return _with_capacity_fields(data) if data else None


def _with_capacity_fields(session: dict) -> dict:
    capacity = int(session.get("capacity_max") or DEFAULT_CAPACITY_MAX)
    active = int(session.get("active_booking_count") or 0)
    confirmed = int(session.get("confirmed_booking_count") or session.get("confirmed_count") or 0)
    session["active_booking_count"] = active
    session["requested_count"] = int(session.get("requested_count") or 0)
    session["confirmed_booking_count"] = confirmed
    session["remaining_capacity"] = max(capacity - active, 0)
    session["is_request_full"] = active >= capacity
    return session


def create_booking(data: dict) -> str:
    booking_id = str(uuid.uuid4())
    now = _now()
    raw_amount = data.get("payment_amount_krw")
    amount = int(DEFAULT_PRICE if raw_amount in (None, "") else raw_amount)
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
        WITH booking_order AS (
            SELECT
                id,
                ROW_NUMBER() OVER (
                    PARTITION BY session_id
                    ORDER BY created_at ASC, id ASC
                ) AS request_rank,
                ROW_NUMBER() OVER (
                    PARTITION BY session_id
                    ORDER BY
                        CASE WHEN confirmed_at IS NULL THEN 1 ELSE 0 END,
                        confirmed_at ASC,
                        created_at ASC,
                        id ASC
                ) AS paid_rank_raw
            FROM bookings
            WHERE status NOT IN ('canceled', 'rejected', 'no_show')
        ),
        waitlist_order AS (
            SELECT
                id,
                ROW_NUMBER() OVER (
                    PARTITION BY session_id
                    ORDER BY created_at ASC, id ASC
                ) AS waitlist_rank
            FROM bookings
            WHERE status = 'waitlisted'
        )
        SELECT
            b.*,
            s.title AS session_title,
            s.starts_at AS session_starts_at,
            s.ends_at AS session_ends_at,
            s.location AS session_location,
            s.capacity_max AS session_capacity_max,
            bo.request_rank,
            CASE WHEN b.status='confirmed' AND b.payment_status='paid' THEN bo.paid_rank_raw END AS paid_rank,
            CASE WHEN b.status='waitlisted' THEN wo.waitlist_rank END AS waitlist_rank,
            m.name AS member_name,
            m.ai_level AS member_ai_level,
            m.plan_type AS member_plan_type
        FROM bookings b
        LEFT JOIN sessions s ON s.id = b.session_id
        LEFT JOIN booking_order bo ON bo.id = b.id
        LEFT JOIN waitlist_order wo ON wo.id = b.id
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
    row = conn.execute(
        """
        WITH booking_order AS (
            SELECT
                id,
                ROW_NUMBER() OVER (
                    PARTITION BY session_id
                    ORDER BY created_at ASC, id ASC
                ) AS request_rank,
                ROW_NUMBER() OVER (
                    PARTITION BY session_id
                    ORDER BY
                        CASE WHEN confirmed_at IS NULL THEN 1 ELSE 0 END,
                        confirmed_at ASC,
                        created_at ASC,
                        id ASC
                ) AS paid_rank_raw
            FROM bookings
            WHERE status NOT IN ('canceled', 'rejected', 'no_show')
        ),
        waitlist_order AS (
            SELECT
                id,
                ROW_NUMBER() OVER (
                    PARTITION BY session_id
                    ORDER BY created_at ASC, id ASC
                ) AS waitlist_rank
            FROM bookings
            WHERE status = 'waitlisted'
        )
        SELECT
            b.*,
            s.title AS session_title,
            s.starts_at AS session_starts_at,
            s.ends_at AS session_ends_at,
            s.location AS session_location,
            s.capacity_max AS session_capacity_max,
            s.confirmed_count AS session_confirmed_count,
            s.price_krw AS session_price_krw,
            s.payment_guide AS session_payment_guide,
            bo.request_rank,
            CASE WHEN b.status='confirmed' AND b.payment_status='paid' THEN bo.paid_rank_raw END AS paid_rank,
            CASE WHEN b.status='waitlisted' THEN wo.waitlist_rank END AS waitlist_rank
        FROM bookings b
        LEFT JOIN sessions s ON s.id = b.session_id
        LEFT JOIN booking_order bo ON bo.id = b.id
        LEFT JOIN waitlist_order wo ON wo.id = b.id
        WHERE b.id=?
        """,
        (booking_id,),
    ).fetchone()
    conn.close()
    return _row_to_dict(row)


def list_member_bookings(member_id: str) -> list[dict]:
    conn = get_conn()
    rows = conn.execute(
        """
        WITH booking_order AS (
            SELECT
                id,
                ROW_NUMBER() OVER (
                    PARTITION BY session_id
                    ORDER BY created_at ASC, id ASC
                ) AS request_rank,
                ROW_NUMBER() OVER (
                    PARTITION BY session_id
                    ORDER BY
                        CASE WHEN confirmed_at IS NULL THEN 1 ELSE 0 END,
                        confirmed_at ASC,
                        created_at ASC,
                        id ASC
                ) AS paid_rank_raw
            FROM bookings
            WHERE status NOT IN ('canceled', 'rejected', 'no_show')
        ),
        waitlist_order AS (
            SELECT
                id,
                ROW_NUMBER() OVER (
                    PARTITION BY session_id
                    ORDER BY created_at ASC, id ASC
                ) AS waitlist_rank
            FROM bookings
            WHERE status = 'waitlisted'
        )
        SELECT
            b.*,
            s.title AS session_title,
            s.starts_at AS session_starts_at,
            s.ends_at AS session_ends_at,
            s.location AS session_location,
            s.capacity_max AS session_capacity_max,
            s.price_krw AS session_price_krw,
            bo.request_rank,
            CASE WHEN b.status='confirmed' AND b.payment_status='paid' THEN bo.paid_rank_raw END AS paid_rank,
            CASE WHEN b.status='waitlisted' THEN wo.waitlist_rank END AS waitlist_rank
        FROM bookings b
        LEFT JOIN sessions s ON s.id = b.session_id
        LEFT JOIN booking_order bo ON bo.id = b.id
        LEFT JOIN waitlist_order wo ON wo.id = b.id
        WHERE b.member_id=?
        ORDER BY b.created_at DESC
        """,
        (member_id,),
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def find_active_member_booking(member_id: str, session_id: str) -> dict | None:
    conn = get_conn()
    row = conn.execute(
        """
        SELECT *
        FROM bookings
        WHERE member_id=?
          AND session_id=?
          AND status NOT IN ('canceled', 'rejected', 'no_show')
        ORDER BY created_at DESC
        LIMIT 1
        """,
        (member_id, session_id),
    ).fetchone()
    conn.close()
    return _row_to_dict(row)


def update_booking(booking_id: str, data: dict) -> bool:
    allowed = {"session_id", "status", "payment_status", "payment_note", "confirmed_at", "canceled_at"}
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
    confirmed_count = conn.execute(
        "SELECT COUNT(*) FROM bookings WHERE session_id=? AND status='confirmed'",
        (session_id,),
    ).fetchone()[0]
    active_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM bookings
        WHERE session_id=?
          AND status NOT IN ('canceled', 'rejected', 'no_show')
        """,
        (session_id,),
    ).fetchone()[0]
    row = conn.execute("SELECT capacity_max FROM sessions WHERE id=?", (session_id,)).fetchone()
    status = None
    if row:
        status = "full" if active_count >= int(row["capacity_max"]) else "open"
    if status:
        conn.execute(
            "UPDATE sessions SET confirmed_count=?, status=?, updated_at=? WHERE id=? AND status IN ('open', 'full')",
            (confirmed_count, status, _now(), session_id),
        )
    else:
        conn.execute(
            "UPDATE sessions SET confirmed_count=?, updated_at=? WHERE id=?",
            (confirmed_count, _now(), session_id),
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


def session_acceptance(session: dict | None) -> tuple[bool, str]:
    if not session:
        return False, "선택한 세션을 찾을 수 없습니다."
    if session.get("status") not in {"open", "full"}:
        return False, "현재 공개 예약 가능한 세션이 아닙니다."
    if session.get("status") == "full":
        return False, "이미 마감된 세션입니다."
    active = int(session.get("active_booking_count") or session.get("confirmed_count") or 0)
    capacity = int(session.get("capacity_max") or DEFAULT_CAPACITY_MAX)
    if active >= capacity:
        return False, "신청 정원이 마감된 세션입니다."
    return True, ""


def move_booking_to_session(
    booking_id: str,
    target_session_id: str,
    note: str | None = None,
) -> tuple[bool, str, dict | None]:
    booking = get_booking(booking_id)
    if not booking:
        return False, "예약 신청을 찾을 수 없습니다.", None

    old_session_id = booking.get("session_id")
    if old_session_id == target_session_id:
        return True, "이미 선택한 일정에 연결되어 있습니다.", booking

    if booking.get("status") in NON_MOVABLE_BOOKING_STATUSES:
        return False, "취소/종료된 예약은 일정 이동할 수 없습니다.", booking

    refresh_session_counts(target_session_id)
    target_session = get_session(target_session_id)
    if not target_session:
        return False, "이동할 일정을 찾을 수 없습니다.", booking

    ok, reason = session_acceptance(target_session)
    if not ok:
        return False, reason or "이동할 일정에 자리가 없습니다.", booking

    updates = {"session_id": target_session_id}
    move_note = (note or "").strip()
    if move_note:
        existing_note = (booking.get("payment_note") or "").strip()
        updates["payment_note"] = "\n".join(
            part for part in [existing_note, f"[일정 이동] {move_note}"] if part
        )

    changed = update_booking(booking_id, updates)
    refresh_session_counts(old_session_id)
    refresh_session_counts(target_session_id)
    if not changed:
        return False, "예약 일정을 변경하지 못했습니다.", booking
    return True, "예약 일정을 이동했습니다.", get_booking(booking_id)


def _parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    text = str(value).strip()
    if text.endswith("Z"):
        text = f"{text[:-1]}+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=KST)
    return parsed.astimezone(KST)


def _korean_time(value: datetime) -> str:
    ampm = "오전" if value.hour < 12 else "오후"
    hour = value.hour % 12 or 12
    minute = f" {value.minute:02d}분" if value.minute else ""
    return f"{ampm} {hour}시{minute}"


def _format_korean_datetime_range(starts_at: str | None, ends_at: str | None = None) -> tuple[str, str]:
    start = _parse_datetime(starts_at)
    end = _parse_datetime(ends_at)
    if not start:
        return starts_at or "-", ""
    weekdays = "월화수목금토일"
    date_text = f"{start.year}년 {start.month}월 {start.day}일 ({weekdays[start.weekday()]})"
    time_text = _korean_time(start)
    if end:
        end_text = _korean_time(end)
        if end.date() != start.date():
            end_date = f"{end.month}월 {end.day}일 ({weekdays[end.weekday()]})"
            time_text = f"{time_text} - {end_date} {end_text}"
        else:
            time_text = f"{time_text} - {end_text}"
    return date_text, time_text


def _payment_account_lines(payment_account: dict | None = None) -> list[str]:
    if not payment_account:
        return []
    bank = str(payment_account.get("bank") or "").strip()
    number = str(payment_account.get("number") or "").strip()
    holder = str(payment_account.get("holder") or "").strip()
    memo = str(payment_account.get("memo") or "").strip()
    account = " ".join(part for part in [bank, number] if part)
    lines: list[str] = []
    if account:
        lines.append(f"입금 계좌: {account}")
    if holder:
        lines.append(f"예금주: {holder}")
    if memo:
        lines.append(f"계좌 메모: {memo}")
    return lines


def default_payment_guide(
    session: dict | None,
    booking: dict | None = None,
    payment_account: dict | None = None,
) -> str:
    amount = int((booking or {}).get("payment_amount_krw") or (session or {}).get("price_krw") or DEFAULT_PRICE)
    title = (session or {}).get("title") or DEFAULT_TITLE
    starts = (session or {}).get("starts_at") or ""
    ends = (session or {}).get("ends_at") or ""
    date_text, time_text = _format_korean_datetime_range(starts, ends)
    location = (session or {}).get("location") or ""
    custom = ((session or {}).get("payment_guide") or "").strip()
    lines = [
        "[입금 안내]",
        f"과정: {title}",
        f"일정: {date_text}",
        f"시간: {time_text or '-'}",
        f"장소: {location}",
        f"금액: {amount:,}원",
    ]
    account_lines = _payment_account_lines(payment_account)
    if account_lines:
        lines.append("")
        lines.extend(account_lines)
    elif not custom:
        lines.append("")
        lines.append("계좌 정보는 운영자가 확인 후 개별 안내합니다.")
    lines.append("")
    lines.append("입금 후 입금자명과 신청자명이 다르면 운영자에게 알려주세요.")
    if custom:
        lines.append("")
        lines.append(custom)
    return "\n".join(lines).strip()


def send_payment_guide_state(
    booking_id: str,
    note: str | None = None,
    payment_account: dict | None = None,
) -> dict | None:
    booking = get_booking(booking_id)
    if not booking:
        return None
    guide = note or default_payment_guide(
        {
            "title": booking.get("session_title"),
            "starts_at": booking.get("session_starts_at"),
            "ends_at": booking.get("session_ends_at"),
            "location": booking.get("session_location"),
            "price_krw": booking.get("session_price_krw"),
            "payment_guide": booking.get("session_payment_guide"),
        },
        booking,
        payment_account,
    )
    set_booking_state(
        booking_id,
        status="payment_guide_sent",
        payment_status="guide_sent",
        payment_note=guide,
    )
    return get_booking(booking_id)


def confirm_payment_state(booking_id: str, note: str | None = None) -> tuple[bool, str, dict | None]:
    booking = get_booking(booking_id)
    if not booking:
        return False, "예약 신청을 찾을 수 없습니다.", None
    if booking.get("status") == "confirmed":
        return True, "이미 확정된 예약입니다.", booking
    if booking.get("session_id"):
        refresh_session_counts(booking.get("session_id"))
        session = get_session(booking["session_id"])
        confirmed = int((session or {}).get("confirmed_count") or 0)
        capacity = int((session or {}).get("capacity_max") or DEFAULT_CAPACITY_MAX)
        if confirmed >= capacity:
            return False, "정원이 이미 마감되어 확정할 수 없습니다.", booking
    payment_note = note if note is not None else booking.get("payment_note")
    set_booking_state(
        booking_id,
        status="confirmed",
        payment_status="paid",
        payment_note=payment_note,
    )
    return True, "입금 확인 및 예약 확정 완료", get_booking(booking_id)


def default_location_guide(booking: dict | None) -> str:
    booking = booking or {}
    title = booking.get("session_title") or DEFAULT_TITLE
    starts = booking.get("session_starts_at") or ""
    ends = booking.get("session_ends_at") or ""
    date_text, time_text = _format_korean_datetime_range(starts, ends)
    location = booking.get("session_location") or DEFAULT_LOCATION
    name = booking.get("applicant_name") or booking.get("member_name") or "신청자"
    return "\n".join(
        [
            "[장소 안내]",
            "",
            f"{name}님, 입금 확인되어 예약이 확정되었습니다.",
            "",
            "예약 정보",
            f"과정: {title}",
            f"일정: {date_text}",
            f"시간: {time_text or '-'}",
            f"장소: {location}",
            "",
            "오시기 전 확인",
            "준비물: 노트북, 충전기, 사용 중인 AI 계정 정보, 자동화하고 싶은 업무 예시",
            "도착 전 문의가 있으면 1:1 문의방으로 편하게 남겨주세요.",
        ]
    ).strip()


def default_free_class_guide(booking: dict | None) -> str:
    booking = booking or {}
    title = booking.get("session_title") or DEFAULT_TITLE
    starts = booking.get("session_starts_at") or ""
    ends = booking.get("session_ends_at") or ""
    date_text, time_text = _format_korean_datetime_range(starts, ends)
    location = booking.get("session_location") or DEFAULT_LOCATION
    name = booking.get("applicant_name") or booking.get("member_name") or "신청자"
    return "\n".join(
        [
            "[무료강의 안내]",
            "",
            f"{name}님, 무료강의 신청이 확인되었습니다.",
            "",
            "강의 정보",
            f"과정: {title}",
            f"일정: {date_text}",
            f"시간: {time_text or '-'}",
            f"장소: {location}",
            "",
            "참여 전 확인",
            "참석 가능 여부를 답장으로 알려주세요.",
            "준비물: 노트북 또는 태블릿, 사용 중인 AI 계정, 궁금한 자동화 주제",
            "변경이 필요하면 1:1 문의방으로 편하게 남겨주세요.",
        ]
    ).strip()


def default_refund_guide(booking: dict | None) -> str:
    booking = booking or {}
    title = booking.get("session_title") or DEFAULT_TITLE
    starts = booking.get("session_starts_at") or ""
    ends = booking.get("session_ends_at") or ""
    date_text, time_text = _format_korean_datetime_range(starts, ends)
    amount = int(booking.get("payment_amount_krw") or DEFAULT_PRICE)
    name = booking.get("applicant_name") or booking.get("member_name") or "신청자"
    return "\n".join(
        [
            "[예약 취소 및 환불 안내]",
            f"{name}님, 아래 강의 예약이 취소 처리되었습니다.",
            f"과정: {title}",
            f"일정: {date_text}",
            f"시간: {time_text or '-'}",
            f"확인 필요 금액: {amount:,}원",
            "입금이 완료된 예약이어서 운영자가 환불 계좌를 확인한 뒤 환불을 진행해야 합니다.",
            "환불받으실 은행/계좌번호/예금주를 보내주시면 확인 후 처리하겠습니다.",
        ]
    ).strip()


def seed_default_sunday_sessions(weeks: int = 4) -> dict[str, list[str]]:
    """Create or reopen Sunday sessions from the nearest upcoming Sunday."""
    weeks = max(1, min(int(weeks), 12))
    now_local = datetime.now()
    days_until_sunday = (6 - now_local.weekday()) % 7
    if days_until_sunday == 0:
        days_until_sunday = 7
    first = now_local + timedelta(days=days_until_sunday)
    slots = [(10, 12), (13, 15), (16, 18)]
    created: list[str] = []
    updated: list[str] = []
    existing = list_sessions(include_closed=True)
    existing_by_start = {s["starts_at"]: s for s in existing}
    for week in range(weeks):
        day = first + timedelta(days=7 * week)
        for start_h, end_h in slots:
            start = day.replace(hour=start_h, minute=0, second=0, microsecond=0)
            end = day.replace(hour=end_h, minute=0, second=0, microsecond=0)
            data = {
                "title": DEFAULT_TITLE,
                "description": DEFAULT_DESCRIPTION,
                "starts_at": start.isoformat(),
                "ends_at": end.isoformat(),
                "location": DEFAULT_LOCATION,
                "materials": DEFAULT_MATERIALS,
                "price_krw": DEFAULT_PRICE,
                "status": "open",
            }
            existing_session = existing_by_start.get(data["starts_at"])
            if existing_session:
                updates = {
                    "title": DEFAULT_TITLE,
                    "description": DEFAULT_DESCRIPTION,
                    "ends_at": data["ends_at"],
                    "location": DEFAULT_LOCATION,
                    "materials": DEFAULT_MATERIALS,
                    "price_krw": DEFAULT_PRICE,
                    "capacity_min": DEFAULT_CAPACITY_MIN,
                    "capacity_max": DEFAULT_CAPACITY_MAX,
                    "status": "open",
                }
                changed = any(existing_session.get(key) != value for key, value in updates.items())
                if changed and update_session(existing_session["id"], updates):
                    updated.append(existing_session["id"])
                continue
            session_id = create_session(data)
            created.append(session_id)
            existing_by_start[data["starts_at"]] = get_session(session_id) or {"id": session_id}
    return {"created": created, "updated": updated}
