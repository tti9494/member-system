from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADMIN_HTML = ROOT / "frontend" / "admin.html"
MAIN_PY = ROOT / "main.py"
BUILD_PAGES = ROOT / "cloudflare" / "scripts" / "build-pages.mjs"
WORKER_JS = ROOT / "cloudflare" / "src" / "worker.js"
KAKAO_MEMBERS_HTML = ROOT / "frontend" / "kakao-members.html"


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


def test_session_admin_page_and_course_defaults_contracts():
    session_admin = (ROOT / "frontend" / "session-admin.html").read_text(encoding="utf-8")
    admin_html = ADMIN_HTML.read_text(encoding="utf-8")
    worker_js = WORKER_JS.read_text(encoding="utf-8")
    booking_manager = (ROOT / "agents" / "booking_manager.py").read_text(encoding="utf-8")
    build_pages = BUILD_PAGES.read_text(encoding="utf-8")

    for token in [
        "/admin/sessions",
        "/admin/bookings?session_id=",
        "/members/${encodeURIComponent(booking.member_id)}/contact",
        "/members/${encodeURIComponent(booking.member_id)}/access-code",
        "/admin/bookings/${encodeURIComponent(booking.id)}/send-payment-guide",
        "/admin/bookings/${encodeURIComponent(booking.id)}/confirm-payment",
        "/admin/bookings/${encodeURIComponent(booking.id)}/location-guide",
        "/admin/preparation-guide",
        "/admin/bookings/${encodeURIComponent(booking.id)}/move-session",
        "/admin/bookings/${encodeURIComponent(booking.id)}/state",
        "카카오톡 문구 복사",
        "후기 요청 문구 복사",
    ]:
        assert token in session_admin

    assert "session-admin.html?session_id=" in admin_html
    assert "상세 관리" in admin_html

    assert '"session-admin.html"' in build_pages
    assert 'DEFAULT_TITLE = "AI 결과물 제작 초급 4주반"' in booking_manager
    assert "DEFAULT_PRICE = 100000" in booking_manager
    assert 'const DEFAULT_TITLE = "AI 결과물 제작 초급 4주반";' in worker_js
    assert "const DEFAULT_PRICE = 100000;" in worker_js
    assert 'const DEFAULT_LOCATION = "추후 공지";' in worker_js


def test_admin_member_group_tab_and_download_contracts():
    html = ADMIN_HTML.read_text(encoding="utf-8")

    assert "admin-tab-member-groups" in html
    assert "멤버 그룹" in html
    assert "member-group-plan-filter" in html
    assert '<option value="consultation">상담</option>' in html
    assert '<option value="lead_email">소식(이메일)</option>' in html
    assert '<option value="lead_phone">소식(번호)</option>' in html
    assert "member-group-status-filter" in html
    assert "member-group-search-input" in html
    assert "Google CSV" in html
    assert "memberGroupExportQuery" in html
    assert 'plan_type", planType' in html
    assert "Google 연락처용" in html


def test_member_page_profile_progress_and_review_contracts():
    member_html = (ROOT / "frontend" / "member.html").read_text(encoding="utf-8")
    admin_html = ADMIN_HTML.read_text(encoding="utf-8")
    worker_js = WORKER_JS.read_text(encoding="utf-8")
    schema_sql = (ROOT / "cloudflare" / "schema.sql").read_text(encoding="utf-8")
    deploy_script = (ROOT / "cloudflare" / "scripts" / "deploy-cloudflare.mjs").read_text(encoding="utf-8")

    for token in [
        "member-openchat",
        "member-level",
        "member-points",
        "member-access",
        "nickname-form",
        "review-form",
        "review-booking",
        "renderProgress",
        "renderReviews",
        "/member/profile",
        "/member/reviews",
    ]:
        assert token in member_html

    for token in [
        "admin-tab-kakao-members",
        "kakao-members-panel",
        "renderKakaoMembers",
        "kakaoMemberFilter",
        "오픈톡 닉네임",
    ]:
        assert token in admin_html

    assert "openchat_nickname TEXT" in schema_sql
    assert "member_id TEXT REFERENCES members" in schema_sql
    assert "booking_id TEXT REFERENCES bookings" in schema_sql
    assert "ALTER TABLE members ADD COLUMN openchat_nickname" in deploy_script
    assert "ALTER TABLE review_entries ADD COLUMN member_id" in deploy_script
    assert "ALTER TABLE review_entries ADD COLUMN booking_id" in deploy_script
    assert "function memberLevelProfile" in worker_js
    assert "function handleMemberProfileUpdate" in worker_js
    assert "function handleMemberReviewCreate" in worker_js


