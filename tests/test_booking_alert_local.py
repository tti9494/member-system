"""
강의 신청/예약 Telegram 알림 로컬 테스트
- 네트워크 호출 없음: httpx.post 전부 mock
- DB 없음: log_action 의존 케이스만 임시 DB 사용
- Telegram/Kakao/SMS 실발송 없음
- 기존 test_hermes_status.py 의 patch.object 패턴 그대로 사용
"""

import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import db
from agents import db_manager, telegram_notifier

MOCK_PATCHES = dict(
    TELEGRAM_NOTIFY_ENABLED=True,
    TELEGRAM_BOOKING_NOTIFY_ENABLED=True,
    TELEGRAM_APPLICATION_NOTIFY_ENABLED=True,
    BOT_TOKEN="mock-token",
    ADMIN_CHAT_ID="mock-chat",
)

OK_RESPONSE = Mock(status_code=200)


def _active_patches(**overrides):
    """모든 필수 모듈 변수를 mock으로 교체하는 context 반환."""
    cfg = {**MOCK_PATCHES, **overrides}
    return [patch.object(telegram_notifier, k, v) for k, v in cfg.items()]


def _realistic_booking(**overrides) -> dict:
    base = {
        "id": "booking-test-1",
        "applicant_name": "홍길동",
        "phone_masked": "010-1234-5678",
        "session_title": "AI 기초 셋팅 강의",
        "session_starts_at": "2026-05-17T10:00:00+09:00",
        "session_ends_at": "2026-05-17T12:00:00+09:00",
        "status": "requested",
        "payment_status": "not_sent",
        "payment_amount_krw": 50000,
        "request_rank": 1,
        "paid_rank": None,
        "desired_outcome": "이 원문 목표는 알림에 포함 금지",
        "preparedness": "이 준비상태 원문도 알림에 포함 금지",
    }
    base.update(overrides)
    return base


class ApplyAlertLocalTest(unittest.TestCase):
    """신청(apply) 알림 — notify_admin_new_apply"""

    def _patches(self, **overrides):
        return _active_patches(**overrides)

    def test_apply_alert_without_booking_uses_not_requested_status(self):
        """booking=None 이면 예약상태 'not_requested' 로 표시되어야 한다."""
        member = {"id": "m-1", "name": "홍길동", "phone_masked": "010-1234-5678", "status": "pending"}
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            result = telegram_notifier.notify_admin_new_apply(member, booking=None)

        self.assertEqual(result, "ok")
        text = post.call_args.kwargs["json"]["text"]
        self.assertIn("not_requested", text)
        self.assertNotIn("booking-", text)

    def test_apply_alert_includes_applicant_name_and_phone(self):
        """신청 알림 본문에 운영자가 확인할 신청자 이름·연락처가 포함되어야 한다."""
        member = {"id": "m-2", "name": "홍길동", "phone_masked": "010-1234-5678", "status": "pending"}
        booking = {"id": "booking-x", "status": "requested"}
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            telegram_notifier.notify_admin_new_apply(member, booking=booking)

        text = post.call_args.kwargs["json"]["text"]
        self.assertIn("홍길동", text)
        self.assertIn("010-1234-5678", text)

    def test_apply_alert_includes_booking_id_and_status(self):
        """신청 알림에 예약 ID와 예약 상태가 포함되어야 한다."""
        member = {"id": "m-3", "name": "김민수", "phone_masked": "010-9999-0001", "status": "pending"}
        booking = {"id": "booking-abc", "status": "requested"}
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            telegram_notifier.notify_admin_new_apply(member, booking=booking)

        text = post.call_args.kwargs["json"]["text"]
        self.assertIn("booking-abc", text)
        self.assertIn("requested", text)
        self.assertIn("m-3", text)

    def test_apply_alert_application_switch_off_disables_even_when_booking_on(self):
        """TELEGRAM_APPLICATION_NOTIFY_ENABLED=False 이면 신청 알림은 disabled."""
        member = {"id": "m-4", "name": "박철수", "phone_masked": "010-5555-0001", "status": "pending"}
        patches = self._patches(TELEGRAM_APPLICATION_NOTIFY_ENABLED=False)
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post") as post,
        ):
            result = telegram_notifier.notify_admin_new_apply(member)

        self.assertEqual(result, "disabled")
        post.assert_not_called()

    def test_apply_alert_storage_status_param_does_not_leak_to_message(self):
        """storage_status dict 값이 Telegram 메시지에 포함되지 않아야 한다."""
        member = {"id": "m-5", "name": "이영희", "phone_masked": "010-7777-0001", "status": "pending"}
        storage_status = {"hermes": {"configured": True}, "secret_key": "SHOULD_NOT_APPEAR"}
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            telegram_notifier.notify_admin_new_apply(member, storage_status=storage_status)

        text = post.call_args.kwargs["json"]["text"]
        self.assertNotIn("SHOULD_NOT_APPEAR", text)
        self.assertNotIn("secret_key", text)


