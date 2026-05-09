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


class HermesStatusTest(unittest.TestCase):
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

    def _insert_member(self, member_id="member-1"):
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
                member_id,
                "테스트",
                "encrypted-email",
                "010-****-1234",
                "encrypted-phone",
                "남",
                30,
                "운영자",
                "검색",
                "상태 확인 테스트 신청입니다",
                "입문",
                "basic",
                1,
                "2026-05-09T00:00:00+00:00",
                "1.0",
                "2026-05-09T00:00:00+00:00",
            ),
        )
        conn.commit()
        conn.close()
        return member_id

    def test_send_status_not_configured_does_not_post(self):
        with patch.object(telegram_notifier, "TELEGRAM_NOTIFY_ENABLED", True), patch.object(
            telegram_notifier, "BOT_TOKEN", ""
        ), patch.object(
            telegram_notifier, "ADMIN_CHAT_ID", ""
        ), patch.object(telegram_notifier.httpx, "post") as post:
            self.assertEqual(telegram_notifier._send_status("", "message"), "not_configured")
            post.assert_not_called()

    def test_send_status_disabled_does_not_post_even_when_configured(self):
        with patch.object(telegram_notifier, "TELEGRAM_NOTIFY_ENABLED", False), patch.object(
            telegram_notifier, "BOT_TOKEN", "token"
        ), patch.object(
            telegram_notifier, "ADMIN_CHAT_ID", "chat"
        ), patch.object(telegram_notifier.httpx, "post") as post:
            self.assertEqual(telegram_notifier._send_status("chat", "message"), "disabled")
            post.assert_not_called()

    def test_send_status_success_and_failure_are_distinct(self):
        with patch.object(telegram_notifier, "TELEGRAM_NOTIFY_ENABLED", True), patch.object(
            telegram_notifier, "BOT_TOKEN", "token"
        ), patch.object(
            telegram_notifier, "ADMIN_CHAT_ID", "chat"
        ):
            with patch.object(telegram_notifier.httpx, "post", return_value=Mock(status_code=200)):
                self.assertEqual(telegram_notifier._send_status("chat", "message"), "ok")
            with patch.object(telegram_notifier.httpx, "post", return_value=Mock(status_code=500)):
                self.assertEqual(telegram_notifier._send_status("chat", "message"), "failed")

    def test_new_apply_notification_is_minimal_and_masked(self):
        member = {
            "id": "member-1",
            "name": "홍길동",
            "phone_masked": "010-****-5678",
            "status": "pending",
            "reason": "원문 신청 이유는 알림에 포함되면 안 됩니다",
        }
        booking = {"id": "booking-1", "status": "requested"}
        with patch.object(telegram_notifier, "TELEGRAM_NOTIFY_ENABLED", True), patch.object(
            telegram_notifier, "BOT_TOKEN", "token"
        ), patch.object(
            telegram_notifier, "ADMIN_CHAT_ID", "chat"
        ), patch.object(telegram_notifier.httpx, "post", return_value=Mock(status_code=200)) as post:
            self.assertEqual(telegram_notifier.notify_admin_new_apply(member, booking=booking), "ok")

        text = post.call_args.kwargs["json"]["text"]
        self.assertIn("홍*동", text)
        self.assertIn("010-****-5678", text)
        self.assertIn("member-1", text)
        self.assertIn("pending", text)
        self.assertIn("booking-1", text)
        self.assertIn("requested", text)
        self.assertNotIn("홍길동", text)
        self.assertNotIn("원문 신청 이유", text)

    def test_storage_status_exposes_latest_hermes_log_per_application(self):
        member_id = self._insert_member()
        db_manager.log_action(member_id, "apply", "plan=basic", "127.0.0.1")
        db_manager.log_action(member_id, "hermes_notify", "not_configured", "127.0.0.1")

        with patch.object(db_manager, "TELEGRAM_NOTIFY_ENABLED", False), patch.object(
            db_manager, "TELEGRAM_BOT_TOKEN", ""
        ), patch.object(
            db_manager, "TELEGRAM_ADMIN_CHAT_ID", ""
        ):
            status = db_manager.get_storage_status(limit=1)

        self.assertFalse(status["hermes"]["configured"])
        self.assertFalse(status["hermes"]["enabled"])
        self.assertFalse(status["hermes"]["active"])
        self.assertEqual(status["hermes"]["status"], "OFF")
        self.assertEqual(status["hermes"]["mode"], "not_configured")
        self.assertEqual(status["recent"][0]["id"], member_id)
        self.assertEqual(status["recent"][0]["hermes_status"], "not_configured")
        self.assertIsNotNone(status["recent"][0]["hermes_checked_at"])

    def test_operator_health_contains_only_public_summary(self):
        member_id = self._insert_member()
        conn = sqlite3.connect(str(self.db_path))
        conn.execute(
            """
            INSERT INTO sessions (
                id, title, program_type, audience_level, starts_at, ends_at,
                timezone, capacity_min, capacity_max, confirmed_count, price_krw,
                location, status, created_at, updated_at
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                "session-1",
                "공개 일정",
                "ai_basic_setup",
                "all",
                "2026-05-10T10:00:00+09:00",
                "2026-05-10T12:00:00+09:00",
                "Asia/Seoul",
                4,
                5,
                0,
                50000,
                "서울",
                "open",
                "2026-05-09T00:00:00+00:00",
                "2026-05-09T00:00:00+00:00",
            ),
        )
        conn.execute(
            """
            INSERT INTO bookings (
                id, session_id, member_id, applicant_name, phone_masked,
                status, payment_status, payment_amount_krw, created_at, updated_at
            ) VALUES (?,?,?,?,?,?,?,?,?,?)
            """,
            (
                "booking-1",
                "session-1",
                member_id,
                "테스트",
                "010-****-1234",
                "requested",
                "not_sent",
                50000,
                "2026-05-09T00:00:00+00:00",
                "2026-05-09T00:00:00+00:00",
            ),
        )
        conn.commit()
        conn.close()
        db_manager.log_action(
            "system",
            "db_backup",
            '{"ok_count": 1, "failed_count": 0, "targets": [{"name": "local", "status": "ok"}]}',
            "127.0.0.1",
        )

        status = db_manager.get_operator_health()
        status_text = str(status)

        self.assertTrue(status["server"]["alive"])
        self.assertEqual(status["public_sessions"]["count"], 1)
        self.assertEqual(status["application_system"]["status"], "accepting")
        self.assertEqual(status["application_system"]["requested_booking_count"], 1)
        self.assertTrue(status["backup"]["last_success"])
        self.assertNotIn("테스트", status_text)
        self.assertNotIn("010-****-1234", status_text)
        self.assertNotIn("encrypted", status_text)
        self.assertNotIn("targets", status_text)

    def test_storage_snapshot_is_masked_read_only_summary(self):
        member_id = self._insert_member()
        conn = sqlite3.connect(str(self.db_path))
        conn.execute(
            """
            INSERT INTO bookings (
                id, session_id, member_id, applicant_name, phone_masked,
                desired_outcome, preparedness, status, payment_status,
                payment_amount_krw, created_at, updated_at
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                "booking-1",
                None,
                member_id,
                "테스트",
                "010-****-1234",
                "민감한 자유입력 목표 원문",
                "민감한 준비상태 원문",
                "requested",
                "not_sent",
                50000,
                "2026-05-09T00:00:00+00:00",
                "2026-05-09T00:00:00+00:00",
            ),
        )
        conn.commit()
        conn.close()

        snapshot = db_manager.get_storage_snapshot(limit=10)
        snapshot_text = str(snapshot)

        self.assertEqual(snapshot["storage"]["mode"], "sqlite_file")
        self.assertEqual(snapshot["storage"]["path"], str(self.db_path))
        self.assertEqual(snapshot["counts"]["members"], 1)
        self.assertEqual(snapshot["counts"]["bookings"], 1)
        self.assertEqual(snapshot["recent"][0]["member_id"], member_id)
        self.assertEqual(snapshot["recent"][0]["applicant"], "테*트")
        self.assertEqual(snapshot["recent"][0]["phone_masked"], "010-****-1234")
        self.assertNotIn("encrypted-email", snapshot_text)
        self.assertNotIn("encrypted-phone", snapshot_text)
        self.assertNotIn("민감한 자유입력", snapshot_text)
        self.assertNotIn("민감한 준비상태", snapshot_text)


if __name__ == "__main__":
    unittest.main()
