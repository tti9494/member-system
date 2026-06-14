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

    def _log_and_fetch_hermes_status(self, member_id, status):
        db_manager.log_action(member_id, "hermes_notify", status, "127.0.0.1")
        conn = sqlite3.connect(str(self.db_path))
        row = conn.execute(
            """
            SELECT detail
            FROM member_logs
            WHERE member_id=? AND action='hermes_notify'
            ORDER BY created_at DESC
            LIMIT 1
            """,
            (member_id,),
        ).fetchone()
        conn.close()
        return row[0] if row else None

    def _assert_no_storage_pii(self, payload, forbidden_values):
        payload_text = str(payload)
        for value in forbidden_values:
            self.assertNotIn(value, payload_text)

    def test_send_status_not_configured_does_not_post(self):
        with patch.object(telegram_notifier, "TELEGRAM_NOTIFY_ENABLED", True), patch.object(
            telegram_notifier, "BOT_TOKEN", ""
        ), patch.object(
            telegram_notifier, "ADMIN_CHAT_ID", ""
        ), patch.object(telegram_notifier.httpx, "post") as post, self.assertLogs(
            "member-system", level="INFO"
        ) as logs:
            self.assertEqual(telegram_notifier._send_status("", "message"), "not_configured")
            post.assert_not_called()
        self.assertTrue(any("not_configured" in line for line in logs.output))

    def test_send_status_disabled_does_not_post_even_when_configured(self):
        with patch.object(telegram_notifier, "TELEGRAM_NOTIFY_ENABLED", False), patch.object(
            telegram_notifier, "BOT_TOKEN", "token"
        ), patch.object(
            telegram_notifier, "ADMIN_CHAT_ID", "chat"
        ), patch.object(telegram_notifier.httpx, "post") as post, self.assertLogs(
            "member-system", level="INFO"
        ) as logs:
            self.assertEqual(telegram_notifier._send_status("chat", "message"), "disabled")
            post.assert_not_called()
        self.assertTrue(any("disabled" in line for line in logs.output))

    def test_send_status_success_and_failure_are_distinct(self):
        with patch.object(telegram_notifier, "TELEGRAM_NOTIFY_ENABLED", True), patch.object(
            telegram_notifier, "TELEGRAM_BOOKING_NOTIFY_ENABLED", True
        ), patch.object(
            telegram_notifier, "BOT_TOKEN", "token"
        ), patch.object(
            telegram_notifier, "ADMIN_CHAT_ID", "chat"
        ):
            with patch.object(telegram_notifier.httpx, "post", return_value=Mock(status_code=200)):
                self.assertEqual(telegram_notifier._send_status("chat", "message"), "ok")
            with patch.object(telegram_notifier.httpx, "post", return_value=Mock(status_code=500)):
                self.assertEqual(telegram_notifier._send_status("chat", "message"), "failed")

    def test_new_apply_notification_includes_operator_fields_and_buttons(self):
        member = {
            "id": "member-1",
            "name": "홍길동",
            "phone_masked": "010-1234-5678",
            "status": "pending",
            "plan_type": "full",
            "participation_grade": "starter",
            "job": "운영자",
            "referral_source": "검색",
            "reason": "강의 신청 이유입니다",
            "short_term_goal": "업무 자동화를 배우고 싶습니다",
        }
        booking = {"id": "booking-1", "status": "requested"}
        with patch.object(telegram_notifier, "TELEGRAM_NOTIFY_ENABLED", True), patch.object(
            telegram_notifier, "TELEGRAM_BOOKING_NOTIFY_ENABLED", True
        ), patch.object(
            telegram_notifier, "TELEGRAM_APPLICATION_NOTIFY_ENABLED", True
        ), patch.object(
            telegram_notifier, "BOT_TOKEN", "token"
        ), patch.object(
            telegram_notifier, "ADMIN_CHAT_ID", "chat"
        ), patch.object(telegram_notifier.httpx, "post", return_value=Mock(status_code=200)) as post:
            self.assertEqual(telegram_notifier.notify_admin_new_apply(member, booking=booking), "ok")

        text = post.call_args.kwargs["json"]["text"]
        self.assertIn("홍길동", text)
        self.assertIn("010-1234-5678", text)
        self.assertIn("member-1", text)
        self.assertIn("pending", text)
        self.assertIn("booking-1", text)
        self.assertIn("requested", text)
        self.assertIn("신청 이유: 강의 신청 이유입니다", text)
        self.assertIn("단기 목표: 업무 자동화를 배우고 싶습니다", text)
        self.assertEqual(
            post.call_args.kwargs["json"]["reply_markup"]["inline_keyboard"][0][0]["callback_data"],
            "arsen:approve:member-1",
        )

    def test_new_apply_notification_can_follow_application_switch_when_global_off(self):
        member = {
            "id": "member-1",
            "name": "홍길동",
            "phone_masked": "010-1234-5678",
            "status": "pending",
        }
        with patch.object(telegram_notifier, "TELEGRAM_NOTIFY_ENABLED", False), patch.object(
            telegram_notifier, "TELEGRAM_BOOKING_NOTIFY_ENABLED", True
        ), patch.object(
            telegram_notifier, "TELEGRAM_APPLICATION_NOTIFY_ENABLED", True
        ), patch.object(
            telegram_notifier, "BOT_TOKEN", "token"
        ), patch.object(
            telegram_notifier, "ADMIN_CHAT_ID", "chat"
        ), patch.object(telegram_notifier.httpx, "post", return_value=Mock(status_code=200)) as post:
            self.assertEqual(telegram_notifier.notify_admin_new_apply(member), "ok")
            post.assert_called_once()

    def test_booking_notifications_include_operator_fields_and_buttons(self):
        booking = {
            "id": "booking-1",
            "member_id": "member-1",
            "applicant_name": "홍길동",
            "phone_masked": "010-1234-5678",
            "session_title": "AI 기초 셋팅",
            "session_starts_at": "2026-05-17T10:00:00+09:00",
            "status": "requested",
            "payment_status": "not_sent",
            "payment_amount_krw": 50000,
            "request_rank": 1,
            "paid_rank": None,
            "desired_outcome": "강의에서 자동화를 배우고 싶습니다",
            "preparedness": "노트북 준비 완료",
        }
        with patch.object(telegram_notifier, "TELEGRAM_NOTIFY_ENABLED", True), patch.object(
            telegram_notifier, "TELEGRAM_BOOKING_NOTIFY_ENABLED", True
        ), patch.object(
            telegram_notifier, "BOT_TOKEN", "token"
        ), patch.object(
            telegram_notifier, "ADMIN_CHAT_ID", "chat"
        ), patch.object(telegram_notifier.httpx, "post", return_value=Mock(status_code=200)) as post:
            self.assertEqual(telegram_notifier.notify_booking_requested({}, booking), "ok")
            self.assertEqual(telegram_notifier.notify_booking_payment_guide(booking), "ok")
            self.assertEqual(telegram_notifier.notify_booking_payment_confirmed(booking), "ok")

        texts = [call.kwargs["json"]["text"] for call in post.call_args_list]
        self.assertEqual(len(texts), 3)
        for text in texts:
            self.assertIn("홍*동", text)
            self.assertIn("***-****-5678", text)
            self.assertIn("booking-1", text)
            self.assertIn("member-1", text)
            self.assertIn("AI 기초 셋팅", text)
            self.assertIn("오전 10시", text)
            self.assertIn("목표/내용: 입력 있음", text)
            self.assertIn("준비상태: 입력 있음", text)
            self.assertNotIn("홍길동", text)
            self.assertNotIn("강의에서 자동화를 배우고 싶습니다", text)
            self.assertNotIn("노트북 준비 완료", text)
            self.assertNotIn("T10", text)
            self.assertNotIn("010-1234-5678", text)
        self.assertEqual(
            post.call_args_list[0].kwargs["json"]["reply_markup"]["inline_keyboard"][0][0]["callback_data"],
            "arsen:payguide:booking-1",
        )

    def test_booking_notifications_disabled_never_post(self):
        booking = {
            "id": "booking-1",
            "applicant_name": "홍길동",
            "phone_masked": "010-1234-5678",
            "status": "requested",
            "payment_status": "not_sent",
        }
        with patch.object(telegram_notifier, "TELEGRAM_NOTIFY_ENABLED", False), patch.object(
            telegram_notifier, "TELEGRAM_BOOKING_NOTIFY_ENABLED", False
        ), patch.object(
            telegram_notifier, "BOT_TOKEN", "token"
        ), patch.object(
            telegram_notifier, "ADMIN_CHAT_ID", "chat"
        ), patch.object(telegram_notifier.httpx, "post") as post, self.assertLogs(
            "member-system", level="INFO"
        ) as logs:
            statuses = [
                telegram_notifier.notify_booking_requested({}, booking),
                telegram_notifier.notify_booking_payment_guide(booking),
                telegram_notifier.notify_booking_payment_confirmed(booking),
            ]

        self.assertEqual(statuses, ["disabled", "disabled", "disabled"])
        post.assert_not_called()
        self.assertTrue(any("disabled" in line for line in logs.output))

    def test_booking_notifications_not_configured_never_post(self):
        booking = {
            "id": "booking-1",
            "applicant_name": "홍길동",
            "phone_masked": "010-1234-5678",
            "status": "requested",
            "payment_status": "not_sent",
        }
        with patch.object(telegram_notifier, "TELEGRAM_NOTIFY_ENABLED", True), patch.object(
            telegram_notifier, "TELEGRAM_BOOKING_NOTIFY_ENABLED", True
        ), patch.object(
            telegram_notifier, "BOT_TOKEN", ""
        ), patch.object(
            telegram_notifier, "ADMIN_CHAT_ID", ""
        ), patch.object(telegram_notifier.httpx, "post") as post, self.assertLogs(
            "member-system", level="INFO"
        ) as logs:
            statuses = [
                telegram_notifier.notify_booking_requested({}, booking),
                telegram_notifier.notify_booking_payment_guide(booking),
                telegram_notifier.notify_booking_payment_confirmed(booking),
            ]

        self.assertEqual(statuses, ["not_configured", "not_configured", "not_configured"])
        post.assert_not_called()
        self.assertTrue(any("not_configured" in line for line in logs.output))

    def test_new_booking_apply_notification_disabled_logs_status_and_never_posts(self):
        member_id = self._insert_member()
        member = {
            "id": member_id,
            "name": "테스트",
            "phone_masked": "010-****-1234",
            "status": "pending",
        }
        booking = {"id": "booking-1", "status": "requested"}

        with patch.object(telegram_notifier, "TELEGRAM_NOTIFY_ENABLED", False), patch.object(
            telegram_notifier, "TELEGRAM_APPLICATION_NOTIFY_ENABLED", False
        ), patch.object(
            telegram_notifier, "BOT_TOKEN", "token"
        ), patch.object(
            telegram_notifier, "ADMIN_CHAT_ID", "chat"
        ), patch.object(telegram_notifier.httpx, "post") as post, self.assertLogs(
            "member-system", level="INFO"
        ) as logs:
            status = telegram_notifier.notify_admin_new_apply(member, booking=booking)

        self.assertEqual(status, "disabled")
        post.assert_not_called()
        self.assertTrue(any("disabled" in line for line in logs.output))
        self.assertEqual(self._log_and_fetch_hermes_status(member_id, status), "disabled")

    def test_new_booking_apply_notification_not_configured_logs_status_and_never_posts(self):
        member_id = self._insert_member()
        member = {
            "id": member_id,
            "name": "테스트",
            "phone_masked": "010-****-1234",
            "status": "pending",
        }
        booking = {"id": "booking-1", "status": "requested"}

        with patch.object(telegram_notifier, "TELEGRAM_NOTIFY_ENABLED", True), patch.object(
            telegram_notifier, "TELEGRAM_APPLICATION_NOTIFY_ENABLED", True
        ), patch.object(
            telegram_notifier, "BOT_TOKEN", ""
        ), patch.object(
            telegram_notifier, "ADMIN_CHAT_ID", ""
        ), patch.object(telegram_notifier.httpx, "post") as post, self.assertLogs(
            "member-system", level="INFO"
        ) as logs:
            status = telegram_notifier.notify_admin_new_apply(member, booking=booking)

        self.assertEqual(status, "not_configured")
        post.assert_not_called()
        self.assertTrue(any("not_configured" in line for line in logs.output))
        self.assertEqual(self._log_and_fetch_hermes_status(member_id, status), "not_configured")

    def test_storage_status_exposes_latest_hermes_log_per_application(self):
        member_id = self._insert_member()
        db_manager.log_action(member_id, "apply", "plan=basic", "127.0.0.1")
        db_manager.log_action(member_id, "hermes_notify", "not_configured", "127.0.0.1")

        with patch.object(db_manager, "TELEGRAM_NOTIFY_ENABLED", False), patch.object(
            db_manager, "TELEGRAM_APPLICATION_NOTIFY_ENABLED", False
        ), patch.object(
            db_manager, "TELEGRAM_BOOKING_NOTIFY_ENABLED", False
        ), patch.object(
            db_manager, "TELEGRAM_BOT_TOKEN", ""
        ), patch.object(
            db_manager, "TELEGRAM_ADMIN_CHAT_ID", ""
        ):
            status = db_manager.get_storage_status(limit=1)

        self.assertFalse(status["hermes"]["configured"])
        self.assertFalse(status["hermes"]["global_enabled"])
        self.assertFalse(status["hermes"]["application_enabled"])
        self.assertFalse(status["hermes"]["booking_enabled"])
        self.assertFalse(status["hermes"]["active_application"])
        self.assertFalse(status["hermes"]["active_booking"])
        self.assertFalse(status["hermes"]["active"])
        self.assertEqual(status["hermes"]["status"], "OFF")
        self.assertEqual(status["hermes"]["mode"], "not_configured")
        self.assertEqual(status["hermes"]["application_mode"], "not_configured")
        self.assertEqual(status["hermes"]["booking_mode"], "not_configured")
        self.assertEqual(status["recent"][0]["id"], member_id)
        self.assertEqual(status["recent"][0]["hermes_status"], "not_configured")
        self.assertIsNotNone(status["recent"][0]["hermes_checked_at"])

    def test_storage_status_reports_application_active_when_global_switch_off(self):
        with patch.object(db_manager, "TELEGRAM_NOTIFY_ENABLED", False), patch.object(
            db_manager, "TELEGRAM_APPLICATION_NOTIFY_ENABLED", True
        ), patch.object(
            db_manager, "TELEGRAM_BOOKING_NOTIFY_ENABLED", False
        ), patch.object(
            db_manager, "TELEGRAM_BOT_TOKEN", "unit-test-token"
        ), patch.object(
            db_manager, "TELEGRAM_ADMIN_CHAT_ID", "unit-test-chat-id"
        ):
            status = db_manager.get_storage_status(limit=1)
            health = db_manager.get_operator_health()

        for payload in (status, health):
            payload_text = str(payload)
            self.assertNotIn("unit-test-token", payload_text)
            self.assertNotIn("unit-test-chat-id", payload_text)

        hermes = status["hermes"]
        self.assertTrue(hermes["configured"])
        self.assertFalse(hermes["global_enabled"])
        self.assertTrue(hermes["application_enabled"])
        self.assertFalse(hermes["booking_enabled"])
        self.assertTrue(hermes["active_application"])
        self.assertFalse(hermes["active_booking"])
        self.assertEqual(hermes["status"], "ON")
        self.assertEqual(hermes["mode"], "telegram_sendMessage")
        self.assertEqual(hermes["global_mode"], "global_switch_off")
        self.assertEqual(hermes["application_mode"], "telegram_sendMessage")
        self.assertEqual(hermes["booking_mode"], "disabled")
        self.assertEqual(health["hermes"], hermes)

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

        with patch.object(db_manager, "TELEGRAM_NOTIFY_ENABLED", True), patch.object(
            db_manager, "TELEGRAM_APPLICATION_NOTIFY_ENABLED", True
        ), patch.object(
            db_manager, "TELEGRAM_BOOKING_NOTIFY_ENABLED", True
        ), patch.object(
            db_manager, "TELEGRAM_BOT_TOKEN", "unit-test-token"
        ), patch.object(
            db_manager, "TELEGRAM_ADMIN_CHAT_ID", "unit-test-chat-id"
        ):
            status = db_manager.get_operator_health()
        status_text = str(status)

        self.assertTrue(status["server"]["alive"])
        self.assertEqual(status["public_sessions"]["count"], 1)
        self.assertEqual(status["application_system"]["status"], "accepting")
        self.assertEqual(status["application_system"]["requested_booking_count"], 1)
        self.assertTrue(status["hermes"]["configured"])
        self.assertTrue(status["hermes"]["active_application"])
        self.assertTrue(status["hermes"]["active_booking"])
        self.assertTrue(status["backup"]["last_success"])
        self.assertNotIn("테스트", status_text)
        self.assertNotIn("010-****-1234", status_text)
        self.assertNotIn("encrypted", status_text)
        self.assertNotIn("targets", status_text)
        self.assertNotIn("unit-test-token", status_text)
        self.assertNotIn("unit-test-chat-id", status_text)

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

    def test_storage_snapshot_and_status_mask_edge_case_pii_fields(self):
        member_id = "member-edge"
        raw_name = "김민수"
        raw_phone = "010-9876-5432"
        encrypted_email = "EDGE_ENCRYPTED_EMAIL_PAYLOAD"
        encrypted_phone = "EDGE_ENCRYPTED_PHONE_PAYLOAD"
        desired_outcome = "원문 목표: 가족 사업 매출 2배와 개인 연락처 010-1111-2222"
        preparedness = "준비상태 원문: 집주소 서울시 민감동 123"
        backup_target_detail = "backup detail includes 김민수 010-9876-5432 EDGE_ENCRYPTED_PHONE_PAYLOAD"
        backup_file = "/tmp/backups/김민수-010-9876-5432.db"
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
                raw_name,
                encrypted_email,
                raw_phone,
                encrypted_phone,
                "여",
                33,
                "개인사업자",
                "지인소개",
                "신청 사유 원문 010-3333-4444",
                "중급",
                "full",
                1,
                "2026-05-09T00:00:00+00:00",
                "1.0",
                "2026-05-09T01:00:00+00:00",
            ),
        )
        conn.execute(
            """
            INSERT INTO bookings (
                id, session_id, member_id, applicant_name, phone_masked,
                desired_outcome, preparedness, status, payment_status,
                payment_amount_krw, created_at, updated_at
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                "booking-edge",
                None,
                member_id,
                raw_name,
                raw_phone,
                desired_outcome,
                preparedness,
                "requested",
                "not_sent",
                50000,
                "2026-05-09T01:00:00+00:00",
                "2026-05-09T01:00:00+00:00",
            ),
        )
        conn.commit()
        conn.close()
        db_manager.log_action(
            "system",
            "db_backup",
            (
                '{"ok_count": 1, "failed_count": 1, "targets": ['
                '{"name": "local", "status": "ok", "detail": "'
                + backup_target_detail
                + '", "file": "'
                + backup_file
                + '"}, {"name": "macpro", "status": "failed", "detail": "'
                + encrypted_email
                + '"}]}'
            ),
            "127.0.0.1",
        )

        snapshot = db_manager.get_storage_snapshot(limit=10)
        status = db_manager.get_storage_status(limit=10)
        forbidden = [
            raw_name,
            raw_phone,
            encrypted_email,
            encrypted_phone,
            desired_outcome,
            preparedness,
            "010-1111-2222",
            "010-3333-4444",
            "서울시 민감동",
            backup_target_detail,
            backup_file,
        ]

        self.assertEqual(snapshot["recent"][0]["applicant"], "김*수")
        self.assertEqual(snapshot["recent"][0]["phone_masked"], "010-****-5432")
        self.assertNotIn("desired_outcome", snapshot["recent"][0])
        self.assertNotIn("preparedness", snapshot["recent"][0])
        self.assertEqual(status["recent"][0]["name"], "김*수")
        self.assertEqual(status["recent"][0]["phone_masked"], "010-****-5432")
        self.assertEqual(status["backup"]["last_run"]["detail"]["ok_count"], 1)
        self.assertEqual(status["backup"]["last_run"]["detail"]["failed_count"], 1)
        self.assertEqual(
            status["backup"]["last_run"]["detail"]["targets"],
            [{"name": "local", "status": "ok"}, {"name": "macpro", "status": "failed"}],
        )
        self._assert_no_storage_pii(snapshot, forbidden)
        self._assert_no_storage_pii(status, forbidden)

    def test_storage_status_reports_local_backup_after_existing_backup_api(self):
        backup_dir = Path(self.tmpdir.name) / "snapshots"
        with patch.object(
            db_manager,
            "_backup_targets",
            return_value=[
                {
                    "name": "local",
                    "label": "Mac Air local",
                    "path": backup_dir,
                    "available": True,
                }
            ],
        ), patch.object(db_manager, "_run_quiet", return_value=(False, "test_skip_remote")):
            result = db_manager.backup_database(reason="test")
            db_manager.log_action(
                "system",
                "db_backup",
                '{"ok_count": 1, "failed_count": 1, "targets": [{"name": "local", "status": "ok"}, {"name": "macpro", "status": "failed"}]}',
                "127.0.0.1",
            )
            status = db_manager.get_storage_status()

        local_target = next(target for target in status["backup"]["targets"] if target["name"] == "local")
        status_text = str(status)

        self.assertTrue(backup_dir.exists())
        self.assertEqual(result["targets"][0]["status"], "ok")
        self.assertEqual(local_target["path"], str(backup_dir))
        self.assertIsNotNone(local_target["latest"])
        self.assertEqual(status["backup"]["last_run"]["detail"]["ok_count"], 1)
        self.assertEqual(status["backup"]["last_run"]["detail"]["failed_count"], 1)
        self.assertNotIn("encrypted-email", status_text)
        self.assertNotIn("encrypted-phone", status_text)


if __name__ == "__main__":
    unittest.main()