def test_kakao_members_standalone_admin_page_contracts():
    html = KAKAO_MEMBERS_HTML.read_text(encoding="utf-8")
    admin_html = ADMIN_HTML.read_text(encoding="utf-8")
    build_pages = BUILD_PAGES.read_text(encoding="utf-8")

    for token in [
        "ARSEN 카카오 회원 관리",
        "loadKakaoMembers",
        'api("/members")',
        "/admin/members/${encodeURIComponent(member.id)}/kakao-unlink",
        "kakao-filter",
        "approved-unlinked",
        "전체 관리자에서 보기",
        "승인 미연동",
    ]:
        assert token in html

    assert "kakao-members.html" in build_pages
    assert "/frontend/kakao-members.html" in admin_html


def test_admin_member_modal_free_schedule_and_attendance_contracts():
    html = ADMIN_HTML.read_text(encoding="utf-8")
    main_py = MAIN_PY.read_text(encoding="utf-8")
    worker_js = WORKER_JS.read_text(encoding="utf-8")
    join_free_html = (ROOT / "frontend" / "join-free.html").read_text(encoding="utf-8")

    for token in [
        "openMemberDetailModal",
        "renderMemberModal",
        "markContactRegistered",
        "contact-registered",
        "kickMemberFromClasses",
        "kakaoLinkedPill",
        "unlinkMemberKakao",
        "카카오 연결 해제",
        "memberClassHistorySection",
        "new-session-program-type",
        "seed-free-sessions-btn",
        "무료 일정 생성",
        "seed-free-class",
        "무료 참여자로 추가",
        "showFreeClassGuide",
        "무료 안내 복사",
        "free-guide-template-copy-btn",
        "copyFreeClassTemplateGuide",
        "무료강의 안내 복사",
        "무료강의 안내 문구",
        "markAttendance",
        "참여 완료",
        "불참",
    ]:
        assert token in html

    assert '@app.put("/admin/members/{member_id}")' in main_py
    assert '@app.post("/admin/members/{member_id}/contact-registered")' in main_py
    assert '@app.post("/admin/members/{member_id}/kakao-unlink")' in main_py
    assert '@app.post("/admin/members/{member_id}/kick")' in main_py
    assert '@app.post("/admin/bookings/{booking_id}/free-guide")' in main_py
    assert '@app.post("/admin/sessions/seed-free-class")' in main_py
    assert 'parts[1] === "members"' in worker_js
    assert 'parts[2] === "seed-free-class"' in worker_js
    assert 'parts[3] === "kakao-unlink"' in worker_js
    assert 'parts[3] === "free-guide"' in worker_js
    assert "contact_registered" in worker_js
    assert "kakao_unlinked_by_admin" in worker_js

    assert "loadFreeSessions" in join_free_html
    assert 'id="session_id"' in join_free_html
    assert "선택한 무료강의 일정 신청까지 함께 접수되었습니다." in join_free_html
    assert "비용 0원" in join_free_html
    assert "입문/체험 중심" in join_free_html
    assert "일정 변동 가능" in join_free_html

    join_full_html = (ROOT / "frontend" / "join-full.html").read_text(encoding="utf-8")
    assert "승인 코드 필요" in join_full_html
    assert "입금 확인 후 확정" in join_full_html
    assert "소수정예 실습" in join_full_html


