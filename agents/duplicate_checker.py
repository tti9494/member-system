import sys
from pathlib import Path
sys.path.insert(0, str(Path.home() / "member-system"))

from db import get_conn
from agents.encryptor import hash_phone, hash_email


def check_duplicate(data: dict) -> dict:
    errors = []

    phone_hash = hash_phone(data.get("phone", ""))
    email_hash = hash_email(data.get("email", ""))

    conn = get_conn()
    cur = conn.cursor()

    # 블랙리스트 + 중복 확인 (phone_hash)
    row = cur.execute(
        "SELECT status FROM members WHERE phone_hash=?", (phone_hash,)
    ).fetchone()
    if row:
        if row["status"] == "blacklist":
            conn.close()
            return {"ok": False, "errors": ["접근이 제한된 신청자입니다."]}
        errors.append("이미 신청된 연락처입니다.")

    # 이메일 중복 확인 (email_hash)
    row2 = cur.execute(
        "SELECT status FROM members WHERE email_hash=?", (email_hash,)
    ).fetchone()
    if row2:
        if row2["status"] == "blacklist":
            conn.close()
            return {"ok": False, "errors": ["접근이 제한된 신청자입니다."]}
        if "이미 신청된 연락처입니다." not in errors:
            errors.append("이미 신청된 이메일입니다.")

    conn.close()
    return {"ok": len(errors) == 0, "errors": errors}
