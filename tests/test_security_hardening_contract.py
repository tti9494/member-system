"""2026-08-31 보안 하드닝 회귀 계약.

- 원문 라이선스 키/paymentKey가 저장·재반환되지 않는다 (생성 응답 1회만)
- 관리자 키 비교는 상수시간이다
- 백업 상태 표기는 사실(plain_sqlite_backup)이다
- 보안 헤더가 FastAPI/Worker 양쪽에 있다
- 고객 안내문에 구 런처 ZIP 직접 링크가 없다
- Worker는 kakao 세션 서명·최상위 500에서 fail-closed/고정 문구를 쓴다
"""

import importlib
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

MAIN_PY = ROOT / "main.py"
WORKER_JS = ROOT / "cloudflare" / "src" / "worker.js"
WORKER_SCHEMA = ROOT / "cloudflare" / "schema.sql"
ORDER_MANAGER_PY = ROOT / "agents" / "order_manager.py"
DB_MANAGER_PY = ROOT / "agents" / "db_manager.py"
LICENSE_ADMIN_HTML = ROOT / "frontend" / "license-admin.html"
PAYMENT_ADMIN_HTML = ROOT / "frontend" / "payment-admin.html"


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


class SecurityHeadersAndAdminAuthTest(unittest.TestCase):
    ADMIN_KEY = "security-hardening-test-admin-key"

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

    def test_security_headers_present_on_every_response(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers.get("x-content-type-options"), "nosniff")
        self.assertEqual(response.headers.get("x-frame-options"), "DENY")
        self.assertEqual(response.headers.get("referrer-policy"), "strict-origin-when-cross-origin")
        self.assertEqual(
            response.headers.get("permissions-policy"),
            "camera=(), microphone=(), geolocation=()",
        )
        # HTTP 요청에는 HSTS 없음
        self.assertIsNone(response.headers.get("strict-transport-security"))

    def test_public_release_and_manifest_are_no_store(self):
        for path in ("/api/yoonbot/release", "/api/yoonbot/manifest"):
            response = self.client.get(path)
            self.assertEqual(response.status_code, 200, path)
            self.assertEqual(response.headers.get("cache-control"), "no-store, max-age=0", path)
            self.assertEqual(response.headers.get("pragma"), "no-cache", path)

    def test_hsts_only_on_https_without_include_subdomains(self):
        response = self.client.get("/health", headers={"x-forwarded-proto": "https"})
        hsts = response.headers.get("strict-transport-security", "")
        self.assertEqual(hsts, "max-age=31536000")
        self.assertNotIn("includeSubDomains", hsts)

    def test_admin_auth_contract_401_and_503(self):
        wrong = self.client.get("/admin/licenses", headers={"X-Admin-Key": "wrong-key"})
        self.assertEqual(wrong.status_code, 401)
        missing = self.client.get("/admin/licenses")
        self.assertEqual(missing.status_code, 401)

        self.main.ADMIN_API_KEY = ""
        try:
            unconfigured = self.client.get("/admin/licenses", headers={"X-Admin-Key": "any"})
            self.assertEqual(unconfigured.status_code, 503)
        finally:
            self.main.ADMIN_API_KEY = self.ADMIN_KEY

    def test_admin_key_comparison_is_constant_time_in_source(self):
        main_py = MAIN_PY.read_text(encoding="utf-8")
        self.assertIn("hmac.compare_digest(key.encode(", main_py)
        self.assertNotIn('key != ADMIN_API_KEY', main_py)