def test_admin_applicant_detail_panel_and_copy_name_contracts():
    html = ADMIN_HTML.read_text(encoding="utf-8")
    worker_js = WORKER_JS.read_text(encoding="utf-8")
    db_manager = (ROOT / "agents" / "db_manager.py").read_text(encoding="utf-8")
    deploy_script = (ROOT / "cloudflare" / "scripts" / "deploy-cloudflare.mjs").read_text(encoding="utf-8")

    assert "selectMember(member.id);" in html
    assert "openMemberDetailModal(member.id);" not in html
    assert 'actionButton("이름 양식 복사", "green", isErased, () => copyMemberArchiveName(member))' in html
    assert "regionCopyToken" in html
    assert "looksLikeEncryptedAccessCode" in html
    assert "approvalCodeCopyToken" in html
    assert "year.slice(-2).padStart(2" in html
    assert "if (code) parts.push(code);" in html

    assert "readableAccessCode" in worker_js
    assert "accessCodeMatches" in worker_js
    assert 'decryptValue(stored, env, "CODE_SECRET_KEY")' in worker_js
    assert "member.access_code !== String(body.code" not in worker_js
    assert "code_exists: Boolean(code)" in worker_js
    assert "CODE_SECRET_KEY" in deploy_script

    assert "b.status='completed'" in db_manager
    assert "b.status='confirmed'" in db_manager
    assert "COALESCE(s.starts_at, b.confirmed_at, b.updated_at, b.created_at) <= ?" in db_manager


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
    assert "theme-change-warning" in html
    assert "테마 적용 전 확인" in html
    assert "전체 백업" in html
    assert "data-consultation-form" in html
    assert "홈페이지 공개 페이지" in html
    assert 'value="/index.html" data-public-preview="true"' in html
    assert 'value="/education.html" data-public-preview="true"' in html
    assert 'value="/frontend/class-dashboard.html"' in html
    assert "수업용 대시보드" in html
    assert "YOONBOT 공개 상세" in html
    assert "YOONBOT 운영 상세" in html
    assert 'function publicSitePreviewOrigin' in html
    assert 'https://arsen-ai.com' in html
    assert "function renderSiteTheme" in html
    assert "function applySiteTheme" in html
    assert "function siteThemeApplyWarning" in html
    assert "function warnThemeSelectionChange" in html
    assert "/admin/site-theme" in html
    assert "assets/theme-loader.js" in html

    assert 'DEFAULT_SITE_THEME_ID = "arsen-modern"' in main_py
    assert '@app.get("/api/site-theme")' in main_py
    assert '@app.get("/admin/site-theme")' in main_py
    assert '@app.put("/admin/site-theme")' in main_py
    assert 'path === "/api/site-theme"' in WORKER_JS.read_text(encoding="utf-8")
    assert 'path === "/admin/site-theme"' in WORKER_JS.read_text(encoding="utf-8")


def test_admin_launcher_status_contracts():
    html = ADMIN_HTML.read_text(encoding="utf-8")
    main_py = MAIN_PY.read_text(encoding="utf-8")
    worker_js = WORKER_JS.read_text(encoding="utf-8")
    release_contract = (ROOT / "cloudflare" / "scripts" / "check-launcher-release-contract.mjs").read_text(encoding="utf-8")

    assert "런처 공지 / 버전" in html
    assert 'id="launcher-status"' in html
    assert "/admin/launcher-status" in html
    assert "/api/daf/manifest" in html
    assert "/api/launcher/release" in html
    assert "function renderLauncherStatus" in html
    assert "state.launcherStatus" in html

    assert '@app.get("/admin/launcher-status")' in main_py
    assert "_admin_launcher_status" in main_py

    assert 'path === "/admin/launcher-status"' in worker_js
    assert "adminLauncherStatusPayload" in worker_js
    assert "launcher_artifact_url_not_https" in worker_js

    assert '"/admin/launcher-status"' in release_contract
    assert "launcher admin status" in release_contract