class BookingAlertLocalTest(unittest.TestCase):
    """예약 알림 — notify_booking_requested / _payment_guide / _payment_confirmed"""

    def _patches(self, **overrides):
        return _active_patches(**overrides)

    def test_booking_requested_message_header(self):
        """예약 신청 알림은 'ARSEN 신규 예약 신청' 헤더를 가져야 한다."""
        booking = _realistic_booking()
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            result = telegram_notifier.notify_booking_requested({}, booking)

        self.assertEqual(result, "ok")
        text = post.call_args.kwargs["json"]["text"]
        self.assertIn("ARSEN 신규 예약 신청", text)

    def test_booking_payment_guide_message_header(self):
        """입금 안내 알림은 'ARSEN 입금 안내 처리' 헤더를 가져야 한다."""
        booking = _realistic_booking(status="payment_guide_sent", payment_status="guide_sent")
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            result = telegram_notifier.notify_booking_payment_guide(booking)

        self.assertEqual(result, "ok")
        text = post.call_args.kwargs["json"]["text"]
        self.assertIn("ARSEN 입금 안내 처리", text)

    def test_booking_payment_confirmed_message_header(self):
        """입금 확인 알림은 'ARSEN 입금 확인/예약 확정' 헤더를 가져야 한다."""
        booking = _realistic_booking(status="confirmed", payment_status="paid", paid_rank=1)
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            result = telegram_notifier.notify_booking_payment_confirmed(booking)

        self.assertEqual(result, "ok")
        text = post.call_args.kwargs["json"]["text"]
        self.assertIn("ARSEN 입금 확인/예약 확정", text)

    def test_booking_amount_formatted_with_comma(self):
        """결제 금액 50000 → '50,000원' 형식으로 포맷되어야 한다."""
        booking = _realistic_booking(payment_amount_krw=50000)
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            telegram_notifier.notify_booking_requested({}, booking)

        text = post.call_args.kwargs["json"]["text"]
        self.assertIn("50,000원", text)

    def test_booking_request_rank_displayed(self):
        """신청 순서(request_rank)가 메시지에 포함되어야 한다."""
        booking = _realistic_booking(request_rank=2, paid_rank=None)
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            telegram_notifier.notify_booking_requested({}, booking)

        text = post.call_args.kwargs["json"]["text"]
        self.assertIn("신청 2", text)
        self.assertIn("입금확정 -", text)

    def test_booking_paid_rank_displayed_after_confirmation(self):
        """입금 확정 후 paid_rank가 메시지에 포함되어야 한다."""
        booking = _realistic_booking(status="confirmed", payment_status="paid", request_rank=1, paid_rank=1)
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            telegram_notifier.notify_booking_payment_confirmed(booking)

        text = post.call_args.kwargs["json"]["text"]
        self.assertIn("입금확정 1", text)

    def test_booking_session_title_in_all_three_alerts(self):
        """세션 제목이 3개 예약 알림 모두에 포함되어야 한다."""
        booking = _realistic_booking()
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            telegram_notifier.notify_booking_requested({}, booking)
            telegram_notifier.notify_booking_payment_guide(booking)
            telegram_notifier.notify_booking_payment_confirmed(booking)

        for call in post.call_args_list:
            text = call.kwargs["json"]["text"]
            self.assertIn("AI 기초 셋팅 강의", text)

    def test_booking_korean_datetime_in_all_three_alerts(self):
        """한국어 날짜/시간 형식이 3개 예약 알림 모두에 포함되어야 한다."""
        booking = _realistic_booking()
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            telegram_notifier.notify_booking_requested({}, booking)
            telegram_notifier.notify_booking_payment_guide(booking)
            telegram_notifier.notify_booking_payment_confirmed(booking)

        for call in post.call_args_list:
            text = call.kwargs["json"]["text"]
            self.assertIn("오전 10시", text)
            self.assertNotIn("T10", text)
            self.assertNotIn("+09:00", text)

    def test_booking_free_text_fields_excluded_from_all_alerts(self):
        """desired_outcome, preparedness 원문은 3개 알림 모두에서 제외되어야 한다."""
        booking = _realistic_booking()
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            telegram_notifier.notify_booking_requested({}, booking)
            telegram_notifier.notify_booking_payment_guide(booking)
            telegram_notifier.notify_booking_payment_confirmed(booking)

        for call in post.call_args_list:
            text = call.kwargs["json"]["text"]
            self.assertNotIn("이 원문 목표", text)
            self.assertNotIn("이 준비상태 원문", text)
            self.assertNotIn("desired_outcome", text)

    def test_full_flow_sends_exactly_three_http_calls_with_distinct_headers(self):
        """신청→안내→확정 전체 흐름에서 HTTP POST가 3회, 헤더가 각각 다르게 전송."""
        booking = _realistic_booking()
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            telegram_notifier.notify_booking_requested({}, booking)
            telegram_notifier.notify_booking_payment_guide(booking)
            telegram_notifier.notify_booking_payment_confirmed(booking)

        self.assertEqual(post.call_count, 3)
        texts = [call.kwargs["json"]["text"] for call in post.call_args_list]
        self.assertIn("ARSEN 신규 예약 신청", texts[0])
        self.assertIn("ARSEN 입금 안내 처리", texts[1])
        self.assertIn("ARSEN 입금 확인/예약 확정", texts[2])

    def test_booking_switch_off_blocks_booking_not_apply(self):
        """TELEGRAM_BOOKING_NOTIFY_ENABLED=False 이면 예약 알림 disabled, 신청 알림은 통과."""
        member = {"id": "m-sw", "name": "스위치", "phone_masked": "010-0000-0001", "status": "pending"}
        booking = _realistic_booking()
        patches = self._patches(TELEGRAM_BOOKING_NOTIFY_ENABLED=False)
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            apply_result = telegram_notifier.notify_admin_new_apply(member)
            booking_result = telegram_notifier.notify_booking_requested({}, booking)

        self.assertEqual(apply_result, "ok")
        self.assertEqual(booking_result, "disabled")
        self.assertEqual(post.call_count, 1)

    def test_booking_missing_session_fields_safe(self):
        """session_title, session_starts_at 없어도 예외 없이 알림 전송되어야 한다."""
        booking = _realistic_booking(session_title=None, session_starts_at=None, session_ends_at=None)
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            result = telegram_notifier.notify_booking_requested({}, booking)

        self.assertEqual(result, "ok")
        text = post.call_args.kwargs["json"]["text"]
        self.assertIn("예약ID: booking-test-1", text)

    def test_booking_global_switch_off_booking_switch_on_still_sends(self):
        """TELEGRAM_NOTIFY_ENABLED=False 이지만 TELEGRAM_BOOKING_NOTIFY_ENABLED=True 이면 발송."""
        booking = _realistic_booking()
        patches = self._patches(TELEGRAM_NOTIFY_ENABLED=False, TELEGRAM_BOOKING_NOTIFY_ENABLED=True)
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE) as post,
        ):
            result = telegram_notifier.notify_booking_requested({}, booking)

        self.assertEqual(result, "ok")
        post.assert_called_once()

    def test_booking_http_500_returns_failed(self):
        """HTTP 500 응답 시 'failed' 반환, 예외 없어야 한다."""
        booking = _realistic_booking()
        patches = self._patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=Mock(status_code=500)),
        ):
            result = telegram_notifier.notify_booking_requested({}, booking)

        self.assertEqual(result, "failed")