class BackupLabelTest(unittest.TestCase):
    def test_backup_detail_reports_plain_sqlite_backup(self):
        from agents import db_manager

        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        tmp = Path(tmpdir.name)
        source_db = tmp / "members.db"

        original_db_path = db.DB_PATH
        original_dm_db_path = db_manager.DB_PATH
        original_targets = db_manager._backup_targets
        original_run_quiet = db_manager._run_quiet
        db.DB_PATH = source_db
        db_manager.DB_PATH = source_db
        db.init_db()
        db_manager._backup_targets = lambda: [
            {"name": "local", "label": "test-local", "path": tmp / "backups", "available": True},
        ]
        db_manager._run_quiet = lambda *args, **kwargs: (False, "test_skip_no_ssh")
        try:
            summary = db_manager.backup_database(reason="unit_test")
        finally:
            db.DB_PATH = original_db_path
            db_manager.DB_PATH = original_dm_db_path
            db_manager._backup_targets = original_targets
            db_manager._run_quiet = original_run_quiet

        local = next(item for item in summary["targets"] if item["name"] == "local")
        self.assertEqual(local["status"], "ok")
        # 백업은 평문 SQLite 복사이므로 표기도 사실이어야 한다
        self.assertEqual(local["detail"], "plain_sqlite_backup")
        self.assertNotIn("encrypted", str(summary))

    def test_backup_source_never_claims_encryption(self):
        source = DB_MANAGER_PY.read_text(encoding="utf-8")
        self.assertNotIn("encrypted_sqlite_backup", source)
        self.assertIn("plain_sqlite_backup", source)


