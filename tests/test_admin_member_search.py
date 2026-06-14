"""Admin member search, filter, and erase regression tests.

Covers:
- /members endpoint includes/excludes erased members correctly
- Erased member re-erase is idempotent
- list_members() status filtering
- Double-erase does not corrupt data
"""

import importlib
import sys
import tempfile
import types
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import db
from agents import db_manager
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
            pass

    asyncio_module.AsyncIOScheduler = AsyncIOScheduler
    cron_module.CronTrigger = CronTrigger
    sys.modules["apscheduler"] = apscheduler
    sys.modules["apscheduler.schedulers"] = schedulers
    sys.modules["apscheduler.schedulers.asyncio"] = asyncio_module
    sys.modules["apscheduler.triggers"] = triggers
    sys.modules["apscheduler.triggers.cron"] = cron_module


def _make_member_payload(**overrides):
    encrypted = encrypt_data({"phone": "010-1234-5678", "email": "test@example.com"})
    base = {
        "name": "테스트 신청자",
        "email_encrypted": encrypted["email_encrypted"],
        "email_hash": encrypted["email_hash"],
        "phone_masked": encrypted["phone_masked"],
        "phone_encrypted": encrypted["phone_encrypted"],
        "phone_hash": encrypted["phone_hash"],
        "gender": "남",
        "age": 30,
        "job": "개발자",
        "referral_source": "unit-test",
        "reason": "regression test",
        "ai_level": "입문",
        "plan_type": "basic",
        "consent_personal": True,
        "consent_marketing": False,
        "consent_at": "2026-05-10T00:00:00+00:00",
        "consent_version": "1.0",
    }
    base.update(overrides)
    return base


