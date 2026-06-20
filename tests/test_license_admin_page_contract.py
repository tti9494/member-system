from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LICENSE_ADMIN_HTML = ROOT / "frontend" / "license-admin.html"
YOONBOT_HTML = ROOT / "frontend" / "yoonbot.html"
PAYMENT_ADMIN_HTML = ROOT / "frontend" / "payment-admin.html"
ADMIN_HTML = ROOT / "frontend" / "admin.html"
STATUS_HTML = ROOT / "frontend" / "status.html"
MEMBER_HTML = ROOT / "frontend" / "member.html"
MAIN_PY = ROOT / "main.py"
WORKER_JS = ROOT / "cloudflare" / "src" / "worker.js"
WORKER_SCHEMA = ROOT / "cloudflare" / "schema.sql"
DEPLOY_SCRIPT = ROOT / "cloudflare" / "scripts" / "deploy-cloudflare.mjs"


def test_license_admin_page_contains_operator_contracts():
    html = LICENSE_ADMIN_HTML.read_text(encoding="utf-8")

    assert "YOONBOT 라이선스 관리" in html
    assert "/admin/licenses" in html
    assert "/members" in html
    assert "/api/license/activate" in html
    assert "/api/license/verify" in html
    assert "activation_token" in html
    assert "memberLabel" in html
    assert "loadMembers" in html
    assert '<select id="member-id">' in html
    assert '<select id="member-filter">' in html
    assert '<select id="sort-filter">' in html
    assert 'id="member-search"' in html
    assert 'id="license-search"' in html
    assert 'id="date-from"' in html
    assert 'id="date-to"' in html
    assert 'value="member_asc"' in html
    assert "top-grid" in html
    assert "license-table" in html
    assert "filteredLicenses" in html
    assert "sortedLicenses" in html
    assert "memberNumber" in html
    assert "issueLabel" in html
    assert "memberCell" in html
    assert "발급 안 함" in html
    assert "발급함" in html
    assert "회원 번호순" in html
    assert "회원 연결 없음" in html
    assert "개발 키" in html
    assert "copy-dev-key" in html
    assert 'member.status !== "erased"' in html
    assert "삭제된 회원" in html
    assert "삭제 제외 회원" in html
    assert "발급된 키는 지금 한 번만 표시됩니다." in html
    assert "기기 초기화" in html
    assert "회수" in html
    assert "/frontend/payment-admin.html" in html


def test_admin_page_links_to_license_admin():
    admin_html = ADMIN_HTML.read_text(encoding="utf-8")

    assert "/frontend/license-admin.html" in admin_html
    assert "YOONBOT 라이선스" in admin_html
    assert "/frontend/yoonbot.html" in admin_html
    assert "/frontend/payment-admin.html" in admin_html
    assert "YOONBOT 결제/주문" in admin_html
    assert "YOONBOT 운영 상세" in admin_html


def test_yoonbot_sales_and_payment_admin_pages_contain_order_contracts():
    sales_html = YOONBOT_HTML.read_text(encoding="utf-8")
    payment_html = PAYMENT_ADMIN_HTML.read_text(encoding="utf-8")

    assert "YOONBOT" in sales_html
    assert "카카오톡 자동 프로그램" in sales_html
    assert "<h1>YOONBOT</h1>" in sales_html
    assert "/frontend/assets/yoonbot-hero.png" in sales_html
    assert "/api/yoonbot/orders" in sales_html
    assert 'href="#download"' in sales_html
    assert 'id="download"' in sales_html
    assert 'id="launcher-download-link"' in sales_html
    assert "Windows 런처 다운로드" in sales_html
    assert "/api/daf/launcher/artifacts/arsen-content-launcher-0.1.0-win-x64.zip" in sales_html
    assert "/api/launcher/release" in sales_html
    assert "artifact_download_url" in sales_html
    assert "consent_privacy" in sales_html
    assert "LICENSE_API_URL" in sales_html
    assert "https://apply.arsen-ai.com" in sales_html
    assert "/frontend/status.html" not in sales_html
    assert "신청 확인" not in sales_html
    assert "강의 신청" not in sales_html

    assert "YOONBOT 결제/주문 관리" in payment_html
    assert "/admin/yoonbot/orders" in payment_html
    assert "mark-paid" in payment_html
    assert "issue-license" in payment_html
    assert "refund-note" in payment_html
    assert "발급된 키는 지금 한 번만 표시됩니다." in payment_html