class RawSecretPersistenceSourceContractTest(unittest.TestCase):
    """소스 수준 계약: 원문 비밀이 저장·반환 경로에 다시 나타나지 않는다."""

    def test_worker_never_persists_raw_license_key_or_payment_key(self):
        worker_js = WORKER_JS.read_text(encoding="utf-8")
        schema_sql = WORKER_SCHEMA.read_text(encoding="utf-8")

        self.assertNotIn("dev_license_key", worker_js)
        self.assertNotIn("dev_license_key", schema_sql)
        self.assertIn("yoonbotPaymentKeyFingerprint", worker_js)
        self.assertNotIn("payment_ref: body.payment_key", worker_js)

    def test_worker_admin_and_session_auth_hardening(self):
        worker_js = WORKER_JS.read_text(encoding="utf-8")

        self.assertIn("constantTimeTextEqual(actual, expected)", worker_js)
        # FastAPI parity: ADMIN_API_KEY 미설정은 503 (실행 검증은 check-security-headers.mjs)
        self.assertIn('fail(503, "ADMIN_API_KEY is not configured")', worker_js)
        self.assertNotIn('fail(500, "ADMIN_API_KEY is not configured")', worker_js)
        self.assertNotIn("arsen-local-kakao-session", worker_js)
        self.assertIn("KAKAO_SESSION_SECRET is not configured", worker_js)
        # 최상위 500은 고정 문구만 반환, console에는 고정 이벤트명+error.name만
        self.assertNotIn('error.message || "server error"', worker_js)
        self.assertIn("서버 내부 오류가 발생했습니다", worker_js)
        self.assertIn('console.error("unhandled_error", String(error?.name || "Error"));', worker_js)
        self.assertNotIn('console.error("unhandled_error", String(error?.name || "Error"), ', worker_js)
        # Toss upstream body는 오류에 포함하지 않는다
        self.assertNotIn("Toss confirm HTTP ${response.status}: ${body}", worker_js)

    def test_worker_asset_early_return_goes_through_with_cors(self):
        worker_js = WORKER_JS.read_text(encoding="utf-8")
        # 정적 asset 조기 return도 withCors(보안 헤더)를 거친다.
        # 실행 검증은 cloudflare/scripts/check-security-headers.mjs (npm run check).
        self.assertIn("return withCors(assetResponse, request, env);", worker_js)
        handle_request = worker_js.split("export async function handleRequest", 1)[1]
        self.assertNotIn("return assetResponse;\n", handle_request)
        check_script = (ROOT / "cloudflare" / "scripts" / "check-security-headers.mjs").read_text(encoding="utf-8")
        self.assertIn("asset early-return", check_script)
        package_json = (ROOT / "cloudflare" / "package.json").read_text(encoding="utf-8")
        self.assertIn("node scripts/check-security-headers.mjs", package_json)

    def test_no_predictable_dev_fallback_secrets(self):
        """운영 코드에 예측 가능한 공개 fallback secret이 없고, 미설정은 fail-closed."""
        worker_js = WORKER_JS.read_text(encoding="utf-8")
        main_py = MAIN_PY.read_text(encoding="utf-8")
        order_py = ORDER_MANAGER_PY.read_text(encoding="utf-8")
        license_py = (ROOT / "agents" / "license_manager.py").read_text(encoding="utf-8")
        education_py = (ROOT / "agents" / "education_payment_manager.py").read_text(encoding="utf-8")

        for source in (worker_js, main_py, order_py, license_py, education_py):
            self.assertNotIn("local-order-dev-secret", source)
            self.assertNotIn("local-license-dev-secret", source)
            self.assertNotIn("local-education-payment-secret", source)
            self.assertNotIn("arsen-local-kakao-session", source)
        # Worker legacyRawKey: 빈 secret으로 zero key를 만들지 않는다
        self.assertIn("is not configured`)", worker_js)

    def test_missing_secrets_fail_closed_at_runtime(self):
        from agents import education_payment_manager, license_manager, order_manager

        _install_scheduler_stub()
        saved = {
            name: os.environ.pop(name, None)
            for name in ("CODE_SECRET_KEY", "LICENSE_SECRET_KEY", "KAKAO_SESSION_SECRET")
        }
        try:
            with self.assertRaises(RuntimeError):
                order_manager._secret("EMAIL_SECRET_KEY_MISSING_FOR_TEST")
            with self.assertRaises(RuntimeError):
                license_manager._secret()
            with self.assertRaises(RuntimeError):
                education_payment_manager._payment_key_fingerprint("pk_test_failclosed")
            with self.assertRaises(RuntimeError):
                importlib.import_module("main")._kakao_session_secret()
        finally:
            for name, value in saved.items():
                if value is not None:
                    os.environ[name] = value

    def test_kakao_session_secret_requires_only_its_own_env(self):
        _install_scheduler_stub()
        main_module = importlib.import_module("main")
        saved = {
            name: os.environ.pop(name, None)
            for name in ("KAKAO_SESSION_SECRET", "ADMIN_KEY", "TELEGRAM_WEBHOOK_SECRET")
        }
        try:
            # 다른 secret이 있어도 대체(fallback)로 쓰이지 않는다
            os.environ["ADMIN_KEY"] = "admin-key-must-not-be-used"
            os.environ["TELEGRAM_WEBHOOK_SECRET"] = "webhook-secret-must-not-be-used"
            with self.assertRaises(RuntimeError):
                main_module._kakao_session_secret()
            os.environ["KAKAO_SESSION_SECRET"] = "explicit-kakao-session-secret"
            self.assertEqual(main_module._kakao_session_secret(), b"explicit-kakao-session-secret")
        finally:
            for name in ("KAKAO_SESSION_SECRET", "ADMIN_KEY", "TELEGRAM_WEBHOOK_SECRET"):
                os.environ.pop(name, None)
            for name, value in saved.items():
                if value is not None:
                    os.environ[name] = value

    def test_worker_sets_security_headers(self):
        worker_js = WORKER_JS.read_text(encoding="utf-8")
        for header in (
            '"x-content-type-options", "nosniff"',
            '"x-frame-options", "DENY"',
            '"referrer-policy", "strict-origin-when-cross-origin"',
            '"permissions-policy", "camera=(), microphone=(), geolocation=()"',
            '"strict-transport-security", "max-age=31536000"',
        ):
            self.assertIn(header, worker_js)
        self.assertNotIn("includeSubDomains", worker_js)
        # Worker json() 응답의 no-store 캐시 계약 유지 (release/manifest 포함 전 JSON 경로)
        self.assertIn('headers.set("cache-control", "no-store, max-age=0");', worker_js)
        self.assertIn('headers.set("pragma", "no-cache");', worker_js)

    def test_fastapi_order_manager_never_stores_raw_payment_key(self):
        source = ORDER_MANAGER_PY.read_text(encoding="utf-8")
        self.assertIn("_payment_key_fingerprint", source)
        self.assertNotIn("payment_ref=payment_key", source)
        # Toss upstream body 인용 금지
        self.assertNotIn("exc.read()", source)

    def test_license_admin_ui_has_no_raw_key_column(self):
        html = LICENSE_ADMIN_HTML.read_text(encoding="utf-8")
        self.assertNotIn("dev_license_key", html)
        self.assertNotIn("copy-dev-key", html)
        # 생성 응답 1회 노출 안내는 유지
        self.assertIn("발급된 키는 지금 한 번만 표시됩니다.", html)