class AdminMemberSearchTest(unittest.TestCase):
    ADMIN_KEY = "search-test-admin-key"

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

    def _headers(self):
        return {"X-Admin-Key": self.ADMIN_KEY}

    def _create_member(self, **overrides):
        member_id = db_manager.create_member(_make_member_payload(**overrides))
        return db_manager.get_member(member_id)

    # --- /members endpoint ---

    def test_members_endpoint_includes_erased_by_default(self):
        """GET /members (no filter) must include erased members in response."""
        member = self._create_member()
        db_manager.erase_member_personal_data(member["id"], cancel_bookings=False)

        resp = self.client.get("/members", headers=self._headers())
        self.assertEqual(resp.status_code, 200)
        ids = [m["id"] for m in resp.json()["data"]]
        self.assertIn(member["id"], ids, "Erased member should appear in unfiltered /members")

    def test_members_endpoint_status_filter_erased(self):
        """GET /members?status=erased returns only erased members."""
        active = self._create_member(name="활성 신청자")
        erased_member = self._create_member(name="지울 신청자")
        db_manager.erase_member_personal_data(erased_member["id"], cancel_bookings=False)

        resp = self.client.get("/members?status=erased", headers=self._headers())
        self.assertEqual(resp.status_code, 200)
        data = resp.json()["data"]
        returned_ids = {m["id"] for m in data}
        self.assertIn(erased_member["id"], returned_ids)
        self.assertNotIn(active["id"], returned_ids)

    def test_members_endpoint_status_filter_pending_excludes_erased(self):
        """GET /members?status=pending must not include erased members."""
        erased_member = self._create_member()
        db_manager.erase_member_personal_data(erased_member["id"], cancel_bookings=False)

        resp = self.client.get("/members?status=pending", headers=self._headers())
        self.assertEqual(resp.status_code, 200)
        ids = [m["id"] for m in resp.json()["data"]]
        self.assertNotIn(erased_member["id"], ids, "Pending filter must exclude erased")

    def test_members_endpoint_no_sensitive_fields(self):
        """GET /members must strip phone_encrypted and email_encrypted."""
        self._create_member()
        resp = self.client.get("/members", headers=self._headers())
        self.assertEqual(resp.status_code, 200)
        for member in resp.json()["data"]:
            self.assertNotIn("phone_encrypted", member)
            self.assertNotIn("email_encrypted", member)
            self.assertNotIn("access_code", member)

    # --- erase endpoint ---

    def test_erase_sets_status_to_erased(self):
        """POST /members/{id}/erase must set status to 'erased'."""
        member = self._create_member()
        resp = self.client.post(
            f"/members/{member['id']}/erase",
            json={"cancel_bookings": False},
            headers=self._headers(),
        )
        self.assertEqual(resp.status_code, 200)
        body = resp.json()
        self.assertTrue(body["ok"])
        self.assertEqual(body["data"]["status"], "erased")

        updated = db_manager.get_member(member["id"])
        self.assertEqual(updated["status"], "erased")

    def test_erase_anonymizes_name_and_phone(self):
        """Erased member must have anonymized name and phone."""
        member = self._create_member()
        self.client.post(
            f"/members/{member['id']}/erase",
            json={"cancel_bookings": False},
            headers=self._headers(),
        )
        updated = db_manager.get_member(member["id"])
        self.assertEqual(updated["name"], "삭제된 신청자")
        self.assertEqual(updated["phone_masked"], "삭제됨")

    def test_erase_twice_is_idempotent(self):
        """Re-erasing an already-erased member must succeed and not raise 404."""
        member = self._create_member()
        for _ in range(2):
            resp = self.client.post(
                f"/members/{member['id']}/erase",
                json={"cancel_bookings": False},
                headers=self._headers(),
            )
            self.assertEqual(resp.status_code, 200, f"Re-erase must succeed, got {resp.status_code}")
            self.assertEqual(resp.json()["data"]["status"], "erased")

        updated = db_manager.get_member(member["id"])
        self.assertEqual(updated["status"], "erased")
        self.assertEqual(updated["name"], "삭제된 신청자")

    def test_erase_nonexistent_member_returns_404(self):
        """Erasing a member that does not exist must return 404."""
        resp = self.client.post(
            "/members/nonexistent-id/erase",
            json={"cancel_bookings": False},
            headers=self._headers(),
        )
        self.assertEqual(resp.status_code, 404)

    # --- list_members() DB helper ---

    def test_list_members_no_filter_includes_erased(self):
        """list_members() with no filter returns all members including erased."""
        member = self._create_member()
        db_manager.erase_member_personal_data(member["id"], cancel_bookings=False)

        all_members = db_manager.list_members()
        ids = [m["id"] for m in all_members]
        self.assertIn(member["id"], ids)

    def test_list_members_status_erased_filter(self):
        """list_members(status='erased') returns only erased members."""
        active = self._create_member(name="활성")
        erased_member = self._create_member(name="삭제")
        db_manager.erase_member_personal_data(erased_member["id"], cancel_bookings=False)

        erased_list = db_manager.list_members(status="erased")
        ids = {m["id"] for m in erased_list}
        self.assertIn(erased_member["id"], ids)
        self.assertNotIn(active["id"], ids)

    def test_list_members_status_pending_excludes_erased(self):
        """list_members(status='pending') must not include erased members."""
        erased_member = self._create_member()
        db_manager.erase_member_personal_data(erased_member["id"], cancel_bookings=False)

        pending_list = db_manager.list_members(status="pending")
        ids = [m["id"] for m in pending_list]
        self.assertNotIn(erased_member["id"], ids)

    def test_erase_requires_admin_auth(self):
        """POST /members/{id}/erase without admin key must return 401/403."""
        member = self._create_member()
        resp = self.client.post(
            f"/members/{member['id']}/erase",
            json={"cancel_bookings": False},
        )
        self.assertIn(resp.status_code, (401, 403))

    def test_members_endpoint_requires_admin_auth(self):
        """GET /members without admin key must return 401/403."""
        resp = self.client.get("/members")
        self.assertIn(resp.status_code, (401, 403))

    # --- storage status / snapshot erased-member exclusion ---

    def test_storage_status_recent_excludes_erased_members(self):
        """get_storage_status() recent panel must not include erased members."""
        active = self._create_member(name="활성 신청자")
        erased_member = self._create_member(name="지울 신청자")
        db_manager.erase_member_personal_data(erased_member["id"], cancel_bookings=False)

        status = db_manager.get_storage_status(limit=10)
        recent_ids = [m["id"] for m in status["recent"]]
        self.assertIn(active["id"], recent_ids, "Active member must appear in recent panel")
        self.assertNotIn(erased_member["id"], recent_ids, "Erased member must not appear in recent panel")

    def test_storage_snapshot_recent_excludes_erased_members(self):
        """get_storage_snapshot() recent rows must not include erased members."""
        active = self._create_member(name="활성 신청자")
        erased_member = self._create_member(name="지울 신청자")
        db_manager.erase_member_personal_data(erased_member["id"], cancel_bookings=False)

        snapshot = db_manager.get_storage_snapshot(limit=10)
        recent_ids = [m["member_id"] for m in snapshot["recent"]]
        self.assertIn(active["id"], recent_ids, "Active member must appear in snapshot recent rows")
        self.assertNotIn(erased_member["id"], recent_ids, "Erased member must not appear in snapshot recent rows")

    def test_storage_status_only_erased_shows_empty_recent(self):
        """get_storage_status() recent must be empty when only erased members exist."""
        erased_member = self._create_member()
        db_manager.erase_member_personal_data(erased_member["id"], cancel_bookings=False)

        status = db_manager.get_storage_status(limit=10)
        self.assertEqual(status["recent"], [], "Recent panel must be empty when all members are erased")


if __name__ == "__main__":
    unittest.main()