def test_public_entry_points_prioritize_paid_application_and_keep_free_legacy_route():
    admin_html = ADMIN_HTML.read_text(encoding="utf-8")
    main_py = MAIN_PY.read_text(encoding="utf-8")
    build_pages = BUILD_PAGES.read_text(encoding="utf-8")

    assert "/frontend/join-free.html" in admin_html
    assert "무료 신청서" in admin_html
    assert "/frontend/join-full.html" in main_py
    assert "AI 결과물 제작 초급 4주반 신청" in main_py
    assert "/frontend/class-stories.html" in main_py
    assert "공개 후기 보기" in main_py
    assert "/frontend/yoonbot.html#download" in main_py
    assert "YOONBOT 다운로드" in main_py
    assert "/frontend/status.html" in main_py
    assert "예약 확인" in main_py
    assert "/frontend/study.html" in main_py
    assert "스터디 참가" in main_py
    assert "/frontend/member.html" in main_py
    assert "회원 페이지" in main_py
    assert '"join-free.html"' in build_pages
    assert "/frontend/join-full.html" in build_pages
    assert "AI 결과물 제작 초급 4주반 신청" in build_pages
    assert "/frontend/class-stories.html" in build_pages
    assert "공개 후기 보기" in build_pages
    assert "/frontend/yoonbot.html#download" in build_pages
    assert "YOONBOT 다운로드" in build_pages
    assert "/frontend/status.html" in build_pages
    assert "예약 확인" in build_pages
    assert "study.html" in build_pages
    assert "/frontend/study.html" in build_pages
    assert "/frontend/member.html" in build_pages
    assert "회원 페이지" in build_pages
    assert "class-dashboard.html" in build_pages


def test_study_page_and_booking_policy_contracts():
    admin_html = ADMIN_HTML.read_text(encoding="utf-8")
    study_html = (ROOT / "frontend" / "study.html").read_text(encoding="utf-8")
    main_py = MAIN_PY.read_text(encoding="utf-8")
    worker_js = WORKER_JS.read_text(encoding="utf-8")

    for token in [
        '<option value="study">스터디</option>',
        "new-session-audience-level",
        '<option value="approved">승인멤버 전체</option>',
        '<option value="paid_only">유료강의 수강자만</option>',
        "isStudySession",
        "스터디 참여자로 추가",
        "참여확정",
        "sessionAudienceLabel",
    ]:
        assert token in admin_html

    for token in [
        "ARSEN 스터디 참가",
        "승인 멤버 전용 스터디",
        "/study/sessions",
        "/member/bookings",
        "유료 수강자 전용",
        "승인 멤버 전체",
        "paid_class_count",
        "/auth/kakao/start?next=/frontend/study.html",
    ]:
        assert token in study_html

    for token in [
        '@app.get("/study/sessions")',
        "study_member_acceptance",
        "member_paid_class_count",
        "is_study_session",
        "session_program_type",
        "session_audience_level",
    ]:
        assert token in main_py

    for token in [
        'path === "/study/sessions"',
        'path === "/study/sessions" ||',
        "studyMemberAcceptance",
        "memberPaidClassCount",
        "withPublicMemberStats",
        "MEMBER_LOOKUP_CHUNK_SIZE",
        "for (const chunk of chunkValues(memberIds))",
        "session_program_type",
        "session_audience_level",
    ]:
        assert token in worker_js


