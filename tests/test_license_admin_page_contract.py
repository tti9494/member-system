from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LICENSE_ADMIN_HTML = ROOT / "frontend" / "license-admin.html"
YOONBOT_HTML = ROOT / "frontend" / "yoonbot.html"
PAYMENT_ADMIN_HTML = ROOT / "frontend" / "payment-admin.html"
ADMIN_HTML = ROOT / "frontend" / "admin.html"
STATUS_HTML = ROOT / "frontend" / "status.html"
MAIN_PY = ROOT / "main.py"
WORKER_JS = ROOT / "cloudflare" / "src" / "worker.js"
WORKER_SCHEMA = ROOT / "cloudflare" / "schema.sql"


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
    assert "YOONBOT 상세" in admin_html


def test_yoonbot_sales_and_payment_admin_pages_contain_order_contracts():
    sales_html = YOONBOT_HTML.read_text(encoding="utf-8")
    payment_html = PAYMENT_ADMIN_HTML.read_text(encoding="utf-8")

    assert "YOONBOT" in sales_html
    assert "카카오톡 자동 프로그램" in sales_html
    assert "<h1>YOONBOT</h1>" in sales_html
    assert "/frontend/assets/yoonbot-hero.png" in sales_html
    assert "/api/yoonbot/orders" in sales_html
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


def test_cloudflare_worker_license_contract_is_registered():
    worker_js = WORKER_JS.read_text(encoding="utf-8")
    schema_sql = WORKER_SCHEMA.read_text(encoding="utf-8")

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