class PaymentAdminXssContractTest(unittest.TestCase):
    """payment-admin.html 저장형 XSS 회귀 계약: 서버/사용자 유래 문자열은
    innerHTML에 escapeHtml 없이 들어가지 않는다."""

    XSS_PROBE = '<img src=x onerror=alert(1)>'

    def test_escape_html_helper_neutralizes_markup(self):
        html = PAYMENT_ADMIN_HTML.read_text(encoding="utf-8")
        self.assertIn("function escapeHtml(value)", html)
        for rule in ('.replace(/&/g, "&amp;")', '.replace(/</g, "&lt;")', '.replace(/>/g, "&gt;")',
                     '.replace(/"/g, "&quot;")', ".replace(/'/g, \"&#039;\")"):
            self.assertIn(rule, html)
        # escapeHtml 체인을 그대로 적용하면 XSS 프로브에 태그 문자가 남지 않는다
        escaped = (self.XSS_PROBE
                   .replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                   .replace('"', "&quot;").replace("'", "&#039;"))
        self.assertNotIn("<", escaped)
        self.assertNotIn(">", escaped)

    def test_all_server_derived_interpolations_are_escaped(self):
        html = PAYMENT_ADMIN_HTML.read_text(encoding="utf-8")
        # 반드시 escape 적용된 형태가 존재
        for required in (
            "${escapeHtml(order.buyer_name)}",
            '${escapeHtml(order.buyer_email_masked || "-")}',
            '${escapeHtml(order.buyer_phone_masked || "-")}',
            "${escapeHtml(order.plan_code)}",
            '${escapeHtml(order.payment_ref || "-")}',
            '${escapeHtml(order.license_key_hint || order.license_id || "-")}',
            'data-id="${escapeHtml(order.id)}"',
            "${escapeHtml(dc.code)}",
            '${escapeHtml(dc.label || "-")}',
            '${escapeHtml(dc.plan_code || "전체")}',
            'data-code="${escapeHtml(dc.code)}"',
            'class="badge ${escapeHtml(status || "")}"',
        ):
            self.assertIn(required, html)
        # innerHTML 렌더 영역에는 raw 삽입 형태가 존재하지 않는다
        # (renderDetail의 textContent 조립은 안전하므로 검사에서 제외)
        inner_html_region = (
            html.split("function badge(", 1)[1].split("function renderDetail(", 1)[0]
            + html.split("function renderDiscounts(", 1)[1].split("document.addEventListener", 1)[0]
        )
        for forbidden in (
            "${order.buyer_name}",
            "${order.buyer_email_masked",
            "${order.buyer_phone_masked",
            "${order.plan_code}",
            "${order.payment_ref",
            "${order.license_key_hint",
            'data-id="${order.id}"',
            "${dc.code}",
            "${dc.label",
            "${dc.plan_code",
            "${dc.expires_at",
            'data-code="${dc.code}"',
            '${status || ""}',
            '${status || "unknown"}',
        ):
            self.assertNotIn(forbidden, inner_html_region)
        self.assertNotIn('<a href="${link}"', html)
        # 날짜 fallback도 escape 경유
        self.assertIn("return escapeHtml(value);", html)


class LicenseEmptyInputGuardTest(unittest.TestCase):
    """FastAPI parity: 빈/공백 hwid·token은 해시/DB 접근 전에 INVALID_REQUEST."""

    def test_activate_rejects_empty_or_blank_inputs(self):
        from agents.license_manager import activate_license

        for license_key, hwid in (("", "HW-1"), ("YB-XXXX", ""), ("YB-XXXX", "   "), ("  ", "HW-1")):
            result = activate_license(license_key=license_key, hwid=hwid)
            self.assertFalse(result["ok"], (license_key, hwid))
            self.assertEqual(result["code"], "INVALID_REQUEST", (license_key, hwid))

    def test_verify_rejects_empty_or_blank_inputs(self):
        from agents.license_manager import verify_license

        for token, hwid in (("", "HW-1"), ("   ", "HW-1"), ("tok-1", ""), ("tok-1", "   ")):
            result = verify_license(activation_token=token, hwid=hwid)
            self.assertFalse(result["ok"], (token, hwid))
            self.assertEqual(result["code"], "INVALID_REQUEST", (token, hwid))