def test_status_page_copy_does_not_claim_numeric_eight_digit_codes():
    html = STATUS_HTML.read_text(encoding="utf-8")

    assert "ARSEN 강의 신청·예약 확인" in html
    assert "AI 모임 예약 상태 확인" not in html
    assert "8자리" not in html
    assert "숫자 코드" not in html
    assert 'maxlength="8"' not in html
    assert 'inputmode="numeric"' not in html
    assert "발급받은 승인 코드" in html
    assert "/frontend/member.html" in html


def test_member_page_uses_code_login_and_booking_contracts():
    html = MEMBER_HTML.read_text(encoding="utf-8")
    worker_js = WORKER_JS.read_text(encoding="utf-8")
    build_pages = (ROOT / "cloudflare" / "scripts" / "build-pages.mjs").read_text(encoding="utf-8")

    assert "ARSEN 회원 페이지" in html
    assert "카카오로 계속하기 준비중" not in html
    assert "준비중" not in html
    assert "승인 코드로 확인" in html
    assert "카카오로 확인" in html
    assert 'role="tablist"' in html
    assert 'disabled>카카오로 확인' not in html
    assert "/auth/kakao/start" in html
    assert "/auth/kakao/me" in html
    assert "/auth/kakao/link" in html
    assert "/member/verify-code" in html
    assert "/member/bookings" in html
    assert "/sessions" in html
    assert "예약·수강 이력" in html
    assert "수업용 대시보드" in html
    assert "/frontend/education.html" in html
    assert "처음 신청하시는 분은" in html
    assert "member.html" in build_pages

    assert "session_location" in worker_js
    assert "request_rank" in worker_js
    assert "paid_rank" in worker_js
    assert 'path === "/auth/kakao/start"' in worker_js
    assert 'path === "/auth/kakao/callback"' in worker_js
    assert 'path === "/auth/kakao/me"' in worker_js
    assert 'path === "/auth/kakao/link"' in worker_js


def test_license_api_routes_are_registered():
    main_py = MAIN_PY.read_text(encoding="utf-8")

    assert '@app.post("/api/license/activate")' in main_py
    assert '@app.post("/api/license/verify")' in main_py
    assert '@app.get("/admin/licenses")' in main_py
    assert '@app.post("/admin/licenses/{license_id}/reset-device")' in main_py
    assert '@app.get("/api/yoonbot/products")' in main_py
    assert '@app.post("/api/yoonbot/orders")' in main_py
    assert '@app.get("/admin/yoonbot/orders")' in main_py
    assert '@app.post("/admin/yoonbot/orders/{order_id}/issue-license")' in main_py
    assert '@app.get("/auth/kakao/start")' in main_py
    assert '@app.get("/auth/kakao/callback")' in main_py
    assert '@app.get("/auth/kakao/me")' in main_py
    assert '@app.post("/auth/kakao/link")' in main_py


