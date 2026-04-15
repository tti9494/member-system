"""
전체 시나리오 테스트
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path.home() / "member-system"))

from db import init_db
from agents.validator import validate
from agents.security_checker import check_security
from agents.consent_checker import check_consent
from agents.encryptor import encrypt_phone, decrypt_phone, encrypt_email, mask_phone, hash_phone, hash_email
from agents.db_manager import create_member, get_member, update_status, blacklist_member, get_stats, log_action
from agents.code_generator import generate_code, verify_code, increment_fail, check_lock
from agents.duplicate_checker import check_duplicate

init_db()

PASS = "✅"
FAIL = "❌"

def test(name, condition):
    status = PASS if condition else FAIL
    print(f"  {status} {name}")
    return condition

results = []

print("\n══ 1. 나이 13세 → 차단 ══")
r = validate({"name":"홍길동","email":"a@b.com","phone":"010-1234-5678","gender":"남","age":13,"job":"학생","referral_source":"유튜브","reason":"AI에 대해 배우고 싶어서 신청했습니다 정말로요","ai_level":"입문","plan_type":"basic"})
results.append(test("age=13 차단", not r["ok"]))
results.append(test("에러 메시지 포함", any("14" in e or "미만" in e for e in r["errors"])))

print("\n══ 2. reason 19자 → 차단 ══")
r = validate({"name":"홍길동","email":"a@b.com","phone":"010-1234-5678","gender":"남","age":20,"job":"직장인","referral_source":"유튜브","reason":"1234567890123456789","ai_level":"입문","plan_type":"basic"})
results.append(test("reason 19자 차단", not r["ok"]))

print("\n══ 3. 필수 항목 누락 ══")
r = validate({"name":"","email":"","phone":"","gender":"","age":20,"job":"","referral_source":"","reason":"","ai_level":"","plan_type":""})
results.append(test("필수 누락 → 에러 반환", not r["ok"] and len(r["errors"]) > 0))

print("\n══ 4. SQL Injection 차단 ══")
r = check_security({"name":"'; DROP TABLE members; --","email":"a@b.com","phone":"010-1111-2222","reason":"test"})
results.append(test("SQL injection 차단", not r["ok"]))

print("\n══ 5. XSS 차단 ══")
r = check_security({"name":"<script>alert(1)</script>","email":"a@b.com","phone":"010-1111-2222","reason":"test"})
results.append(test("XSS 차단", not r["ok"]))

print("\n══ 6. 암호화 ══")
phone = "010-9999-1234"
enc = encrypt_phone(phone)
dec = decrypt_phone(enc)
results.append(test("전화번호 암호화/복호화", dec == phone))
results.append(test("마스킹", mask_phone(phone) == "010-****-1234"))

print("\n══ 7. 정상 basic 신청 ══")
base_data = {
    "name": "테스트유저",
    "email_encrypted": encrypt_email("test@test.com"),
    "email_hash": hash_email("test@test.com"),
    "phone_masked": mask_phone("010-1111-2222"),
    "phone_encrypted": encrypt_phone("010-1111-2222"),
    "phone_hash": hash_phone("010-1111-2222"),
    "gender": "남",
    "age": 25,
    "job": "개발자",
    "referral_source": "유튜브",
    "reason": "AI 기술을 배우고 활용하고 싶어서 신청합니다",
    "ai_level": "초급",
    "plan_type": "basic",
    "consent_personal": True,
    "consent_marketing": False,
    "consent_at": "2026-04-13T00:00:00+00:00",
    "consent_version": "1.0",
    "participation_grade": "🌱 새싹",
}
mid = create_member(base_data)
member = get_member(mid)
results.append(test("DB 저장 확인", member is not None))
results.append(test("상태 pending", member["status"] == "pending"))
results.append(test("등급 저장", member["participation_grade"] == "🌱 새싹"))
log_action(mid, "apply", "test", "127.0.0.1")

print("\n══ 8. 중복 전화번호 차단 ══")
r = check_duplicate({"phone": "010-1111-2222", "email": "different@test.com"})
results.append(test("중복 전화번호 차단", not r["ok"]))

print("\n══ 9. full 신청 + 등급 계산 ══")
full_data = {
    **base_data,
    "name": "풀신청자",
    "email_encrypted": encrypt_email("full@test.com"),
    "email_hash": hash_email("full@test.com"),
    "phone_masked": mask_phone("010-2222-3333"),
    "phone_encrypted": encrypt_phone("010-2222-3333"),
    "phone_hash": hash_phone("010-2222-3333"),
    "plan_type": "full",
    "ai_tools": '["ChatGPT","Claude"]',
    "ai_subscription": "ChatGPT Plus",
    "ai_weekly_hours": "3-5시간",
    "ai_use_cases": '["코딩","분석"]',
    "group_goals": '["배움","네트워킹"]',
    "short_term_goal": "AI 자동화 마스터하기",
    "participation_grade": "⭐ 적극",
}
mid2 = create_member(full_data)
m2 = get_member(mid2)
results.append(test("full 신청 저장", m2 is not None))
results.append(test("등급 ⭐ 적극 저장", m2["participation_grade"] == "⭐ 적극"))

print("\n══ 10. 승인 → 코드 생성 ══")
update_status(mid, "approved")
code = generate_code(mid)
results.append(test("코드 생성 (8자리)", len(code) == 8))
results.append(test("상태 approved", get_member(mid)["status"] == "approved"))

print("\n══ 11. 코드 검증 ══")
r = verify_code(code, mid)
results.append(test("올바른 코드 → 성공", r["ok"]))
r2 = verify_code("WRONGCOD", mid)
results.append(test("틀린 코드 → 실패", not r2["ok"]))

print("\n══ 12. 코드 5회 실패 → 잠금 ══")
for _ in range(5):
    verify_code("XXXXXXXX", mid)
lock = check_lock(mid)
results.append(test("5회 실패 후 잠금", lock.get("locked", False)))

print("\n══ 13. 거절 ══")
update_status(mid2, "rejected", "참여 요건 미충족")
m2 = get_member(mid2)
results.append(test("거절 상태 저장", m2["status"] == "rejected"))
results.append(test("거절 사유 저장", m2["rejection_reason"] == "참여 요건 미충족"))

print("\n══ 14. 블랙리스트 재신청 차단 ══")
# 새 멤버 등록 후 블랙리스트
bl_data = {
    **base_data,
    "name": "블랙리스트",
    "email_encrypted": encrypt_email("black@test.com"),
    "email_hash": hash_email("black@test.com"),
    "phone_masked": mask_phone("010-9876-5432"),
    "phone_encrypted": encrypt_phone("010-9876-5432"),
    "phone_hash": hash_phone("010-9876-5432"),
    "participation_grade": "🌱 새싹",
}
mid3 = create_member(bl_data)
blacklist_member(mid3)
r = check_duplicate({"phone": "010-9876-5432", "email": "black@test.com"})
results.append(test("블랙리스트 재신청 차단", not r["ok"]))

print("\n══ 15. 참여 등급 계산 ══")
from main import _grade_count
d0 = {}
d6 = {"ai_tools": ["ChatGPT"], "ai_subscription": "Plus", "ai_weekly_hours": "3-5시간", "ai_use_cases": ["코딩"], "group_goals": ["배움"], "short_term_goal": "목표"}
d14 = {"ai_tools": ["ChatGPT"], "ai_subscription": "Plus", "ai_weekly_hours": "5시간 이상", "ai_use_cases": ["코딩"], "group_goals": ["배움"], "short_term_goal": "목표", "participation_type": "온라인", "preferred_schedule": "주말", "region": "서울", "main_device": "맥", "can_code": True, "can_present": False, "skills": "개발", "contribution": "강의"}
results.append(test("0개 → 🌱 새싹", _grade_count(d0) == "🌱 새싹"))
results.append(test("6개 → ⭐ 적극", _grade_count(d6) == "⭐ 적극"))
results.append(test("14개 → 👑 마스터", _grade_count(d14) == "👑 마스터"))

print("\n══ 16. 통계 ══")
stats = get_stats()
results.append(test("통계 조회", stats["total"] >= 3))
results.append(test("등급별 통계", isinstance(stats["grades"], dict)))

print(f"\n{'='*40}")
passed = sum(results)
total = len(results)
print(f"결과: {passed}/{total} 통과 {'🎉' if passed == total else '⚠️'}")
if passed < total:
    print(f"실패: {total - passed}개")
