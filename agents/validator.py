import re
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=str(__import__("pathlib").Path.home() / "member-system" / ".env"))

MIN_AGE = int(os.getenv("MIN_AGE", "14"))

VALID_AI_LEVELS = {"입문", "초급", "중급", "고급"}
VALID_PLAN_TYPES = {"free", "basic", "full"}
VALID_REFERRALS = {"유튜브", "지인소개", "SNS", "기타"}
PHONE_PATTERN = re.compile(r"^01[0-9]-\d{3,4}-\d{4}$")
EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$")


def validate(data: dict) -> dict:
    errors = []

    required_fields = [
        "name", "email", "phone", "gender", "age",
        "job", "referral_source", "reason", "ai_level", "plan_type"
    ]
    for field in required_fields:
        if not data.get(field) and data.get(field) != 0:
            errors.append(f"필수 항목 누락: {field}")

    if errors:
        return {"ok": False, "errors": errors}

    # 나이 검증
    try:
        age = int(data["age"])
        if age < MIN_AGE:
            errors.append(f"나이 제한: {MIN_AGE}세 미만은 신청할 수 없습니다.")
    except (ValueError, TypeError):
        errors.append("나이는 숫자여야 합니다.")

    # 전화번호 형식
    phone = str(data.get("phone", "")).strip()
    if not PHONE_PATTERN.match(phone):
        errors.append("전화번호 형식이 올바르지 않습니다. (예: 010-1234-5678)")

    # 이메일 형식
    email = str(data.get("email", "")).strip()
    if not EMAIL_PATTERN.match(email):
        errors.append("이메일 형식이 올바르지 않습니다.")

    # reason 최소 20자
    reason = str(data.get("reason", "")).strip()
    if len(reason) < 20:
        errors.append(f"신청 이유는 최소 20자 이상이어야 합니다. (현재 {len(reason)}자)")

    # ai_level 유효값
    if data.get("ai_level") not in VALID_AI_LEVELS:
        errors.append(f"AI 레벨은 {'/'.join(VALID_AI_LEVELS)} 중 하나여야 합니다.")

    # plan_type 유효값
    if data.get("plan_type") not in VALID_PLAN_TYPES:
        errors.append("플랜 유형은 free/basic/full 중 하나여야 합니다.")

    # gender 유효값
    if data.get("gender") not in ("남", "여"):
        errors.append("성별은 남/여 중 하나여야 합니다.")

    # 무료강의는 운영자가 일정을 확정 안내해야 하므로 지역/시간대가 필요하다.
    # (join-free.html 프론트 필수 검증과 동일 기준 — API 직접 호출 우회 방지)
    if data.get("plan_type") == "free":
        region = str(data.get("region") or "").strip()
        if not region:
            errors.append("무료강의 신청은 참여 가능 지역을 입력해야 합니다.")
        slots = data.get("available_time_slots") or []
        if not isinstance(slots, list):
            slots = [slots]
        if not [s for s in slots if str(s or "").strip()]:
            errors.append("무료강의 신청은 참여 가능 시간대를 최소 1개 선택해야 합니다.")

    return {"ok": len(errors) == 0, "errors": errors}
