import importlib
import json
import sqlite3
import sys
import tempfile
import types
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import db
from agents import booking_manager
from agents import db_manager
from agents import code_generator
from agents import telegram_notifier
from agents.encryptor import encrypt_data


def _install_scheduler_stub():
    if "apscheduler.schedulers.asyncio" in sys.modules:
        return
    try:
        import apscheduler.schedulers.asyncio  # noqa: F401
        import apscheduler.triggers.cron  # noqa: F401
        return
    except ModuleNotFoundError:
        pass

    apscheduler = types.ModuleType("apscheduler")
    schedulers = types.ModuleType("apscheduler.schedulers")
    asyncio_module = types.ModuleType("apscheduler.schedulers.asyncio")
    triggers = types.ModuleType("apscheduler.triggers")
    cron_module = types.ModuleType("apscheduler.triggers.cron")

    class AsyncIOScheduler:
        def __init__(self, *args, **kwargs):
            self.jobs = []

        def add_job(self, *args, **kwargs):
            self.jobs.append((args, kwargs))
            return None

        def start(self):
            return None

        def shutdown(self):
            return None

    class CronTrigger:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    asyncio_module.AsyncIOScheduler = AsyncIOScheduler
    cron_module.CronTrigger = CronTrigger
    sys.modules["apscheduler"] = apscheduler
    sys.modules["apscheduler.schedulers"] = schedulers
    sys.modules["apscheduler.schedulers.asyncio"] = asyncio_module
    sys.modules["apscheduler.triggers"] = triggers
    sys.modules["apscheduler.triggers.cron"] = cron_module


