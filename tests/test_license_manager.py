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
