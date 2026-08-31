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

ARTIFACT_NAME = "YoonBot-Setup-1.1.0.exe"
MACOS_ARTIFACT_NAME = "YoonBot-1.1.0-arm64.dmg"
ARTIFACT_ENDPOINT = f"/api/yoonbot/artifacts/{ARTIFACT_NAME}"
EXE_CONTENT_TYPE = "application/vnd.microsoft.portable-executable"
YOONBOT_ENV_VARS = (
    "YOONBOT_ARTIFACT_DOWNLOAD_URL",
    "YOONBOT_ARTIFACT_SHA256",
    "YOONBOT_ARTIFACT_SIZE_BYTES",
    "YOONBOT_ARTIFACT_URL_ALLOWED_HOSTS",
    "ARSEN_YOONBOT_ARTIFACT_BASE_URL",
    "YOONBOT_RELEASE_READY_APPROVED",
    "YOONBOT_CODE_SIGNING_STATUS",
)
ADMIN_KEY = "release-contract-admin-key"
ADMIN_STATUS_ENDPOINT = "/admin/yoonbot/release-status"
# FastAPI와 Worker admin payload의 키 집합 계약. Worker 쪽 동일 목록은
# cloudflare/scripts/check-yoonbot-release-contract.mjs 가 검증한다.
ADMIN_STATUS_KEYS = {
    "service",
    "source",
    "served_at",
    "latest_version",
    "minimum_supported_version",
    "artifact_name",
    "sha256",
    "size_bytes",
    "artifact_source",
    "artifact_verified",
    "code_signing_status",
    "code_signing_ready",
    "release_ready_approved",
    "download_ready",
    "public_status",
    "blocked_reasons",
    "endpoints",
}


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

    def _open_gates(self):
        os.environ["YOONBOT_RELEASE_READY_APPROVED"] = "true"
        os.environ["YOONBOT_CODE_SIGNING_STATUS"] = "signed"

    def _admin_status(self):
        response = self.client.get(ADMIN_STATUS_ENDPOINT, headers={"X-Admin-Key": ADMIN_KEY})
        self.assertEqual(response.status_code, 200)
        return response.json()["data"]

    def _assert_closed(self, release):
        self.assertFalse(release["download_ready"])
        self.assertEqual(release["artifact_download_url"], "")
        self.assertEqual(release["sha256"], "")
        self.assertEqual(release["size_bytes"], 0)
        self.assertEqual(release["status"], "preparing")

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
        self._open_gates()
        response = self.client.get("/api/yoonbot/release")
        self.assertEqual(response.status_code, 200)
        release = response.json()
        self.assertTrue(release["download_ready"])
        self.assertEqual(release["status"], "available")
        self.assertEqual(
            release["artifact_download_url"],
            f"https://apply.arsen-ai.com{ARTIFACT_ENDPOINT}",
        )
        self.assertEqual(release["sha256"], hashlib.sha256(payload).hexdigest())
        self.assertEqual(release["size_bytes"], len(payload))

    def test_macos_manifest_is_platform_specific_and_fails_closed(self):
        response = self.client.get("/api/yoonbot/manifest?platform=macos")
        self.assertEqual(response.status_code, 200)
        release = response.json()["release"]
        self.assertEqual(release["platform"], "macos")
        self.assertEqual(release["arch"], "arm64")
        self.assertEqual(release["package_type"], "dmg")
        self.assertEqual(release["artifact_name"], MACOS_ARTIFACT_NAME)
        self.assertTrue(release["artifact_endpoint"].endswith(MACOS_ARTIFACT_NAME))
        self._assert_closed(release)

        direct = self.client.get("/api/yoonbot/release?platform=macos").json()
        self.assertEqual(direct, release)

    def test_release_fails_closed_over_plain_http(self):
        self._write_artifact()
        self._open_gates()
        http_client = TestClient(self.main.app, base_url="http://testserver")
        release = http_client.get("/api/yoonbot/release").json()
        self.assertFalse(release["download_ready"])
        self.assertEqual(release["artifact_download_url"], "")

    def test_release_blocked_without_operator_gates_even_with_verified_artifact(self):
        self._write_artifact()
        self._assert_closed(self.client.get("/api/yoonbot/release").json())
        artifact = self.client.get(ARTIFACT_ENDPOINT, follow_redirects=False)
        self.assertEqual(artifact.status_code, 404)
        self.assertEqual(artifact.json()["detail"], "yoonbot_release_not_ready")
        head = self.client.head(ARTIFACT_ENDPOINT)
        self.assertEqual(head.status_code, 404)

    def test_release_blocked_when_code_signing_not_signed(self):
        payload = self._write_artifact()
        os.environ["YOONBOT_RELEASE_READY_APPROVED"] = "true"
        os.environ["YOONBOT_CODE_SIGNING_STATUS"] = "not_signed"
        self._assert_closed(self.client.get("/api/yoonbot/release").json())
        self.assertEqual(self.client.get(ARTIFACT_ENDPOINT).status_code, 404)

        status = self._admin_status()
        self.assertEqual(status["code_signing_status"], "not_signed")
        self.assertFalse(status["code_signing_ready"])
        self.assertTrue(status["release_ready_approved"])
        self.assertFalse(status["download_ready"])
        self.assertEqual(status["public_status"], "preparing")
        self.assertIn("blocked_code_signing", status["blocked_reasons"])
        self.assertNotIn("blocked_release_ready_approval", status["blocked_reasons"])
        # 관리자에게는 검증된 artifact 정보가 보인다 (공개 계약과 분리).
        self.assertTrue(status["artifact_verified"])
        self.assertEqual(status["sha256"], hashlib.sha256(payload).hexdigest())
        self.assertEqual(status["size_bytes"], len(payload))

    def test_release_blocked_without_release_ready_approval(self):
        self._write_artifact()
        os.environ["YOONBOT_CODE_SIGNING_STATUS"] = "signed"
        self._assert_closed(self.client.get("/api/yoonbot/release").json())
        status = self._admin_status()
        self.assertTrue(status["code_signing_ready"])
        self.assertFalse(status["release_ready_approved"])
        self.assertIn("blocked_release_ready_approval", status["blocked_reasons"])
        self.assertNotIn("blocked_code_signing", status["blocked_reasons"])

    def test_admin_release_status_key_set_is_worker_parity_contract(self):
        self.assertEqual(set(self._admin_status().keys()), ADMIN_STATUS_KEYS)

    def test_admin_release_status_requires_admin_key(self):
        self.assertEqual(self.client.get(ADMIN_STATUS_ENDPOINT).status_code, 401)
        denied = self.client.get(ADMIN_STATUS_ENDPOINT, headers={"X-Admin-Key": "wrong-key"})
        self.assertEqual(denied.status_code, 401)

    def test_admin_release_status_reports_full_contract(self):
        # artifact 미검증 + 게이트 미통과 상태
        status = self._admin_status()
        self.assertFalse(status["download_ready"])
        self.assertFalse(status["artifact_verified"])
        self.assertEqual(status["sha256"], "")
        self.assertEqual(status["size_bytes"], 0)
        self.assertEqual(
            status["blocked_reasons"],
            ["blocked_code_signing", "blocked_release_ready_approval", "blocked_artifact_unverified"],
        )

        payload = self._write_artifact()
        self._open_gates()
        ready = self._admin_status()
        self.assertEqual(ready["latest_version"], "1.1.0")
        self.assertEqual(ready["artifact_name"], ARTIFACT_NAME)
        self.assertTrue(ready["download_ready"])
        self.assertEqual(ready["public_status"], "available")
        self.assertEqual(ready["blocked_reasons"], [])
        self.assertEqual(ready["artifact_source"], "staged_file")
        self.assertEqual(ready["sha256"], hashlib.sha256(payload).hexdigest())
        # 민감정보(라이선스 키/토큰/관리자 키)가 응답에 없어야 한다.
        text = json.dumps(ready)
        for forbidden in ("license_key", "activation_token", ADMIN_KEY):
            self.assertNotIn(forbidden, text)

    def test_release_uses_verified_external_url_only_with_sha256_and_size(self):
        self._open_gates()
        os.environ["YOONBOT_ARTIFACT_DOWNLOAD_URL"] = f"https://downloads.example.test/{ARTIFACT_NAME}"
        os.environ["YOONBOT_ARTIFACT_URL_ALLOWED_HOSTS"] = "downloads.example.test"
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

    def test_external_url_fails_closed_without_host_allowlist(self):
        # HTTPS + SHA-256 + size alone must never open an arbitrary domain.
        self._open_gates()
        os.environ["YOONBOT_ARTIFACT_DOWNLOAD_URL"] = f"https://attacker.example.test/{ARTIFACT_NAME}"
        os.environ["YOONBOT_ARTIFACT_SHA256"] = "a" * 64
        os.environ["YOONBOT_ARTIFACT_SIZE_BYTES"] = "12345"
        self._assert_closed(self.client.get("/api/yoonbot/release").json())
        artifact = self.client.get(ARTIFACT_ENDPOINT, follow_redirects=False)
        self.assertNotIn(artifact.status_code, (301, 302, 307, 308))
        self.assertEqual(artifact.status_code, 404)

    def test_external_url_fails_closed_when_host_not_in_allowlist(self):
        self._open_gates()
        os.environ["YOONBOT_ARTIFACT_DOWNLOAD_URL"] = f"https://attacker.example.test/{ARTIFACT_NAME}"
        os.environ["YOONBOT_ARTIFACT_URL_ALLOWED_HOSTS"] = "downloads.example.test"
        os.environ["YOONBOT_ARTIFACT_SHA256"] = "a" * 64
        os.environ["YOONBOT_ARTIFACT_SIZE_BYTES"] = "12345"
        self._assert_closed(self.client.get("/api/yoonbot/release").json())

    def test_external_url_fails_closed_without_canonical_basename(self):
        self._open_gates()
        os.environ["YOONBOT_ARTIFACT_DOWNLOAD_URL"] = "https://downloads.example.test/other-app.exe"
        os.environ["YOONBOT_ARTIFACT_URL_ALLOWED_HOSTS"] = "downloads.example.test"
        os.environ["YOONBOT_ARTIFACT_SHA256"] = "a" * 64
        os.environ["YOONBOT_ARTIFACT_SIZE_BYTES"] = "12345"
        self._assert_closed(self.client.get("/api/yoonbot/release").json())

    def test_external_url_fails_closed_on_nonstandard_port(self):
        self._open_gates()
        os.environ["YOONBOT_ARTIFACT_DOWNLOAD_URL"] = f"https://downloads.example.test:8443/{ARTIFACT_NAME}"
        os.environ["YOONBOT_ARTIFACT_URL_ALLOWED_HOSTS"] = "downloads.example.test"
        os.environ["YOONBOT_ARTIFACT_SHA256"] = "a" * 64
        os.environ["YOONBOT_ARTIFACT_SIZE_BYTES"] = "12345"
        self._assert_closed(self.client.get("/api/yoonbot/release").json())

    def test_artifact_get_and_head_use_exe_attachment_nosniff(self):
        payload = self._write_artifact()
        self._open_gates()
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
        self._open_gates()
        response = self.client.get(ARTIFACT_ENDPOINT)
        self.assertEqual(response.status_code, 404)

    def test_artifact_rejects_traversal_and_foreign_names(self):
        self._write_artifact()
        self._open_gates()
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
        # 운영자 게이트 + 관리자 상태 계약도 양쪽에 동일하게 존재해야 한다.
        self.assertIn('@app.get("/admin/yoonbot/release-status")', main_py)
        self.assertIn('path === "/admin/yoonbot/release-status"', worker_js)
        for source in (main_py, worker_js):
            self.assertIn("blocked_code_signing", source)
            self.assertIn("blocked_release_ready_approval", source)
            self.assertIn("blocked_artifact_unverified", source)
            self.assertIn("YOONBOT_CODE_SIGNING_STATUS", source)
            self.assertIn("YOONBOT_RELEASE_READY_APPROVED", source)
            self.assertIn("yoonbot_release_not_ready", source)
            self.assertIn("YOONBOT_ARTIFACT_URL_ALLOWED_HOSTS", source)

    def test_worker_parity_license_abuse_contract_strings(self):
        license_py = (ROOT / "agents" / "license_manager.py").read_text(encoding="utf-8")
        worker_js = (ROOT / "cloudflare" / "src" / "worker.js").read_text(encoding="utf-8")
        for source in (license_py, worker_js):
            self.assertIn("RATE_LIMITED", source)
            self.assertIn("LICENSE_RATE_WINDOW_SECONDS", source)
            self.assertIn("LICENSE_ACTIVATE_RATE_MAX", source)
            self.assertIn("LICENSE_VERIFY_FAIL_RATE_MAX", source)
            self.assertIn("LICENSE_KEY_MAX_LEN", source)
            self.assertIn("LICENSE_HWID_MAX_LEN", source)
            self.assertIn("LICENSE_TOKEN_MAX_LEN", source)


if __name__ == "__main__":
    unittest.main()
