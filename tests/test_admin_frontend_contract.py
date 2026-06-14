from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADMIN_HTML = ROOT / "frontend" / "admin.html"
MAIN_PY = ROOT / "main.py"
BUILD_PAGES = ROOT / "cloudflare" / "scripts" / "build-pages.mjs"
WORKER_JS = ROOT / "cloudflare" / "src" / "worker.js"


def test_admin_member_search_and_erase_ux_contracts():
    html = ADMIN_HTML.read_text(encoding="utf-8")

    assert "normalizeSearchText" in html
    assert "memberMatchesSearch" in html
    assert "검색어와 맞는 신청자" in html
    assert "삭제 처리된 신청자는 현재 “삭제 제외” 목록에서 숨겨졌습니다." in html
    assert "삭제 제외 목록에서는 더 이상 표시하지 않습니다." in html


def test_admin_booking_filter_and_move_ux_contracts():
    html = ADMIN_HTML.read_text(encoding="utf-8")

    assert "selectedBookingDateKey" in html
    assert "이 날짜에 연결된 예약" in html
    assert "시간 카드를 누르면 해당 시간" in html
    assert 'bookingTab: "bookings"' in html
    assert "sessionDateKey({ starts_at: booking.session_starts_at })" in html


def test_admin_member_group_tab_and_download_contracts():
    html = ADMIN_HTML.read_text(encoding="utf-8")

    assert "admin-tab-member-groups" in html
    assert "멤버 그룹" in html
    assert "member-group-plan-filter" in html
    assert "member-group-status-filter" in html
    assert "member-group-search-input" in html
    assert "Google CSV" in html
    assert "memberGroupExportQuery" in html
    assert 'plan_type", planType' in html
    assert "Google 연락처용" in html


def test_admin_local_preview_db_is_visibly_labeled():
    html = ADMIN_HTML.read_text(encoding="utf-8")

    assert "data-source-badge" in html
    assert "local-preview-banner" in html
    assert "로컬 테스트 DB" in html
    assert "테스트 전용 DB" in html
    assert "body.local-preview .local-preview-banner" in html
    assert "function renderDataSourceMode" in html
    assert "운영자 콘솔 · 로컬 테스트 DB" in html


def test_admin_theme_manager_contracts():
    html = ADMIN_HTML.read_text(encoding="utf-8")
    main_py = MAIN_PY.read_text(encoding="utf-8")

    assert "site-theme-select" in html
    assert "site-theme-preview-btn" in html
    assert "site-theme-apply-btn" in html
    assert "홈페이지 공개 페이지" in html
    assert 'value="/index.html" data-public-preview="true"' in html
    assert 'value="/education.html" data-public-preview="true"' in html
    assert 'function publicSitePreviewOrigin' in html
    assert 'https://arsen-ai.com' in html
    assert "function renderSiteTheme" in html
    assert "function applySiteTheme" in html
    assert "/admin/site-theme" in html
    assert "assets/theme-loader.js" in html

    assert 'DEFAULT_SITE_THEME_ID = "arsen-modern"' in main_py
    assert '@app.get("/api/site-theme")' in main_py
    assert '@app.get("/admin/site-theme")' in main_py
    assert '@app.put("/admin/site-theme")' in main_py
    assert 'path === "/api/site-theme"' in WORKER_JS.read_text(encoding="utf-8")
    assert 'path === "/admin/site-theme"' in WORKER_JS.read_text(encoding="utf-8")


def test_public_entry_points_include_free_application_link():
    admin_html = ADMIN_HTML.read_text(encoding="utf-8")
    main_py = MAIN_PY.read_text(encoding="utf-8")
    build_pages = BUILD_PAGES.read_text(encoding="utf-8")

    assert "/frontend/join-free.html" in admin_html
    assert "무료 신청서" in admin_html
    assert "/frontend/join-free.html" in main_py
    assert "무료 강의 신청" in main_py
    assert "/frontend/class-stories.html" in main_py
    assert "공개 후기 보기" in main_py
    assert "/frontend/join-free.html" in build_pages
    assert "무료 강의 신청" in build_pages
    assert "/frontend/class-stories.html" in build_pages
    assert "공개 후기 보기" in build_pages


def test_review_board_frontend_contracts():
    admin_html = ADMIN_HTML.read_text(encoding="utf-8")
    stories_html = (ROOT / "frontend" / "class-stories.html").read_text(encoding="utf-8")
    main_py = MAIN_PY.read_text(encoding="utf-8")
    worker_js = WORKER_JS.read_text(encoding="utf-8")

    assert "admin-tab-review-board" in admin_html
    assert "review-board-panel" in admin_html
    assert "review-entry-new-btn" in admin_html
    assert "review-instructor-new-btn" in admin_html
    assert "review-invite-new-btn" in admin_html
    assert "/admin/review-board" in admin_html
    assert "/admin/review-board/invites" in admin_html
    assert "/frontend/class-stories.html" in admin_html
    assert "/frontend/review-submit.html" in admin_html

    assert "ARSEN 후기보드" in stories_html
    assert "/api/review-board" in stories_html
    assert "/frontend/review-submit.html" in stories_html
    assert "loadReviewBoard" in stories_html
    assert "demoMode" in stories_html
    assert "state.loadError = true" in stories_html
    assert 'get("demo") === "1"' in stories_html

    submit_html = (ROOT / "frontend" / "review-submit.html").read_text(encoding="utf-8")
    assert "ARSEN 후기 작성" in submit_html
    assert "/api/review-board/submit/" in submit_html
    assert "consent_public_review" in submit_html
    assert "승인 후 공개" in submit_html

    assert '@app.get("/api/review-board")' in main_py
    assert '@app.get("/api/review-board/submit/{token}")' in main_py
    assert '@app.post("/api/review-board/submit/{token}")' in main_py
    assert '@app.get("/admin/review-board")' in main_py
    assert '@app.post("/admin/review-board/invites")' in main_py
    assert 'path === "/api/review-board"' in worker_js
    assert 'path.startsWith("/api/review-board/submit/")' in worker_js
    assert 'path === "/admin/review-board"' in worker_js
    assert 'path === "/admin/review-board/invites"' in worker_js


def test_cloudflare_contacts_export_contract_matches_fastapi():
    source = WORKER_JS.read_text(encoding="utf-8")

    assert 'indexUrl.pathname = "/index.html"' in source
    assert "contactExportDetail" in source
    assert 'pii: "decrypted_for_admin_export"' in source
    assert 'grade: url.searchParams.get("grade")' in source
    assert "booking_status_summary" in source
    assert '"booking_status_summary"' in source
    assert 'logAction(env, "system", "contacts_export", contactExportDetail("csv", contacts), request)' in source
    assert 'logAction(env, "system", "contacts_export", contactExportDetail("vcf", contacts), request)' in source