class ArtifactFailClosedTest(unittest.TestCase):
    """FastAPI artifact 직다운로드: 검증된 staged_file 계약일 때만 서빙."""

    ARTIFACT_NAME = "YoonBot-Setup-1.1.0.exe"
    ENDPOINT = f"/api/yoonbot/artifacts/{ARTIFACT_NAME}"
    ENV_VARS = (
        "YOONBOT_ARTIFACT_DOWNLOAD_URL",
        "YOONBOT_ARTIFACT_SHA256",
        "YOONBOT_ARTIFACT_SIZE_BYTES",
        "ARSEN_YOONBOT_ARTIFACT_BASE_URL",
        "YOONBOT_RELEASE_READY_APPROVED",
        "YOONBOT_CODE_SIGNING_STATUS",
    )

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.tmpdir.name) / "members.db"
        self.original_db_path = db.DB_PATH
        db.DB_PATH = self.db_path
        db.init_db()

        _install_scheduler_stub()
        self.main = importlib.import_module("main")
        self.original_artifact_dir = self.main.YOONBOT_ARTIFACT_DIR
        self.artifact_dir = Path(self.tmpdir.name) / "yoonbot-artifacts"
        self.artifact_dir.mkdir()
        self.main.YOONBOT_ARTIFACT_DIR = self.artifact_dir
        self.main._YOONBOT_SHA256_CACHE.clear()

        self.original_env = {}
        for key in self.ENV_VARS:
            self.original_env[key] = os.environ.pop(key, None)
        os.environ["YOONBOT_RELEASE_READY_APPROVED"] = "true"
        os.environ["YOONBOT_CODE_SIGNING_STATUS"] = "signed"
        (self.artifact_dir / self.ARTIFACT_NAME).write_bytes(b"MZ-fake-installer-payload")

        self.client = TestClient(self.main.app, base_url="https://apply.arsen-ai.com")

    def tearDown(self):
        self.main.YOONBOT_ARTIFACT_DIR = self.original_artifact_dir
        self.main._YOONBOT_SHA256_CACHE.clear()
        for key, value in self.original_env.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
        db.DB_PATH = self.original_db_path
        self.tmpdir.cleanup()

    def test_staged_verified_contract_serves_get_and_head(self):
        for method in ("get", "head"):
            response = getattr(self.client, method)(self.ENDPOINT)
            self.assertEqual(response.status_code, 200, method)

    def test_file_on_disk_alone_is_not_enough_over_plain_http(self):
        # HTTPS base URL을 만들 수 없으면 verified 소스가 없으므로 404
        http_client = TestClient(self.main.app, base_url="http://testserver")
        response = http_client.get(self.ENDPOINT)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "yoonbot_artifact_not_verified")

    def test_configured_external_url_disables_local_serving_even_with_file(self):
        os.environ["YOONBOT_ARTIFACT_DOWNLOAD_URL"] = f"https://downloads.example.test/{self.ARTIFACT_NAME}"
        os.environ["YOONBOT_ARTIFACT_SHA256"] = "a" * 64
        os.environ["YOONBOT_ARTIFACT_SIZE_BYTES"] = "12345"
        response = self.client.get(self.ENDPOINT, follow_redirects=False)
        self.assertNotIn(response.status_code, (301, 302, 307, 308))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "yoonbot_artifact_not_verified")

    def test_invalid_external_sha_or_size_still_404_with_file_present(self):
        os.environ["YOONBOT_ARTIFACT_DOWNLOAD_URL"] = f"https://downloads.example.test/{self.ARTIFACT_NAME}"
        os.environ["YOONBOT_ARTIFACT_SHA256"] = "not-a-sha"
        os.environ["YOONBOT_ARTIFACT_SIZE_BYTES"] = "0"
        response = self.client.get(self.ENDPOINT)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "yoonbot_artifact_not_verified")

    def test_source_calls_verified_artifact_source_in_handler(self):
        main_py = MAIN_PY.read_text(encoding="utf-8")
        handler = main_py.split('@app.api_route("/api/yoonbot/artifacts/{artifact_name}"', 1)[1]
        handler = handler.split("@app.get", 1)[0]
        self.assertIn("_yoonbot_verified_artifact_source(request)", handler)
        self.assertIn('verified.get("source") != "staged_file"', handler)
        self.assertIn("yoonbot_artifact_not_verified", handler)


