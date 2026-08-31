import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import db
from agents import license_manager


class LicenseManagerTest(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.tmpdir.name) / "members.db"
        self.original_db_path = db.DB_PATH
        db.DB_PATH = self.db_path
        db.init_db()

    def tearDown(self):
        db.DB_PATH = self.original_db_path
        self.tmpdir.cleanup()

    def _stored_license_row(self, license_id):
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT * FROM licenses WHERE id=?", (license_id,)).fetchone()
        conn.close()
        return dict(row)

    def test_create_license_stores_hash_and_hint_only(self):
        result = license_manager.create_license(plan_code="pro")

        self.assertTrue(result["ok"])
        key = result["license_key"]
        license_id = result["license"]["id"]
        row = self._stored_license_row(license_id)

        self.assertNotEqual(row["license_key_hash"], key)
        self.assertNotIn(key, str(row))
        self.assertEqual(result["license"]["license_key_hint"], row["license_key_hint"])
        self.assertTrue(result["license"]["license_key_hint"].startswith("YB-****"))

    def test_activate_and_verify_license_binds_hwid(self):
        created = license_manager.create_license(plan_code="basic")
        activated = license_manager.activate_license(
            license_key=created["license_key"],
            hwid="WINDOWS-HWID-1",
            app_version="1.0.0",
            platform="windows",
        )

        self.assertTrue(activated["ok"])
        self.assertEqual(activated["status"], "active")
        self.assertIn("activation_token", activated)

        verified = license_manager.verify_license(
            activation_token=activated["activation_token"],
            hwid="WINDOWS-HWID-1",
            app_version="1.0.0",
            platform="windows",
        )

        self.assertTrue(verified["ok"])
        self.assertTrue(verified["license"]["bound_device"])

    def test_other_hwid_is_rejected_until_device_reset(self):
        created = license_manager.create_license(plan_code="basic")
        license_id = created["license"]["id"]
        first = license_manager.activate_license(
            license_key=created["license_key"],
            hwid="WINDOWS-HWID-1",
        )
        self.assertTrue(first["ok"])

        blocked = license_manager.activate_license(
            license_key=created["license_key"],
            hwid="WINDOWS-HWID-2",
        )
        self.assertFalse(blocked["ok"])
        self.assertEqual(blocked["code"], "HWID_MISMATCH")

        reset = license_manager.reset_license_device(license_id, "unit_test")
        self.assertTrue(reset["ok"])
        self.assertFalse(reset["license"]["bound_device"])

        second = license_manager.activate_license(
            license_key=created["license_key"],
            hwid="WINDOWS-HWID-2",
        )
        self.assertTrue(second["ok"])

    def test_activate_rejects_overlong_or_control_inputs_without_db_writes(self):
        created = license_manager.create_license(plan_code="basic")

        cases = [
            {"license_key": "K" * (license_manager.LICENSE_KEY_MAX_LEN + 1), "hwid": "HWID-1"},
            {"license_key": created["license_key"], "hwid": "H" * (license_manager.LICENSE_HWID_MAX_LEN + 1)},
            {"license_key": "BAD\x00KEY", "hwid": "HWID-1"},
            {"license_key": created["license_key"], "hwid": "HWID-1",
             "app_version": "9" * (license_manager.LICENSE_APP_VERSION_MAX_LEN + 1)},
            {"license_key": created["license_key"], "hwid": "HWID-1",
             "platform": "P" * (license_manager.LICENSE_PLATFORM_MAX_LEN + 1)},
            {"license_key": created["license_key"], "hwid": "HWID-1",
             "device_name": "D" * (license_manager.LICENSE_DEVICE_NAME_MAX_LEN + 1)},
        ]
        for body in cases:
            result = license_manager.activate_license(
                license_key=body["license_key"],
                hwid=body["hwid"],
                app_version=body.get("app_version"),
                platform=body.get("platform", "windows"),
                device_name=body.get("device_name"),
            )
            self.assertFalse(result["ok"])
            self.assertEqual(result["code"], "INVALID_REQUEST")

        conn = sqlite3.connect(str(self.db_path))
        count = conn.execute(
            "SELECT COUNT(*) FROM license_events WHERE event_type='license_activate'"
        ).fetchone()[0]
        conn.close()
        self.assertEqual(count, 0)

    def test_verify_rejects_overlong_token(self):
        result = license_manager.verify_license(
            activation_token="T" * (license_manager.LICENSE_TOKEN_MAX_LEN + 1),
            hwid="HWID-1",
        )
        self.assertFalse(result["ok"])
        self.assertEqual(result["code"], "INVALID_REQUEST")

    def test_verify_rejects_invalid_optional_inputs(self):
        for kwargs in (
            {"app_version": "9" * (license_manager.LICENSE_APP_VERSION_MAX_LEN + 1)},
            {"platform": "P" * (license_manager.LICENSE_PLATFORM_MAX_LEN + 1)},
        ):
            result = license_manager.verify_license(
                activation_token="valid-shape-token",
                hwid="HWID-1",
                **kwargs,
            )
            self.assertFalse(result["ok"])
            self.assertEqual(result["code"], "INVALID_REQUEST")

    def test_activate_rate_limit_blocks_repeated_failures_from_same_ip(self):
        original = license_manager.LICENSE_ACTIVATE_RATE_MAX
        license_manager.LICENSE_ACTIVATE_RATE_MAX = 3
        try:
            for _ in range(3):
                result = license_manager.activate_license(
                    license_key="YB-XXXX-XXXX-XXXX-XXXX",
                    hwid="HWID-BRUTE",
                    client_ip="203.0.113.9",
                )
                self.assertEqual(result["code"], "LICENSE_NOT_FOUND")

            limited = license_manager.activate_license(
                license_key="YB-XXXX-XXXX-XXXX-XXXX",
                hwid="HWID-BRUTE",
                client_ip="203.0.113.9",
            )
            self.assertFalse(limited["ok"])
            self.assertEqual(limited["code"], "RATE_LIMITED")

            # 다른 IP는 계속 정상 흐름을 탄다 (per-ip 제한).
            other_ip = license_manager.activate_license(
                license_key="YB-XXXX-XXXX-XXXX-XXXX",
                hwid="HWID-BRUTE",
                client_ip="198.51.100.7",
            )
            self.assertEqual(other_ip["code"], "LICENSE_NOT_FOUND")
        finally:
            license_manager.LICENSE_ACTIVATE_RATE_MAX = original

    def test_successful_verify_is_never_rate_limited(self):
        created = license_manager.create_license(plan_code="basic")
        activated = license_manager.activate_license(
            license_key=created["license_key"],
            hwid="HWID-OK",
            client_ip="203.0.113.20",
        )
        self.assertTrue(activated["ok"])

        original = license_manager.LICENSE_VERIFY_FAIL_RATE_MAX
        license_manager.LICENSE_VERIFY_FAIL_RATE_MAX = 2
        try:
            # 정상 verify는 blocked 이벤트를 만들지 않으므로 제한 없이 반복 가능.
            for _ in range(5):
                verified = license_manager.verify_license(
                    activation_token=activated["activation_token"],
                    hwid="HWID-OK",
                    client_ip="203.0.113.20",
                )
                self.assertTrue(verified["ok"])

            # 실패 verify가 임계값에 도달하면 같은 IP는 제한된다.
            for _ in range(2):
                failed = license_manager.verify_license(
                    activation_token="not-a-real-token",
                    hwid="HWID-OK",
                    client_ip="203.0.113.20",
                )
                self.assertEqual(failed["code"], "TOKEN_NOT_FOUND")
            limited = license_manager.verify_license(
                activation_token=activated["activation_token"],
                hwid="HWID-OK",
                client_ip="203.0.113.20",
            )
            self.assertEqual(limited["code"], "RATE_LIMITED")
        finally:
            license_manager.LICENSE_VERIFY_FAIL_RATE_MAX = original

    def test_revoke_blocks_existing_token(self):
        created = license_manager.create_license(plan_code="basic")
        activated = license_manager.activate_license(
            license_key=created["license_key"],
            hwid="WINDOWS-HWID-1",
        )

        revoked = license_manager.revoke_license(created["license"]["id"], "unit_test")
        self.assertTrue(revoked["ok"])
        self.assertEqual(revoked["license"]["status"], "revoked")

        verified = license_manager.verify_license(
            activation_token=activated["activation_token"],
            hwid="WINDOWS-HWID-1",
        )
        self.assertFalse(verified["ok"])
        self.assertIn(verified["code"], {"TOKEN_REVOKED", "LICENSE_REVOKED"})


if __name__ == "__main__":
    unittest.main()
