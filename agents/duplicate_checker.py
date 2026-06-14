import sys
from pathlib import Path
sys.path.insert(0, str(Path.home() / "member-system"))

from db import get_conn
from agents.encryptor import hash_phone, hash_email


def _phone_candidates(value: str) -> list[str]:
    raw = str(value or "").strip()
    digits = "".join(ch for ch in raw if ch.isdigit())
    formatted = f"{digits[:3]}-{digits[3:7]}-{digits[7:]}" if len(digits) == 11 else raw
    candidates = [raw, formatted, digits]
    return [item for index, item in enumerate(candidates) if item and item not in candidates[:index]]


def find_duplicate_member(data: dict) -> dict | None:
    phone = (data.get("phone") or "").strip()
    email = (data.get("email") or "").strip()
    email_hash = hash_email(email) if email else ""
    phone_candidates = _phone_candidates(phone)
    if not phone_candidates and not email_hash:
        return None

    conn = get_conn()
    cur = conn.cursor()
    try:
        for candidate in phone_candidates:
            phone_hash = hash_phone(candidate)
            row = cur.execute(
                """
                SELECT id, name, phone_masked, status, plan_type, participation_grade, created_at
                FROM members
                WHERE phone_hash=? AND status!='erased'
                ORDER BY created_at DESC
                LIMIT 1
                """,
                (phone_hash,),
            ).fetchone()
            if row:
                result = dict(row)
                result["duplicate_source"] = "phone"
                return result
        if email_hash:
            row = cur.execute(
                """
                SELECT id, name, phone_masked, status, plan_type, participation_grade, created_at
                FROM members
                WHERE email_hash=? AND status!='erased'
                ORDER BY created_at DESC
                LIMIT 1
                """,
                (email_hash,),
            ).fetchone()
            if row:
                result = dict(row)
                result["duplicate_source"] = "email"
                return result
        return None
    finally:
        conn.close()


def check_duplicate(data: dict) -> dict:
    errors = []

    phone = (data.get("phone") or "").strip()
    email = (data.get("email") or "").strip()
    phone_candidates = _phone_candidates(phone)
    email_hash = hash_email(email) if email else ""

    conn = get_conn()
    cur = conn.cursor()

    # 블랙리스트 + 중복 확인 (phone_hash)
    row = None
    for candidate in phone_candidates:
        phone_hash = hash_phone(candidate)
        row = cur.execute(
            "SELECT status FROM members WHERE phone_hash=? AND status!='erased' ORDER BY created_at DESC LIMIT 1",
            (phone_hash,),
        ).fetchone()
        if row:
            break
    if row:
        if row["status"] == "blacklist":
            conn.close()
            return {"ok": False, "errors": ["접근이 제한된 신청자입니다."]}
        errors.append("이미 신청된 연락처입니다.")

    # 이메일 중복 확인 (email_hash)
    row2 = None
    if email_hash:
        row2 = cur.execute(
            "SELECT status FROM members WHERE email_hash=? AND status!='erased' ORDER BY created_at DESC LIMIT 1",
            (email_hash,),
        ).fetchone()
    if row2:
        if row2["status"] == "blacklist":
            conn.close()
            return {"ok": False, "errors": ["접근이 제한된 신청자입니다."]}
        if "이미 신청된 연락처입니다." not in errors:
            errors.append("이미 신청된 이메일입니다.")

    conn.close()
    return {"ok": len(errors) == 0, "errors": errors}
