"""
검증 결과 재검토 에이전트
validator.py 결과를 받아 누락/경계값/메시지 명확성 확인
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=str(Path.home() / "member-system" / ".env"))
MIN_AGE = int(os.getenv("MIN_AGE", "14"))


def meta_validate(original_data: dict, validation_result: dict) -> dict:
    issues = []

    # validator가 ok인데 필수 항목 실제로 비어있는지 재확인
    if validation_result.get("ok"):
        required = ["name", "email", "phone", "gender", "age", "job",
                    "referral_source", "reason", "ai_level", "plan_type"]
        for f in required:
            if not original_data.get(f) and original_data.get(f) != 0:
                issues.append(f"[누락 재검출] {f} 필드가 비어있습니다.")

        # 경계값: 나이 정확히 MIN_AGE
        try:
            age = int(original_data.get("age", 0))
            if age == MIN_AGE - 1:
                issues.append(f"[경계값] 나이 {age}세는 MIN_AGE({MIN_AGE}) 미만으로 차단되어야 합니다.")
        except (ValueError, TypeError):
            pass

        # 경계값: reason 정확히 20자
        reason = str(original_data.get("reason", ""))
        if len(reason) == 19:
            issues.append("[경계값] reason이 19자입니다. 20자 미만 차단이 정상 작동하는지 확인 필요.")

    # 에러 메시지 명확성: 에러가 있는데 메시지 없는 경우
    errors = validation_result.get("errors", [])
    if not validation_result.get("ok") and len(errors) == 0:
        issues.append("[에러메시지 누락] ok=False인데 errors가 비어있습니다.")

    return {"ok": len(issues) == 0, "issues": issues}