class EncryptorFailClosedTest(unittest.TestCase):
    """연락처 암호화 키 미설정은 명시적으로 실패한다 (all-zero key 금지)."""

    def test_missing_phone_or_email_secret_fails_closed(self):
        from agents import encryptor

        saved = {name: os.environ.pop(name, None) for name in ("PHONE_SECRET_KEY", "EMAIL_SECRET_KEY")}
        try:
            with self.assertRaises(RuntimeError):
                encryptor.encrypt_phone("010-1234-5678")
            with self.assertRaises(RuntimeError):
                encryptor.hash_phone("010-1234-5678")
            with self.assertRaises(RuntimeError):
                encryptor.encrypt_email("user@example.com")
            with self.assertRaises(RuntimeError):
                encryptor.hash_email("user@example.com")
        finally:
            for name, value in saved.items():
                if value is not None:
                    os.environ[name] = value

    def test_existing_short_key_padding_compatibility_is_kept(self):
        from agents import encryptor

        saved = os.environ.get("PHONE_SECRET_KEY")
        os.environ["PHONE_SECRET_KEY"] = "short-key"
        try:
            encrypted = encryptor.encrypt_phone("010-1234-5678")
            self.assertEqual(encryptor.decrypt_phone(encrypted), "010-1234-5678")
        finally:
            if saved is None:
                os.environ.pop("PHONE_SECRET_KEY", None)
            else:
                os.environ["PHONE_SECRET_KEY"] = saved


class CustomerMessageDownloadContractTest(unittest.TestCase):
    OLD_ZIP = "arsen-content-launcher-0.1.0-win-x64.zip"

    def _extract_worker_function(self, name: str) -> str:
        worker_js = WORKER_JS.read_text(encoding="utf-8")
        start = worker_js.index(f"function {name}")
        end = worker_js.index("\n}\n", start + 1) + 3
        return worker_js[start:end]

    def test_fastapi_customer_message_points_only_to_homepage(self):
        from agents.order_manager import customer_license_message

        msg = customer_license_message("YB-TEST-TEST-TEST-TEST", {"expires_at": "2027-01-01T00:00:00+00:00"})
        self.assertIn("https://arsen-ai.com/yoonbot", msg)
        self.assertIn("공개 릴리스가 준비된 경우에만", msg)
        self.assertNotIn(self.OLD_ZIP, msg)
        self.assertNotIn("/api/daf/launcher", msg)
        self.assertNotIn("/api/launcher/release", msg)

    def test_worker_customer_message_parity(self):
        body = self._extract_worker_function("yoonbotCustomerLicenseMessage")
        worker_js = WORKER_JS.read_text(encoding="utf-8")
        self.assertIn("YOONBOT_CUSTOMER_DOWNLOAD_PAGE", body)
        self.assertIn('"https://arsen-ai.com/yoonbot"', worker_js)
        self.assertIn("공개 릴리스가 준비된 경우에만", body)
        self.assertNotIn(self.OLD_ZIP, body)
        self.assertNotIn("LAUNCHER_DIRECT_DOWNLOAD_URL", body)
        self.assertNotIn("LAUNCHER_RELEASE_URL", worker_js)

    def test_fastapi_order_manager_has_no_launcher_zip_reference(self):
        source = ORDER_MANAGER_PY.read_text(encoding="utf-8")
        self.assertNotIn(self.OLD_ZIP, source)
        self.assertNotIn("/api/daf/launcher", source)


if __name__ == "__main__":
    unittest.main()