class CodeIssuanceFlowTest(unittest.TestCase):
    ADMIN_KEY = "unit-test-admin-key"

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.tmpdir.name) / "members.db"
        self.original_db_path = db.DB_PATH
        self.original_manager_db_path = db_manager.DB_PATH
        self.original_code_ledger_path = code_generator.CODE_LEDGER_PATH
        db.DB_PATH = self.db_path
        db_manager.DB_PATH = self.db_path
        code_generator.CODE_LEDGER_PATH = Path(self.tmpdir.name) / "private" / "code_ledger.jsonl"
        db.init_db()

        _install_scheduler_stub()
        self.main = importlib.import_module("main")
        self.original_admin_key = self.main.ADMIN_API_KEY
        self.original_admin_env_path = self.main.ADMIN_ENV_PATH
        self.original_admin_tool_backup_targets = self.main.ADMIN_TOOL_BACKUP_TARGETS
        self.original_payment_accounts_path = self.main.PAYMENT_ACCOUNTS_PATH
        self.original_preparation_guide_path = self.main.PREPARATION_GUIDE_PATH
        self.original_local_open = self.main.MEMBER_ADMIN_LOCAL_OPEN
        self.original_local_flag = self.main.LOCAL_ADMIN_OPEN_FLAG
        self.main.ADMIN_API_KEY = self.ADMIN_KEY
        self.main.ADMIN_ENV_PATH = Path(self.tmpdir.name) / ".env"
        self.main.ADMIN_ENV_PATH.write_text(f"ADMIN_API_KEY={self.ADMIN_KEY}\n", encoding="utf-8")
        self.main.ADMIN_ENV_PATH.chmod(0o600)
        self.main.ADMIN_TOOL_BACKUP_TARGETS = [
            {
                "name": "local",
                "label": "Local",
                "root": Path(self.tmpdir.name),
                "path": Path(self.tmpdir.name) / "admin-tools",
            }
        ]
        self.main.PAYMENT_ACCOUNTS_PATH = Path(self.tmpdir.name) / "private" / "payment_accounts.json"
        self.main.PREPARATION_GUIDE_PATH = Path(self.tmpdir.name) / "private" / "preparation_guide.json"
        self.main.MEMBER_ADMIN_LOCAL_OPEN = False
        self.main.LOCAL_ADMIN_OPEN_FLAG = Path(self.tmpdir.name) / ".local_admin_open"
        self.client = TestClient(self.main.app)

    def tearDown(self):
        self.main.ADMIN_API_KEY = self.original_admin_key
        self.main.ADMIN_ENV_PATH = self.original_admin_env_path
        self.main.ADMIN_TOOL_BACKUP_TARGETS = self.original_admin_tool_backup_targets
        self.main.PAYMENT_ACCOUNTS_PATH = self.original_payment_accounts_path
        self.main.PREPARATION_GUIDE_PATH = self.original_preparation_guide_path
        self.main.MEMBER_ADMIN_LOCAL_OPEN = self.original_local_open
        self.main.LOCAL_ADMIN_OPEN_FLAG = self.original_local_flag
        db.DB_PATH = self.original_db_path
        db_manager.DB_PATH = self.original_manager_db_path
        code_generator.CODE_LEDGER_PATH = self.original_code_ledger_path
        self.tmpdir.cleanup()

    def _admin_headers(self):
        return {"X-Admin-Key": self.ADMIN_KEY}

    def _create_pending_member(self):
        encrypted = encrypt_data({"phone": "010-2222-3333", "email": "code-test@example.com"})
        return db_manager.create_member(
            {
                "name": "Code Issuance Test",
                "email_encrypted": encrypted["email_encrypted"],
                "email_hash": encrypted["email_hash"],
                "phone_masked": encrypted["phone_masked"],
                "phone_encrypted": encrypted["phone_encrypted"],
                "phone_hash": encrypted["phone_hash"],
                "gender": "테스트",
                "age": 30,
                "job": "QA",
                "referral_source": "unit-test",
                "reason": "code issuance verification",
                "ai_level": "입문",
                "plan_type": "full",
                "consent_personal": True,
                "consent_marketing": False,
                "consent_at": "2026-05-12T00:00:00+00:00",
                "consent_version": "1.0",
            }
        )

    def _stored_member(self, member_id):
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT status, access_code, code_issued_at, code_expires_at FROM members WHERE id=?",
            (member_id,),
        ).fetchone()
        conn.close()
        return dict(row)

    def test_local_admin_preview_requires_loopback_host(self):
        self.main.MEMBER_ADMIN_LOCAL_OPEN = True
        request = types.SimpleNamespace(
            client=types.SimpleNamespace(host="127.0.0.1"),
            url=types.SimpleNamespace(hostname="apply.arsen-ai.com"),
            headers={},
        )
        self.assertFalse(self.main.is_local_admin_preview(request))

    def test_local_admin_preview_allows_true_localhost(self):
        self.main.MEMBER_ADMIN_LOCAL_OPEN = True
        request = types.SimpleNamespace(
            client=types.SimpleNamespace(host="127.0.0.1"),
            url=types.SimpleNamespace(hostname="127.0.0.1"),
            headers={},
        )
        self.assertTrue(self.main.is_local_admin_preview(request))

    def test_local_admin_preview_rejects_cloudflare_forwarded_request(self):
        self.main.MEMBER_ADMIN_LOCAL_OPEN = True
        request = types.SimpleNamespace(
            client=types.SimpleNamespace(host="127.0.0.1"),
            url=types.SimpleNamespace(hostname="127.0.0.1"),
            headers={"cf-connecting-ip": "203.0.113.10", "x-forwarded-proto": "https"},
        )
        self.assertFalse(self.main.is_local_admin_preview(request))

    def test_stats_requires_admin_password(self):
        response = self.client.get("/stats")
        self.assertEqual(response.status_code, 401)

        response = self.client.get("/stats", headers=self._admin_headers())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["ok"])

    def test_admin_password_change_requires_auth_and_rotates_runtime_key(self):
        new_key = "new-unit-test-admin-key"

        denied = self.client.post("/admin/password", json={"new_password": new_key})
        self.assertEqual(denied.status_code, 401)

        response = self.client.post(
            "/admin/password",
            headers=self._admin_headers(),
            json={"new_password": new_key},
        )

        self.assertEqual(response.status_code, 200)
        payload_text = json.dumps(response.json(), ensure_ascii=False)
        self.assertNotIn(new_key, payload_text)
        self.assertEqual(self.main.ADMIN_API_KEY, new_key)
        self.assertIn(f"ADMIN_API_KEY={new_key}", self.main.ADMIN_ENV_PATH.read_text(encoding="utf-8"))

        old_key_response = self.client.get("/stats", headers=self._admin_headers())
        self.assertEqual(old_key_response.status_code, 401)
        new_key_response = self.client.get("/stats", headers={"X-Admin-Key": new_key})
        self.assertEqual(new_key_response.status_code, 200)

    def test_admin_password_change_rejects_short_password(self):
        response = self.client.post(
            "/admin/password",
            headers=self._admin_headers(),
            json={"new_password": "short"},
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.main.ADMIN_API_KEY, self.ADMIN_KEY)

    def test_admin_tool_backup_requires_auth_and_copies_only_tool_files(self):
        denied = self.client.post("/admin/admin-tools/backup")
        self.assertEqual(denied.status_code, 401)

        response = self.client.post("/admin/admin-tools/backup", headers=self._admin_headers())

        self.assertEqual(response.status_code, 200)
        payload = response.json()["data"]
        self.assertEqual(payload["ok_count"], 1)
        backup_dir = Path(self.tmpdir.name) / "admin-tools"
        self.assertTrue((backup_dir / "set_admin_password.py").exists())
        self.assertFalse((backup_dir / ".env").exists())

    def test_approve_requires_admin_key(self):
        member_id = self._create_pending_member()

        response = self.client.post(f"/approve/{member_id}")

        self.assertEqual(response.status_code, 401)
        self.assertEqual(self._stored_member(member_id)["status"], "pending")

    def test_admin_bookings_requires_admin_key(self):
        response = self.client.get("/admin/bookings")

        self.assertEqual(response.status_code, 401)

    def test_admin_can_manual_add_paid_booking_to_session(self):
        now = datetime.now(timezone.utc)
        session_id = booking_manager.create_session(
            {
                "title": "Manual Paid Session",
                "starts_at": (now + timedelta(days=4)).isoformat(),
                "ends_at": (now + timedelta(days=4, hours=2)).isoformat(),
                "location": "영등포시장역 사무실",
                "status": "open",
                "capacity_max": 5,
                "price_krw": 50000,
            }
        )

        response = self.client.post(
            f"/admin/sessions/{session_id}/manual-booking",
            headers=self._admin_headers(),
            json={
                "applicant_name": "Manual Paid",
                "phone": "01012345678",
                "desired_outcome": "현장 입금 확인",
                "payment_note": "운영자 수동 입금 확인",
                "payment_amount_krw": 50000,
            },
        )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        booking = payload["data"]
        self.assertEqual(booking["status"], "confirmed")
        self.assertEqual(booking["payment_status"], "paid")
        self.assertEqual(booking["session_id"], session_id)
        self.assertEqual(payload["reused_member"], False)
        self.assertTrue(payload["member_id"])

        session = booking_manager.get_session(session_id)
        self.assertEqual(session["confirmed_booking_count"], 1)
        member_detail = self.client.get(
            f"/members/{payload['member_id']}",
            headers=self._admin_headers(),
        ).json()["data"]
        self.assertEqual(member_detail["status"], "approved")
        self.assertEqual(member_detail["participation_type"], "manual_confirmed")

    def test_admin_can_manual_add_existing_member_without_retyping_phone(self):
        now = datetime.now(timezone.utc)
        session_id = booking_manager.create_session(
            {
                "title": "Existing Member Manual Session",
                "starts_at": (now + timedelta(days=5)).isoformat(),
                "ends_at": (now + timedelta(days=5, hours=2)).isoformat(),
                "location": "영등포시장역 사무실",
                "status": "open",
                "capacity_max": 5,
                "price_krw": 50000,
            }
        )
        member_id = self._create_pending_member()

        response = self.client.post(
            f"/admin/sessions/{session_id}/manual-booking",
            headers=self._admin_headers(),
            json={
                "member_id": member_id,
                "desired_outcome": "기존 신청자 입금 확인",
                "payment_note": "기존 신청자 선택 후 입금 확인",
            },
        )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        booking = payload["data"]
        self.assertEqual(payload["member_id"], member_id)
        self.assertEqual(payload["reused_member"], True)
        self.assertEqual(booking["member_id"], member_id)
        self.assertEqual(booking["status"], "confirmed")
        self.assertEqual(booking["payment_status"], "paid")
        self.assertEqual(self._stored_member(member_id)["status"], "approved")

    def test_admin_booking_manual_and_guide_flows_do_not_send_telegram(self):
        now = datetime.now(timezone.utc)
        session_id = booking_manager.create_session(
            {
                "title": "No Send Session",
                "starts_at": (now + timedelta(days=6)).isoformat(),
                "ends_at": (now + timedelta(days=6, hours=2)).isoformat(),
                "location": "영등포시장역 사무실",
                "status": "open",
                "capacity_max": 5,
                "price_krw": 50000,
            }
        )
        member_id = self._create_pending_member()
        booking_id = booking_manager.create_booking(
            {
                "session_id": session_id,
                "member_id": member_id,
                "applicant_name": "No Send Existing",
                "phone_masked": "010-****-5555",
                "status": "requested",
                "payment_status": "not_sent",
                "payment_amount_krw": 50000,
            }
        )

        with (
            patch.object(telegram_notifier, "BOT_TOKEN", "test-token"),
            patch.object(telegram_notifier, "ADMIN_CHAT_ID", "test-chat"),
            patch.object(telegram_notifier, "TELEGRAM_NOTIFY_ENABLED", True),
            patch.object(telegram_notifier, "TELEGRAM_BOOKING_NOTIFY_ENABLED", True),
            patch.object(telegram_notifier.httpx, "post") as post,
        ):
            manual = self.client.post(
                f"/admin/sessions/{session_id}/manual-booking",
                headers=self._admin_headers(),
                json={
                    "applicant_name": "Manual No Send",
                    "phone": "01099998888",
                    "desired_outcome": "no-send manual booking",
                    "payment_note": "운영자 수동 입금 확인",
                    "payment_amount_krw": 50000,
                },
            )
            guide = self.client.post(
                f"/admin/bookings/{booking_id}/send-payment-guide",
                headers=self._admin_headers(),
                json={},
            )
            confirm = self.client.post(
                f"/admin/bookings/{booking_id}/confirm-payment",
                headers=self._admin_headers(),
                json={"payment_note": "운영자 수동 입금 확인"},
            )
            location = self.client.post(
                f"/admin/bookings/{booking_id}/location-guide",
                headers=self._admin_headers(),
            )
            refund = self.client.post(
                f"/admin/bookings/{booking_id}/refund-guide",
                headers=self._admin_headers(),
            )
            preparation_saved = self.client.put(
                "/admin/preparation-guide",
                headers=self._admin_headers(),
                json={"message": "[강의 준비물 안내]\n노트북과 충전기를 준비해 주세요. 테스트용 문구입니다."},
            )
            preparation_listed = self.client.get("/admin/preparation-guide", headers=self._admin_headers())

        for response in [manual, guide, confirm, location, refund, preparation_saved, preparation_listed]:
            self.assertEqual(response.status_code, 200)
        for response in [manual, guide, confirm, location, refund]:
            payload = response.json()
            self.assertEqual(payload["applicant_delivery"], "not_sent")
            self.assertEqual(payload["operator_notification"], "not_sent")
        post.assert_not_called()

    def test_payment_accounts_require_admin_and_persist_sanitized_values(self):
        denied = self.client.get("/admin/payment-accounts")
        self.assertEqual(denied.status_code, 401)

        payload = {
            "active_id": "main",
            "accounts": [
                {
                    "id": "main",
                    "label": "주계좌",
                    "bank": "테스트은행",
                    "number": "123-456",
                    "holder": "아르센",
                    "memo": "수업 입금",
                }
            ],
        }
        saved = self.client.put(
            "/admin/payment-accounts",
            headers=self._admin_headers(),
            json=payload,
        )
        listed = self.client.get("/admin/payment-accounts", headers=self._admin_headers())

        self.assertEqual(saved.status_code, 200)
        self.assertEqual(listed.status_code, 200)
        data = listed.json()["data"]
        self.assertEqual(data["active_id"], "main")
        self.assertEqual(data["accounts"][0]["bank"], "테스트은행")
        self.assertEqual(self.main.PAYMENT_ACCOUNTS_PATH.stat().st_mode & 0o077, 0)

    def test_preparation_guide_requires_admin_and_persists_message(self):
        denied = self.client.get("/admin/preparation-guide")
        self.assertEqual(denied.status_code, 401)

        message = "[강의 준비물 안내]\n노트북과 충전기를 준비해 주세요. 구현하고 싶은 주제를 적어오세요."
        saved = self.client.put(
            "/admin/preparation-guide",
            headers=self._admin_headers(),
            json={"message": message},
        )
        listed = self.client.get("/admin/preparation-guide", headers=self._admin_headers())

        self.assertEqual(saved.status_code, 200)
        self.assertEqual(listed.status_code, 200)
        self.assertEqual(listed.json()["data"]["message"], message)
        self.assertIn("노트북", listed.json()["data"]["default_message"])
        self.assertEqual(self.main.PREPARATION_GUIDE_PATH.stat().st_mode & 0o077, 0)

    def test_health_is_public_and_reports_local_admin_preview_state(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["service"], "member-system")
        self.assertFalse(payload["local_admin_preview"])

    def test_approve_pending_member_issues_persistent_invite_code_and_hides_stored_code_in_detail(self):
        member_id = self._create_pending_member()

        response = self.client.post(f"/approve/{member_id}", headers=self._admin_headers())
        detail = self.client.get(f"/members/{member_id}", headers=self._admin_headers())

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertTrue(payload["ok"])
        self.assertRegex(payload["code"], r"^\d{8}$")
        self.assertIsNone(payload["expires_at"])
        self.assertIn("delivery_message", payload)

        stored = self._stored_member(member_id)
        self.assertEqual(stored["status"], "approved")
        self.assertTrue(stored["access_code"])
        self.assertTrue(stored["code_issued_at"])
        self.assertIsNone(stored["code_expires_at"])
        self.assertTrue(code_generator.CODE_LEDGER_PATH.exists())

        detail_text = str(detail.json())
        self.assertNotIn("access_code", detail_text)
        self.assertNotIn(payload["code"], detail_text)

    def test_admin_can_reveal_current_code_after_approval(self):
        member_id = self._create_pending_member()
        approved = self.client.post(f"/approve/{member_id}", headers=self._admin_headers()).json()

        denied = self.client.get(f"/members/{member_id}/access-code")
        response = self.client.get(f"/members/{member_id}/access-code", headers=self._admin_headers())

        self.assertEqual(denied.status_code, 401)
        self.assertEqual(response.status_code, 200)
        payload = response.json()["data"]
        self.assertEqual(payload["code"], approved["code"])
        self.assertIsNone(payload["expires_at"])
        self.assertEqual(payload["expiry_label"], "기한 없음")
        self.assertIn("예약자 확인", payload["delivery_message"])

    def test_admin_can_reveal_code_from_private_ledger_if_db_code_is_missing(self):
        member_id = self._create_pending_member()
        approved = self.client.post(f"/approve/{member_id}", headers=self._admin_headers()).json()
        conn = sqlite3.connect(str(self.db_path))
        conn.execute("UPDATE members SET access_code=NULL WHERE id=?", (member_id,))
        conn.commit()
        conn.close()

        response = self.client.get(f"/members/{member_id}/access-code", headers=self._admin_headers())

        self.assertEqual(response.status_code, 200)
        payload = response.json()["data"]
        self.assertEqual(payload["code"], approved["code"])
        self.assertEqual(payload["source"], "ledger")

    def test_regen_code_for_approved_member_issues_new_code(self):
        member_id = self._create_pending_member()
        approved = self.client.post(f"/approve/{member_id}", headers=self._admin_headers()).json()

        response = self.client.post(f"/regen-code/{member_id}", headers=self._admin_headers())

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertRegex(payload["code"], r"^\d{8}$")
        self.assertNotEqual(payload["code"], approved["code"])
        self.assertEqual(self._stored_member(member_id)["status"], "approved")

    def test_code_delivery_log_requires_admin(self):
        member_id = self._create_pending_member()

        resp = self.client.post(
            f"/admin/members/{member_id}/code-delivery-log",
            json={"channel": "telegram"},
        )

        self.assertEqual(resp.status_code, 401)

    def test_code_delivery_log_records_channel_and_appears_in_detail(self):
        member_id = self._create_pending_member()
        self.client.post(f"/approve/{member_id}", headers=self._admin_headers())

        log_resp = self.client.post(
            f"/admin/members/{member_id}/code-delivery-log",
            headers=self._admin_headers(),
            json={"channel": "telegram", "note": "카카오 전달 완료"},
        )
        self.assertEqual(log_resp.status_code, 200)
        self.assertTrue(log_resp.json()["ok"])

        detail_resp = self.client.get(f"/members/{member_id}", headers=self._admin_headers())
        self.assertEqual(detail_resp.status_code, 200)
        payload = detail_resp.json()

        logs = payload.get("code_delivery_logs", [])
        self.assertTrue(any(l["action"] == "code_delivered" for l in logs))
        delivered = next(l for l in logs if l["action"] == "code_delivered")
        info = json.loads(delivered["detail"])
        self.assertEqual(info["channel"], "telegram")
        self.assertEqual(info["note"], "카카오 전달 완료")

    def test_code_delivery_log_does_not_create_booking(self):
        member_id = self._create_pending_member()
        self.client.post(f"/approve/{member_id}", headers=self._admin_headers())

        response = self.client.post(
            f"/admin/members/{member_id}/code-delivery-log",
            headers=self._admin_headers(),
            json={"channel": "kakao", "note": "전달 완료"},
        )
        bookings = self.client.get("/admin/bookings", headers=self._admin_headers())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(bookings.status_code, 200)
        self.assertEqual(bookings.json()["total"], 0)

    def test_apply_with_session_preference_does_not_create_booking_before_code(self):
        session_id = self.main.create_session(
            {
                "title": "TEST Apply Preference",
                "starts_at": "2026-05-17T10:00:00+09:00",
                "ends_at": "2026-05-17T12:00:00+09:00",
                "location": "영등포시장역 사무실",
                "status": "open",
                "price_krw": 50000,
            }
        )
        payload = {
            "name": "Code Apply Test",
            "email": "apply-pref@example.com",
            "phone": "010-3333-4444",
            "gender": "남",
            "age": 33,
            "job": "운영자",
            "referral_source": "기타",
            "reason": "승인 코드 전에는 예약이 만들어지면 안 되는지 검증합니다.",
            "ai_level": "입문",
            "plan_type": "basic",
            "session_id": session_id,
            "desired_outcome": "업무 자동화",
            "preparedness": "노트북 지참 가능",
            "consent_personal": True,
            "consent_marketing": False,
        }

        with patch.object(self.main, "save_to_sheets", return_value=False), patch.object(
            self.main,
            "backup_database",
            return_value={"ok_count": 0, "failed_count": 0, "targets": []},
        ), patch.object(self.main, "notify_admin_new_apply", return_value="disabled"):
            response = self.client.post("/apply", json=payload)
        bookings = self.client.get("/admin/bookings", headers=self._admin_headers())

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertTrue(body["ok"])
        self.assertIsNone(body["booking_id"])
        self.assertIsNone(body["reservation"])
        self.assertEqual(bookings.json()["total"], 0)

    def test_public_booking_after_code_notifies_operator(self):
        member_id = self._create_pending_member()
        approved = self.client.post(f"/approve/{member_id}", headers=self._admin_headers()).json()
        session_id = self.main.create_session(
            {
                "title": "TEST Public Booking",
                "starts_at": "2026-05-17T10:00:00+09:00",
                "ends_at": "2026-05-17T12:00:00+09:00",
                "location": "영등포시장역 사무실",
                "status": "open",
                "price_krw": 50000,
            }
        )

        with patch.object(self.main, "notify_booking_requested", return_value="ok") as notify:
            response = self.client.post(
                "/member/bookings",
                json={
                    "member_id": member_id,
                    "code": approved["code"],
                    "session_id": session_id,
                    "desired_outcome": "업무 자동화",
                    "preparedness": "노트북 지참 가능",
                },
            )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["ok"])
        notify.assert_called_once()

    def test_detail_does_not_expose_access_code_even_with_delivery_logs(self):
        member_id = self._create_pending_member()
        approve_resp = self.client.post(f"/approve/{member_id}", headers=self._admin_headers())
        issued_code = approve_resp.json()["code"]

        self.client.post(
            f"/admin/members/{member_id}/code-delivery-log",
            headers=self._admin_headers(),
            json={"channel": "direct"},
        )

        detail_resp = self.client.get(f"/members/{member_id}", headers=self._admin_headers())
        payload_text = str(detail_resp.json())
        self.assertNotIn("access_code", payload_text)
        self.assertNotIn(issued_code, payload_text)

    def test_approve_action_appears_in_delivery_logs(self):
        member_id = self._create_pending_member()
        self.client.post(f"/approve/{member_id}", headers=self._admin_headers())

        detail_resp = self.client.get(f"/members/{member_id}", headers=self._admin_headers())
        logs = detail_resp.json().get("code_delivery_logs", [])

        self.assertTrue(any(l["action"] == "approve" for l in logs))

    def test_code_view_action_appears_in_member_detail_delivery_logs(self):
        member_id = self._create_pending_member()
        self.client.post(f"/approve/{member_id}", headers=self._admin_headers())
        self.client.get(f"/members/{member_id}/access-code", headers=self._admin_headers())

        detail_resp = self.client.get(f"/members/{member_id}", headers=self._admin_headers())
        payload = detail_resp.json()
        logs = payload.get("code_delivery_logs", [])

        self.assertTrue(any(l["action"] == "code_viewed" for l in logs))
        self.assertTrue(any(l["action"] == "code_viewed" for l in payload["data"].get("code_delivery_logs", [])))


if __name__ == "__main__":
    unittest.main()
