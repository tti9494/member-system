import hashlib
import importlib
import json
import os
import sys
import tempfile
import types
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import db

ARTIFACT_NAME = "yoonbot-1.1.0-win-x64.exe"
ARTIFACT_ENDPOINT = f"/api/yoonbot/artifacts/{ARTIFACT_NAME}"
EXE_CONTENT_TYPE = "application/vnd.microsoft.portable-executable"
YOONBOT_ENV_VARS = (
    "YOONBOT_ARTIFACT_DOWNLOAD_URL",
    "YOONBOT_ARTIFACT_SHA256",
    "YOONBOT_ARTIFACT_SIZE_BYTES",
    "ARSEN_YOONBOT_ARTIFACT_BASE_URL",
)


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


class YoonbotReleaseContractTest(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.tmpdir.name) / "members.db"
        self.original_db_path = db.DB_PATH
        db.DB_PATH = self.db_path
        db.init_db()

        _install_scheduler_stub()
        self.main = importlib.import_module("main")

        self.original_admin_key = self.main.ADMIN_API_KEY
        self.main.ADMIN_API_KEY = "release-contract-admin-key"
        self.original_artifact_dir = self.main.YOONBOT_ARTIFACT_DIR
        self.artifact_dir = Path(self.tmpdir.name) / "yoonbot-artifacts"
        self.artifact_dir.mkdir()
        self.main.YOONBOT_ARTIFACT_DIR = self.artifact_dir
        self.main._YOONBOT_SHA256_CACHE.clear()

        self.original_env = {}
        for key in YOONBOT_ENV_VARS:
            self.original_env[key] = os.environ.pop(key, None)

        self.client = TestClient(self.main.app, base_url="https://apply.arsen-ai.com")

    def tearDown(self):
        self.main.ADMIN_API_KEY = self.original_admin_key
        self.main.YOONBOT_ARTIFACT_DIR = self.original_artifact_dir
        self.main._YOONBOT_SHA256_CACHE.clear()
        for key, value in self.original_env.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
        db.DB_PATH = self.original_db_path
        self.tmpdir.cleanup()

    def _write_artifact(self, payload=b"yoonbot-fake-exe-bytes"):
        (self.artifact_dir / ARTIFACT_NAME).write_bytes(payload)
        return payload

    def _assert_closed(self, release):
        self.assertFalse(release["download_ready"])
        self.assertEqual(release["artifact_download_url"], "")
        self.assertEqual(release["sha256"], "")
        self.assertEqual(release["size_bytes"], 0)

    def test_manifest_is_public_and_fails_closed_without_artifact(self):
        response = self.client.get("/api/yoonbot/manifest")
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertIn("server_time", body)
        self.assertIsInstance(body["notices"], list)
        release = body["release"]
        self.assertEqual(release["latest_version"], "1.1.0")
        self.assertEqual(release["minimum_supported_version"], "1.0.0")
        self.assertEqual(release["artifact_name"], ARTIFACT_NAME)
        self.assertEqual(release["artifact_name"], Path(release["artifact_name"]).name)
        self.assertTrue(release["artifact_name"].endswith(".exe"))
        self.assertIsInstance(release["release_notes"], list)
        self.assertTrue(release["release_notes"])
        self._assert_closed(release)

    def test_release_serves_real_size_sha256_and_https_url_when_artifact_exists(self):
        payload = self._write_artifact()
        response = self.client.get("/api/yoonbot/release")
        self.assertEqual(response.status_code, 200)
        release = response.json()
        self.assertTrue(release["download_ready"])
        self.assertEqual(
            release["artifact_download_url"],
            f"https://apply.arsen-ai.com{ARTIFACT_ENDPOINT}",
        )
        self.assertEqual(release["sha256"], hashlib.sha256(payload).hexdigest())
        self.assertEqual(release["size_bytes"], len(payload))

    def test_release_fails_closed_over_plain_http(self):
        self._write_artifact()
        http_client = TestClient(self.main.app, base_url="http://testserver")
        release = http_client.get("/api/yoonbot/release").json()
        self.assertFalse(release["download_ready"])
        self.assertEqual(release["artifact_download_url"], "")

    def test_release_uses_verified_external_url_only_with_sha256_and_size(self):
        os.environ["YOONBOT_ARTIFACT_DOWNLOAD_URL"] = f"https://downloads.example.test/{ARTIFACT_NAME}"
        os.environ["YOONBOT_ARTIFACT_SHA256"] = "A" * 64
        os.environ["YOONBOT_ARTIFACT_SIZE_BYTES"] = "12345"
        release = self.client.get("/api/yoonbot/release").json()
        self.assertTrue(release["download_ready"])
        self.assertEqual(release["artifact_download_url"], f"https://downloads.example.test/{ARTIFACT_NAME}")
        self.assertEqual(release["sha256"], "a" * 64)
        self.assertEqual(release["size_bytes"], 12345)

        os.environ.pop("YOONBOT_ARTIFACT_SHA256")
        self._assert_closed(self.client.get("/api/yoonbot/release").json())
        artifact = self.client.get(ARTIFACT_ENDPOINT, follow_redirects=False)
        self.assertNotIn(artifact.status_code, (301, 302, 307, 308))
        self.assertEqual(artifact.status_code, 404)

    def test_artifact_get_and_head_use_exe_attachment_nosniff(self):
        payload = self._write_artifact()
        response = self.client.get(ARTIFACT_ENDPOINT)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, payload)
        self.assertEqual(response.headers["content-type"], EXE_CONTENT_TYPE)
        self.assertIn(f'filename="{ARTIFACT_NAME}"', response.headers["content-disposition"])
        self.assertIn("attachment", response.headers["content-disposition"])
        self.assertEqual(response.headers["x-content-type-options"], "nosniff")

        head = self.client.head(ARTIFACT_ENDPOINT)
        self.assertEqual(head.status_code, 200)
        self.assertEqual(head.headers["content-length"], str(len(payload)))
        self.assertEqual(head.content, b"")

    def test_artifact_missing_returns_404(self):
        response = self.client.get(ARTIFACT_ENDPOINT)
        self.assertEqual(response.status_code, 404)

    def test_artifact_rejects_traversal_and_foreign_names(self):
        self._write_artifact()
        (self.artifact_dir / "secret.txt").write_text("secret", encoding="utf-8")

        bad_names = ["..%2Fsecret.exe", "..%5Csecret.exe", "secret.txt", "arsen-content-launcher-0.1.0-win-x64.zip"]
        for name in bad_names:
            response = self.client.get(f"/api/yoonbot/artifacts/{name}")
            self.assertIn(response.status_code, (400, 404), name)
            self.assertNotIn(b"secret", response.content)

        unknown_exe = self.client.get("/api/yoonbot/artifacts/other-app-9.9.9.exe")
        self.assertEqual(unknown_exe.status_code, 404)

    def test_launcher_release_contract_unchanged(self):
        original_manifest_path = self.main.LAUNCHER_MANIFEST_PATH
        original_launcher_dir = self.main.LAUNCHER_ARTIFACT_DIR
        try:
            manifest_path = Path(self.tmpdir.name) / "launcher_ops.json"
            manifest_path.write_text(
                json.dumps({"launcher": {"artifact_name": "arsen-content-launcher-0.1.0-win-x64.zip"}}),
                encoding="utf-8",
            )
            self.main.LAUNCHER_MANIFEST_PATH = manifest_path
            self.main.LAUNCHER_ARTIFACT_DIR = Path(self.tmpdir.name) / "launcher-artifacts-empty"
            self._write_artifact()
            release = self.client.get("/api/launcher/release").json()
            self.assertEqual(release["artifact_name"], "arsen-content-launcher-0.1.0-win-x64.zip")
            self.assertFalse(release["artifact_available"])
            self.assertEqual(release["artifact_download_url"], "")
        finally:
            self.main.LAUNCHER_MANIFEST_PATH = original_manifest_path
            self.main.LAUNCHER_ARTIFACT_DIR = original_launcher_dir

    def test_worker_parity_contract_strings(self):
        main_py = (ROOT / "main.py").read_text(encoding="utf-8")
        worker_js = (ROOT / "cloudflare" / "src" / "worker.js").read_text(encoding="utf-8")
        for source in (main_py, worker_js):
            self.assertIn(ARTIFACT_NAME, source)
            self.assertIn(EXE_CONTENT_TYPE, source)
            self.assertIn('"1.1.0"', source)
        self.assertIn('@app.get("/api/yoonbot/manifest")', main_py)
        self.assertIn('@app.get("/api/yoonbot/release")', main_py)
        self.assertIn('path === "/api/yoonbot/manifest"', worker_js)
        self.assertIn('path === "/api/yoonbot/release"', worker_js)


if __name__ == "__main__":
    unittest.main()
