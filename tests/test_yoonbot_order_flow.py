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


class YoonbotOrderFlowTest(unittest.TestCase):
    ADMIN_KEY = "yoonbot-order-test-admin-key"

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

    def _create_order(self, plan_code="monthly"):
        response = self.client.post(
            "/api/yoonbot/orders",
            json={
                "buyer_name": "테스트구매자",
                "buyer_email": "buyer@example.com",
                "buyer_phone": "010-1234-5678",
                "plan_code": plan_code,
                "consent_privacy": True,
                "consent_terms": True,
            },
        )
        self.assertEqual(response.status_code, 200)
        return response.json()["data"]

    def test_products_and_public_order_creation_store_masked_contact_only(self):
        products = self.client.get("/api/yoonbot/products")
        self.assertEqual(products.status_code, 200)
        self.assertIn("monthly", {plan["code"] for plan in products.json()["plans"]})

        order = self._create_order()

        self.assertEqual(order["status"], "payment_pending")
        self.assertEqual(order["product_code"], "yoonbot")
        self.assertEqual(order["plan_code"], "monthly")
        self.assertIn("*", order["buyer_email_masked"])
        self.assertIn("*", order["buyer_phone_masked"])
        self.assertNotIn("buyer@example.com", str(order))
        self.assertNotIn("010-1234-5678", str(order))

        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT * FROM orders WHERE id=?", (order["id"],)).fetchone()
        conn.close()
        self.assertNotEqual(row["buyer_email_hash"], "buyer@example.com")
        self.assertNotIn("010-1234-5678", str(dict(row)))

    def test_admin_mark_paid_issue_license_and_prevent_duplicate_issue(self):
        order = self._create_order("monthly")

        denied = self.client.get("/admin/yoonbot/orders")
        self.assertEqual(denied.status_code, 401)

        paid = self.client.post(
            f"/admin/yoonbot/orders/{order['id']}/mark-paid",
            headers=self._headers(),
            json={"payment_provider": "manual_bank_transfer", "payment_ref": order["payment_ref"]},
        )
        self.assertEqual(paid.status_code, 200)
        self.assertEqual(paid.json()["data"]["status"], "paid")

        issued = self.client.post(
            f"/admin/yoonbot/orders/{order['id']}/issue-license",
            headers=self._headers(),
        )
        self.assertEqual(issued.status_code, 200)
        issued_payload = issued.json()
        self.assertTrue(issued_payload["ok"])
        self.assertIn("license_key", issued_payload)
        self.assertEqual(issued_payload["order"]["status"], "license_issued")

        duplicate = self.client.post(
            f"/admin/yoonbot/orders/{order['id']}/issue-license",
            headers=self._headers(),
        )
        self.assertEqual(duplicate.status_code, 400)

    def test_cancel_and_refund_orders_do_not_issue_license(self):
        canceled = self._create_order("trial")
        cancel_response = self.client.post(
            f"/admin/yoonbot/orders/{canceled['id']}/cancel",
            headers=self._headers(),
            json={"note": "unit test cancel"},
        )
        self.assertEqual(cancel_response.status_code, 200)
        blocked_cancel = self.client.post(
            f"/admin/yoonbot/orders/{canceled['id']}/issue-license",
            headers=self._headers(),
        )
        self.assertEqual(blocked_cancel.status_code, 400)

        refunded = self._create_order("yearly")
        refund_response = self.client.post(
            f"/admin/yoonbot/orders/{refunded['id']}/refund-note",
            headers=self._headers(),
            json={"note": "unit test refund"},
        )
        self.assertEqual(refund_response.status_code, 200)
        blocked_refund = self.client.post(
            f"/admin/yoonbot/orders/{refunded['id']}/issue-license",
            headers=self._headers(),
        )
        self.assertEqual(blocked_refund.status_code, 400)


if __name__ == "__main__":
    unittest.main()
