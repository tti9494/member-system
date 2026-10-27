"""Test ARSEN 3기 수강생 접수·운영 자동화 파이프라인.

검증 항목:
1. 3기 4주 토요일 세션 시드 생성 (정원 3~8명, 25만원, 180분)
2. 수강 신청 접수 (암호화, 마스킹, 슬랙 알림 메시지 생성)
3. 개인정보 노출 방지 안전 검사 (슬랙 메시지에 원본 전화번호 노출 차단)
4. 입금 확인 및 수강 확정 (booking_status=confirmed, payment_status=paid)
5. 정원 확정 인원(confirmed_count) 정확한 증가
6. 수강생 명부(roster) 안전 조회
"""

import sys
import tempfile
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import db
from agents import db_manager, booking_manager
from scripts.arsen_3rd_automation_pipeline import (
    seed_arsen_3rd_sessions,
    process_arsen_3rd_application,
    confirm_arsen_3rd_payment,
    get_arsen_3rd_roster,
    ARSEN_3RD_PRICE,
    ARSEN_3RD_CAPACITY_MAX,
)


@pytest.fixture(autouse=True)
def isolated_db(monkeypatch):
    """각 테스트마다 격리된 임시 SQLite DB를 사용합니다."""
    with tempfile.TemporaryDirectory(prefix="arsen-3rd-test-") as tmpdir:
        test_db = Path(tmpdir) / "test_members.db"
        monkeypatch.setattr(db, "DB_PATH", test_db)
        monkeypatch.setattr(db_manager, "DB_PATH", test_db)
        db.init_db()
        yield test_db


def test_seed_arsen_3rd_sessions():
    sessions = seed_arsen_3rd_sessions(weeks=4)
    assert len(sessions) == 4
    for idx, s in enumerate(sessions):
        assert f"{idx + 1}주차" in s["title"]
        assert s["price_krw"] == ARSEN_3RD_PRICE
        assert s["capacity_max"] == ARSEN_3RD_CAPACITY_MAX
        assert s["status"] == "open"
        assert s["program_type"] == "arsen_paid_beginner_3"


def test_process_arsen_3rd_application():
    raw_phone = "010-9876-5432"
    raw_name = "김수강"
    raw_email = "student.kim@example.com"

    sessions = seed_arsen_3rd_sessions(weeks=1)
    session_id = sessions[0]["id"]

    result = process_arsen_3rd_application(
        name=raw_name,
        phone=raw_phone,
        email=raw_email,
        session_id=session_id,
        job="기획자",
        desired_outcome="업무 자동화 및 숏폼 제작",
    )

    assert result["ok"] is True
    assert result["applicant_name"] == raw_name
    assert result["phone_masked"] == "010-****-5432"

    # 개인정보 안전 검사: 슬랙 알림과 안내문에 원본 전화번호 노출 금지
    assert raw_phone not in result["slack_notification"]
    assert "010-****-5432" in result["slack_notification"]
    assert "신규 수강 신청 접수" in result["slack_notification"]

    # DB 저장 상태 확인
    booking = booking_manager.get_booking(result["booking_id"])
    assert booking is not None
    assert booking["status"] == "payment_guide_sent"
    assert booking["payment_status"] == "guide_sent"


def test_confirm_arsen_3rd_payment():
    sessions = seed_arsen_3rd_sessions(weeks=1)
    session_id = sessions[0]["id"]

    app_res = process_arsen_3rd_application(
        name="이실습",
        phone="010-1111-2222",
        email="lee@example.com",
        session_id=session_id,
    )
    booking_id = app_res["booking_id"]

    confirm_res = confirm_arsen_3rd_payment(booking_id, operator_note="국민은행 입금 확인")
    assert confirm_res["ok"] is True
    assert confirm_res["confirmed_count"] == 1
    assert "수강 확정 완료" in confirm_res["confirmation_notice"]

    # 세션 확정 수치 확인
    sess = booking_manager.get_session(session_id)
    assert sess["confirmed_booking_count"] == 1

    # 명부 확인
    roster = get_arsen_3rd_roster(session_id)
    assert len(roster) == 1
    assert roster[0]["status"] == "confirmed"
    assert roster[0]["payment_status"] == "paid"
