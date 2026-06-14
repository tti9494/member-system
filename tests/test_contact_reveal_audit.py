import importlib
import sqlite3
import sys
import tempfile
import types
import unittest
from pathlib import Path

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

        free_csv = self.client.get(
            "/admin/contacts-export.csv?plan_type=free",
            headers=self._admin_headers(),
        )
        full_vcf = self.client.get(
            "/admin/contacts-export.vcf?plan_type=full",
            headers=self._admin_headers(),
        )

        self.assertEqual(free_csv.status_code, 200)
        self.assertIn("[ARSEN 무료] Free Applicant", free_csv.text)
        self.assertNotIn("Paid Applicant", free_csv.text)
        self.assertEqual(full_vcf.status_code, 200)
        self.assertIn("FN:[ARSEN 유료] Paid Applicant", full_vcf.text)
        self.assertNotIn("Free Applicant", full_vcf.text)

        logs = self._system_contacts_export_logs()
        self.assertEqual(len(logs), 2)
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