def test_cloudflare_worker_license_contract_is_registered():
    worker_js = WORKER_JS.read_text(encoding="utf-8")
    schema_sql = WORKER_SCHEMA.read_text(encoding="utf-8")
    deploy_script = DEPLOY_SCRIPT.read_text(encoding="utf-8")

    assert 'path === "/api/license/activate"' in worker_js
    assert 'path === "/api/license/verify"' in worker_js
    assert 'path === "/admin/licenses"' in worker_js
    assert 'parts[3] === "reset-device"' in worker_js
    assert "LICENSE_SECRET_KEY" in worker_js
    assert "dev_license_key" in worker_js
    assert "authorization,content-type,x-admin-key" in worker_js
    assert "CREATE TABLE IF NOT EXISTS licenses" in schema_sql
    assert "dev_license_key TEXT" in schema_sql
    assert "CREATE TABLE IF NOT EXISTS license_activations" in schema_sql
    assert "CREATE TABLE IF NOT EXISTS license_events" in schema_sql
    assert 'path === "/api/yoonbot/products"' in worker_js
    assert 'path === "/api/yoonbot/orders"' in worker_js
    assert 'path === "/admin/yoonbot/orders"' in worker_js
    assert 'parts[4] === "issue-license"' in worker_js
    assert "CREATE TABLE IF NOT EXISTS orders" in schema_sql
    assert "idx_orders_status_created" in schema_sql
    assert "kakao_id TEXT" in schema_sql
    assert "idx_members_kakao_id" in deploy_script
    assert "ALTER TABLE members ADD COLUMN kakao_id TEXT" in deploy_script
    # Worker products readiness must be dynamic — not hardcoded to manual_bank_transfer
    assert "yoonbotProducts(env)" in worker_js
    assert "env.YOONBOT_PAYMENT_PROVIDER" in worker_js
    assert "env.TOSS_PAYMENTS_CLIENT_KEY" in worker_js
    assert "env.TOSS_PAYMENTS_SECRET_KEY" in worker_js
    handle_request = worker_js.split("export async function handleRequest", 1)[1]
    assert 'const parts = path.split("/").filter(Boolean);' in handle_request


def test_yoonbot_discount_code_frontend_contract():
    """yoonbot.html must have discount code input with URL prefill support."""
    sales_html = YOONBOT_HTML.read_text(encoding="utf-8")

    # Discount code input field
    assert 'id="discount-code"' in sales_html
    assert 'name="discount_code"' in sales_html
    # URL prefill from ?discount= query param
    assert 'params.get("discount")' in sales_html
    # Button text stays purchase-oriented while clearly marking the pilot stage.
    assert "구매" in sales_html
    assert "파일럿" in sales_html
    assert "정식 배포 완료" not in sales_html
    assert "정식 공개 판매" in sales_html
    assert "신청 접수" not in sales_html


def test_yoonbot_discount_admin_page_contract():
    """payment-admin.html must display discount info and provide discount management UI."""
    payment_html = PAYMENT_ADMIN_HTML.read_text(encoding="utf-8")

    # Discount column in orders table
    assert "할인" in payment_html
    # Admin discount management section
    assert "/admin/yoonbot/discounts" in payment_html
    assert "discount_type" in payment_html
    assert "discount_value" in payment_html
    assert "disable-discount" in payment_html


def test_discount_admin_api_routes_registered():
    """main.py must register all discount admin endpoints."""
    main_py = MAIN_PY.read_text(encoding="utf-8")

    assert '@app.get("/admin/yoonbot/discounts")' in main_py
    assert '@app.post("/admin/yoonbot/discounts")' in main_py
    assert '@app.post("/admin/yoonbot/discounts/{code}/disable")' in main_py


def test_cloudflare_worker_discount_contract():
    """Worker and schema must support the discount feature."""
    worker_js = WORKER_JS.read_text(encoding="utf-8")
    schema_sql = WORKER_SCHEMA.read_text(encoding="utf-8")

    # Worker discount routes
    assert 'path === "/admin/yoonbot/discounts"' in worker_js
    assert '"disable"' in worker_js
    # Worker discount helpers
    assert "validateAndApplyDiscount" in worker_js
    assert "normalizeDiscountCode" in worker_js
    assert "discountRowPublic" in worker_js
    # Schema has discount codes table and required columns
    assert "CREATE TABLE IF NOT EXISTS yoonbot_discount_codes" in schema_sql
    assert "discount_type TEXT NOT NULL" in schema_sql
    assert "redeemed_count INTEGER NOT NULL DEFAULT 0" in schema_sql
    assert "idx_discount_codes_code" in schema_sql
    # Orders table has discount columns in schema
    assert "discount_code TEXT" in schema_sql
    assert "discount_amount_krw INTEGER NOT NULL DEFAULT 0" in schema_sql
    assert "original_amount_krw INTEGER" in schema_sql
