import importlib
import json
import sqlite3
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import db
from agents import booking_manager, db_manager
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


class ContactRevealAuditTest(unittest.TestCase):
    ADMIN_KEY = "unit-test-admin-key"
    RAW_PHONE = "010-2222-3333"
    RAW_EMAIL = "contact-reveal-test@example.com"

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.tmpdir.name) / "members.db"
        self.original_db_path = db.DB_PATH
        self.original_manager_db_path = db_manager.DB_PATH
        db.DB_PATH = self.db_path
        db_manager.DB_PATH = self.db_path
        db.init_db()

        _install_scheduler_stub()
        self.main = importlib.import_module("main")
        self.original_admin_key = self.main.ADMIN_API_KEY
        self.original_local_open = self.main.MEMBER_ADMIN_LOCAL_OPEN
        self.original_local_flag = self.main.LOCAL_ADMIN_OPEN_FLAG
        self.main.ADMIN_API_KEY = self.ADMIN_KEY
        self.main.MEMBER_ADMIN_LOCAL_OPEN = False
        self.main.LOCAL_ADMIN_OPEN_FLAG = Path(self.tmpdir.name) / ".local_admin_open"
        self.client = TestClient(self.main.app)

    def tearDown(self):
        self.main.ADMIN_API_KEY = self.original_admin_key
        self.main.MEMBER_ADMIN_LOCAL_OPEN = self.original_local_open
        self.main.LOCAL_ADMIN_OPEN_FLAG = self.original_local_flag
        db.DB_PATH = self.original_db_path
        db_manager.DB_PATH = self.original_manager_db_path
        self.tmpdir.cleanup()

    def _create_member(self, **overrides):
        encrypted = encrypt_data({"phone": self.RAW_PHONE, "email": self.RAW_EMAIL})
        payload = {
            "name": "Contact Reveal Test",
            "email_encrypted": encrypted["email_encrypted"],
            "email_hash": encrypted["email_hash"],
            "phone_masked": encrypted["phone_masked"],
            "phone_encrypted": encrypted["phone_encrypted"],
            "phone_hash": encrypted["phone_hash"],
            "gender": "테스트",
            "age": 30,
            "job": "QA",
            "referral_source": "unit-test",
            "reason": "contact reveal audit verification",
            "ai_level": "입문",
            "plan_type": "basic",
            "consent_personal": True,
            "consent_marketing": False,
            "consent_at": "2026-05-10T00:00:00+00:00",
            "consent_version": "1.0",
        }
        payload.update(overrides)
        return db_manager.create_member(payload)

    def _admin_headers(self):
        return {"X-Admin-Key": self.ADMIN_KEY}

    def _contact_view_logs(self, member_id):
        conn = sqlite3.connect(str(self.db_path))
        rows = conn.execute(
            """
            SELECT action, detail, ip
            FROM member_logs
            WHERE member_id=? AND action='contact_view'
            ORDER BY created_at ASC
            """,
            (member_id,),
        ).fetchall()
        conn.close()
        return rows

    def _system_contact_export_logs(self):
        conn = sqlite3.connect(str(self.db_path))
        rows = conn.execute(
            """
            SELECT action, detail
            FROM member_logs
            WHERE member_id='system' AND action LIKE 'contact_export_%'
            ORDER BY created_at ASC
            """
        ).fetchall()
        conn.close()
        return rows

    def _system_contacts_export_logs(self):
        conn = sqlite3.connect(str(self.db_path))
        rows = conn.execute(
            """
            SELECT action, detail
            FROM member_logs
            WHERE member_id='system' AND action='contacts_export'
            ORDER BY created_at ASC
            """
        ).fetchall()
        conn.close()
        return rows

    def test_contact_reveal_requires_admin_auth_and_does_not_audit_denied_view(self):
        member_id = self._create_member()

        response = self.client.get(f"/members/{member_id}/contact")

        self.assertEqual(response.status_code, 401)
        self.assertEqual(self._contact_view_logs(member_id), [])

    def test_admin_contact_reveal_returns_contact_and_writes_audit_log(self):
        member_id = self._create_member()

        response = self.client.get(f"/members/{member_id}/contact", headers=self._admin_headers())

        self.assertEqual(response.status_code, 200)
        payload = response.json()["data"]
        self.assertEqual(payload["phone"], self.RAW_PHONE)
        self.assertEqual(payload["email"], self.RAW_EMAIL)
        self.assertEqual(payload["phone_masked"], "010-****-3333")

        logs = self._contact_view_logs(member_id)
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0][0], "contact_view")
        self.assertEqual(logs[0][1], "admin_contact_reveal")
        self.assertNotIn(self.RAW_PHONE, logs[0][1])
        self.assertNotIn(self.RAW_EMAIL, logs[0][1])

    def test_member_list_and_detail_do_not_expose_decrypted_or_encrypted_contacts(self):
        member_id = self._create_member()
        stored = db_manager.get_member(member_id)

        list_response = self.client.get("/members", headers=self._admin_headers())
        detail_response = self.client.get(f"/members/{member_id}", headers=self._admin_headers())

        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(detail_response.status_code, 200)
        self.assertEqual(list_response.json()["data"][0]["phone_masked"], "010-****-3333")
        for payload in (list_response.json(), detail_response.json()):
            payload_text = str(payload)
            self.assertNotIn(self.RAW_PHONE, payload_text)
            self.assertNotIn(self.RAW_EMAIL, payload_text)
            self.assertNotIn(stored["phone_encrypted"], payload_text)
            self.assertNotIn(stored["email_encrypted"], payload_text)
            self.assertNotIn("phone_encrypted", payload_text)
            self.assertNotIn("email_encrypted", payload_text)

    def test_public_consultation_creates_consultation_member(self):
        response = self.client.post(
            "/api/consultations",
            json={
                "source": "consulting_page",
                "topic": "자동화 상담",
                "name": "상담 테스트",
                "phone": "010-4444-5555",
                "email": "consultation-local@example.com",
                "product_interest": "YOONBOT",
                "message": "카카오톡 자동화 상담을 받고 싶습니다.",
                "page_url": "http://127.0.0.1:8130/consulting.html",
                "consent_privacy": True,
            },
        )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertTrue(payload["ok"])
        member = db_manager.get_member(payload["member_id"])
        self.assertIsNotNone(member)
        self.assertEqual(member["plan_type"], "consultation")
        self.assertEqual(member["participation_type"], "상담")
        self.assertEqual(member["participation_grade"], "상담")
        self.assertEqual(member["status"], "pending")
        self.assertIn("자동화 상담", member["reason"])
        self.assertIn("YOONBOT", member["reason"])

    def test_public_newsletter_requires_name_and_phone(self):
        response = self.client.post(
            "/api/consultations",
            json={
                "source": "home_newsletter",
                "topic": "소식 받기",
                "name": "",
                "contact": "newsletter-local@example.com",
                "consent_privacy": True,
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("이름", response.json()["detail"])

    def test_public_newsletter_phone_creates_lead_phone_member(self):
        response = self.client.post(
            "/api/consultations",
            json={
                "source": "home_newsletter",
                "topic": "소식 받기",
                "name": "번호 소식 테스트",
                "contact": "010-5555-6666",
                "consent_privacy": True,
            },
        )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertTrue(payload["ok"])
        member = db_manager.get_member(payload["member_id"])
        self.assertIsNotNone(member)
        self.assertEqual(member["plan_type"], "lead_phone")
        self.assertEqual(member["participation_type"], "소식 받기 · 번호")
        self.assertIn("분류: 소식 받기 · 번호", member["reason"])

        conn = db_manager.get_conn()
        try:
            row = conn.execute("SELECT * FROM consultations WHERE member_id=?", (payload["member_id"],)).fetchone()
        finally:
            conn.close()
        self.assertIsNotNone(row)
        self.assertEqual(row["source"], "home_newsletter")

    def test_newsletter_lead_upgrades_to_free_application(self):
        lead_response = self.client.post(
            "/api/consultations",
            json={
                "source": "home_newsletter",
                "topic": "소식 받기",
                "name": "소식 리드",
                "contact": "010-7777-8888",
                "consent_privacy": True,
            },
        )
        self.assertEqual(lead_response.status_code, 200)
        lead_member_id = lead_response.json()["member_id"]
        self.assertEqual(db_manager.get_member(lead_member_id)["plan_type"], "lead_phone")

        apply_payload = {
            "name": "소식 리드",
            "email": "lead-upgrade@example.com",
            "phone": "010-7777-8888",
            "gender": "여",
            "age": 31,
            "job": "마케터",
            "referral_source": "홈페이지 소식받기",
            "reason": "무료 강의 신청으로 전환해서 실제 신청자 목록에 보여야 합니다.",
            "ai_level": "입문",
            "plan_type": "free",
            "ai_tools": ["ChatGPT"],
            "ai_subscription": "무료",
            "ai_weekly_hours": "1시간 미만",
            "ai_use_cases": ["문서자동화"],
            "group_goals": ["업무 자동화"],
            "short_term_goal": "자동화 감 잡기",
            "participation_type": "무료강의",
            "preferred_schedule": "평일 오전",
            "available_time_slots": ["평일 오전"],
            "region": "서울",
            "main_device": "노트북",
            "can_code": False,
            "can_present": False,
            "skills": "초보",
            "contribution": "후기 공유",
            "consent_personal": True,
            "consent_marketing": False,
        }
        with patch.object(self.main, "save_to_sheets", return_value=False), patch.object(
            self.main,
            "backup_database",
            return_value={"ok_count": 0, "failed_count": 0, "targets": []},
        ), patch.object(self.main, "notify_admin_new_apply", return_value="ok") as notify:
            apply_response = self.client.post("/apply", json=apply_payload)

        self.assertEqual(apply_response.status_code, 200)
        body = apply_response.json()
        self.assertTrue(body["ok"])
        self.assertFalse(body["duplicate"])
        self.assertTrue(body["upgraded_from_lead"])
        self.assertEqual(body["member_id"], lead_member_id)
        self.assertIn("소식받기", body["message"])
        self.assertIn("무료강의", body["message"])
        upgraded = db_manager.get_member(lead_member_id)
        self.assertEqual(upgraded["plan_type"], "free")
        self.assertEqual(upgraded["status"], "pending")
        self.assertEqual(upgraded["name"], "소식 리드")
        self.assertEqual(upgraded["region"], "서울")
        self.assertEqual(upgraded["class_summary"]["free_completed"], 0)
        notify.assert_called_once()
        self.assertEqual(notify.call_args.kwargs["lead_upgrade_from"], "lead_phone")

        conn = db_manager.get_conn()
        try:
            row = conn.execute("SELECT status, admin_note FROM consultations WHERE member_id=?", (lead_member_id,)).fetchone()
            logs = conn.execute(
                "SELECT action, detail FROM member_logs WHERE member_id=? ORDER BY created_at ASC",
                (lead_member_id,),
            ).fetchall()
        finally:
            conn.close()
        self.assertEqual(row["status"], "closed")
        self.assertIn("강의 신청으로 전환", row["admin_note"])
        self.assertTrue(any(log["action"] == "lead_upgraded_to_apply" for log in logs))
        duplicate_log = next(log for log in logs if log["action"] == "duplicate_apply")
        self.assertTrue(json.loads(duplicate_log["detail"])["converted"])

    def test_consultation_lead_upgrades_to_paid_application(self):
        lead_response = self.client.post(
            "/api/consultations",
            json={
                "source": "consulting_page",
                "topic": "자동화 상담",
                "name": "상담 리드",
                "phone": "010-8888-9999",
                "email": "consult-lead@example.com",
                "message": "유료 강의 상담 후 신청 예정입니다.",
                "consent_privacy": True,
            },
        )
        self.assertEqual(lead_response.status_code, 200)
        lead_member_id = lead_response.json()["member_id"]
        self.assertEqual(db_manager.get_member(lead_member_id)["plan_type"], "consultation")

        apply_payload = {
            "name": "상담 리드",
            "email": "consult-lead@example.com",
            "phone": "010-8888-9999",
            "gender": "남",
            "age": 39,
            "job": "대표",
            "referral_source": "기타",
            "reason": "상담 이후 유료 강의 신청으로 전환하는 흐름을 검증합니다.",
            "ai_level": "초급",
            "plan_type": "full",
            "ai_tools": ["ChatGPT"],
            "ai_subscription": "유료",
            "ai_weekly_hours": "1-3시간",
            "ai_use_cases": ["문서자동화"],
            "group_goals": ["사업 자동화"],
            "short_term_goal": "카카오톡 자동화 설계",
            "participation_type": "유료강의",
            "preferred_schedule": "주말 오후",
            "available_time_slots": ["주말 오후"],
            "region": "경기 안양",
            "main_device": "노트북",
            "can_code": False,
            "can_present": True,
            "skills": "기획",
            "contribution": "사례 공유",
            "consent_personal": True,
            "consent_marketing": True,
        }
        with patch.object(self.main, "save_to_sheets", return_value=False), patch.object(
            self.main,
            "backup_database",
            return_value={"ok_count": 0, "failed_count": 0, "targets": []},
        ), patch.object(self.main, "notify_admin_new_apply", return_value="ok") as notify:
            apply_response = self.client.post("/apply", json=apply_payload)

        self.assertEqual(apply_response.status_code, 200)
        body = apply_response.json()
        self.assertTrue(body["ok"])
        self.assertFalse(body["duplicate"])
        self.assertTrue(body["upgraded_from_lead"])
        self.assertEqual(body["member_id"], lead_member_id)
        self.assertIn("상담", body["message"])
        self.assertIn("유료강의", body["message"])
        upgraded = db_manager.get_member(lead_member_id)
        self.assertEqual(upgraded["plan_type"], "full")
        self.assertEqual(upgraded["status"], "pending")
        self.assertEqual(upgraded["job"], "대표")
        notify.assert_called_once()
        self.assertEqual(notify.call_args.kwargs["lead_upgrade_from"], "consultation")

        conn = db_manager.get_conn()
        try:
            row = conn.execute("SELECT status FROM consultations WHERE member_id=?", (lead_member_id,)).fetchone()
        finally:
            conn.close()
        self.assertEqual(row["status"], "closed")

    def test_member_erasure_requires_admin_anonymizes_contact_and_cancels_bookings(self):
        member_id = self._create_member()
        session_id = booking_manager.create_session(
            {
                "starts_at": "2026-05-17T01:00:00+00:00",
                "ends_at": "2026-05-17T03:00:00+00:00",
                "location": "영등포시장역 사무실",
                "status": "open",
            }
        )
        booking_id = booking_manager.create_booking(
            {
                "session_id": session_id,
                "member_id": member_id,
                "applicant_name": "Contact Reveal Test",
                "phone_masked": "010-****-3333",
                "status": "requested",
                "payment_status": "not_sent",
            }
        )

        denied = self.client.post(f"/members/{member_id}/erase", json={"cancel_bookings": True})
        allowed = self.client.post(
            f"/members/{member_id}/erase",
            headers=self._admin_headers(),
            json={"cancel_bookings": True},
        )

        self.assertEqual(denied.status_code, 401)
        self.assertEqual(allowed.status_code, 200)
        self.assertEqual(allowed.json()["data"]["bookings_canceled"], 1)

        detail = self.client.get(f"/members/{member_id}", headers=self._admin_headers())
        self.assertEqual(detail.status_code, 200)
        detail_payload = detail.json()["data"]
        self.assertEqual(detail_payload["status"], "erased")
        self.assertEqual(detail_payload["name"], "삭제된 신청자")
        self.assertEqual(detail_payload["phone_masked"], "삭제됨")
        self.assertNotIn(self.RAW_PHONE, str(detail.json()))
        self.assertNotIn(self.RAW_EMAIL, str(detail.json()))

        contact = self.client.get(f"/members/{member_id}/contact", headers=self._admin_headers())
        self.assertEqual(contact.status_code, 200)
        contact_payload = contact.json()["data"]
        self.assertEqual(contact_payload["phone"], "")
        self.assertEqual(contact_payload["email"], "")
        self.assertEqual(contact_payload["phone_masked"], "삭제됨")

        booking = booking_manager.get_booking(booking_id)
        self.assertEqual(booking["status"], "canceled")
        self.assertEqual(booking["applicant_name"], "삭제된 신청자")
        self.assertEqual(booking["phone_masked"], "삭제됨")
        session = booking_manager.get_session(session_id)
        self.assertEqual(session["active_booking_count"], 0)

    def test_contact_csv_export_requires_admin_and_writes_minimal_audit_log(self):
        self._create_member()

        denied = self.client.get("/admin/contacts.csv")
        allowed = self.client.get("/admin/contacts.csv", headers=self._admin_headers())

        self.assertEqual(denied.status_code, 401)
        self.assertEqual(allowed.status_code, 200)
        self.assertEqual(allowed.headers["content-type"], "text/csv; charset=utf-8")
        body = allowed.text
        self.assertIn("Name,Given Name,Family Name,Phone 1 - Type,Phone 1 - Value", body)
        self.assertIn("[ARSEN 기본] Contact Reveal Test", body)
        self.assertIn("plan=basic; status=pending; member_id=", body)
        self.assertIn("member_id,name,phone,email,status,plan_type,participation_grade,created_at", body)
        self.assertIn(self.RAW_PHONE, body)
        self.assertIn(self.RAW_EMAIL, body)

        logs = self._system_contact_export_logs()
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0][0], "contact_export_csv")
        self.assertEqual(logs[0][1], "count=1")
        self.assertNotIn(self.RAW_PHONE, logs[0][1])
        self.assertNotIn(self.RAW_EMAIL, logs[0][1])

    def test_contact_vcard_export_requires_admin_and_returns_vcard(self):
        self._create_member()

        denied = self.client.get("/admin/contacts.vcf")
        allowed = self.client.get("/admin/contacts.vcf", headers=self._admin_headers())

        self.assertEqual(denied.status_code, 401)
        self.assertEqual(allowed.status_code, 200)
        self.assertEqual(allowed.headers["content-type"], "text/vcard; charset=utf-8")
        body = allowed.text
        self.assertIn("BEGIN:VCARD", body)
        self.assertIn("VERSION:3.0", body)
        self.assertIn("FN:[ARSEN 기본] Contact Reveal Test", body)
        self.assertIn("NOTE:plan=basic\\; status=pending\\; member_id=", body)
        self.assertIn(f"TEL;TYPE=CELL:{self.RAW_PHONE}", body)
        self.assertIn(f"EMAIL:{self.RAW_EMAIL}", body)

        logs = self._system_contact_export_logs()
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0][0], "contact_export_vcard")
        self.assertEqual(logs[0][1], "count=1")
        self.assertNotIn(self.RAW_PHONE, logs[0][1])
        self.assertNotIn(self.RAW_EMAIL, logs[0][1])

    def test_contacts_export_csv_new_route_writes_contacts_export_audit_log(self):
        self._create_member()

        denied = self.client.get("/admin/contacts-export.csv")
        allowed = self.client.get("/admin/contacts-export.csv", headers=self._admin_headers())

        self.assertEqual(denied.status_code, 401)
        self.assertEqual(allowed.status_code, 200)
        self.assertEqual(allowed.headers["content-type"], "text/csv; charset=utf-8")
        body = allowed.text
        self.assertIn("Name,Given Name,Family Name,Phone 1 - Type,Phone 1 - Value", body)
        self.assertIn("[ARSEN 기본] Contact Reveal Test", body)
        self.assertIn("plan=basic; status=pending; member_id=", body)
        self.assertIn("member_id,name,phone,email,status,plan_type,participation_grade,created_at,booking_status_summary", body)
        self.assertIn(self.RAW_PHONE, body)
        self.assertIn(self.RAW_EMAIL, body)

        logs = self._system_contacts_export_logs()
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0][0], "contacts_export")
        self.assertIn('"format": "csv"', logs[0][1])
        self.assertIn('"count": 1', logs[0][1])
        self.assertNotIn(self.RAW_PHONE, logs[0][1])
        self.assertNotIn(self.RAW_EMAIL, logs[0][1])

    def test_contacts_export_vcard_new_route_writes_contacts_export_audit_log(self):
        self._create_member()

        allowed = self.client.get("/admin/contacts-export.vcf", headers=self._admin_headers())

        self.assertEqual(allowed.status_code, 200)
        self.assertEqual(allowed.headers["content-type"], "text/vcard; charset=utf-8")
        body = allowed.text
        self.assertIn("BEGIN:VCARD", body)
        self.assertIn("FN:[ARSEN 기본] Contact Reveal Test", body)
        self.assertIn(f"TEL;TYPE=CELL:{self.RAW_PHONE}", body)
        self.assertIn(f"EMAIL:{self.RAW_EMAIL}", body)
        self.assertIn("plan=basic\\; status=pending\\; member_id=", body)

        logs = self._system_contacts_export_logs()
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0][0], "contacts_export")
        self.assertIn('"format": "vcf"', logs[0][1])
        self.assertNotIn(self.RAW_PHONE, logs[0][1])
        self.assertNotIn(self.RAW_EMAIL, logs[0][1])

    def test_contacts_export_plan_filter_uses_group_name_prefixes(self):
        self._create_member(name="Free Applicant", plan_type="free")
        self._create_member(name="Paid Applicant", plan_type="full")
        self._create_member(name="Consult Applicant", plan_type="consultation")

        free_csv = self.client.get(
            "/admin/contacts-export.csv?plan_type=free",
            headers=self._admin_headers(),
        )
        full_vcf = self.client.get(
            "/admin/contacts-export.vcf?plan_type=full",
            headers=self._admin_headers(),
        )
        consultation_csv = self.client.get(
            "/admin/contacts-export.csv?plan_type=consultation",
            headers=self._admin_headers(),
        )

        self.assertEqual(free_csv.status_code, 200)
        self.assertIn("[ARSEN 무료] Free Applicant", free_csv.text)
        self.assertNotIn("Paid Applicant", free_csv.text)
        self.assertNotIn("Consult Applicant", free_csv.text)
        self.assertEqual(full_vcf.status_code, 200)
        self.assertIn("FN:[ARSEN 유료] Paid Applicant", full_vcf.text)
        self.assertNotIn("Free Applicant", full_vcf.text)
        self.assertNotIn("Consult Applicant", full_vcf.text)
        self.assertEqual(consultation_csv.status_code, 200)
        self.assertIn("[ARSEN 상담] Consult Applicant", consultation_csv.text)
        self.assertNotIn("Free Applicant", consultation_csv.text)
        self.assertNotIn("Paid Applicant", consultation_csv.text)

        logs = self._system_contacts_export_logs()
        self.assertEqual(len(logs), 3)
        for _, detail in logs:
            self.assertNotIn(self.RAW_PHONE, detail)
            self.assertNotIn(self.RAW_EMAIL, detail)

    def test_contacts_export_routes_use_strict_admin_key_dependency(self):
        source = Path(self.main.__file__).read_text(encoding="utf-8")
        routes = [
            '@app.get("/admin/contacts-export.csv")',
            '@app.head("/admin/contacts-export.csv")',
            '@app.get("/admin/contacts-export.vcf")',
            '@app.head("/admin/contacts-export.vcf")',
        ]

        for route in routes:
            start = source.index(route)
            next_route = source.find("@app.", start + len(route))
            section = source[start: next_route if next_route != -1 else len(source)]
            self.assertIn("Depends(require_admin_key)", section)
            self.assertNotIn("Depends(require_admin)", section)


if __name__ == "__main__":
    unittest.main()
