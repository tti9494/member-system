import importlib
import os
import sqlite3
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import MagicMock

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

    def test_issue_license_customer_message_contains_download_and_install_guide(self):
        order = self._create_order("monthly")
        self.client.post(
            f"/admin/yoonbot/orders/{order['id']}/mark-paid",
            headers=self._headers(),
            json={"payment_provider": "manual_bank_transfer", "payment_ref": order["payment_ref"]},
        )
        issued = self.client.post(
            f"/admin/yoonbot/orders/{order['id']}/issue-license",
            headers=self._headers(),
        )
        self.assertEqual(issued.status_code, 200)
        payload = issued.json()
        msg = payload.get("customer_message", "")

        # 다운로드 안내는 공식 홈페이지 한 곳만 가리킨다
        self.assertIn("https://arsen-ai.com/yoonbot", msg)
        self.assertIn("공개 릴리스가 준비된 경우에만", msg)
        # 구 Arsen Content Launcher ZIP 직접 링크와 launcher release 링크 금지
        self.assertNotIn("arsen-content-launcher-0.1.0-win-x64.zip", msg)
        self.assertNotIn("/api/daf/launcher", msg)
        self.assertNotIn("/api/launcher/release", msg)
        # 설치 안내 포함 여부
        self.assertIn("설치 방법", msg)
        self.assertIn("라이선스 키를 입력", msg)
        # 초기 파일럿/베타 안내 포함 여부
        self.assertIn("파일럿", msg)
        # 문의/피드백 안내 포함 여부
        self.assertIn("피드백", msg)

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