def test_class_dashboard_archive_contracts():
    admin_html = ADMIN_HTML.read_text(encoding="utf-8")
    dashboard_html = (ROOT / "frontend" / "class-dashboard.html").read_text(encoding="utf-8")
    education_html = (ROOT / "frontend" / "education.html").read_text(encoding="utf-8")
    main_py = MAIN_PY.read_text(encoding="utf-8")

    assert "/frontend/class-dashboard.html" in admin_html
    assert "수업용 대시보드" in admin_html
    assert "/frontend/class-dashboard.html" in education_html

    assert "ARSEN class dashboard" in dashboard_html
    assert '<body class="ops-tool-page class-dashboard-page">' in dashboard_html
    assert "body.class-dashboard-page .btn.green" in dashboard_html
    assert "body.class-dashboard-page .archive-card" in dashboard_html
    assert "/api/education?include_hidden=true" in dashboard_html
    assert "JSON 백업" in dashboard_html
    assert "백업 불러오기" in dashboard_html
    assert "분류 추천" in dashboard_html
    for label in ["영상생성", "스토리보드", "인물 프롬프트", "문서자동화", "앱 만들기", "알면 좋은 팁"]:
        assert label in dashboard_html
    for field in ["category", "kind", "image_url", "tags", "created_at", "updated_at"]:
        assert field in main_py
    assert ".arsen-work-bus" in main_py


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


def test_public_consultation_contracts():
    admin_html = ADMIN_HTML.read_text(encoding="utf-8")
    worker_js = WORKER_JS.read_text(encoding="utf-8")
    schema_sql = (ROOT / "cloudflare" / "schema.sql").read_text(encoding="utf-8")
    admin_theme = (ROOT / "frontend" / "assets" / "arsen-theme.css").read_text(encoding="utf-8")
    modern_theme = (ROOT / "frontend" / "assets" / "themes" / "arsen-modern.css").read_text(encoding="utf-8")
    public_root = Path("/Users/yoon/arsen-ai-web")

    assert "admin-tab-consultations" in admin_html
    assert "admin-tab-newsletter" in admin_html
    assert "consultations-panel" in admin_html
    assert "newsletter-panel" in admin_html
    assert "consultations-list" in admin_html
    assert "newsletter-list" in admin_html
    assert "/admin/consultations?status=active" in admin_html
    assert "kind=consultation" in admin_html
    assert "kind=newsletter" in admin_html
    assert "showConsultationContact" in admin_html
    assert "updateConsultationStatus" in admin_html
    assert "stat-consultation" in admin_html
    assert '<option value="consultation">상담</option>' in admin_html

    assert "CREATE TABLE IF NOT EXISTS consultations" in schema_sql
    assert 'path === "/api/consultations"' in worker_js
    assert 'path === "/admin/consultations"' in worker_js
    assert "consultationMessage" in worker_js
    assert "consultation_contact_view" in worker_js
    assert 'memberPlanType' in worker_js
    assert '"consultation"' in worker_js
    assert '"lead_email"' in worker_js
    assert '"lead_phone"' in worker_js
    assert "consultation_mirror" in worker_js
    assert "canUpgradeLeadToApplication" in worker_js
    assert "upgradeLeadToApplication" in worker_js
    assert "canRefreshDuplicateApplication" in worker_js
    assert "refreshDuplicateApplication" in worker_js
    assert "latest_application_refreshed" in worker_js
    assert "latest_activity_at" in worker_js
    assert "upgraded_from_lead" in worker_js
    assert "lead_upgraded_to_apply" in worker_js
    assert "리드를 신청자/멤버 목록" in worker_js
    assert "최근접수" in admin_html
    assert "latestDuplicatePlanType" in admin_html
    assert "최근 재신청 유형" in admin_html
    assert "재신청 이력" in admin_html
    assert "pill reapply" in admin_html
    assert '@app.post("/api/consultations")' in MAIN_PY.read_text(encoding="utf-8")
    assert "upgrade_lead_to_application" in MAIN_PY.read_text(encoding="utf-8")
    assert "refresh_duplicate_application" in MAIN_PY.read_text(encoding="utf-8")
    assert '"plan_type": plan_type' in MAIN_PY.read_text(encoding="utf-8")
    assert '"lead_email"' in MAIN_PY.read_text(encoding="utf-8")
    assert '"lead_phone"' in MAIN_PY.read_text(encoding="utf-8")

    index_page = (public_root / "index.html").read_text(encoding="utf-8")
    site_js = (public_root / "assets" / "site.js").read_text(encoding="utf-8")
    assert "전화번호 입력" in index_page
    assert 'name="name"' in index_page
    assert "lead-capture-message" in index_page
    assert "novalidate" in index_page
    assert 'name="contact"' in index_page
    assert 'payload.contact_type = "phone"' in site_js
    assert "이름을 입력해주세요." in site_js
    assert "전화번호를 입력해주세요." in site_js

    for theme in [admin_theme, modern_theme]:
        assert "#newsletter-panel .review-board-panel" in theme
        assert "#newsletter-panel .consultation-row" in theme
        assert "#newsletter-panel .consultation-row-head" in theme
        assert "#newsletter-panel .consultation-row:not(.consultation-row-head):hover" in theme
        assert "rgba(16, 27, 42, 0.92)" in theme
        assert "rgba(8, 17, 29, 0.96)" in theme
        assert "background: #ffffff !important" not in theme[theme.rfind("Admin consultation/newsletter guard:"):]

    for page_name in ["index.html", "consulting.html", "store.html", "yoonbot.html"]:
        page = (public_root / page_name).read_text(encoding="utf-8")
        assert "data-consultation-form" in page
        assert "data-error" in page
        assert "실제 외부 전송 없이" not in page


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


