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


class LicenseApiContractTest(unittest.TestCase):
    ADMIN_KEY = "license-api-test-admin-key"

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.tmpdir.name) / "members.db"
        self.original_db_path = db.DB_PATH
        db.DB_PATH = self.db_path
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
        self.tmpdir.cleanup()

    def _headers(self):
        return {"X-Admin-Key": self.ADMIN_KEY}

    def test_admin_create_license_requires_auth_and_returns_key_once(self):
        denied = self.client.post("/admin/licenses", json={"plan_code": "pro"})
        self.assertEqual(denied.status_code, 401)

        response = self.client.post(
            "/admin/licenses",
            headers=self._headers(),
            json={"plan_code": "pro", "max_devices": 1},
        )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertTrue(payload["ok"])
        self.assertIn("license_key", payload)
        self.assertEqual(payload["license"]["plan_code"], "pro")
        self.assertNotIn("license_key_hash", payload["license"])

        listed = self.client.get("/admin/licenses", headers=self._headers())
        self.assertEqual(listed.status_code, 200)
        listed_text = str(listed.json())
        self.assertNotIn(payload["license_key"], listed_text)
        self.assertIn(payload["license"]["license_key_hint"], listed_text)

    def test_activate_and_verify_public_contract(self):
        created = self.client.post(
            "/admin/licenses",
            headers=self._headers(),
            json={"plan_code": "basic", "max_devices": 1},
        ).json()

        activated = self.client.post(
            "/api/license/activate",
            json={
                "license_key": created["license_key"],
                "hwid": "WIN-HWID-API-1",
                "app_version": "1.0.0",
                "platform": "windows",
                "device_name": "test-pc",
            },
        )

        self.assertEqual(activated.status_code, 200)
        activated_payload = activated.json()
        self.assertTrue(activated_payload["ok"])
        self.assertIn("activation_token", activated_payload)

        verified = self.client.post(
            "/api/license/verify",
            headers={"Authorization": f"Bearer {activated_payload['activation_token']}"},
            json={
                "hwid": "WIN-HWID-API-1",
                "app_version": "1.0.0",
                "platform": "windows",
            },
        )

        self.assertEqual(verified.status_code, 200)
        self.assertTrue(verified.json()["ok"])

    def test_verify_requires_bearer_token(self):
        response = self.client.post(
            "/api/license/verify",
            json={"hwid": "WIN-HWID-API-1"},
        )

        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