class TossPaymentIntegrationTest(unittest.TestCase):
    """Tests for Toss Payments integration without real API calls."""

    ADMIN_KEY = "toss-test-admin-key"

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

        # Ensure clean env (no Toss keys by default) + fingerprint secret for tests
        self._clear_toss_env()
        self.original_code_secret = os.environ.get("CODE_SECRET_KEY")
        os.environ["CODE_SECRET_KEY"] = "toss-test-code-secret-key-32chars!!"

    def tearDown(self):
        self.main.ADMIN_API_KEY = self.original_admin_key
        self.main.MEMBER_ADMIN_LOCAL_OPEN = self.original_local_open
        self.main.LOCAL_ADMIN_OPEN_FLAG = self.original_local_flag
        db.DB_PATH = self.original_db_path
        self.tmpdir.cleanup()
        self._clear_toss_env()
        if self.original_code_secret is None:
            os.environ.pop("CODE_SECRET_KEY", None)
        else:
            os.environ["CODE_SECRET_KEY"] = self.original_code_secret

    def _clear_toss_env(self):
        for key in ("YOONBOT_PAYMENT_PROVIDER", "TOSS_PAYMENTS_CLIENT_KEY", "TOSS_PAYMENTS_SECRET_KEY"):
            os.environ.pop(key, None)

    def _headers(self):
        return {"X-Admin-Key": self.ADMIN_KEY}

    def _create_order(self, plan_code="monthly"):
        response = self.client.post(
            "/api/yoonbot/orders",
            json={
                "buyer_name": "토스테스트",
                "buyer_email": "toss@example.com",
                "buyer_phone": "010-9999-1111",
                "plan_code": plan_code,
                "consent_privacy": True,
                "consent_terms": True,
            },
        )
        self.assertEqual(response.status_code, 200)
        return response.json()

    def test_manual_flow_is_default_when_toss_not_configured(self):
        """Without Toss env vars, order creation returns manual_bank_transfer mode."""
        payload = self._create_order("monthly")
        self.assertEqual(payload["payment"]["mode"], "manual_bank_transfer")
        self.assertFalse(payload["payment"]["auto_charge"])
        # secret key must never appear in response
        self.assertNotIn("secret", str(payload).lower())
        self.assertNotIn("TOSS_PAYMENTS_SECRET_KEY", str(payload))

    def test_toss_mode_payload_does_not_expose_secret_key(self):
        """When Toss is configured, response includes client_key but not secret_key."""
        os.environ["YOONBOT_PAYMENT_PROVIDER"] = "toss_payments"
        os.environ["TOSS_PAYMENTS_CLIENT_KEY"] = "test_ck_testkey123"
        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_supersecret999"

        payload = self._create_order("monthly")
        payment = payload["payment"]

        self.assertEqual(payment["mode"], "toss_payments")
        self.assertIn("client_key", payment)
        self.assertEqual(payment["client_key"], "test_ck_testkey123")
        # Secret key must NEVER appear anywhere in the response
        response_str = str(payload)
        self.assertNotIn("test_sk_supersecret999", response_str)
        self.assertNotIn("TOSS_PAYMENTS_SECRET_KEY", response_str)
        self.assertIn("toss_order_id", payment)
        self.assertTrue(payment["toss_order_id"].startswith("yb-"))

    def test_toss_confirm_rejects_tampered_amount(self):
        """confirm_toss_payment raises ValueError when client_amount != server amount."""
        from agents.order_manager import confirm_toss_payment, generate_toss_order_id

        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_secret"

        # Create order via API to get a real order_id
        api_payload = self._create_order("monthly")
        order = api_payload["data"]
        order_id = order["id"]
        correct_toss_order_id = generate_toss_order_id(order_id)
        correct_amount = int(order["amount_krw"])

        stub_client = MagicMock()
        stub_client.confirm.return_value = {"status": "DONE"}

        with self.assertRaises(ValueError) as ctx:
            confirm_toss_payment(
                order_id=order_id,
                payment_key="pk_test_tamperedkey",
                client_amount=correct_amount + 1,  # tampered
                toss_order_id=correct_toss_order_id,
                confirm_client=stub_client,
            )
        self.assertIn("금액", str(ctx.exception))
        stub_client.confirm.assert_not_called()

    def test_toss_confirm_rejects_tampered_order_id(self):
        """confirm_toss_payment raises ValueError when toss_order_id doesn't match server value."""
        from agents.order_manager import confirm_toss_payment

        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_secret"

        api_payload = self._create_order("monthly")
        order = api_payload["data"]
        order_id = order["id"]
        correct_amount = int(order["amount_krw"])

        stub_client = MagicMock()

        with self.assertRaises(ValueError) as ctx:
            confirm_toss_payment(
                order_id=order_id,
                payment_key="pk_test_key",
                client_amount=correct_amount,
                toss_order_id="yb-tampered0000000000000000000001",  # wrong
                confirm_client=stub_client,
            )
        self.assertIn("orderId", str(ctx.exception))
        stub_client.confirm.assert_not_called()

    def test_toss_confirm_succeeds_with_mocked_client_and_marks_paid(self):
        """confirm_toss_payment marks order paid when mock client succeeds."""
        from agents.order_manager import confirm_toss_payment, generate_toss_order_id, get_order

        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_secret"

        api_payload = self._create_order("monthly")
        order = api_payload["data"]
        order_id = order["id"]
        correct_toss_order_id = generate_toss_order_id(order_id)
        correct_amount = int(order["amount_krw"])

        stub_client = MagicMock()
        stub_client.confirm.return_value = {"status": "DONE", "paymentKey": "pk_test_success"}

        result = confirm_toss_payment(
            order_id=order_id,
            payment_key="pk_test_success",
            client_amount=correct_amount,
            toss_order_id=correct_toss_order_id,
            confirm_client=stub_client,
        )

        self.assertTrue(result["ok"])
        stub_client.confirm.assert_called_once_with("pk_test_success", correct_toss_order_id, correct_amount)

        # Order must now be paid
        updated = get_order(order_id)
        self.assertEqual(updated["status"], "paid")
        self.assertEqual(updated["payment_provider"], "toss_payments")

    def test_toss_confirm_does_not_auto_issue_license(self):
        """After Toss confirm, order is paid but license is NOT automatically issued."""
        from agents.order_manager import confirm_toss_payment, generate_toss_order_id, get_order

        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_secret"

        api_payload = self._create_order("monthly")
        order = api_payload["data"]
        order_id = order["id"]
        correct_toss_order_id = generate_toss_order_id(order_id)
        correct_amount = int(order["amount_krw"])

        stub_client = MagicMock()
        stub_client.confirm.return_value = {"status": "DONE"}

        confirm_toss_payment(
            order_id=order_id,
            payment_key="pk_test_nolicenseauto",
            client_amount=correct_amount,
            toss_order_id=correct_toss_order_id,
            confirm_client=stub_client,
        )

        updated = get_order(order_id)
        self.assertEqual(updated["status"], "paid")
        self.assertIsNone(updated.get("license_id"))  # no license auto-issued

    def test_pending_unpaid_order_cannot_issue_license_via_admin(self):
        """payment_pending order must be blocked from license issuance via admin endpoint."""
        api_payload = self._create_order("monthly")
        order = api_payload["data"]
        order_id = order["id"]

        blocked = self.client.post(
            f"/admin/yoonbot/orders/{order_id}/issue-license",
            headers=self._headers(),
        )
        self.assertEqual(blocked.status_code, 400)
        self.assertIn("결제", blocked.json().get("detail", ""))

    def test_toss_confirm_endpoint_via_api(self):
        """POST /api/yoonbot/orders/{id}/payments/toss/confirm requires valid payload."""
        from agents import order_manager
        from agents.order_manager import generate_toss_order_id

        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_secret"

        api_payload = self._create_order("monthly")
        order = api_payload["data"]
        order_id = order["id"]
        correct_toss_order_id = generate_toss_order_id(order_id)
        correct_amount = int(order["amount_krw"])

        # Patch confirm_yoonbot_toss_payment in main to use a stub confirm_client
        original_fn = self.main.confirm_yoonbot_toss_payment

        def patched_confirm(order_id, payment_key, client_amount, toss_order_id, confirm_client=None):
            stub = MagicMock()
            stub.confirm.return_value = {"status": "DONE"}
            return original_fn(order_id, payment_key, client_amount, toss_order_id, confirm_client=stub)

        self.main.confirm_yoonbot_toss_payment = patched_confirm
        try:
            response = self.client.post(
                f"/api/yoonbot/orders/{order_id}/payments/toss/confirm",
                json={
                    "payment_key": "pk_test_apitest",
                    "order_id": correct_toss_order_id,
                    "amount": correct_amount,
                },
            )
        finally:
            self.main.confirm_yoonbot_toss_payment = original_fn

        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertTrue(result["ok"])
        self.assertEqual(result["data"]["status"], "paid")

    def test_toss_confirm_endpoint_rejects_tampered_amount_via_api(self):
        """Tampered amount is rejected by the confirm endpoint with 400."""
        from agents.order_manager import generate_toss_order_id

        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_secret"

        api_payload = self._create_order("monthly")
        order = api_payload["data"]
        order_id = order["id"]
        correct_toss_order_id = generate_toss_order_id(order_id)
        correct_amount = int(order["amount_krw"])

        response = self.client.post(
            f"/api/yoonbot/orders/{order_id}/payments/toss/confirm",
            json={
                "payment_key": "pk_test_tamper",
                "order_id": correct_toss_order_id,
                "amount": correct_amount + 9999,  # tampered
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("금액", response.json().get("detail", ""))

    def test_success_url_points_to_frontend_page_not_api(self):
        """success_url in Toss payload must be a frontend HTML page, not a POST-only API route."""
        from agents.order_manager import build_toss_payment_payload, generate_toss_order_id

        os.environ["YOONBOT_PAYMENT_PROVIDER"] = "toss_payments"
        os.environ["TOSS_PAYMENTS_CLIENT_KEY"] = "test_ck_key"
        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_secret"

        api_payload = self._create_order("monthly")
        order = api_payload["data"]
        payment = build_toss_payment_payload(order)

        self.assertIn("success_url", payment)
        self.assertNotIn("/api/", payment["success_url"])
        self.assertIn(".html", payment["success_url"])
        self.assertNotIn("confirm", payment["success_url"])

    def test_toss_order_id_stored_on_order_creation(self):
        """toss_order_id must be stored in the DB on order creation."""
        import sqlite3

        api_payload = self._create_order("monthly")
        order = api_payload["data"]
        order_id = order["id"]

        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT toss_order_id FROM orders WHERE id=?", (order_id,)).fetchone()
        conn.close()

        self.assertIsNotNone(row["toss_order_id"])
        self.assertTrue(str(row["toss_order_id"]).startswith("yb-"))

    def test_confirm_by_toss_order_id_endpoint(self):
        """POST /api/yoonbot/orders/by-toss-id/{toss_order_id}/payments/toss/confirm succeeds."""
        from agents import order_manager
        from agents.order_manager import generate_toss_order_id

        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_secret"

        api_payload = self._create_order("monthly")
        order = api_payload["data"]
        order_id = order["id"]
        correct_toss_order_id = generate_toss_order_id(order_id)
        correct_amount = int(order["amount_krw"])

        original_fn = self.main.confirm_yoonbot_toss_payment

        def patched_confirm(order_id, payment_key, client_amount, toss_order_id, confirm_client=None):
            stub = MagicMock()
            stub.confirm.return_value = {"status": "DONE"}
            return original_fn(order_id, payment_key, client_amount, toss_order_id, confirm_client=stub)

        self.main.confirm_yoonbot_toss_payment = patched_confirm
        try:
            response = self.client.post(
                f"/api/yoonbot/orders/by-toss-id/{correct_toss_order_id}/payments/toss/confirm",
                json={
                    "payment_key": "pk_test_by_toss_id",
                    "order_id": correct_toss_order_id,
                    "amount": correct_amount,
                },
            )
        finally:
            self.main.confirm_yoonbot_toss_payment = original_fn

        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertTrue(result["ok"])
        self.assertEqual(result["data"]["status"], "paid")

    def test_toss_confirm_rejects_non_done_status(self):
        """confirm_toss_payment raises ValueError when Toss returns non-DONE status."""
        from agents.order_manager import confirm_toss_payment, generate_toss_order_id

        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_secret"

        api_payload = self._create_order("monthly")
        order = api_payload["data"]
        order_id = order["id"]
        correct_toss_order_id = generate_toss_order_id(order_id)
        correct_amount = int(order["amount_krw"])

        stub_client = MagicMock()
        stub_client.confirm.return_value = {"status": "WAITING_FOR_DEPOSIT"}

        with self.assertRaises(ValueError) as ctx:
            confirm_toss_payment(
                order_id=order_id,
                payment_key="pk_test_pending",
                client_amount=correct_amount,
                toss_order_id=correct_toss_order_id,
                confirm_client=stub_client,
            )
        self.assertIn("상태", str(ctx.exception))

        from agents.order_manager import get_order
        updated = get_order(order_id)
        self.assertEqual(updated["status"], "payment_pending")

    def test_toss_confirm_stores_fingerprint_never_raw_payment_key(self):
        """payment_ref must hold an HMAC fingerprint; the raw paymentKey never
        appears in the DB row, the response, or error messages."""
        from agents.order_manager import confirm_toss_payment, generate_toss_order_id

        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_secret"
        raw_payment_key = "pk_live_raw_key_must_not_persist_0001"

        api_payload = self._create_order("monthly")
        order = api_payload["data"]
        order_id = order["id"]
        correct_toss_order_id = generate_toss_order_id(order_id)
        correct_amount = int(order["amount_krw"])

        stub_client = MagicMock()
        stub_client.confirm.return_value = {"status": "DONE"}

        result = confirm_toss_payment(
            order_id=order_id,
            payment_key=raw_payment_key,
            client_amount=correct_amount,
            toss_order_id=correct_toss_order_id,
            confirm_client=stub_client,
        )
        self.assertTrue(result["ok"])
        self.assertNotIn(raw_payment_key, str(result))

        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT * FROM orders WHERE id=?", (order_id,)).fetchone()
        conn.close()
        self.assertNotIn(raw_payment_key, str(dict(row)))
        self.assertTrue(str(row["payment_ref"]).startswith("toss:"))

        # Same paymentKey → idempotent success (fingerprint constant-time match)
        idem = confirm_toss_payment(
            order_id=order_id,
            payment_key=raw_payment_key,
            client_amount=correct_amount,
            toss_order_id=correct_toss_order_id,
            confirm_client=stub_client,
        )
        self.assertTrue(idem.get("idempotent"))

        # Different paymentKey on a paid order → rejected
        with self.assertRaises(ValueError):
            confirm_toss_payment(
                order_id=order_id,
                payment_key="pk_live_other_key_0002",
                client_amount=correct_amount,
                toss_order_id=correct_toss_order_id,
                confirm_client=stub_client,
            )

    def test_toss_confirm_fails_closed_without_fingerprint_secret(self):
        """Missing CODE_SECRET_KEY must fail closed (RuntimeError), never fall
        back to storing the raw paymentKey."""
        from agents.order_manager import confirm_toss_payment, generate_toss_order_id

        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_secret"

        api_payload = self._create_order("monthly")
        order = api_payload["data"]
        order_id = order["id"]
        correct_toss_order_id = generate_toss_order_id(order_id)
        correct_amount = int(order["amount_krw"])

        stub_client = MagicMock()
        stub_client.confirm.return_value = {"status": "DONE"}

        saved = os.environ.pop("CODE_SECRET_KEY", None)
        try:
            with self.assertRaises(RuntimeError):
                confirm_toss_payment(
                    order_id=order_id,
                    payment_key="pk_test_failclosed",
                    client_amount=correct_amount,
                    toss_order_id=correct_toss_order_id,
                    confirm_client=stub_client,
                )
        finally:
            if saved is not None:
                os.environ["CODE_SECRET_KEY"] = saved
        stub_client.confirm.assert_not_called()

        from agents.order_manager import get_order
        updated = get_order(order_id)
        self.assertEqual(updated["status"], "payment_pending")

    def test_toss_confirm_rejects_mismatched_total_amount_in_response(self):
        """confirm_toss_payment raises ValueError when Toss response totalAmount differs."""
        from agents.order_manager import confirm_toss_payment, generate_toss_order_id

        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_secret"

        api_payload = self._create_order("monthly")
        order = api_payload["data"]
        order_id = order["id"]
        correct_toss_order_id = generate_toss_order_id(order_id)
        correct_amount = int(order["amount_krw"])

        stub_client = MagicMock()
        stub_client.confirm.return_value = {"status": "DONE", "totalAmount": correct_amount + 1}

        with self.assertRaises(ValueError) as ctx:
            confirm_toss_payment(
                order_id=order_id,
                payment_key="pk_test_mismatch",
                client_amount=correct_amount,
                toss_order_id=correct_toss_order_id,
                confirm_client=stub_client,
            )
        self.assertIn("금액", str(ctx.exception))

        from agents.order_manager import get_order
        updated = get_order(order_id)
        self.assertEqual(updated["status"], "payment_pending")

    def test_by_toss_id_route_returns_404_for_unknown_toss_order(self):
        """by-toss-id endpoint returns 404 for unknown toss_order_id."""
        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_secret"

        response = self.client.post(
            "/api/yoonbot/orders/by-toss-id/yb-nonexistent0000000000000000000/payments/toss/confirm",
            json={
                "payment_key": "pk_test_notfound",
                "order_id": "yb-nonexistent0000000000000000000",
                "amount": 99000,
            },
        )
        self.assertEqual(response.status_code, 404)

    def test_toss_with_client_key_only_falls_back_to_manual(self):
        """provider=toss + client_key set + secret_key missing → manual fallback, not Toss payload."""
        os.environ["YOONBOT_PAYMENT_PROVIDER"] = "toss_payments"
        os.environ["TOSS_PAYMENTS_CLIENT_KEY"] = "test_ck_only"
        # TOSS_PAYMENTS_SECRET_KEY intentionally not set

        payload = self._create_order("monthly")
        payment = payload["payment"]

        self.assertEqual(payment["mode"], "manual_bank_transfer")
        self.assertFalse(payment["auto_charge"])
        self.assertNotIn("client_key", payment)
        self.assertNotIn("toss_order_id", payment)
        self.assertNotIn("test_ck_only", str(payment))

    def test_toss_with_secret_key_only_falls_back_to_manual(self):
        """provider=toss + client_key missing + secret_key set → manual fallback, not Toss payload."""
        os.environ["YOONBOT_PAYMENT_PROVIDER"] = "toss_payments"
        # TOSS_PAYMENTS_CLIENT_KEY intentionally not set
        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_only"

        payload = self._create_order("monthly")
        payment = payload["payment"]

        self.assertEqual(payment["mode"], "manual_bank_transfer")
        self.assertFalse(payment["auto_charge"])
        self.assertNotIn("client_key", payment)
        self.assertNotIn("toss_order_id", payment)
        self.assertNotIn("test_sk_only", str(payment))

    def test_toss_fully_configured_returns_toss_payload(self):
        """provider=toss + both keys set → Toss payload with client_key, no secret_key."""
        os.environ["YOONBOT_PAYMENT_PROVIDER"] = "toss_payments"
        os.environ["TOSS_PAYMENTS_CLIENT_KEY"] = "test_ck_full"
        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_full"

        payload = self._create_order("monthly")
        payment = payload["payment"]

        self.assertEqual(payment["mode"], "toss_payments")
        self.assertTrue(payment["auto_charge"])
        self.assertEqual(payment["client_key"], "test_ck_full")
        self.assertNotIn("test_sk_full", str(payment))
        self.assertIn("toss_order_id", payment)

    def test_products_endpoint_reflects_toss_readiness(self):
        """products endpoint shows toss_payments mode only when both keys configured."""
        # Default: no Toss keys → manual
        resp = self.client.get("/api/yoonbot/products")
        self.assertEqual(resp.status_code, 200)
        product = resp.json()["product"]
        self.assertEqual(product["payment_mode"], "manual_bank_transfer")
        self.assertFalse(product["auto_charge"])

        # Partial config → still manual
        os.environ["YOONBOT_PAYMENT_PROVIDER"] = "toss_payments"
        os.environ["TOSS_PAYMENTS_CLIENT_KEY"] = "test_ck_partial"
        resp = self.client.get("/api/yoonbot/products")
        product = resp.json()["product"]
        self.assertEqual(product["payment_mode"], "manual_bank_transfer")

        # Full config → toss_payments
        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_partial"
        resp = self.client.get("/api/yoonbot/products")
        product = resp.json()["product"]
        self.assertEqual(product["payment_mode"], "toss_payments")
        self.assertTrue(product["auto_charge"])


class DiscountCodeFlowTest(unittest.TestCase):
    """Tests for discount code validation and order creation with discounts."""

    ADMIN_KEY = "discount-test-admin-key"

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

    def _create_code(self, code, dtype, dvalue, max_redemptions=10, plan_code=None):
        from agents.order_manager import create_discount_code
        return create_discount_code(
            code=code,
            label=f"Test {code}",
            plan_code=plan_code,
            discount_type=dtype,
            discount_value=dvalue,
            max_redemptions=max_redemptions,
        )

    def _create_order(self, plan_code="monthly", discount_code=None):
        body = {
            "buyer_name": "할인테스트",
            "buyer_email": "discount@example.com",
            "plan_code": plan_code,
            "consent_privacy": True,
            "consent_terms": True,
        }
        if discount_code:
            body["discount_code"] = discount_code
        response = self.client.post("/api/yoonbot/orders", json=body)
        self.assertEqual(response.status_code, 200)
        return response.json()["data"]

    def test_order_without_discount_keeps_original_price(self):
        order = self._create_order("monthly")
        self.assertEqual(order["amount_krw"], 99000)
        self.assertEqual(order["original_amount_krw"], 99000)
        self.assertEqual(order["discount_amount_krw"], 0)
        self.assertIsNone(order["discount_code"])

    def test_percent_discount_applies_correctly(self):
        self._create_code("PCT20", "percent", 20)
        order = self._create_order("monthly", "PCT20")
        self.assertEqual(order["original_amount_krw"], 99000)
        self.assertEqual(order["discount_amount_krw"], 19800)
        self.assertEqual(order["amount_krw"], 79200)
        self.assertEqual(order["discount_code"], "PCT20")

    def test_amount_discount_applies_correctly(self):
        self._create_code("FIXED10K", "amount", 10000)
        order = self._create_order("monthly", "FIXED10K")
        self.assertEqual(order["original_amount_krw"], 99000)
        self.assertEqual(order["discount_amount_krw"], 10000)
        self.assertEqual(order["amount_krw"], 89000)

    def test_override_amount_discount_applies_correctly(self):
        self._create_code("OVERRIDE50K", "override_amount", 50000)
        order = self._create_order("monthly", "OVERRIDE50K")
        self.assertEqual(order["original_amount_krw"], 99000)
        self.assertEqual(order["amount_krw"], 50000)
        self.assertEqual(order["discount_amount_krw"], 49000)

    def test_one_use_discount_cannot_be_reused(self):
        self._create_code("ONCE1", "percent", 10, max_redemptions=1)
        order1 = self._create_order("monthly", "ONCE1")
        self.assertEqual(order1["amount_krw"], 99000 - 9900)

        response = self.client.post(
            "/api/yoonbot/orders",
            json={
                "buyer_name": "두번째",
                "buyer_email": "second@example.com",
                "plan_code": "monthly",
                "consent_privacy": True,
                "consent_terms": True,
                "discount_code": "ONCE1",
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("소진", response.json()["detail"])

    def test_disabled_code_fails_order_creation(self):
        self._create_code("DISABLED", "percent", 10, max_redemptions=10)
        from agents.order_manager import disable_discount_code
        disable_discount_code("DISABLED")

        response = self.client.post(
            "/api/yoonbot/orders",
            json={
                "buyer_name": "테스트",
                "buyer_email": "t@example.com",
                "plan_code": "monthly",
                "consent_privacy": True,
                "consent_terms": True,
                "discount_code": "DISABLED",
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("사용 중지", response.json()["detail"])

    def test_plan_mismatched_code_fails(self):
        self._create_code("YEARLYONLY", "percent", 10, max_redemptions=5, plan_code="yearly")
        response = self.client.post(
            "/api/yoonbot/orders",
            json={
                "buyer_name": "테스트",
                "buyer_email": "t@example.com",
                "plan_code": "monthly",
                "consent_privacy": True,
                "consent_terms": True,
                "discount_code": "YEARLYONLY",
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("플랜", response.json()["detail"])

    def test_invalid_code_fails(self):
        response = self.client.post(
            "/api/yoonbot/orders",
            json={
                "buyer_name": "테스트",
                "buyer_email": "t@example.com",
                "plan_code": "monthly",
                "consent_privacy": True,
                "consent_terms": True,
                "discount_code": "NONEXISTENT999",
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("유효하지 않은", response.json()["detail"])

    def test_malformed_code_is_rejected_not_sanitized(self):
        self._create_code("BADC0DE", "percent", 10, max_redemptions=5)
        response = self.client.post(
            "/api/yoonbot/orders",
            json={
                "buyer_name": "테스트",
                "buyer_email": "t@example.com",
                "plan_code": "monthly",
                "consent_privacy": True,
                "consent_terms": True,
                "discount_code": "BAD!C0DE",
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("형식", response.json()["detail"])

    def test_admin_discount_create_rejects_malformed_code(self):
        resp = self.client.post(
            "/admin/yoonbot/discounts",
            headers=self._headers(),
            json={
                "code": "ADMIN!10",
                "label": "잘못된 코드",
                "discount_type": "percent",
                "discount_value": 10,
            },
        )
        self.assertEqual(resp.status_code, 400)
        self.assertIn("허용", resp.json()["detail"])

    def test_toss_payload_uses_discounted_final_amount(self):
        """When Toss is configured, Toss payload amount uses final (discounted) amount."""
        import os
        os.environ["YOONBOT_PAYMENT_PROVIDER"] = "toss_payments"
        os.environ["TOSS_PAYMENTS_CLIENT_KEY"] = "test_ck_discount"
        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_discount"
        try:
            self._create_code("TOSS10PCT", "percent", 10, max_redemptions=5)
            response = self.client.post(
                "/api/yoonbot/orders",
                json={
                    "buyer_name": "토스할인",
                    "buyer_email": "toss@example.com",
                    "plan_code": "monthly",
                    "consent_privacy": True,
                    "consent_terms": True,
                    "discount_code": "TOSS10PCT",
                },
            )
            self.assertEqual(response.status_code, 200)
            payload = response.json()
            order = payload["data"]
            payment = payload["payment"]
            self.assertEqual(payment["mode"], "toss_payments")
            # Toss amount.value must equal final (discounted) amount
            self.assertEqual(payment["amount"]["value"], order["amount_krw"])
            self.assertLess(order["amount_krw"], order["original_amount_krw"])
        finally:
            for key in ("YOONBOT_PAYMENT_PROVIDER", "TOSS_PAYMENTS_CLIENT_KEY", "TOSS_PAYMENTS_SECRET_KEY"):
                os.environ.pop(key, None)

    def test_toss_confirm_rejects_amount_not_matching_discounted_final(self):
        """Toss confirm should reject client_amount that does not match discounted final amount."""
        import os
        from agents.order_manager import confirm_toss_payment, generate_toss_order_id

        os.environ["TOSS_PAYMENTS_SECRET_KEY"] = "test_sk_secret"
        try:
            self._create_code("TOSSDISC20", "percent", 20, max_redemptions=5)
            response = self.client.post(
                "/api/yoonbot/orders",
                json={
                    "buyer_name": "토스확인",
                    "buyer_email": "tc@example.com",
                    "plan_code": "monthly",
                    "consent_privacy": True,
                    "consent_terms": True,
                    "discount_code": "TOSSDISC20",
                },
            )
            self.assertEqual(response.status_code, 200)
            order = response.json()["data"]
            order_id = order["id"]
            correct_toss_order_id = generate_toss_order_id(order_id)
            final_amount = order["amount_krw"]
            original_amount = order["original_amount_krw"]

            stub_client = MagicMock()
            # Sending original (non-discounted) amount should be rejected
            with self.assertRaises(ValueError) as ctx:
                confirm_toss_payment(
                    order_id=order_id,
                    payment_key="pk_test_disc",
                    client_amount=original_amount,
                    toss_order_id=correct_toss_order_id,
                    confirm_client=stub_client,
                )
            self.assertIn("금액", str(ctx.exception))
            stub_client.confirm.assert_not_called()
        finally:
            os.environ.pop("TOSS_PAYMENTS_SECRET_KEY", None)

    def test_admin_discount_endpoints_require_auth(self):
        """Admin discount endpoints must return 401 without admin key."""
        r = self.client.get("/admin/yoonbot/discounts")
        self.assertEqual(r.status_code, 401)
        r = self.client.post("/admin/yoonbot/discounts", json={})
        self.assertEqual(r.status_code, 401)
        r = self.client.post("/admin/yoonbot/discounts/SOMECODE/disable")
        self.assertEqual(r.status_code, 401)

    def test_admin_discount_create_and_list(self):
        """Admin can create and list discount codes."""
        resp = self.client.post(
            "/admin/yoonbot/discounts",
            headers=self._headers(),
            json={
                "code": "ADMIN10",
                "label": "어드민 생성 코드",
                "discount_type": "percent",
                "discount_value": 10,
                "max_redemptions": 1,
            },
        )
        self.assertEqual(resp.status_code, 200)
        dc = resp.json()["data"]
        self.assertEqual(dc["code"], "ADMIN10")
        self.assertTrue(dc["enabled"])

        list_resp = self.client.get("/admin/yoonbot/discounts", headers=self._headers())
        self.assertEqual(list_resp.status_code, 200)
        codes = [item["code"] for item in list_resp.json()["data"]]
        self.assertIn("ADMIN10", codes)

    def test_admin_disable_discount(self):
        """Admin can disable a discount code."""
        self._create_code("TODISABLE", "percent", 5, max_redemptions=5)
        resp = self.client.post(
            "/admin/yoonbot/discounts/TODISABLE/disable",
            headers=self._headers(),
        )
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(resp.json()["data"]["enabled"])

    def test_final_amount_never_negative(self):
        """Discount that exceeds price should set final amount to 0, not negative."""
        self._create_code("BIGDISC", "amount", 999999)
        order = self._create_order("monthly", "BIGDISC")
        self.assertEqual(order["amount_krw"], 0)
        self.assertGreaterEqual(order["amount_krw"], 0)


if __name__ == "__main__":
    unittest.main()