class BookingAlertLogIntegrationTest(unittest.TestCase):
    """알림 상태가 member_logs 에 기록되는지 DB 통합 검증 (임시 DB 사용)."""

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.tmpdir.name) / "members.db"
        self.original_db_path = db.DB_PATH
        self.original_manager_db_path = db_manager.DB_PATH
        db.DB_PATH = self.db_path
        db_manager.DB_PATH = self.db_path
        db.init_db()

    def tearDown(self):
        db.DB_PATH = self.original_db_path
        db_manager.DB_PATH = self.original_manager_db_path
        self.tmpdir.cleanup()

    def _insert_member(self, member_id="member-log-1"):
        conn = sqlite3.connect(str(self.db_path))
        conn.execute(
            """
            INSERT INTO members (
                id, name, email_encrypted, phone_masked, phone_encrypted,
                gender, age, job, referral_source, reason, ai_level, plan_type,
                consent_personal, consent_at, consent_version, created_at
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                member_id, "로그테스트", "enc-email", "010-****-9999", "enc-phone",
                "남", 28, "개발자", "검색", "테스트 사유", "입문", "basic",
                1, "2026-05-17T00:00:00+00:00", "1.0", "2026-05-17T00:00:00+00:00",
            ),
        )
        conn.commit()
        conn.close()
        return member_id

    def _fetch_last_log(self, member_id: str, action: str) -> str | None:
        conn = sqlite3.connect(str(self.db_path))
        row = conn.execute(
            "SELECT detail FROM member_logs WHERE member_id=? AND action=? ORDER BY created_at DESC LIMIT 1",
            (member_id, action),
        ).fetchone()
        conn.close()
        return row[0] if row else None

    def test_apply_alert_disabled_status_can_be_logged(self):
        """신청 알림 disabled 상태를 member_logs에 기록할 수 있어야 한다."""
        member_id = self._insert_member()
        member = {"id": member_id, "name": "로그테스트", "phone_masked": "010-****-9999", "status": "pending"}
        patches = _active_patches(TELEGRAM_APPLICATION_NOTIFY_ENABLED=False)
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post") as post,
        ):
            status = telegram_notifier.notify_admin_new_apply(member)

        self.assertEqual(status, "disabled")
        post.assert_not_called()
        db_manager.log_action(member_id, "hermes_notify", status, "127.0.0.1")
        self.assertEqual(self._fetch_last_log(member_id, "hermes_notify"), "disabled")

    def test_booking_alert_ok_status_can_be_logged(self):
        """예약 알림 ok 상태를 booking_telegram_notify 액션으로 기록할 수 있어야 한다."""
        member_id = self._insert_member("member-log-2")
        booking = _realistic_booking()
        patches = _active_patches()
        with (
            patches[0], patches[1], patches[2], patches[3], patches[4],
            patch.object(telegram_notifier.httpx, "post", return_value=OK_RESPONSE),
        ):
            status = telegram_notifier.notify_booking_requested({}, booking)

        self.assertEqual(status, "ok")
        db_manager.log_action(member_id, "booking_telegram_notify", status, "127.0.0.1")
        self.assertEqual(self._fetch_last_log(member_id, "booking_telegram_notify"), "ok")


if __name__ == "__main__":
    unittest.main()