def test_yoonbot_brand_copy_and_theme_button_state_contracts():
    yoonbot_html = (ROOT / "frontend" / "yoonbot.html").read_text(encoding="utf-8")
    admin_html = ADMIN_HTML.read_text(encoding="utf-8")
    theme_css = (ROOT / "frontend" / "assets" / "arsen-theme.css").read_text(encoding="utf-8")
    modern_css = (ROOT / "frontend" / "assets" / "themes" / "arsen-modern.css").read_text(encoding="utf-8")

    # 공개 판매 페이지와 관리자 화면의 브랜드 표기는 YOONBOT으로 통일한다.
    assert "YOONBOT 파일럿 구매 접수" in yoonbot_html
    assert "윤봇" not in yoonbot_html
    assert "YoonBot" not in admin_html

    # 공개 판매 페이지에 내부 개발 용어(MVP)를 노출하지 않는다.
    assert "MVP" not in yoonbot_html

    # !important 색상 속성을 transition 대상으로 두면 Chromium에서 버튼이
    # disabled 해제 후에도 저대비 회색 상태로 고정되는 문제가 있어 transform만 전환한다.
    for css in (theme_css, modern_css):
        assert "transition: transform 0.18s ease;" in css
        assert "background 0.18s" not in css
        assert "opacity 0.18s" not in css


def test_apply_free_plan_backend_validation_contracts():
    validator_py = (ROOT / "agents" / "validator.py").read_text(encoding="utf-8")
    worker_js = WORKER_JS.read_text(encoding="utf-8")
    status_html = (ROOT / "frontend" / "status.html").read_text(encoding="utf-8")

    # 무료강의 신청의 지역/시간대 필수 검증은 main.py(validator)와 worker.js 양쪽에 있어야 한다.
    for source in (validator_py, worker_js):
        assert "무료강의 신청은 참여 가능 지역을 입력해야 합니다." in source
        assert "무료강의 신청은 참여 가능 시간대를 최소 1개 선택해야 합니다." in source

    # status.html은 사이트 테마 체계를 따르고, 동적 카드 색상은 테마 변수를 사용한다.
    assert 'data-arsen-theme="active"' in status_html
    assert "theme-loader.js" in status_html
    assert "#d9e5f2" not in status_html
    assert "#0c131b" not in status_html
