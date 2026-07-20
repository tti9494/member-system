import os
import sys
import json
import csv
import io
import logging
import shutil
import uuid
import base64
import hashlib
import hmac
import secrets
import urllib.parse
from html import escape as html_escape
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from pathlib import Path
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, FileResponse, Response, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Any
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import httpx

load_dotenv(dotenv_path=str(Path.home() / "member-system" / ".env"))
sys.path.insert(0, str(Path.home() / "member-system"))

from db import init_db, get_conn
from agents.validator import validate
from agents.duplicate_checker import check_duplicate, find_duplicate_member
from agents.consent_checker import check_consent
from agents.db_manager import (
    create_member, get_member, list_members, update_member, update_status,
    blacklist_member, get_stats, save_to_sheets, log_action,
    backup_database, cleanup_expired_codes, get_expiring_soon, get_storage_status,
    get_latest_member_by_phone_hash, get_operator_health, get_storage_snapshot,
    release_expired_locks, get_code_delivery_logs, erase_member_personal_data,
    get_member_by_kakao_id, link_member_kakao, unlink_member_kakao,
    upgrade_lead_to_application, refresh_duplicate_application,
    list_review_board, get_review_instructor, get_review_entry,
    create_review_instructor, update_review_instructor, delete_review_instructor,
    create_review_entry, update_review_entry, delete_review_entry,
    create_review_invite, get_review_invite_by_token, get_review_invite,
    list_review_invites, revoke_review_invite, submit_review_from_invite,
)
from agents.booking_manager import (
    DEFAULT_PRICE, confirm_payment_state, create_booking, create_session, default_free_class_guide, default_location_guide, default_payment_guide,
    default_refund_guide,
    delete_booking, delete_session, find_active_member_booking, get_booking, get_session, list_bookings, list_member_bookings,
    list_sessions, list_study_sessions, member_paid_class_count, move_booking_to_session, refresh_session_counts, seed_default_free_class_sessions,
    seed_default_sunday_sessions, send_payment_guide_state, is_study_session, study_member_acceptance,
    session_acceptance, set_booking_state, update_session,
)
from agents.code_generator import generate_code, get_current_code, verify_code, revoke_code, regenerate_code
from agents.license_manager import (
    activate_license, create_license, extend_license, get_license,
    license_summary, list_licenses, reset_license_device, revoke_license,
    verify_license as verify_yoonbot_license,
)
from agents.order_manager import (
    cancel_order as cancel_yoonbot_order,
    confirm_toss_payment as confirm_yoonbot_toss_payment,
    create_order as create_yoonbot_order,
    create_discount_code as create_yoonbot_discount_code,
    disable_discount_code as disable_yoonbot_discount_code,
    get_order as get_yoonbot_order,
    get_order_by_toss_order_id as get_yoonbot_order_by_toss_id,
    get_toss_payment_config,
    build_toss_payment_payload,
    issue_license as issue_yoonbot_order_license,
    list_discount_codes as list_yoonbot_discount_codes,
    list_orders as list_yoonbot_orders,
    mark_paid as mark_yoonbot_order_paid,
    order_summary as yoonbot_order_summary,
    products as yoonbot_products,
    refund_order as refund_yoonbot_order,
)
from agents.telegram_notifier import (
    notify_admin_new_apply, notify_member_approved, notify_member_rejected,
    notify_expiring_codes, notify_cleanup_result, send_weekly_report,
    notify_booking_requested, notify_admin_duplicate_apply,
    answer_callback_query, send_admin_message,
)
from agents.meta_validator import meta_validate
from agents.security_checker import check_security
from agents.encryptor import encrypt_data, decrypt_email, decrypt_phone, hash_phone  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("member-system")
SYSTEM_VERSION = "1.1.0-member-v4-foundation"
TELEGRAM_WEBHOOK_SECRET = os.getenv("TELEGRAM_WEBHOOK_SECRET", "")


def build_implementation_status() -> dict:
    """Return an operator-safe V1~V4 implementation map without exposing PII."""
    health = get_operator_health()
    storage = get_storage_status()
    counts = storage.get("counts", {})
    backup = health.get("backup", {})
    accepting = health.get("application_system", {}).get("accepting_applications", False)
    requested = health.get("application_system", {}).get("requested_booking_count", 0)
    active = health.get("application_system", {}).get("active_booking_count", 0)
    hermes = health.get("hermes", {})

    stages = [
        {
            "version": "V1",
            "title": "신청서 접수 / 관리자 확인",
            "status": "done" if counts.get("members", 0) >= 0 else "check",
            "summary": "신청 저장, 중복 검사, 관리자 목록, 연락처 확인 감사 로그가 동작합니다.",
        },
        {
            "version": "V2",
            "title": "강의 일정 / 예약 인원 관리",
            "status": "done" if counts.get("sessions", 0) >= 0 and counts.get("bookings", 0) >= 0 else "check",
            "summary": f"일정 {counts.get('sessions', 0)}개, 예약 {counts.get('bookings', 0)}건을 같은 DB에서 관리합니다.",
        },
        {
            "version": "V3",
            "title": "운영 알림 / 백업 / 내보내기",
            "status": "partial" if backup.get("last_success") else "check",
            "summary": f"최근 백업 상태는 {backup.get('status', 'unknown')}이며 JSON/CSV 내보내기를 제공합니다.",
        },
        {
            "version": "V4",
            "title": "24시간 중앙 운영 / 결제 / 캘린더",
            "status": "next",
            "summary": "Mac Pro 또는 클라우드 상시화, 입금 확인, 캘린더 연동은 다음 구현 게이트입니다.",
        },
    ]
    return {
        "service": "member-system",
        "version": SYSTEM_VERSION,
        "current_phase": "V3 운영 확인 + V4 기반 착수",
        "counts": {
            "members": counts.get("members", 0),
            "bookings": counts.get("bookings", 0),
            "sessions": counts.get("sessions", 0),
            "requested_bookings": requested,
            "active_bookings": active,
        },
        "accepting_applications": accepting,
        "db": {
            "exists": storage.get("db", {}).get("exists", False),
            "path": storage.get("db", {}).get("path", ""),
        },
        "backup": backup,
        "hermes": {
            "configured": hermes.get("configured", False),
            "global_enabled": hermes.get("global_enabled", False),
            "application_enabled": hermes.get("application_enabled", False),
            "booking_enabled": hermes.get("booking_enabled", False),
            "active_application": hermes.get("active_application", False),
            "active_booking": hermes.get("active_booking", False),
            "mode": hermes.get("mode", "not_configured"),
            "application_mode": hermes.get("application_mode", "not_configured"),
            "booking_mode": hermes.get("booking_mode", "not_configured"),
        },
        "stages": stages,
        "next_gates": [
            "운영 DB를 Mac Pro/클라우드 중 어디에 둘지 결정",
            "입금 확인을 수동 체크로 둘지, 계좌/PG 연동으로 갈지 결정",
            "Google Calendar 연동 승인",
            "외부 공개 도메인과 관리자 접근 정책 확정",
        ],
    }

# ── 스케줄 작업 ──────────────────────────────────────

def job_cleanup():
    """매일 자정: 만료 코드 정리 + 잠금 해제"""
    cleaned = cleanup_expired_codes()
    released = release_expired_locks()
    log.info(f"[cleanup] 만료코드 {cleaned['cleaned']}건 / 잠금해제 {released['released']}건")
    notify_cleanup_result(cleaned["cleaned"], released["released"])


def job_expiry_warning():
    """매일 10:00: 7일 내 만료 예정 경고"""
    expiring = get_expiring_soon(days=7)
    log.info(f"[expiry-warning] 만료 예정 {len(expiring)}건")
    notify_expiring_codes(expiring)


def job_unlock_check():
    """1시간마다: 시간 지난 잠금 해제"""
    result = release_expired_locks()
    if result["released"] > 0:
        log.info(f"[unlock] 잠금 해제 {result['released']}건: {result['ids']}")


def job_weekly_report():
    """매주 월요일 09:00 KST: 주간 리포트"""
    stats = get_stats()
    expiring = get_expiring_soon(days=7)
    stats["expiring_7d"] = len(expiring)
    ok = send_weekly_report(stats)
    log.info(f"[weekly-report] 전송 {'성공' if ok else '실패'} | {stats}")


# ── DB 초기화 + 서버 수명주기 ────────────────────────

init_db()

scheduler = AsyncIOScheduler(timezone="Asia/Seoul")

# 매일 00:00 — 만료 코드 정리
scheduler.add_job(job_cleanup, CronTrigger(hour=0, minute=0), id="cleanup", replace_existing=True)
# 매일 10:00 — 만료 7일 전 경고
scheduler.add_job(job_expiry_warning, CronTrigger(hour=10, minute=0), id="expiry_warn", replace_existing=True)
# 1시간마다 — 잠금 해제 확인
scheduler.add_job(job_unlock_check, CronTrigger(minute=0), id="unlock_check", replace_existing=True)
# 매주 월요일 09:00 — 주간 리포트
scheduler.add_job(job_weekly_report, CronTrigger(day_of_week="mon", hour=9, minute=0), id="weekly_report", replace_existing=True)

ENABLE_API_DOCS = os.getenv("ENABLE_API_DOCS", "").lower() in {"1", "true", "yes", "on"}


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    log.info("스케줄러 시작 — cleanup(일00:00) / expiry_warn(일10:00) / unlock(매시) / weekly_report(월09:00)")
    # 서버 시작 직후 잠금 해제 1회 즉시 실행
    job_unlock_check()
    yield
    scheduler.shutdown()
    log.info("스케줄러 종료")


app = FastAPI(
    title="Member System",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs" if ENABLE_API_DOCS else None,
    redoc_url="/redoc" if ENABLE_API_DOCS else None,
    openapi_url="/openapi.json" if ENABLE_API_DOCS else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8100", "http://127.0.0.1:8100",
        "https://arsen-ai.com", "https://www.arsen-ai.com",
        "https://apply.arsen-ai.com",
    ],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.middleware("http")
async def no_cache_admin_preview(request: Request, call_next):
    response = await call_next(request)
    if request.url.path == "/frontend/admin.html":
        response.headers["Cache-Control"] = "no-store, max-age=0"
        response.headers["Pragma"] = "no-cache"
    return response

FRONTEND_DIR = Path.home() / "member-system" / "frontend"
app.mount("/frontend", StaticFiles(directory=str(FRONTEND_DIR)), name="frontend")
# member-system is the canonical online API owner for arsen-ai.com education edits.
# The legacy dashboard keeps this JSON path as the shared live store.
EDUCATION_DATA_PATH = Path.home() / "arsen-dashboard" / "data" / "education_resources.json"
PAYMENT_ACCOUNTS_PATH = Path.home() / "member-system" / "private" / "payment_accounts.json"
PREPARATION_GUIDE_PATH = Path.home() / "member-system" / "private" / "preparation_guide.json"
SITE_THEME_PATH = Path.home() / "member-system" / "private" / "site_theme.json"
LAUNCHER_MANIFEST_PATH = Path.home() / "arsen-dashboard" / "data" / "launcher_ops.json"
LAUNCHER_ARTIFACT_DIR = Path.home() / ".arsen-work-bus" / "artifacts" / "launcher"
DEFAULT_SITE_THEME_ID = "arsen-modern"
SITE_THEME_PROFILES = [
    {
        "id": "legacy",
        "name": "구버전 기본",
        "scope": "public-and-admin",
        "css_path": "assets/themes/legacy.css",
        "description": "각 페이지에 원래 들어 있던 기본 스타일을 우선 사용합니다.",
        "enabled": True,
    },
    {
        "id": "arsen-modern",
        "name": "ARSEN 모던",
        "scope": "public-and-admin",
        "css_path": "assets/themes/arsen-modern.css",
        "description": "현재 적용 중인 ARSEN 테마입니다. 공개 페이지는 라이트, 관리자 운영 화면은 다크 톤을 포함합니다.",
        "enabled": True,
    },
]


def _load_launcher_manifest() -> dict[str, Any]:
    try:
        data = json.loads(LAUNCHER_MANIFEST_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail="launcher_manifest_missing") from exc
    except json.JSONDecodeError as exc:
        raise HTTPException(status_code=500, detail=f"launcher_manifest_invalid: {exc}") from exc
    if not isinstance(data, dict):
        raise HTTPException(status_code=500, detail="launcher_manifest_must_be_object")
    return data


def _safe_launcher_artifact_name(artifact_name: str) -> bool:
    return bool(artifact_name) and artifact_name == Path(artifact_name).name and "/" not in artifact_name and "\\" not in artifact_name


def _launcher_public_base_url(request: Request) -> str:
    configured = os.getenv("ARSEN_LAUNCHER_ARTIFACT_BASE_URL", "").strip().rstrip("/")
    if configured.startswith("https://"):
        return configured
    forwarded_proto = request.headers.get("x-forwarded-proto", request.url.scheme)
    proto = forwarded_proto.split(",")[0].strip().lower()
    if proto != "https":
        return ""
    forwarded_host = request.headers.get("x-forwarded-host") or request.headers.get("host") or request.url.netloc
    host = forwarded_host.split(",")[0].strip()
    return f"https://{host}"


def _public_launcher_release(raw_launcher: Any, request: Request) -> dict[str, Any]:
    launcher = dict(raw_launcher) if isinstance(raw_launcher, dict) else {}
    artifact_name = str(launcher.get("artifact_name") or "").strip()
    launcher["artifact_available"] = False
    if not _safe_launcher_artifact_name(artifact_name):
        launcher["artifact_download_url"] = ""
        return launcher

    artifact_endpoint = f"/api/daf/launcher/artifacts/{artifact_name}"
    artifact_path = LAUNCHER_ARTIFACT_DIR / artifact_name
    launcher["artifact_endpoint"] = artifact_endpoint
    if artifact_path.is_file():
        launcher["artifact_available"] = True
        launcher["size_bytes"] = artifact_path.stat().st_size

    download_url = str(launcher.get("artifact_download_url") or "").strip()
    if not download_url.startswith("https://"):
        base_url = _launcher_public_base_url(request)
        launcher["artifact_download_url"] = f"{base_url}{artifact_endpoint}" if base_url and artifact_path.is_file() else ""
        launcher["artifact_url"] = launcher["artifact_download_url"]
    return launcher


def _public_launcher_programs(raw_programs: Any) -> list[dict[str, Any]]:
    if not isinstance(raw_programs, list):
        return []
    return [
        dict(program)
        for program in raw_programs
        if isinstance(program, dict)
        and program.get("expose_to_customer") is True
        and program.get("internal_only") is not True
    ]


def _public_launcher_tiers(raw_tiers: Any) -> list[dict[str, Any]]:
    if not isinstance(raw_tiers, list):
        return []
    return [
        dict(tier)
        for tier in raw_tiers
        if isinstance(tier, dict) and tier.get("internal_only") is not True
    ]


def _public_launcher_notices(raw_notices: Any, *, audience: str | None = None, level: str | None = None) -> list[dict[str, Any]]:
    if not isinstance(raw_notices, list):
        return []
    filtered: list[dict[str, Any]] = []
    for notice in raw_notices:
        if not isinstance(notice, dict):
            continue
        if level and notice.get("level") != level:
            continue
        if audience == "launcher" and notice.get("show_in_launcher") is False:
            continue
        if audience == "website" and notice.get("show_in_website") is False:
            continue
        filtered.append(dict(notice))
    return sorted(
        filtered,
        key=lambda item: (not item.get("pinned", False), str(item.get("published_at") or "")),
    )


def _public_launcher_manifest(request: Request) -> dict[str, Any]:
    data = dict(_load_launcher_manifest())
    data["launcher"] = _public_launcher_release(data.get("launcher", {}), request)
    data["programs"] = _public_launcher_programs(data.get("programs", []))
    data["tiers"] = _public_launcher_tiers(data.get("tiers", []))
    data["notices"] = _public_launcher_notices(data.get("notices", []), audience="launcher")
    strategy = dict(data.get("product_strategy") or {})
    tracks = strategy.get("tracks")
    if isinstance(tracks, list):
        strategy["tracks"] = [
            dict(track)
            for track in tracks
            if isinstance(track, dict)
            and track.get("expose_to_customer") is True
            and track.get("internal_only") is not True
        ]
    data["product_strategy"] = strategy
    data["served_at"] = datetime.now(timezone.utc).isoformat()
    data["source"] = "member-system-public-launcher-proxy"
    return data


def _admin_launcher_status(request: Request) -> dict[str, Any]:
    manifest = _public_launcher_manifest(request)
    release = manifest.get("launcher") or {}
    programs = manifest.get("programs") if isinstance(manifest.get("programs"), list) else []
    notices = manifest.get("notices") if isinstance(manifest.get("notices"), list) else []
    customer_programs = [
        program for program in programs
        if isinstance(program, dict)
        and program.get("expose_to_customer") is True
        and program.get("internal_only") is not True
    ]
    pinned_notices = [notice for notice in notices if isinstance(notice, dict) and notice.get("pinned")]
    warnings: list[str] = []
    if not release.get("artifact_available"):
        warnings.append("launcher_artifact_unavailable")
    if not str(release.get("artifact_download_url") or "").startswith("https://"):
        warnings.append("launcher_artifact_url_not_https")
    if not release.get("sha256"):
        warnings.append("launcher_sha256_missing")
    if not notices:
        warnings.append("launcher_notices_empty")
    return {
        "service": "arsen-content-launcher",
        "source": "member-system-fastapi-launcher-proxy",
        "managed_by": "launcher_ops_json_contract",
        "editable": False,
        "updated_at": manifest.get("updated_at"),
        "served_at": datetime.now(timezone.utc).isoformat(),
        "endpoints": {
            "manifest": "/api/daf/manifest",
            "programs": "/api/daf/programs",
            "notices": "/api/daf/notices",
            "release": "/api/launcher/release",
            "artifact": release.get("artifact_endpoint") or f"/api/daf/launcher/artifacts/{release.get('artifact_name', '')}",
        },
        "release": release,
        "metrics": {
            "programs_total": len(programs),
            "customer_programs": len(customer_programs),
            "notices_total": len(notices),
            "pinned_notices": len(pinned_notices),
            "release_notes": len(release.get("release_notes") or []),
        },
        "checks": {
            "artifact_available": bool(release.get("artifact_available")),
            "artifact_url_https": str(release.get("artifact_download_url") or "").startswith("https://"),
            "sha256_present": bool(release.get("sha256")),
            "notice_panel_enabled": bool((release.get("update_policy") or {}).get("show_notice_panel_on_start")),
            "release_notes_enabled": bool((release.get("update_policy") or {}).get("show_release_notes_on_start")),
            "customer_programs_only": len(customer_programs) == len(programs),
        },
        "warnings": warnings,
        "programs": programs,
        "notices": notices,
    }

DEFAULT_PREPARATION_GUIDE = """[강의 준비물 안내]
입금 확인되신 분들께 공통 안내드립니다.

1. 노트북과 충전기
- 가능하면 개인 노트북을 가져와 주세요.
- Chrome 최신 버전 설치, 운영체제 업데이트/재부팅, 여유 저장공간 10GB 이상을 권장합니다.
- 사양 확인 방법:
  Mac: 왼쪽 상단 Apple 메뉴 → 이 Mac에 관하여 → 칩/메모리 확인
  Windows: 설정 → 시스템 → 정보 → 프로세서/RAM/Windows 사양 확인
- 권장 사양은 RAM 8GB 이상입니다. 오래된 노트북도 웹 실습은 가능하지만 속도가 느릴 수 있습니다.

2. AI 계정과 구독 준비
- ChatGPT, Claude, Gemini 중 이미 쓰는 계정은 수업 전 로그인까지 확인해 주세요.
- 아무것도 없다면 ChatGPT Plus 또는 Claude Pro 중 하나만 먼저 준비해도 됩니다.
- 여유가 있으면 ChatGPT Plus + Claude Pro 조합을 추천합니다.
- Gemini는 Google 계정으로 무료 시작 후 필요할 때 Google AI Pro를 검토해도 됩니다.
- 결제, 본인인증, 2단계 인증은 수업 중 시간이 오래 걸릴 수 있어 미리 처리하는 편이 좋습니다.

3. 구현하고 싶은 주제
- 주제: 어떤 업무, 콘텐츠, 반복작업을 줄이고 싶은지
- 현재 방식: 지금 어떻게 처리하고 어디서 시간이 걸리는지
- 목표 결과물: 문서, 대시보드, 자동 알림, 예약폼, 블로그 초안, 영상 기획안 등
- 입력 자료: 참고 문서, 예시 링크, 자주 쓰는 문구나 양식
- 완료 기준: 수업 당일 어디까지 만들면 성공인지
- 희망 일정: 언제까지 실제로 써야 하는지

4. 자료와 계정
- 자주 쓰는 이메일/Google 계정 로그인 확인
- 필요한 파일은 Google Drive, USB, 바탕화면 중 한 곳에 모아두기
- 회사/개인정보/API키/비밀번호 원문은 공유하지 말고 테스트용 더미 데이터 준비

5. 있으면 좋은 것
- 스마트폰 핫스팟, 마우스, 메모 앱, 충전 어댑터
- 작업 예시 화면 캡처 2~3장
- 자주 반복하는 메시지, 보고서, 엑셀, 블로그/영상 양식"""

# ── 관리자 인증 ──────────────────────────────────────

ADMIN_API_KEY = os.getenv("ADMIN_API_KEY", "")
ADMIN_ENV_PATH = Path.home() / "member-system" / ".env"
ADMIN_PASSWORD_MIN_LENGTH = 8
ADMIN_PASSWORD_TOOL_FILES = [
    ("set_admin_password.py", Path.home() / "member-system" / "scripts" / "set_admin_password.py"),
    ("admin_access_runbook_ko.md", Path.home() / "member-system" / "docs" / "admin_access_runbook_ko.md"),
]
ADMIN_TOOL_BACKUP_TARGETS = [
    {
        "name": "local",
        "label": "Mac Air local",
        "root": Path.home() / "member-system",
        "path": Path.home() / "member-system" / "backups" / "admin-tools",
    },
    {
        "name": "icloud",
        "label": "iCloud Drive",
        "root": Path.home() / "Library" / "Mobile Documents" / "com~apple~CloudDocs",
        "path": Path.home() / "Library" / "Mobile Documents" / "com~apple~CloudDocs" / "Arsen" / "member-system" / "admin-tools",
    },
    {
        "name": "onedrive",
        "label": "OneDrive",
        "root": Path.home() / "OneDrive",
        "path": Path.home() / "OneDrive" / "Arsen" / "member-system" / "admin-tools",
    },
]
MEMBER_ADMIN_LOCAL_OPEN = os.getenv("MEMBER_ADMIN_LOCAL_OPEN", "0") == "1"
LOCAL_ADMIN_OPEN_FLAG = Path.home() / "member-system" / ".local_admin_open"
LOCAL_ADMIN_HOSTS = {"127.0.0.1", "::1", "localhost"}
LOCAL_ADMIN_PROXY_HEADERS = {
    "cf-connecting-ip",
    "cf-ipcountry",
    "cf-ray",
    "cf-visitor",
    "cdn-loop",
    "x-forwarded-for",
    "x-forwarded-host",
    "x-forwarded-proto",
    "x-real-ip",
}


def is_local_admin_preview(request: Request) -> bool:
    if not (MEMBER_ADMIN_LOCAL_OPEN or LOCAL_ADMIN_OPEN_FLAG.exists()):
        return False
    header_keys = {str(key).lower() for key in (getattr(request, "headers", {}) or {}).keys()}
    if header_keys.intersection(LOCAL_ADMIN_PROXY_HEADERS) or any(key.startswith("cf-") for key in header_keys):
        return False
    client_host = request.client.host if request.client else ""
    request_host = (request.url.hostname or "").lower()
    return client_host in LOCAL_ADMIN_HOSTS and request_host in LOCAL_ADMIN_HOSTS


def require_admin(request: Request):
    if is_local_admin_preview(request):
        return
    require_admin_key(request)


def require_admin_key(request: Request):
    key = request.headers.get("X-Admin-Key", "")
    if not ADMIN_API_KEY:
        log.error("ADMIN_API_KEY 미설정 — 관리자 엔드포인트 차단")
        raise HTTPException(status_code=503, detail="관리자 인증 설정이 필요합니다.")
    if not key or key != ADMIN_API_KEY:
        raise HTTPException(status_code=401, detail="관리자 비밀번호가 필요합니다.")


def _client_ip(request: Request) -> str | None:
    return request.client.host if request.client else None


def _user_agent(request: Request) -> str | None:
    return request.headers.get("user-agent")


def _bearer_token(request: Request) -> str:
    authorization = request.headers.get("authorization", "")
    if not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="라이선스 인증 토큰이 필요합니다.")
    token = authorization.split(" ", 1)[1].strip()
    if not token:
        raise HTTPException(status_code=401, detail="라이선스 인증 토큰이 비어 있습니다.")
    return token


# ── 모델 ────────────────────────────────────────────

class ApplyRequest(BaseModel):
    name: str
    email: str
    phone: str
    gender: str
    age: int
    job: str
    referral_source: str
    reason: str
    ai_level: str
    plan_type: str
    # 선택 항목
    ai_tools: Optional[List[str]] = None
    ai_subscription: Optional[str] = None
    ai_weekly_hours: Optional[str] = None
    ai_use_cases: Optional[List[str]] = None
    group_goals: Optional[List[str]] = None
    short_term_goal: Optional[str] = None
    participation_type: Optional[str] = None
    preferred_schedule: Optional[str] = None
    available_time_slots: Optional[List[str]] = None
    region: Optional[str] = None
    main_device: Optional[str] = None
    can_code: Optional[bool] = None
    can_present: Optional[bool] = None
    skills: Optional[str] = None
    contribution: Optional[str] = None
    session_id: Optional[str] = None
    desired_outcome: Optional[str] = None
    preparedness: Optional[str] = None
    # 동의
    consent_personal: bool
    consent_marketing: Optional[bool] = False


class ConsultationRequest(BaseModel):
    source: Optional[str] = "public_site"
    topic: Optional[str] = "상담"
    consult_type: Optional[str] = None
    subject: Optional[str] = None
    contact: Optional[str] = None
    lead_contact: Optional[str] = None
    contact_type: Optional[str] = None
    name: Optional[str] = None
    buyer_name: Optional[str] = None
    email: Optional[str] = None
    buyer_email: Optional[str] = None
    phone: Optional[str] = None
    buyer_phone: Optional[str] = None
    product_interest: Optional[str] = None
    product: Optional[str] = None
    message: Optional[str] = None
    customer_message: Optional[str] = None
    memo: Optional[str] = None
    page_url: Optional[str] = None
    referrer: Optional[str] = None
    consent_privacy: Optional[bool] = True


class RejectRequest(BaseModel):
    reason: str


class RunJobRequest(BaseModel):
    job_id: str  # cleanup | expiry_warn | unlock_check | weekly_report


class AdminPasswordRequest(BaseModel):
    new_password: str


class VerifyCodeRequest(BaseModel):
    code: str
    member_id: str


class PublicVerifyCodeRequest(BaseModel):
    phone: str
    code: str


class PublicBookingRequest(BaseModel):
    member_id: str
    code: Optional[str] = None
    session_id: str
    desired_outcome: Optional[str] = None
    preparedness: Optional[str] = None


class KakaoLinkRequest(BaseModel):
    phone: str
    code: str


class SessionRequest(BaseModel):
    title: str = "AI 결과물 제작 초급 4주반"
    description: Optional[str] = None
    program_type: str = "ai_basic_setup"
    audience_level: str = "all"
    starts_at: str
    ends_at: str
    timezone: str = "Asia/Seoul"
    capacity_min: int = 4
    capacity_max: int = 8
    price_krw: int = 100000
    location: str
    materials: Optional[str] = None
    status: str = "open"
    payment_guide: Optional[str] = None


class SessionUpdateRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    program_type: Optional[str] = None
    audience_level: Optional[str] = None
    starts_at: Optional[str] = None
    ends_at: Optional[str] = None
    timezone: Optional[str] = None
    capacity_min: Optional[int] = None
    capacity_max: Optional[int] = None
    price_krw: Optional[int] = None
    location: Optional[str] = None
    materials: Optional[str] = None
    status: Optional[str] = None
    payment_guide: Optional[str] = None


class BookingStateRequest(BaseModel):
    status: Optional[str] = None
    payment_status: Optional[str] = None
    payment_note: Optional[str] = None


class BookingMoveRequest(BaseModel):
    session_id: str
    note: Optional[str] = None


class PaymentGuideRequest(BaseModel):
    payment_note: Optional[str] = None
    payment_account_id: Optional[str] = None


class ManualBookingRequest(BaseModel):
    member_id: Optional[str] = None
    applicant_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    desired_outcome: Optional[str] = None
    payment_note: Optional[str] = None
    payment_amount_krw: Optional[int] = None


class PaymentAccountItem(BaseModel):
    id: Optional[str] = None
    label: Optional[str] = None
    bank: Optional[str] = None
    number: Optional[str] = None
    holder: Optional[str] = None
    memo: Optional[str] = None


class PaymentAccountsRequest(BaseModel):
    accounts: List[PaymentAccountItem] = []
    active_id: Optional[str] = None


class PreparationGuideRequest(BaseModel):
    message: str


class SiteThemeRequest(BaseModel):
    active_theme_id: str


class ReviewInstructorRequest(BaseModel):
    name: str
    role: Optional[str] = None
    bio: Optional[str] = None
    specialties: Optional[List[str]] = None
    status: str = "active"
    sort_order: int = 0


class ReviewInstructorUpdateRequest(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    bio: Optional[str] = None
    specialties: Optional[List[str]] = None
    status: Optional[str] = None
    sort_order: Optional[int] = None


class ReviewEntryRequest(BaseModel):
    instructor_id: Optional[str] = None
    class_title: str
    class_date: Optional[str] = None
    title: Optional[str] = None
    summary: Optional[str] = None
    body: Optional[str] = None
    tags: Optional[List[str]] = None
    image_urls: Optional[List[str]] = None
    status: str = "draft"
    source: str = "manual"
    privacy_checked: bool = False
    featured: bool = False


class ReviewEntryUpdateRequest(BaseModel):
    instructor_id: Optional[str] = None
    class_title: Optional[str] = None
    class_date: Optional[str] = None
    title: Optional[str] = None
    summary: Optional[str] = None
    body: Optional[str] = None
    tags: Optional[List[str]] = None
    image_urls: Optional[List[str]] = None
    status: Optional[str] = None
    source: Optional[str] = None
    privacy_checked: Optional[bool] = None
    featured: Optional[bool] = None


class ReviewInviteRequest(BaseModel):
    label: Optional[str] = None
    instructor_id: Optional[str] = None
    class_title: Optional[str] = None
    class_date: Optional[str] = None
    max_submissions: int = 0
    expires_at: Optional[str] = None
    status: str = "active"


class ReviewSubmissionRequest(BaseModel):
    display_name: str
    instructor_id: Optional[str] = None
    class_title: str
    class_date: Optional[str] = None
    rating: int = 5
    title: Optional[str] = None
    summary: Optional[str] = None
    body: Optional[str] = None
    tags: Optional[List[str]] = None
    image_urls: Optional[List[str]] = None
    consent_public_review: bool = False


class SeedSessionsRequest(BaseModel):
    weeks: int = 4


class CodeDeliveryLogRequest(BaseModel):
    channel: str  # telegram / kakao / sms / direct / email
    note: Optional[str] = None


class MemberEraseRequest(BaseModel):
    cancel_bookings: bool = True


class MemberUpdateRequest(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    job: Optional[str] = None
    referral_source: Optional[str] = None
    reason: Optional[str] = None
    ai_level: Optional[str] = None
    plan_type: Optional[str] = None
    ai_tools: Optional[List[str] | str] = None
    ai_subscription: Optional[str] = None
    ai_weekly_hours: Optional[str] = None
    ai_use_cases: Optional[List[str] | str] = None
    group_goals: Optional[List[str] | str] = None
    short_term_goal: Optional[str] = None
    participation_type: Optional[str] = None
    preferred_schedule: Optional[str] = None
    available_time_slots: Optional[List[str] | str] = None
    region: Optional[str] = None
    main_device: Optional[str] = None
    can_code: Optional[bool] = None
    can_present: Optional[bool] = None
    skills: Optional[str] = None
    contribution: Optional[str] = None
    participation_grade: Optional[str] = None
    consent_marketing: Optional[bool] = None
    status: Optional[str] = None
    rejection_reason: Optional[str] = None


class ContactRegisteredRequest(BaseModel):
    registered: bool = True
    note: Optional[str] = None


class MemberKickRequest(BaseModel):
    reason: Optional[str] = None


class LicenseActivateRequest(BaseModel):
    license_key: str
    hwid: str
    app_version: Optional[str] = None
    platform: str = "windows"
    device_name: Optional[str] = None


class LicenseVerifyRequest(BaseModel):
    hwid: str
    app_version: Optional[str] = None
    platform: str = "windows"


class AdminLicenseCreateRequest(BaseModel):
    member_id: Optional[str] = None
    plan_code: str = "basic"
    expires_at: Optional[str] = None
    max_devices: int = 1
    app_min_version: Optional[str] = None
    note: Optional[str] = None


class AdminLicenseRevokeRequest(BaseModel):
    reason: str = "manual"


class AdminLicenseResetDeviceRequest(BaseModel):
    reason: str = "manual"


class AdminLicenseExtendRequest(BaseModel):
    expires_at: str


class YoonbotOrderCreateRequest(BaseModel):
    buyer_name: str
    buyer_email: Optional[str] = None
    buyer_phone: Optional[str] = None
    product_code: str = "yoonbot"
    plan_code: str = "monthly"
    customer_message: Optional[str] = None
    consent_privacy: bool = False
    consent_terms: bool = False
    discount_code: Optional[str] = None


class AdminYoonbotOrderPaidRequest(BaseModel):
    payment_provider: str = "manual_bank_transfer"
    payment_ref: Optional[str] = None
    note: Optional[str] = None


class AdminYoonbotOrderNoteRequest(BaseModel):
    note: Optional[str] = None


class TossPaymentConfirmRequest(BaseModel):
    payment_key: str
    order_id: str   # toss_order_id (yb-... format)
    amount: int


class AdminYoonbotDiscountCreateRequest(BaseModel):
    code: str
    label: Optional[str] = None
    plan_code: Optional[str] = None
    discount_type: str = "percent"
    discount_value: int
    max_redemptions: Optional[int] = 1
    starts_at: Optional[str] = None
    expires_at: Optional[str] = None
    note: Optional[str] = None


# ── 유틸 ────────────────────────────────────────────

def _update_env_value(path: Path, key: str, value: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
    updated = False
    output: list[str] = []
    for line in lines:
        if line.startswith(f"{key}="):
            output.append(f"{key}={value}")
            updated = True
        else:
            output.append(line)
    if not updated:
        if output and output[-1].strip():
            output.append("")
        output.append(f"{key}={value}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(output) + "\n", encoding="utf-8")
    path.chmod(0o600)


def _admin_env_permission_status() -> dict:
    if not ADMIN_ENV_PATH.exists():
        return {"exists": False, "mode": None, "private": False}
    mode = ADMIN_ENV_PATH.stat().st_mode & 0o777
    return {
        "exists": True,
        "mode": oct(mode),
        "private": (mode & 0o077) == 0,
    }


def _latest_admin_tool_backup(path: Path) -> dict | None:
    if not path.exists():
        return None
    candidates = [item for item in path.iterdir() if item.is_file()]
    if not candidates:
        return None
    latest = max(candidates, key=lambda item: item.stat().st_mtime)
    stat = latest.stat()
    return {
        "file": latest.name,
        "path": str(latest),
        "size_bytes": stat.st_size,
        "modified_at": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
    }


def _admin_tool_backup_status() -> list[dict]:
    rows = []
    for target in ADMIN_TOOL_BACKUP_TARGETS:
        root = target["root"]
        path = target["path"]
        rows.append({
            "name": target["name"],
            "label": target["label"],
            "path": str(path),
            "available": root.exists(),
            "latest": _latest_admin_tool_backup(path),
        })
    return rows


def build_admin_security_status() -> dict:
    env_status = _admin_env_permission_status()
    tool_sources = [
        {
            "name": name,
            "path": str(path),
            "exists": path.exists(),
            "size_bytes": path.stat().st_size if path.exists() else 0,
        }
        for name, path in ADMIN_PASSWORD_TOOL_FILES
    ]
    return {
        "admin_password": {
            "configured": bool(ADMIN_API_KEY),
            "length_ok": len(ADMIN_API_KEY) >= ADMIN_PASSWORD_MIN_LENGTH,
            "min_length": ADMIN_PASSWORD_MIN_LENGTH,
            "storage": str(ADMIN_ENV_PATH),
            "env_private": env_status["private"],
            "env_mode": env_status["mode"],
        },
        "password_tool": {
            "sources": tool_sources,
            "backup_targets": _admin_tool_backup_status(),
        },
    }


def backup_admin_password_tools() -> dict:
    sources = [(name, path) for name, path in ADMIN_PASSWORD_TOOL_FILES if path.exists()]
    results = []
    for target in ADMIN_TOOL_BACKUP_TARGETS:
        path = target["path"]
        result = {
            "name": target["name"],
            "label": target["label"],
            "path": str(path),
            "status": "skipped",
            "copied": 0,
        }
        if not target["root"].exists():
            result["detail"] = "target_root_not_available"
            results.append(result)
            continue
        try:
            path.mkdir(parents=True, exist_ok=True)
            for source_name, source_path in sources:
                shutil.copy2(source_path, path / source_name)
            result.update({
                "status": "ok" if sources else "skipped",
                "detail": "tool_files_copied" if sources else "no_tool_files",
                "copied": len(sources),
            })
        except Exception as exc:
            result.update({"status": "failed", "detail": exc.__class__.__name__})
        results.append(result)
    return {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "ok_count": sum(1 for item in results if item["status"] == "ok"),
        "failed_count": sum(1 for item in results if item["status"] == "failed"),
        "targets": results,
    }


def _clean_text(value: str | None, limit: int = 200) -> str:
    return str(value or "").strip()[:limit]


def _telegram_safe(value: object) -> str:
    return html_escape(str(value or "").strip()) if value else "-"


def _normalize_payment_account(raw: dict) -> dict | None:
    account_id = _clean_text(raw.get("id"), 80) or f"acct-{uuid.uuid4().hex[:12]}"
    account = {
        "id": account_id,
        "label": _clean_text(raw.get("label"), 80),
        "bank": _clean_text(raw.get("bank"), 80),
        "number": _clean_text(raw.get("number"), 80),
        "holder": _clean_text(raw.get("holder"), 80),
        "memo": _clean_text(raw.get("memo"), 200),
    }
    if not any(account[key] for key in ("label", "bank", "number", "holder", "memo")):
        return None
    if not account["label"]:
        account["label"] = "입금 계좌"
    return account


def _payment_accounts_payload(accounts: list[dict], active_id: str | None, updated_at: str | None = None) -> dict:
    ids = {item["id"] for item in accounts}
    active = active_id if active_id in ids else (accounts[0]["id"] if accounts else "")
    return {
        "updated_at": updated_at,
        "active_id": active,
        "accounts": accounts,
        "total": len(accounts),
    }


def _load_payment_accounts() -> dict:
    if not PAYMENT_ACCOUNTS_PATH.exists():
        return _payment_accounts_payload([], "")
    try:
        data = json.loads(PAYMENT_ACCOUNTS_PATH.read_text(encoding="utf-8"))
    except Exception:
        log.exception("입금 계좌 설정 파일을 읽지 못했습니다.")
        return _payment_accounts_payload([], "")
    accounts = []
    for item in data.get("accounts", [])[:20]:
        normalized = _normalize_payment_account(item if isinstance(item, dict) else {})
        if normalized:
            accounts.append(normalized)
    return _payment_accounts_payload(accounts, data.get("active_id"), data.get("updated_at"))


def _save_payment_accounts(accounts: list[dict], active_id: str | None) -> dict:
    payload = _payment_accounts_payload(accounts[:20], active_id, datetime.now(timezone.utc).isoformat())
    PAYMENT_ACCOUNTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    try:
        PAYMENT_ACCOUNTS_PATH.parent.chmod(0o700)
    except OSError:
        pass
    PAYMENT_ACCOUNTS_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    try:
        PAYMENT_ACCOUNTS_PATH.chmod(0o600)
    except OSError:
        pass
    return payload


def _selected_payment_account(account_id: str | None = None) -> dict | None:
    data = _load_payment_accounts()
    selected_id = account_id or data.get("active_id")
    for account in data.get("accounts", []):
        if account.get("id") == selected_id:
            return account
    return data.get("accounts", [None])[0] if data.get("accounts") else None


def _theme_profile(theme_id: str | None) -> dict | None:
    if not theme_id:
        return None
    for profile in SITE_THEME_PROFILES:
        if profile["id"] == theme_id and profile.get("enabled", True):
            return dict(profile)
    return None


def _theme_css_exists(profile: dict) -> bool:
    css_path = str(profile.get("css_path") or "")
    if not css_path or css_path.startswith("/") or ".." in Path(css_path).parts:
        return False
    return (FRONTEND_DIR / css_path).exists()


def _theme_payload(active_theme_id: str | None = None, updated_at: str | None = None) -> dict:
    active_id = active_theme_id if _theme_profile(active_theme_id) else DEFAULT_SITE_THEME_ID
    active = _theme_profile(active_id) or _theme_profile(DEFAULT_SITE_THEME_ID)
    themes = []
    for profile in SITE_THEME_PROFILES:
        item = dict(profile)
        item["available"] = _theme_css_exists(item)
        themes.append(item)
    return {
        "active_theme_id": active["id"] if active else DEFAULT_SITE_THEME_ID,
        "active_theme": active,
        "themes": themes,
        "updated_at": updated_at,
    }


def _load_site_theme() -> dict:
    if not SITE_THEME_PATH.exists():
        return _theme_payload(DEFAULT_SITE_THEME_ID)
    try:
        data = json.loads(SITE_THEME_PATH.read_text(encoding="utf-8"))
    except Exception:
        log.exception("사이트 테마 설정 파일을 읽지 못했습니다.")
        return _theme_payload(DEFAULT_SITE_THEME_ID)
    return _theme_payload(data.get("active_theme_id"), data.get("updated_at"))


def _save_site_theme(active_theme_id: str) -> dict:
    profile = _theme_profile(active_theme_id)
    if not profile:
        raise HTTPException(status_code=400, detail="등록되지 않은 테마입니다.")
    if not _theme_css_exists(profile):
        raise HTTPException(status_code=400, detail="테마 CSS 파일을 찾을 수 없습니다.")
    payload = {
        "active_theme_id": profile["id"],
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    SITE_THEME_PATH.parent.mkdir(parents=True, exist_ok=True)
    try:
        SITE_THEME_PATH.parent.chmod(0o700)
    except OSError:
        pass
    SITE_THEME_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    try:
        SITE_THEME_PATH.chmod(0o600)
    except OSError:
        pass
    return _theme_payload(payload["active_theme_id"], payload["updated_at"])


def _preparation_guide_payload(message: str | None = None, updated_at: str | None = None) -> dict:
    text = (message if message is not None else DEFAULT_PREPARATION_GUIDE).strip()
    return {
        "updated_at": updated_at,
        "message": text or DEFAULT_PREPARATION_GUIDE,
        "default_message": DEFAULT_PREPARATION_GUIDE,
    }


def _load_preparation_guide() -> dict:
    if not PREPARATION_GUIDE_PATH.exists():
        return _preparation_guide_payload()
    try:
        data = json.loads(PREPARATION_GUIDE_PATH.read_text(encoding="utf-8"))
    except Exception:
        log.exception("준비물 안내 설정 파일을 읽지 못했습니다.")
        return _preparation_guide_payload()
    return _preparation_guide_payload(data.get("message"), data.get("updated_at"))


def _save_preparation_guide(message: str) -> dict:
    text = _clean_text(message, 6000)
    if len(text) < 20:
        raise HTTPException(400, detail="준비물 안내 문구는 20자 이상 입력하세요.")
    payload = _preparation_guide_payload(text, datetime.now(timezone.utc).isoformat())
    PREPARATION_GUIDE_PATH.parent.mkdir(parents=True, exist_ok=True)
    try:
        PREPARATION_GUIDE_PATH.parent.chmod(0o700)
    except OSError:
        pass
    PREPARATION_GUIDE_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    try:
        PREPARATION_GUIDE_PATH.chmod(0o600)
    except OSError:
        pass
    return payload


def _admin_no_send_delivery(delivery_mode: str = "manual_copy") -> dict:
    # Admin booking flows prepare operator copy only; external sends need a separate approval gate.
    return {
        "delivery_mode": delivery_mode,
        "applicant_delivery": "not_sent",
        "operator_notification": "not_sent",
    }


def _grade_count(data: dict) -> str:
    """선택 항목 입력 개수 기반 등급 계산"""
    optional_fields = [
        "ai_tools", "ai_subscription", "ai_weekly_hours", "ai_use_cases",
        "group_goals", "short_term_goal", "participation_type", "preferred_schedule",
        "available_time_slots", "region", "main_device", "can_code", "can_present", "skills", "contribution",
        "session_id", "desired_outcome", "preparedness",
    ]
    count = 0
    for field in optional_fields:
        val = data.get(field)
        if val is None or val == "" or val == [] or val == "[]":
            continue
        # can_code / can_present: None이 아닌 경우만 카운트
        count += 1

    if count == 0:
        return "🌱 새싹"
    elif count <= 4:
        return "🔥 열정"
    elif count <= 9:
        return "⭐ 적극"
    elif count <= 13:
        return "💎 헌신"
    else:
        return "👑 마스터"


def _phone_candidates(phone: str) -> list[str]:
    raw = (phone or "").strip()
    digits = "".join(ch for ch in raw if ch.isdigit())
    candidates = [raw]
    if len(digits) == 11:
        candidates.append(f"{digits[:3]}-{digits[3:7]}-{digits[7:]}")
        candidates.append(digits)
    unique = []
    for item in candidates:
        if item and item not in unique:
            unique.append(item)
    return unique


def _normalize_phone_for_storage(phone: str) -> str:
    raw = (phone or "").strip()
    digits = "".join(ch for ch in raw if ch.isdigit())
    if len(digits) == 11:
        return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"
    return raw


def _get_member_by_phone(phone: str) -> dict | None:
    for candidate in _phone_candidates(phone):
        member = get_latest_member_by_phone_hash(hash_phone(candidate))
        if member:
            return member
    return None


def _create_manual_member(name: str, phone: str, email: str | None, note: str | None) -> str:
    normalized_phone = _normalize_phone_for_storage(phone)
    manual_email = (email or "").strip() or f"manual-{uuid.uuid4().hex[:12]}@arsen.local"
    now = datetime.now(timezone.utc).isoformat()
    base = {
        "name": name.strip(),
        "email": manual_email,
        "phone": normalized_phone,
        "gender": "미기록",
        "age": 0,
        "job": "운영자 수동 등록",
        "referral_source": "운영자 수동 추가",
        "reason": note or "입금 확인 후 일정에서 수동 추가",
        "ai_level": "미기록",
        "plan_type": "full",
        "ai_tools": [],
        "ai_subscription": "",
        "ai_weekly_hours": "",
        "ai_use_cases": [],
        "group_goals": [],
        "short_term_goal": note or "",
        "participation_type": "manual_confirmed",
        "preferred_schedule": "",
        "available_time_slots": [],
        "region": "",
        "main_device": "",
        "can_code": False,
        "can_present": False,
        "skills": "",
        "contribution": "",
        "participation_grade": "🌱 새싹",
        "consent_personal": True,
        "consent_marketing": False,
        "consent_at": now,
        "consent_version": "manual-admin-v1",
    }
    encrypted = encrypt_data(base)
    member_id = create_member({**base, **encrypted})
    update_status(member_id, "approved")
    return member_id


def _safe_member_profile(member: dict) -> dict:
    return {
        "id": member["id"],
        "name": member["name"],
        "phone_masked": member.get("phone_masked"),
        "status": member.get("status"),
        "plan_type": member.get("plan_type"),
        "participation_grade": member.get("participation_grade"),
        "paid_class_count": member_paid_class_count(member["id"]),
        "approved_at": member.get("approved_at"),
        "code_expires_at": None,
        "code_expiry_label": "기한 없음",
    }


KAKAO_AUTHORIZE_URL = "https://kauth.kakao.com/oauth/authorize"
KAKAO_TOKEN_URL = "https://kauth.kakao.com/oauth/token"
KAKAO_USER_ME_URL = "https://kapi.kakao.com/v2/user/me"
KAKAO_STATE_COOKIE = "arsen_kakao_state"
KAKAO_SESSION_COOKIE = "arsen_kakao_session"
KAKAO_SESSION_MAX_AGE = 60 * 60 * 24 * 30


def _b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")


def _b64url_decode(text: str) -> bytes:
    padding = "=" * (-len(text) % 4)
    return base64.urlsafe_b64decode(f"{text}{padding}".encode("ascii"))


def _kakao_session_secret() -> bytes:
    secret = (
        os.getenv("KAKAO_SESSION_SECRET")
        or os.getenv("ADMIN_KEY")
        or os.getenv("TELEGRAM_WEBHOOK_SECRET")
        or "arsen-local-kakao-session"
    )
    return secret.encode("utf-8")


def _pack_signed_cookie(payload: dict) -> str:
    body = _b64url_encode(json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
    signature = hmac.new(_kakao_session_secret(), body.encode("ascii"), hashlib.sha256).digest()
    return f"{body}.{_b64url_encode(signature)}"


def _unpack_signed_cookie(value: str | None) -> dict | None:
    if not value or "." not in value:
        return None
    body, signature = value.split(".", 1)
    expected = _b64url_encode(hmac.new(_kakao_session_secret(), body.encode("ascii"), hashlib.sha256).digest())
    if not hmac.compare_digest(signature, expected):
        return None
    try:
        payload = json.loads(_b64url_decode(body).decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return None
    return payload if isinstance(payload, dict) else None


def _safe_next_path(next_path: str | None) -> str:
    value = (next_path or "/frontend/member.html").strip()
    if not value.startswith("/") or value.startswith("//") or value.startswith("/auth/"):
        return "/frontend/member.html"
    return value


def _append_kakao_status(next_path: str, status: str) -> str:
    separator = "&" if "?" in next_path else "?"
    return f"{next_path}{separator}kakao={urllib.parse.quote(status)}"


def _set_signed_cookie(response: Response, request: Request, name: str, payload: dict, max_age: int):
    response.set_cookie(
        name,
        _pack_signed_cookie(payload),
        max_age=max_age,
        httponly=True,
        secure=request.url.scheme == "https",
        samesite="lax",
        path="/",
    )


def _read_kakao_session(request: Request) -> dict | None:
    return _unpack_signed_cookie(request.cookies.get(KAKAO_SESSION_COOKIE))


def _delete_kakao_cookie(response: Response, name: str):
    response.delete_cookie(name, path="/")


def _kakao_redirect_uri(request: Request) -> str:
    return os.getenv("KAKAO_REDIRECT_URI") or str(request.url_for("kakao_callback"))


def _kakao_profile_payload(user: dict) -> dict:
    account = user.get("kakao_account") if isinstance(user.get("kakao_account"), dict) else {}
    properties = user.get("properties") if isinstance(user.get("properties"), dict) else {}
    profile = account.get("profile") if isinstance(account.get("profile"), dict) else {}
    return {
        "id": str(user.get("id") or ""),
        "nickname": properties.get("nickname") or profile.get("nickname") or "",
        "email": account.get("email") or "",
        "phone_number": account.get("phone_number") or "",
        "connected_at": user.get("connected_at") or "",
    }


def _kakao_public_payload(session: dict, member: dict | None = None) -> dict:
    profile = session.get("profile") if isinstance(session.get("profile"), dict) else {}
    return {
        "connected": True,
        "linked": bool(session.get("member_id") and member),
        "nickname": profile.get("nickname") or "",
    }


def _code_delivery_message(member: dict, code: str) -> str:
    name = member.get("name") or "신청자"
    return "\n".join(
        [
            f"[ARSEN AI] {name}님 강의 신청 확인 코드입니다.",
            f"코드: {code}",
            "예약자 확인: https://apply.arsen-ai.com/frontend/status.html",
            "정보 공유방: https://open.kakao.com/o/gm9tRoJh",
            "문의: https://open.kakao.com/o/s88zv6pf",
        ]
    )


def _telegram_callback_result(data: str, client_ip: str | None = None) -> str:
    parts = (data or "").split(":")
    if len(parts) != 3 or parts[0] != "arsen":
        return "지원하지 않는 버튼입니다."

    action, target_id = parts[1], parts[2]
    if action == "approve":
        member = get_member(target_id)
        if not member:
            return "신청자를 찾을 수 없습니다."
        if member.get("status") in {"blacklist", "erased", "rejected"}:
            return f"현재 상태가 {member.get('status')}라 코드 발급을 중단했습니다."
        if member.get("status") != "approved":
            update_status(target_id, "approved")
            member = get_member(target_id)
        current = get_current_code(target_id)
        code = current["code"] if current.get("ok") else generate_code(target_id)
        member = get_member(target_id)
        delivery_message = _code_delivery_message(member, code)
        send_admin_message(
            "\n".join(
                [
                    "<b>ARSEN 코드 발급 완료</b>",
                    f"이름: {_telegram_safe(member.get('name'))}",
                    f"회원ID: <code>{_telegram_safe(target_id)}</code>",
                    f"코드: <code>{_telegram_safe(code)}</code>",
                    "",
                    "안내문자/카톡 복사용:",
                    _telegram_safe(delivery_message),
                ]
            ),
            enabled=True,
        )
        log_action(target_id, "telegram_approve_code_issued", "button=approve", client_ip)
        return "승인 및 코드 발급 완료"

    if action == "payguide":
        payment_account = _selected_payment_account()
        updated = send_payment_guide_state(target_id, payment_account=payment_account)
        if not updated:
            return "예약 신청을 찾을 수 없습니다."
        guide = updated.get("payment_note") or default_payment_guide(None, updated, payment_account)
        send_admin_message(
            "\n".join(
                [
                    "<b>ARSEN 입금 안내 문구</b>",
                    f"예약ID: <code>{_telegram_safe(target_id)}</code>",
                    "신청자에게 자동 문자/카톡 전송은 하지 않았습니다. 아래 문구를 복사해 전달하세요.",
                    "",
                    _telegram_safe(guide),
                ]
            ),
            enabled=True,
        )
        log_action(target_id, "telegram_payment_guide_sent", "manual_copy", client_ip)
        return "입금 안내 문구 생성 완료"

    if action == "confirm":
        ok, message, booking = confirm_payment_state(target_id, "텔레그램 버튼 입금 확인")
        if not ok:
            return message
        guide = default_location_guide(booking)
        send_admin_message(
            "\n".join(
                [
                    "<b>ARSEN 입금 확인 + 장소 안내</b>",
                    f"예약ID: <code>{_telegram_safe(target_id)}</code>",
                    "신청자에게 자동 문자/카톡 전송은 하지 않았습니다. 아래 장소 안내를 복사해 전달하세요.",
                    "",
                    _telegram_safe(guide),
                ]
            ),
            enabled=True,
        )
        log_action(target_id, "telegram_payment_confirmed", "manual_confirm", client_ip)
        return message

    if action == "location":
        booking = get_booking(target_id)
        if not booking:
            return "예약 신청을 찾을 수 없습니다."
        guide = default_location_guide(booking)
        send_admin_message(
            "\n".join(
                [
                    "<b>ARSEN 장소 안내 문구</b>",
                    f"예약ID: <code>{_telegram_safe(target_id)}</code>",
                    "신청자에게 자동 문자/카톡 전송은 하지 않았습니다. 아래 문구를 복사해 전달하세요.",
                    "",
                    _telegram_safe(guide),
                ]
            ),
            enabled=True,
        )
        log_action(target_id, "telegram_location_guide_viewed", "manual_copy", client_ip)
        return "장소 안내 문구 생성 완료"

    return "지원하지 않는 버튼입니다."


def _safe_public_booking(booking: dict) -> dict:
    return {
        "id": booking.get("id"),
        "status": booking.get("status"),
        "payment_status": booking.get("payment_status"),
        "payment_amount_krw": booking.get("payment_amount_krw"),
        "session_id": booking.get("session_id"),
        "session_title": booking.get("session_title"),
        "session_program_type": booking.get("session_program_type"),
        "session_audience_level": booking.get("session_audience_level"),
        "session_starts_at": booking.get("session_starts_at"),
        "session_ends_at": booking.get("session_ends_at"),
        "session_location": booking.get("session_location"),
        "session_price_krw": booking.get("session_price_krw"),
        "created_at": booking.get("created_at"),
        "confirmed_at": booking.get("confirmed_at"),
        "request_rank": booking.get("request_rank"),
        "paid_rank": booking.get("paid_rank"),
    }


APPLICATION_PLAN_TYPES = {"free", "basic", "full"}
LEAD_PLAN_TYPES = {"consultation", "lead_email", "lead_phone"}


def _plan_label(plan_type: str | None) -> str:
    return {
        "free": "무료강의",
        "basic": "기본강의",
        "full": "유료강의",
        "consultation": "상담",
        "lead_email": "소식받기",
        "lead_phone": "소식받기",
    }.get(str(plan_type or "").lower(), str(plan_type or "") or "-")


def _can_upgrade_lead_to_application(existing: dict | None, attempted: dict) -> bool:
    existing_plan = str((existing or {}).get("plan_type") or "").lower()
    attempted_plan = str((attempted or {}).get("plan_type") or "").lower()
    return existing_plan in LEAD_PLAN_TYPES and attempted_plan in APPLICATION_PLAN_TYPES


def _can_refresh_duplicate_application(existing: dict | None, attempted: dict) -> bool:
    existing_plan = str((existing or {}).get("plan_type") or "").lower()
    attempted_plan = str((attempted or {}).get("plan_type") or "").lower()
    return existing_plan in APPLICATION_PLAN_TYPES and attempted_plan in APPLICATION_PLAN_TYPES


def _is_free_session(session: dict | None) -> bool:
    if not session:
        return False
    if is_study_session(session):
        return False
    program = str(session.get("program_type") or "").lower()
    return "free" in program or int(session.get("price_krw") or 0) == 0


def _maybe_create_free_session_booking(member: dict, session_id: str | None, request: Request) -> dict | None:
    if not session_id:
        return None
    session = get_session(session_id)
    if not _is_free_session(session):
        raise HTTPException(400, detail="무료강의 일정만 무료 신청에서 바로 예약할 수 있습니다.")
    existing = find_active_member_booking(member["id"], session_id)
    if existing:
        booking = get_booking(existing["id"]) or existing
        return {
            "booking": booking,
            "booking_id": existing["id"],
            "duplicate_booking": True,
            "message": "이미 선택한 무료강의 일정에 신청되어 있습니다.",
        }
    ok, reason = session_acceptance(session)
    if not ok:
        raise HTTPException(400, detail=reason)
    booking_id = create_booking({
        "session_id": session_id,
        "member_id": member["id"],
        "applicant_name": member.get("name") or "신청자",
        "phone_masked": member.get("phone_masked") or "",
        "desired_outcome": member.get("short_term_goal") or member.get("reason") or "",
        "preparedness": member.get("skills") or "",
        "status": "confirmed",
        "payment_status": "waived",
        "payment_amount_krw": 0,
        "payment_note": "무료강의 신청: 입금 없음",
        "confirmed_at": datetime.now(timezone.utc).isoformat(),
    })
    refresh_session_counts(session_id)
    log_action(member["id"], "free_booking_created", f"booking_id={booking_id}", request.client.host if request.client else None)
    return {
        "booking": get_booking(booking_id) or {},
        "booking_id": booking_id,
        "duplicate_booking": False,
        "message": "무료강의 일정 신청이 함께 접수되었습니다.",
    }


def _booking_status_summaries() -> dict[str, str]:
    summaries: dict[str, list[str]] = {}
    for booking in list_bookings():
        member_id = booking.get("member_id")
        if not member_id:
            continue
        parts = [
            str(booking.get("status") or "unknown"),
            f"payment={booking.get('payment_status') or 'unknown'}",
        ]
        session_title = booking.get("session_title")
        if session_title:
            parts.append(str(session_title))
        session_starts_at = booking.get("session_starts_at")
        if session_starts_at:
            parts.append(str(session_starts_at))
        summaries.setdefault(str(member_id), []).append(" / ".join(parts))
    return {member_id: " | ".join(items) for member_id, items in summaries.items()}


def _contact_status_filter(status: Optional[str]) -> Optional[str]:
    normalized = (status or "").strip().lower()
    if normalized in {"", "active", "non_erased", "not_erased", "all_active"}:
        return None
    return normalized


def _contact_plan_filter(plan_type: Optional[str]) -> Optional[str]:
    normalized = (plan_type or "").strip().lower()
    return normalized if normalized in {"free", "full", "basic", "consultation", "lead_email", "lead_phone"} else None


def _contact_plan_label(plan_type: str | None) -> str:
    normalized = (plan_type or "").strip().lower()
    return {
        "free": "무료",
        "full": "유료",
        "basic": "기본",
        "consultation": "상담",
        "lead_email": "소식 이메일",
        "lead_phone": "소식 번호",
    }.get(normalized, "기본")


def _contact_display_name(name: str | None, plan_type: str | None) -> str:
    display_name = str(name or "신청자").strip() or "신청자"
    if display_name.startswith("[ARSEN "):
        return display_name
    return f"[ARSEN {_contact_plan_label(plan_type)}] {display_name}"


def _contact_note(row: dict) -> str:
    return "; ".join([
        f"plan={row.get('plan_type', '') or 'basic'}",
        f"status={row.get('status', '') or 'unknown'}",
        f"member_id={row.get('member_id', '')}",
        f"booking={row.get('booking_status_summary', '') or 'none'}",
        f"created_at={row.get('created_at', '')}",
    ])


def _contact_export_rows(
    status: Optional[str] = None,
    grade: Optional[str] = None,
    plan_type: Optional[str] = None,
) -> list[dict]:
    rows = []
    booking_summaries = _booking_status_summaries()
    status_filter = _contact_status_filter(status)
    plan_filter = _contact_plan_filter(plan_type)
    for member in list_members(status=status_filter, grade=grade):
        if member.get("status") == "erased":
            continue
        if plan_filter and str(member.get("plan_type", "")).lower() != plan_filter:
            continue
        try:
            phone = decrypt_phone(member["phone_encrypted"])
            email = decrypt_email(member["email_encrypted"])
        except Exception:
            log.exception("연락처 export 복호화 실패: %s", member.get("id"))
            phone = ""
            email = ""
        row = {
            "member_id": member.get("id", ""),
            "name": member.get("name", ""),
            "phone": phone,
            "email": email,
            "status": member.get("status", ""),
            "plan_type": member.get("plan_type", ""),
            "booking_status_summary": booking_summaries.get(str(member.get("id", "")), "none"),
            "participation_grade": member.get("participation_grade", ""),
            "created_at": member.get("created_at", ""),
        }
        row["contact_name"] = _contact_display_name(row["name"], row["plan_type"])
        row["contact_note"] = _contact_note(row)
        rows.append(row)
    return rows


def _vcard_escape(value: str | None) -> str:
    text = str(value or "")
    return (
        text.replace("\\", "\\\\")
        .replace("\n", "\\n")
        .replace("\r", "")
        .replace(";", "\\;")
        .replace(",", "\\,")
    )


def _contact_export_detail(format_name: str, rows: list[dict]) -> str:
    return json.dumps(
        {"format": format_name, "count": len(rows), "pii": "decrypted_for_admin_export"},
        ensure_ascii=False,
    )


def _contacts_csv_response(rows: list[dict], filename: str) -> Response:
    output = io.StringIO()
    fields = [
        "Name",
        "Given Name",
        "Family Name",
        "Phone 1 - Type",
        "Phone 1 - Value",
        "E-mail 1 - Type",
        "E-mail 1 - Value",
        "Notes",
        "Group Membership",
        "member_id",
        "name",
        "phone",
        "email",
        "status",
        "plan_type",
        "participation_grade",
        "created_at",
        "booking_status_summary",
    ]
    writer = csv.DictWriter(output, fieldnames=fields)
    writer.writeheader()
    for row in rows:
        writer.writerow({
            "Name": row.get("contact_name", ""),
            "Given Name": "",
            "Family Name": "",
            "Phone 1 - Type": "Mobile" if row.get("phone") else "",
            "Phone 1 - Value": row.get("phone", ""),
            "E-mail 1 - Type": "Home" if row.get("email") else "",
            "E-mail 1 - Value": row.get("email", ""),
            "Notes": row.get("contact_note", ""),
            "Group Membership": "* myContacts",
            **{field: row.get(field, "") for field in fields if field not in {
                "Name",
                "Given Name",
                "Family Name",
                "Phone 1 - Type",
                "Phone 1 - Value",
                "E-mail 1 - Type",
                "E-mail 1 - Value",
                "Notes",
                "Group Membership",
            }},
        })
    return Response(
        content=output.getvalue(),
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


def _contacts_vcard_response(rows: list[dict], filename: str) -> Response:
    cards = []
    for row in rows:
        card = [
            "BEGIN:VCARD",
            "VERSION:3.0",
            f"FN:{_vcard_escape(row.get('contact_name'))}",
            f"N:;{_vcard_escape(row.get('contact_name'))};;;",
        ]
        if row.get("phone"):
            card.append(f"TEL;TYPE=CELL:{_vcard_escape(row.get('phone'))}")
        if row.get("email"):
            card.append(f"EMAIL:{_vcard_escape(row.get('email'))}")
        card.extend([
            f"NOTE:{_vcard_escape(row.get('contact_note'))}",
            "END:VCARD",
        ])
        cards.extend(card)
    content = "\r\n".join(cards) + ("\r\n" if cards else "")
    return Response(
        content=content,
        media_type="text/vcard; charset=utf-8",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


def _normalize_education_resources(raw_resources) -> list[dict]:
    resources = raw_resources if isinstance(raw_resources, list) else []
    normalized = []
    for item in resources:
        if not isinstance(item, dict):
            continue
        title = str(item.get("title") or "").strip()
        if not title:
            continue
        category = str(item.get("category") or item.get("section") or "기타").strip() or "기타"
        resource_id = str(item.get("id") or uuid.uuid4()).strip()
        tags = item.get("tags", [])
        if isinstance(tags, str):
            tags = [part.strip() for part in tags.replace("#", "").replace(",", "\n").splitlines() if part.strip()]
        elif isinstance(tags, list):
            tags = [str(part).strip() for part in tags if str(part).strip()]
        else:
            tags = []
        entry = {
            "id": resource_id,
            "category": category,
            "section": category,
            "kind": str(item.get("kind") or item.get("type") or "link").strip() or "link",
            "title": title,
            "status": str(item.get("status", "")).strip(),
            "description": str(item.get("description") or "").strip(),
            "url": str(item.get("url") or "").strip(),
            "image_url": str(item.get("image_url") or item.get("asset_url") or "").strip(),
            "copy_text": str(item.get("copy_text", "")).strip(),
            "tags": tags,
            "visible": item.get("visible") is not False,
            "created_at": str(item.get("created_at") or datetime.now(timezone.utc).isoformat()).strip(),
            "updated_at": str(item.get("updated_at") or datetime.now(timezone.utc).isoformat()).strip(),
        }
        template_id = str(item.get("template_id", "")).strip()
        if template_id:
            entry["template_id"] = template_id
        normalized.append(entry)
    return normalized


def _load_education_resources() -> dict:
    if not EDUCATION_DATA_PATH.exists():
        return {"updated_at": None, "resources": []}
    try:
        data = json.loads(EDUCATION_DATA_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        raise HTTPException(500, detail=f"수업 자료 파일을 읽지 못했습니다: {exc}") from exc
    if not isinstance(data, dict):
        raise HTTPException(500, detail="수업 자료 파일 형식이 올바르지 않습니다.")
    return {
        "updated_at": data.get("updated_at"),
        "resources": _normalize_education_resources(data.get("resources", [])),
    }


def _education_payload(resources: list[dict], updated_at: str | None = None) -> dict:
    visible_count = sum(1 for item in resources if item.get("visible") is not False)
    return {
        "updated_at": updated_at,
        "resources": resources,
        "visible_count": visible_count,
        "hidden_count": len(resources) - visible_count,
        "total_count": len(resources),
    }


def _save_education_resources(resources: list[dict]) -> dict:
    EDUCATION_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    updated_at = datetime.now(timezone.utc).isoformat()
    payload = _education_payload(resources, updated_at)
    if EDUCATION_DATA_PATH.exists():
        backup_dir = Path.home() / ".arsen-work-bus" / "backups" / "class-dashboard"
        backup_dir.mkdir(parents=True, exist_ok=True)
        backup_name = f"education_resources-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}.json"
        shutil.copy2(EDUCATION_DATA_PATH, backup_dir / backup_name)
    tmp_path = EDUCATION_DATA_PATH.with_name(
        f".{EDUCATION_DATA_PATH.name}.{uuid.uuid4().hex}.tmp"
    )
    try:
        tmp_path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        os.replace(tmp_path, EDUCATION_DATA_PATH)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()
    return payload


# ── 엔드포인트 ──────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <!doctype html>
    <html lang="ko">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>ARSEN 고객 페이지</title>
      <style>
        * { box-sizing: border-box; }
        body {
          margin: 0;
          min-height: 100vh;
          font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;
          background: #0b111c;
          color: #eef4ff;
          display: grid;
          place-items: center;
          padding: 28px 16px;
        }
        main {
          width: min(820px, 100%);
          border: 1px solid #334258;
          border-radius: 16px;
          background: #121a28;
          padding: 30px;
          box-shadow: 0 18px 50px rgba(0, 0, 0, 0.28);
        }
        h1 { margin: 0 0 10px; font-size: clamp(1.8rem, 5vw, 2.4rem); letter-spacing: 0; }
        p { margin: 0 0 22px; color: #b8c6d9; line-height: 1.7; }
        .actions { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
        a {
          display: block;
          border: 1px solid #40526d;
          border-radius: 12px;
          color: #eef4ff;
          text-decoration: none;
          padding: 16px 18px;
          font-weight: 800;
          background: #182234;
        }
        a.primary { background: #18438f; border-color: #6ea8ff; }
        a.product { background: #0f3d35; border-color: #36d399; }
        a span { display: block; margin-top: 4px; color: #b8c6d9; font-weight: 600; font-size: 0.95rem; }
        @media (max-width: 720px) { .actions { grid-template-columns: 1fr; } }
      </style>
    </head>
    <body>
      <main>
        <h1>ARSEN 고객 페이지</h1>
        <p>유료 강의 신청, 예약 확인, 스터디와 회원 기능을 한곳에서 확인합니다.</p>
        <div class="actions">
          <a class="primary" href="/frontend/join-full.html">AI 결과물 제작 초급 4주반 신청<span>1기 · 정원 8명 · 100,000원 · 시간과 장소 수요 확인 중</span></a>
          <a class="product" href="/frontend/yoonbot.html#download">YOONBOT 다운로드<span>Windows 런처를 내려받고 파일럿 구매 정보를 확인합니다.</span></a>
          <a href="/frontend/status.html">예약 확인<span>신청/예약 상태와 안내 문구를 확인합니다.</span></a>
          <a href="/frontend/study.html">스터디 참가<span>승인 멤버 전용 스터디 일정을 확인하고 신청합니다.</span></a>
          <a href="/frontend/class-dashboard.html">수업용 대시보드<span>강의 자료와 공개 학습 아카이브를 봅니다.</span></a>
          <a href="/frontend/class-stories.html">공개 후기 보기<span>관리자가 승인한 후기와 결과물만 표시됩니다.</span></a>
          <a href="/frontend/member.html">회원 페이지<span>승인 코드로 예약과 수강 이력을 확인합니다.</span></a>
          <a href="/frontend/privacy.html">개인정보처리방침</a>
        </div>
      </main>
    </body>
    </html>
    """


@app.get("/api/education")
async def education_resources(
    request: Request,
    include_hidden: Optional[bool] = False,
):
    if include_hidden:
        require_admin(request)
    data = _load_education_resources()
    resources = data["resources"]
    if not include_hidden:
        resources = [item for item in resources if item.get("visible") is not False]
    return _education_payload(resources, data.get("updated_at"))


@app.put("/api/education")
async def update_education_resources(body: dict, request: Request, _=Depends(require_admin)):
    resources = _normalize_education_resources(body.get("resources", body))
    result = _save_education_resources(resources)
    log_action(
        "system",
        "education_resources_update",
        json.dumps(
            {
                "total_count": result["total_count"],
                "visible_count": result["visible_count"],
                "hidden_count": result["hidden_count"],
            },
            ensure_ascii=False,
        ),
        request.client.host if request.client else None,
    )
    return result


def _consultation_text(*values: object, default: str = "") -> str:
    for value in values:
        text = str(value or "").strip()
        if text:
            return text
    return default


def _normalize_consultation_phone(value: str) -> str:
    text = str(value or "").strip()
    digits = "".join(ch for ch in text if ch.isdigit())
    if len(digits) == 11:
        return f"{digits[:3]}-{digits[3:7]}-{digits[7:]}"
    if len(digits) == 10:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    return text


def _looks_like_email(value: str) -> bool:
    text = str(value or "").strip()
    return "@" in text and "." in text.rsplit("@", 1)[-1]


def _mask_email(value: str) -> str:
    text = str(value or "").strip().lower()
    if "@" not in text:
        return ""
    local, domain = text.split("@", 1)
    visible = local[:2] if len(local) >= 2 else local[:1]
    return f"{visible}{'*' * max(3, len(local) - len(visible))}@{domain}"


def _consultation_status(value: str | None) -> str:
    normalized = str(value or "").strip().lower()
    return normalized if normalized in {"new", "contacted", "on_hold", "closed", "spam"} else "new"


def _consultation_public(row: dict | None) -> dict | None:
    if not row:
        return None
    return {
        "id": row.get("id"),
        "source": row.get("source") or "public_site",
        "topic": row.get("topic") or "",
        "name": row.get("name") or "",
        "email_masked": row.get("email_masked") or "",
        "phone_masked": row.get("phone_masked") or "",
        "product_interest": row.get("product_interest") or "",
        "message": row.get("message") or "",
        "status": row.get("status") or "new",
        "admin_note": row.get("admin_note") or "",
        "page_url": row.get("page_url") or "",
        "referrer": row.get("referrer") or "",
        "member_id": row.get("member_id") or "",
        "created_at": row.get("created_at"),
        "updated_at": row.get("updated_at"),
    }


def _consultation_kind_clause(kind: str | None) -> tuple[str, list[str]]:
    normalized = str(kind or "").strip().lower()
    if normalized in {"newsletter", "news", "lead", "leads"}:
        return "source='home_newsletter'", []
    if normalized in {"consultation", "consult", "inquiry"}:
        return "source!='home_newsletter'", []
    return "", []


def _consultation_summary(kind: str | None = None) -> dict:
    where, params = _consultation_kind_clause(kind)
    query = "SELECT status, COUNT(*) AS count FROM consultations"
    if where:
        query += f" WHERE {where}"
    query += " GROUP BY status"
    conn = get_conn()
    try:
        rows = conn.execute(query, params).fetchall()
    finally:
        conn.close()
    counts = {row["status"]: int(row["count"] or 0) for row in rows}
    return {
        "total": sum(counts.values()),
        "new": counts.get("new", 0),
        "contacted": counts.get("contacted", 0),
        "on_hold": counts.get("on_hold", 0),
        "closed": counts.get("closed", 0),
        "spam": counts.get("spam", 0),
    }


def _list_consultations(status: str | None = None, source: str | None = None, kind: str | None = None) -> list[dict]:
    where = []
    params: list[str] = []
    status_text = str(status or "").strip()
    if status_text == "active":
        where.append("status NOT IN ('closed', 'spam')")
    elif status_text:
        where.append("status=?")
        params.append(_consultation_status(status_text))
    source_text = str(source or "").strip()
    if source_text:
        where.append("source=?")
        params.append(source_text[:80])
    kind_clause, kind_params = _consultation_kind_clause(kind)
    if kind_clause:
        where.append(kind_clause)
        params.extend(kind_params)
    query = "SELECT * FROM consultations"
    if where:
        query += " WHERE " + " AND ".join(where)
    query += " ORDER BY created_at DESC LIMIT 300"
    conn = get_conn()
    try:
        rows = conn.execute(query, params).fetchall()
    finally:
        conn.close()
    return [_consultation_public(dict(row)) for row in rows]


def _get_consultation_row(consultation_id: str) -> dict | None:
    conn = get_conn()
    try:
        row = conn.execute("SELECT * FROM consultations WHERE id=?", (consultation_id,)).fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def _safe_decrypt_contact(value: str, decryptor) -> str:
    if not value:
        return ""
    try:
        return decryptor(value)
    except Exception:
        log.exception("상담 연락처 복호화 실패")
        return ""


def _consultation_contact(consultation_id: str) -> dict | None:
    row = _get_consultation_row(consultation_id)
    if not row:
        return None
    return {
        "id": row["id"],
        "name": row.get("name") or "신청자",
        "phone": _safe_decrypt_contact(row.get("phone_encrypted", ""), decrypt_phone),
        "email": _safe_decrypt_contact(row.get("email_encrypted", ""), decrypt_email),
        "phone_masked": row.get("phone_masked") or "",
        "email_masked": row.get("email_masked") or "",
    }


def _update_consultation_status(consultation_id: str, status: str, note: str | None = None) -> dict | None:
    existing = _get_consultation_row(consultation_id)
    if not existing:
        return None
    timestamp = datetime.now(timezone.utc).isoformat()
    conn = get_conn()
    try:
        conn.execute(
            "UPDATE consultations SET status=?, admin_note=COALESCE(?, admin_note), updated_at=? WHERE id=?",
            (_consultation_status(status), (note or "").strip() or None, timestamp, consultation_id),
        )
        conn.commit()
    finally:
        conn.close()
    return _consultation_public(_get_consultation_row(consultation_id))


@app.post("/api/consultations")
async def public_consultation(req: ConsultationRequest, request: Request):
    data = req.model_dump()
    source = _consultation_text(data.get("source"), default="public_site")[:80]
    raw_contact = _consultation_text(data.get("contact"), data.get("lead_contact"))
    contact_digits = "".join(ch for ch in raw_contact if ch.isdigit())
    raw_email = _consultation_text(
        data.get("email"),
        data.get("buyer_email"),
        raw_contact if _looks_like_email(raw_contact) else "",
    ).lower()
    raw_phone = _consultation_text(
        data.get("phone"),
        data.get("buyer_phone"),
        raw_contact if not _looks_like_email(raw_contact) and len(contact_digits) >= 7 else "",
    )
    phone = _normalize_consultation_phone(raw_phone)
    email = raw_email
    contact_type = _consultation_text(data.get("contact_type")).lower() or ("email" if email else "phone" if phone else "")
    is_newsletter = source == "home_newsletter"
    if is_newsletter:
        contact_type = "phone"
    newsletter_label = "번호" if contact_type == "phone" else "이메일"
    topic_base = _consultation_text(
        data.get("topic"),
        data.get("consult_type"),
        data.get("subject"),
        data.get("product_interest"),
        default="상담",
    )[:120]
    topic = f"{topic_base} · {newsletter_label}" if is_newsletter and "·" not in topic_base else topic_base
    name = _consultation_text(data.get("name"), data.get("buyer_name"))[:80]
    product_interest = _consultation_text(
        data.get("product_interest"),
        data.get("product"),
        f"메인 소식 받기 · {newsletter_label}" if is_newsletter else "",
    )
    message = _consultation_text(data.get("message"), data.get("customer_message"), data.get("memo"))
    page_url = _consultation_text(data.get("page_url"))
    referrer = _consultation_text(data.get("referrer"))

    if data.get("consent_privacy") is False:
        raise HTTPException(status_code=400, detail="상담 연락을 위한 개인정보 수집 동의가 필요합니다.")
    if is_newsletter and not name:
        raise HTTPException(status_code=400, detail="소식받기 신청은 이름을 입력해야 합니다.")
    if is_newsletter and not phone:
        raise HTTPException(status_code=400, detail="소식받기 신청은 전화번호를 입력해야 합니다.")
    if not phone and not email:
        raise HTTPException(status_code=400, detail="연락 가능한 전화번호 또는 이메일이 필요합니다.")

    if not name:
        name = "상담 신청자"
    encrypted = encrypt_data({"phone": phone, "email": email})
    plan_type = "lead_phone" if is_newsletter and contact_type == "phone" else "lead_email" if is_newsletter else "consultation"
    kind_label = f"소식 받기 · {newsletter_label}" if is_newsletter else "상담"
    reason_parts = [
        f"분류: {kind_label}",
        f"상담 주제: {topic}",
        f"관심 항목: {product_interest}" if product_interest else "",
        f"내용: {message}" if message else "",
        f"페이지: {page_url}" if page_url else "",
        f"유입: {referrer}" if referrer else "",
    ]
    member_data = {
        "name": name,
        "email": email,
        "phone": phone,
        **encrypted,
        "gender": "상담",
        "age": 0,
        "job": "소식 받기 신청" if is_newsletter else "상담 신청",
        "referral_source": source,
        "reason": "\n".join(part for part in reason_parts if part),
        "ai_level": kind_label,
        "plan_type": plan_type,
        "ai_tools": [],
        "ai_subscription": "",
        "ai_weekly_hours": "",
        "ai_use_cases": [],
        "group_goals": product_interest or kind_label,
        "short_term_goal": message or topic,
        "participation_type": kind_label,
        "preferred_schedule": "",
        "available_time_slots": [],
        "region": "",
        "main_device": "",
        "can_code": False,
        "can_present": False,
        "skills": "",
        "contribution": message or product_interest or kind_label,
        "participation_grade": kind_label,
        "consent_personal": True,
        "consent_marketing": False,
        "consent_at": datetime.now(timezone.utc).isoformat(),
        "consent_version": "public-newsletter-v1" if is_newsletter else "public-consultation-v1",
    }
    member_id = create_member(member_data)
    consultation_id = str(uuid.uuid4())
    timestamp = datetime.now(timezone.utc).isoformat()
    conn = get_conn()
    try:
        conn.execute(
            """
            INSERT INTO consultations (
                id, source, topic, name, email_hash, email_masked, email_encrypted,
                phone_hash, phone_masked, phone_encrypted, product_interest, message,
                status, admin_note, page_url, referrer, user_agent, member_id, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                consultation_id,
                source,
                topic,
                name,
                encrypted.get("email_hash") if email else None,
                _mask_email(email),
                encrypted.get("email_encrypted", "") if email else "",
                encrypted.get("phone_hash") if phone else None,
                encrypted.get("phone_masked", ""),
                encrypted.get("phone_encrypted", "") if phone else "",
                product_interest,
                message,
                "new",
                None,
                page_url,
                referrer,
                request.headers.get("user-agent", "")[:500],
                member_id,
                timestamp,
                timestamp,
            ),
        )
        conn.commit()
    finally:
        conn.close()
    log_action(
        member_id,
        "consultation_created",
        json.dumps({"id": consultation_id, "source": source, "topic": topic, "page_url": page_url}, ensure_ascii=False),
        _client_ip(request),
    )
    return {
        "ok": True,
        "message": "소식받기 신청이 접수되었습니다. 새 소식이 준비되면 안내드리겠습니다." if is_newsletter else "상담 신청이 접수되었습니다. 운영자가 확인 후 연락드립니다.",
        "member_id": member_id,
        "data": {
            "id": consultation_id,
            "member_id": member_id,
            "source": source,
            "topic": topic,
            "name": name,
            "plan_type": plan_type,
        },
    }


@app.get("/admin/consultations")
async def admin_consultations(
    status: Optional[str] = None,
    source: Optional[str] = None,
    kind: Optional[str] = None,
    _=Depends(require_admin),
):
    return {
        "ok": True,
        "summary": _consultation_summary(kind),
        "data": _list_consultations(status=status, source=source, kind=kind),
    }


@app.get("/admin/consultations/{consultation_id}")
async def admin_consultation_detail(consultation_id: str, _=Depends(require_admin)):
    row = _get_consultation_row(consultation_id)
    if not row:
        raise HTTPException(status_code=404, detail="상담 접수를 찾을 수 없습니다.")
    return {"ok": True, "data": _consultation_public(row)}


@app.get("/admin/consultations/{consultation_id}/contact")
async def admin_consultation_contact(consultation_id: str, request: Request, _=Depends(require_admin)):
    contact = _consultation_contact(consultation_id)
    if not contact:
        raise HTTPException(status_code=404, detail="상담 접수를 찾을 수 없습니다.")
    log_action("system", "consultation_contact_view", consultation_id, _client_ip(request))
    return {"ok": True, "data": contact}


@app.post("/admin/consultations/{consultation_id}/status")
async def admin_consultation_status(consultation_id: str, body: dict, request: Request, _=Depends(require_admin)):
    updated = _update_consultation_status(
        consultation_id,
        str(body.get("status") or ""),
        str(body.get("admin_note") or body.get("note") or ""),
    )
    if not updated:
        raise HTTPException(status_code=404, detail="상담 접수를 찾을 수 없습니다.")
    log_action("system", "consultation_status_update", f"{consultation_id}:{updated.get('status')}", _client_ip(request))
    return {"ok": True, "data": updated}


@app.get("/sessions")
async def public_sessions(program_type: Optional[str] = None):
    rows = list_sessions(include_closed=False)
    if program_type:
        rows = [row for row in rows if str(row.get("program_type") or "").lower() == program_type.lower()]
    safe_rows = []
    for row in rows:
        safe = dict(row)
        safe.pop("payment_guide", None)
        safe_rows.append(safe)
    return {
        "ok": True,
        "data": safe_rows,
        "total": len(safe_rows),
        "workflow": "신청 → 승인 코드 확인 → 예약 신청 → 입금 확인 → 자리 확정",
    }


@app.get("/study/sessions")
async def public_study_sessions():
    rows = list_study_sessions(include_closed=False)
    safe_rows = []
    for row in rows:
        safe = dict(row)
        safe.pop("payment_guide", None)
        safe_rows.append(safe)
    return {
        "ok": True,
        "data": safe_rows,
        "total": len(safe_rows),
        "workflow": "회원 확인 → 스터디 선택 → 참가 신청 → 운영자 확인",
    }


@app.post("/apply")
async def apply(req: ApplyRequest, request: Request):
    data = req.model_dump()
    client_ip = request.client.host if request.client else "unknown"
    selected_session = get_session(data.get("session_id")) if data.get("session_id") else None
    if selected_session and not data.get("preferred_schedule"):
        data["preferred_schedule"] = f"{selected_session.get('starts_at', '')} / {selected_session.get('location', '')}".strip(" /")
    if data.get("desired_outcome") and not data.get("short_term_goal"):
        data["short_term_goal"] = data.get("desired_outcome")
    if data.get("preparedness") and not data.get("skills"):
        data["skills"] = data.get("preparedness")

    # 1. 보안 검토
    sec = check_security(data)
    if not sec["ok"]:
        raise HTTPException(400, detail={"errors": sec["threats"]})

    # 2. 입력값 검증
    val = validate(data)
    if not val["ok"]:
        return {"ok": False, "errors": val["errors"]}

    # 3. 검증 재검토
    meta = meta_validate(data, val)
    if not meta["ok"]:
        return {"ok": False, "errors": meta["issues"]}

    # 4. 중복 확인: 같은 신청자가 다시 제출해도 새 신청서를 만들지 않는다.
    duplicate_member = find_duplicate_member(data)
    if duplicate_member:
        if duplicate_member.get("status") == "blacklist":
            return {"ok": False, "errors": ["접근이 제한된 신청자입니다."]}
        if _can_upgrade_lead_to_application(duplicate_member, data):
            con = check_consent(data)
            if not con["ok"]:
                return {"ok": False, "errors": con["errors"]}
            grade = _grade_count(data)
            enc = encrypt_data(data)
            member_data = {
                **data,
                **enc,
                "consent_at": con["consent_data"]["at"],
                "consent_version": con["consent_data"]["version"],
                "consent_marketing": con["consent_data"]["marketing"],
                "participation_grade": grade,
            }
            previous_plan = duplicate_member.get("plan_type")
            upgraded = upgrade_lead_to_application(duplicate_member["id"], member_data)
            if not upgraded:
                raise HTTPException(500, detail="기존 리드를 강의 신청으로 전환하지 못했습니다.")

            member = get_member(duplicate_member["id"])
            sheets_data = {k: v for k, v in member_data.items()
                           if k not in ("phone_encrypted", "email_encrypted")}
            sheets_data["member_id"] = duplicate_member["id"]
            sheets_ok = save_to_sheets(sheets_data)
            log_action(duplicate_member["id"], "sheets_sync", "ok" if sheets_ok else "not_configured_or_failed", client_ip)
            log_action(
                duplicate_member["id"],
                "duplicate_apply",
                json.dumps(
                    {
                        "source": duplicate_member.get("duplicate_source"),
                        "converted": True,
                        "from_plan_type": previous_plan,
                        "to_plan_type": data.get("plan_type"),
                        "attempt_name": data.get("name"),
                        "attempt_phone_masked": enc.get("phone_masked"),
                        "attempt_plan_type": data.get("plan_type"),
                        "attempt_session_id": data.get("session_id"),
                    },
                    ensure_ascii=False,
                ),
                client_ip,
            )
            log_action(
                duplicate_member["id"],
                "lead_upgraded_to_apply",
                json.dumps(
                    {
                        "from_plan_type": previous_plan,
                        "to_plan_type": data.get("plan_type"),
                        "from_label": _plan_label(previous_plan),
                        "to_label": _plan_label(data.get("plan_type")),
                    },
                    ensure_ascii=False,
                ),
                client_ip,
            )

            free_booking = None
            if data.get("plan_type") == "free" and data.get("session_id"):
                free_booking = _maybe_create_free_session_booking(member, data.get("session_id"), request)

            backup_result = backup_database(reason="lead_upgrade_apply")
            backup_summary = {
                "ok_count": backup_result.get("ok_count", 0),
                "failed_count": backup_result.get("failed_count", 0),
                "targets": [
                    {"name": item.get("name"), "status": item.get("status")}
                    for item in backup_result.get("targets", [])
                ],
            }
            log_action(duplicate_member["id"], "db_backup", json.dumps(backup_summary, ensure_ascii=False), client_ip)
            hermes_status = notify_admin_new_apply(
                member,
                booking=(free_booking or {}).get("booking") if free_booking else None,
                storage_status={
                    "db": "ok",
                    "sheets": "ok" if sheets_ok else "not_configured_or_failed",
                    "backup": f"{backup_result.get('ok_count', 0)} ok / {backup_result.get('failed_count', 0)} failed",
                },
                stats=get_stats(),
                raw_application=data,
                lead_upgrade_from=previous_plan,
            )
            log_action(duplicate_member["id"], "hermes_notify", hermes_status, client_ip)
            return {
                "ok": True,
                "duplicate": False,
                "upgraded_from_lead": True,
                "previous_plan_type": previous_plan,
                "message": f"{_plan_label(previous_plan)} 내역을 {_plan_label(data.get('plan_type'))} 신청으로 변경해 접수했습니다.",
                "member_id": duplicate_member["id"],
                "status": member.get("status"),
                "booking_id": (free_booking or {}).get("booking_id"),
                "next_steps": [
                    "운영자가 신청 내용을 확인한 뒤 승인 코드를 발급합니다.",
                    "관리자 신청자/멤버 목록에서는 강의 신청자로 표시됩니다.",
                    "무료강의 일정을 선택했다면 해당 일정 신청도 함께 연결됩니다.",
                ],
                "reservation": _safe_public_booking((free_booking or {}).get("booking") or {}) if free_booking else None,
                "payment": None,
            }
        previous_plan = duplicate_member.get("plan_type")
        active_member = duplicate_member
        refreshed_application = False
        if _can_refresh_duplicate_application(duplicate_member, data):
            con = check_consent(data)
            if not con["ok"]:
                return {"ok": False, "errors": con["errors"]}
            enc = encrypt_data(data)
            member_data = {
                **data,
                **enc,
                "consent_at": con["consent_data"]["at"],
                "consent_version": "duplicate-refresh-v1",
                "consent_marketing": con["consent_data"]["marketing"],
                "participation_grade": _grade_count(data),
            }
            refreshed_application = refresh_duplicate_application(duplicate_member["id"], member_data)
            if not refreshed_application:
                raise HTTPException(500, detail="기존 신청 정보를 최신 신청으로 갱신하지 못했습니다.")
            active_member = get_member(duplicate_member["id"]) or duplicate_member

        free_booking = None
        if data.get("plan_type") == "free" and data.get("session_id"):
            free_booking = _maybe_create_free_session_booking(active_member, data.get("session_id"), request)
        stats_data = get_stats()
        hermes_status = notify_admin_duplicate_apply(active_member, data, stats=stats_data)
        log_action(
            duplicate_member["id"],
            "duplicate_apply",
            json.dumps(
                {
                    "source": duplicate_member.get("duplicate_source"),
                    "notify": hermes_status,
                    "refreshed": refreshed_application,
                    "from_plan_type": previous_plan,
                    "to_plan_type": data.get("plan_type"),
                    "attempt_name": data.get("name"),
                    "attempt_phone_masked": encrypt_data({"phone": data.get("phone") or "", "email": data.get("email") or ""}).get("phone_masked"),
                    "attempt_plan_type": data.get("plan_type"),
                    "attempt_session_id": data.get("session_id"),
                },
                ensure_ascii=False,
            ),
            client_ip,
        )
        return {
            "ok": True,
            "duplicate": True,
            "latest_application_refreshed": refreshed_application,
            "previous_plan_type": previous_plan,
            "message": (
                f"기존 신청 정보를 {_plan_label(data.get('plan_type'))} 기준으로 갱신했습니다."
                if refreshed_application
                else "이미 신청이 접수되어 있습니다. 기존 신청 상태를 기준으로 안내드릴게요."
            ),
            "member_id": duplicate_member["id"],
            "status": active_member.get("status"),
            "next_steps": [
                "관리자 신청자 목록에서 최근 재신청 시간 기준으로 확인할 수 있습니다.",
                "무료강의 일정을 선택했다면 같은 일정에 중복 예약 없이 연결합니다.",
                "유료강의는 승인 코드 받은 뒤 예약자 확인 페이지에서 진행하세요.",
            ],
            "booking_id": (free_booking or {}).get("booking_id"),
            "reservation": _safe_public_booking((free_booking or {}).get("booking") or {}) if free_booking else None,
            "payment": None,
        }

    dup = check_duplicate(data)
    if not dup["ok"]:
        return {"ok": False, "errors": dup["errors"]}

    # 5. 동의 확인
    con = check_consent(data)
    if not con["ok"]:
        return {"ok": False, "errors": con["errors"]}

    # 6. 참여 등급 계산
    grade = _grade_count(data)

    # 7. 개인정보 암호화
    enc = encrypt_data(data)

    # 8. 저장 데이터 구성
    member_data = {
        **data,
        **enc,
        "consent_at": con["consent_data"]["at"],
        "consent_version": con["consent_data"]["version"],
        "consent_marketing": con["consent_data"]["marketing"],
        "participation_grade": grade,
    }

    # 9. DB 저장
    member_id = create_member(member_data)

    # 10. Google Sheets 저장 (실패해도 진행)
    sheets_data = {k: v for k, v in member_data.items()
                   if k not in ("phone_encrypted", "email_encrypted")}
    sheets_data["member_id"] = member_id
    sheets_ok = save_to_sheets(sheets_data)
    log_action(member_id, "sheets_sync", "ok" if sheets_ok else "not_configured_or_failed", client_ip)

    # 11. 이력 기록
    member = get_member(member_id)
    log_action(member_id, "apply", f"plan={data['plan_type']}, grade={grade}", client_ip)
    free_booking = None
    if data.get("plan_type") == "free" and data.get("session_id"):
        free_booking = _maybe_create_free_session_booking(member, data.get("session_id"), request)

    booking_next_steps = [
        "운영자가 신청 내용을 확인한 뒤 승인 코드를 발급합니다.",
        "승인 코드를 받은 뒤 예약자 확인 페이지에서 원하는 일정을 예약합니다.",
        "입금 확인 후 자리가 확정됩니다.",
    ]

    # 12. DB 백업/미러링 (실패해도 신청 접수는 유지)
    backup_result = backup_database(reason="apply")
    backup_summary = {
        "ok_count": backup_result.get("ok_count", 0),
        "failed_count": backup_result.get("failed_count", 0),
        "targets": [
            {"name": item.get("name"), "status": item.get("status")}
            for item in backup_result.get("targets", [])
        ],
    }
    log_action(member_id, "db_backup", json.dumps(backup_summary, ensure_ascii=False), client_ip)

    if free_booking:
        booking_next_steps = [
            "선택한 무료강의 일정에 신청이 접수되었습니다.",
            "운영자가 무료강의 안내 멘트를 복사해 개별 안내할 수 있습니다.",
            "수업 후 운영자가 참여 완료/불참을 표시해 수강 이력에 반영합니다.",
        ]

    # 13. Hermes/Telegram 알림
    hermes_status = notify_admin_new_apply(
        member,
        booking=(free_booking or {}).get("booking") if free_booking else None,
        storage_status={
            "db": "ok",
            "sheets": "ok" if sheets_ok else "not_configured_or_failed",
            "backup": f"{backup_result.get('ok_count', 0)} ok / {backup_result.get('failed_count', 0)} failed",
        },
        stats=get_stats(),
        raw_application=data,
    )
    log_action(member_id, "hermes_notify", hermes_status, client_ip)

    return {
        "ok": True,
        "message": (free_booking or {}).get("message") or "신청이 접수되었습니다.",
        "member_id": member_id,
        "booking_id": (free_booking or {}).get("booking_id"),
        "next_steps": booking_next_steps,
        "reservation": _safe_public_booking((free_booking or {}).get("booking") or {}) if free_booking else None,
        "payment": None,
    }


@app.post("/approve/{member_id}")
async def approve(member_id: str, request: Request, _=Depends(require_admin)):
    member = get_member(member_id)
    if not member:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    if member["status"] != "pending":
        raise HTTPException(400, detail=f"현재 상태: {member['status']}")

    # 코드 생성
    code = generate_code(member_id)
    update_status(member_id, "approved")

    member = get_member(member_id)
    phone = decrypt_phone(member["phone_encrypted"])
    notify_member_approved(member, code, None, phone)
    log_action(member_id, "approve", f"code_issued", request.client.host if request.client else None)

    return {
        "ok": True,
        "message": "승인 완료",
        "code": code,
        "expires_at": None,
        "expiry_label": "기한 없음",
        "delivery_message": _code_delivery_message(member, code),
    }


@app.post("/reject/{member_id}")
async def reject(member_id: str, body: RejectRequest, request: Request, _=Depends(require_admin)):
    member = get_member(member_id)
    if not member:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")

    update_status(member_id, "rejected", body.reason)
    phone = decrypt_phone(member["phone_encrypted"])
    notify_member_rejected(member, body.reason, phone)
    log_action(member_id, "reject", body.reason, request.client.host if request.client else None)

    return {"ok": True, "message": "거절 처리 완료"}


@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    if not TELEGRAM_WEBHOOK_SECRET:
        raise HTTPException(503, detail="Telegram webhook secret is not configured.")
    if request.headers.get("X-Telegram-Bot-Api-Secret-Token") != TELEGRAM_WEBHOOK_SECRET:
        raise HTTPException(401, detail="Invalid Telegram webhook secret.")
    payload = await request.json()
    callback = payload.get("callback_query") or {}
    data = callback.get("data") or ""
    callback_id = callback.get("id") or ""
    client_ip = request.client.host if request.client else None
    message = _telegram_callback_result(data, client_ip)
    answer_callback_query(callback_id, message, show_alert=False)
    return {"ok": True, "message": message}


@app.get("/auth/kakao/start")
async def kakao_start(request: Request, next: Optional[str] = None):
    client_id = (os.getenv("KAKAO_REST_API_KEY") or "").strip()
    next_path = _safe_next_path(next)
    if not client_id:
        return RedirectResponse(_append_kakao_status(next_path, "not_configured"), status_code=302)

    state = secrets.token_urlsafe(24)
    response = RedirectResponse(
        f"{KAKAO_AUTHORIZE_URL}?{urllib.parse.urlencode({
            'response_type': 'code',
            'client_id': client_id,
            'redirect_uri': _kakao_redirect_uri(request),
            'state': state,
        })}",
        status_code=302,
    )
    _set_signed_cookie(
        response,
        request,
        KAKAO_STATE_COOKIE,
        {"state": state, "next": next_path, "iat": datetime.now(timezone.utc).isoformat()},
        600,
    )
    return response


@app.get("/auth/kakao/callback")
async def kakao_callback(
    request: Request,
    code: Optional[str] = None,
    state: Optional[str] = None,
    error: Optional[str] = None,
):
    state_payload = _unpack_signed_cookie(request.cookies.get(KAKAO_STATE_COOKIE))
    next_path = _safe_next_path(state_payload.get("next") if state_payload else None)
    if error:
        response = RedirectResponse(_append_kakao_status(next_path, "error"), status_code=302)
        _delete_kakao_cookie(response, KAKAO_STATE_COOKIE)
        return response
    if not state_payload or state_payload.get("state") != state or not code:
        response = RedirectResponse(_append_kakao_status(next_path, "state_error"), status_code=302)
        _delete_kakao_cookie(response, KAKAO_STATE_COOKIE)
        return response

    client_id = (os.getenv("KAKAO_REST_API_KEY") or "").strip()
    if not client_id:
        response = RedirectResponse(_append_kakao_status(next_path, "not_configured"), status_code=302)
        _delete_kakao_cookie(response, KAKAO_STATE_COOKIE)
        return response

    token_body = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "redirect_uri": _kakao_redirect_uri(request),
        "code": code,
    }
    client_secret = (os.getenv("KAKAO_CLIENT_SECRET") or "").strip()
    if client_secret:
        token_body["client_secret"] = client_secret

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            token_response = await client.post(KAKAO_TOKEN_URL, data=token_body)
            token_response.raise_for_status()
            access_token = token_response.json().get("access_token")
            if not access_token:
                raise ValueError("missing_access_token")
            user_response = await client.get(KAKAO_USER_ME_URL, headers={"Authorization": f"Bearer {access_token}"})
            user_response.raise_for_status()
            user = user_response.json()
    except Exception as exc:
        logging.warning("kakao_login_failed: %s", exc)
        response = RedirectResponse(_append_kakao_status(next_path, "token_error"), status_code=302)
        _delete_kakao_cookie(response, KAKAO_STATE_COOKIE)
        return response

    profile = _kakao_profile_payload(user)
    kakao_id = profile.get("id") or str(user.get("id") or "")
    member = get_member_by_kakao_id(kakao_id)
    session_payload = {
        "kakao_id": kakao_id,
        "member_id": member["id"] if member else "",
        "profile": profile,
        "iat": datetime.now(timezone.utc).isoformat(),
    }
    response = RedirectResponse(_append_kakao_status(next_path, "linked" if member else "unmatched"), status_code=302)
    _delete_kakao_cookie(response, KAKAO_STATE_COOKIE)
    _set_signed_cookie(response, request, KAKAO_SESSION_COOKIE, session_payload, KAKAO_SESSION_MAX_AGE)
    log_action(member["id"] if member else "kakao", "kakao_login", "linked=1" if member else "linked=0", request.client.host if request.client else None)
    return response


@app.get("/auth/kakao/me")
async def kakao_me(request: Request):
    session = _read_kakao_session(request)
    if not session or not session.get("kakao_id"):
        raise HTTPException(401, detail="카카오 로그인이 필요합니다.")
    member = get_member(session.get("member_id")) if session.get("member_id") else None
    return {
        "ok": True,
        "data": {
            "kakao": _kakao_public_payload(session, member),
            "member": _safe_member_profile(member) if member else None,
            "bookings": [_safe_public_booking(item) for item in list_member_bookings(member["id"])] if member else [],
        },
    }


@app.post("/auth/kakao/link")
async def kakao_link(body: KakaoLinkRequest, request: Request):
    session = _read_kakao_session(request)
    if not session or not session.get("kakao_id"):
        raise HTTPException(401, detail="카카오 로그인이 필요합니다.")
    member = _get_member_by_phone(body.phone)
    if not member:
        raise HTTPException(404, detail="신청 정보를 찾을 수 없습니다. 신청한 전화번호를 확인해주세요.")
    result = verify_code(body.code, member["id"])
    log_action(member["id"], "kakao_link_code_used" if result.get("ok") else "kakao_link_code_failed", None, request.client.host if request.client else None)
    if not result.get("ok"):
        raise HTTPException(400, detail=result.get("error") or "코드 확인에 실패했습니다.")
    if member.get("status") != "approved":
        raise HTTPException(400, detail=f"현재 신청 상태는 {member.get('status')}입니다.")

    existing = get_member_by_kakao_id(session["kakao_id"])
    if existing and existing["id"] != member["id"]:
        raise HTTPException(409, detail="이미 다른 회원 정보에 연결된 카카오 계정입니다.")

    profile = session.get("profile") if isinstance(session.get("profile"), dict) else {}
    link_member_kakao(member["id"], session["kakao_id"], profile)
    member = get_member(member["id"]) or member
    response = {
        "ok": True,
        "message": "카카오 계정이 회원 정보와 연결되었습니다.",
        "data": {
            "kakao": {"connected": True, "linked": True, "nickname": profile.get("nickname") or ""},
            "member": _safe_member_profile(member),
            "bookings": [_safe_public_booking(item) for item in list_member_bookings(member["id"])],
        },
    }
    return response


@app.post("/auth/kakao/logout")
async def kakao_logout():
    body = {"ok": True, "message": "카카오 회원 세션을 종료했습니다."}
    response = Response(content=json.dumps(body, ensure_ascii=False), media_type="application/json")
    _delete_kakao_cookie(response, KAKAO_SESSION_COOKIE)
    return response


@app.post("/verify-code")
async def verify(body: VerifyCodeRequest, request: Request):
    result = verify_code(body.code, body.member_id)
    action = "code_used" if result["ok"] else "code_failed"
    log_action(body.member_id, action, None, request.client.host if request.client else None)
    return result


@app.post("/member/verify-code")
async def public_verify_code(body: PublicVerifyCodeRequest, request: Request):
    member = _get_member_by_phone(body.phone)
    if not member:
        raise HTTPException(404, detail="신청 정보를 찾을 수 없습니다. 신청한 전화번호를 확인해주세요.")

    result = verify_code(body.code, member["id"])
    action = "code_used_public" if result.get("ok") else "code_failed_public"
    log_action(member["id"], action, None, request.client.host if request.client else None)
    if not result.get("ok"):
        raise HTTPException(400, detail=result.get("error") or "코드 확인에 실패했습니다.")
    if member.get("status") != "approved":
        raise HTTPException(400, detail=f"현재 신청 상태는 {member.get('status')}입니다.")

    return {
        "ok": True,
        "data": {
            "member": _safe_member_profile(member),
            "bookings": [_safe_public_booking(item) for item in list_member_bookings(member["id"])],
        },
    }


@app.post("/member/bookings")
async def public_create_booking(body: PublicBookingRequest, request: Request):
    member = get_member(body.member_id)
    if not member:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    if member.get("status") != "approved":
        raise HTTPException(400, detail="승인된 신청자만 예약할 수 있습니다.")

    kakao_session = _read_kakao_session(request)
    kakao_member_ok = bool(kakao_session and kakao_session.get("member_id") == body.member_id)
    if body.code:
        result = verify_code(body.code, body.member_id)
        action = "booking_code_verified" if result.get("ok") else "booking_code_failed"
        log_action(body.member_id, action, None, request.client.host if request.client else None)
        if not result.get("ok"):
            raise HTTPException(400, detail=result.get("error") or "코드 확인에 실패했습니다.")
    elif kakao_member_ok:
        log_action(body.member_id, "booking_kakao_verified", None, request.client.host if request.client else None)
    else:
        raise HTTPException(400, detail="승인 코드 확인 또는 카카오 회원 로그인이 필요합니다.")

    session = get_session(body.session_id)
    ok, reason = session_acceptance(session)
    if not ok:
        raise HTTPException(400, detail=reason)
    eligible, eligibility_reason, _eligibility = study_member_acceptance(session, body.member_id)
    if not eligible:
        raise HTTPException(403, detail=eligibility_reason)

    existing = find_active_member_booking(body.member_id, body.session_id)
    if existing:
        return {
            "ok": True,
            "message": "이미 접수된 예약 신청이 있습니다.",
            "data": _safe_public_booking(get_booking(existing["id"]) or existing),
        }

    study_session = is_study_session(session)
    amount = int(session.get("price_krw") or 0) if study_session else int(session.get("price_krw") or DEFAULT_PRICE)
    booking_id = create_booking({
        "session_id": body.session_id,
        "member_id": body.member_id,
        "applicant_name": member["name"],
        "phone_masked": member.get("phone_masked", ""),
        "desired_outcome": body.desired_outcome or member.get("short_term_goal") or member.get("reason") or "",
        "preparedness": body.preparedness or "",
        "status": "requested",
        "payment_status": "waived" if study_session and amount == 0 else "not_sent",
        "payment_amount_krw": amount,
    })
    refresh_session_counts(body.session_id)
    booking = get_booking(booking_id)
    log_action(body.member_id, "booking_requested_public", f"booking_id={booking_id}", request.client.host if request.client else None)
    hermes_status = notify_booking_requested(member, booking or {}, stats=get_stats())
    log_action(body.member_id, "booking_telegram_notify", hermes_status, request.client.host if request.client else None)

    return {
        "ok": True,
        "message": "스터디 참가 신청이 접수되었습니다. 운영자가 인원과 일정을 확인한 뒤 안내합니다." if study_session else "예약 신청이 접수되었습니다. 운영자가 인원과 일정을 확인한 뒤 안내합니다.",
        "data": _safe_public_booking(booking or {}),
    }


@app.post("/regen-code/{member_id}")
async def regen(member_id: str, request: Request, _=Depends(require_admin)):
    member = get_member(member_id)
    if not member:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    code = regenerate_code(member_id)
    member = get_member(member_id)
    phone = decrypt_phone(member["phone_encrypted"])
    notify_member_approved(member, code, None, phone)
    log_action(member_id, "code_issued", "재발급", request.client.host if request.client else None)
    return {
        "ok": True,
        "code": code,
        "expires_at": None,
        "expiry_label": "기한 없음",
        "delivery_message": _code_delivery_message(member, code),
    }


@app.get("/members/{member_id}/access-code")
async def member_access_code(member_id: str, request: Request, _=Depends(require_admin)):
    member = get_member(member_id)
    if not member:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    if member.get("status") not in {"approved", "pending"}:
        raise HTTPException(400, detail=f"현재 상태에서는 코드를 조회할 수 없습니다: {member.get('status')}")
    result = get_current_code(member_id)
    if not result.get("ok"):
        raise HTTPException(404, detail=result.get("error") or "발급된 코드가 없습니다.")
    code = result["code"]
    log_action(member_id, "code_viewed", "admin_code_reveal", request.client.host if request.client else None)
    return {
        "ok": True,
        "data": {
            "code": code,
            "issued_at": result.get("issued_at"),
            "expires_at": None,
            "expiry_label": "기한 없음",
            "source": result.get("source"),
            "delivery_message": _code_delivery_message(member, code),
        },
    }


@app.post("/admin/members/{member_id}/code-delivery-log")
async def record_code_delivery(
    member_id: str,
    body: CodeDeliveryLogRequest,
    request: Request,
    _=Depends(require_admin),
):
    member = get_member(member_id)
    if not member:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    detail = json.dumps({"channel": body.channel, "note": body.note}, ensure_ascii=False)
    log_action(member_id, "code_delivered", detail, request.client.host if request.client else None)
    return {"ok": True, "message": "전달 기록이 저장되었습니다."}


@app.post("/blacklist/{member_id}")
async def add_blacklist(member_id: str, request: Request, _=Depends(require_admin)):
    member = get_member(member_id)
    if not member:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    blacklist_member(member_id)
    log_action(member_id, "blacklist", None, request.client.host if request.client else None)
    return {"ok": True, "message": "블랙리스트 등록 완료"}


@app.post("/unblacklist/{member_id}")
async def remove_blacklist(member_id: str, request: Request, _=Depends(require_admin)):
    member = get_member(member_id)
    if not member:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    if member.get("status") != "blacklist":
        raise HTTPException(400, detail=f"현재 상태: {member.get('status')}")
    update_status(member_id, "pending")
    log_action(member_id, "unblacklist", "status=pending", request.client.host if request.client else None)
    return {"ok": True, "message": "차단 해제 후 대기 상태로 변경했습니다."}


@app.get("/members")
async def members(status: Optional[str] = None, grade: Optional[str] = None, _=Depends(require_admin)):
    rows = list_members(status=status, grade=grade)
    # 암호화 필드 제외
    safe = []
    for r in rows:
        r.pop("phone_encrypted", None)
        r.pop("email_encrypted", None)
        r.pop("access_code", None)
        safe.append(r)
    return {"ok": True, "data": safe, "total": len(safe)}


@app.get("/members/{member_id}")
async def member_detail(member_id: str, _=Depends(require_admin)):
    member = get_member(member_id)
    if not member:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    member.pop("phone_encrypted", None)
    member.pop("email_encrypted", None)
    member.pop("access_code", None)
    delivery_logs = get_code_delivery_logs(member_id)
    member["code_delivery_logs"] = delivery_logs
    return {"ok": True, "data": member, "code_delivery_logs": delivery_logs}


@app.get("/members/{member_id}/contact")
async def member_contact(member_id: str, request: Request, _=Depends(require_admin_key)):
    member = get_member(member_id)
    if not member:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    try:
        phone = decrypt_phone(member["phone_encrypted"])
        email = decrypt_email(member["email_encrypted"])
    except Exception:
        log.exception("연락처 복호화 실패: %s", member_id)
        raise HTTPException(500, detail="연락처 복호화에 실패했습니다.")
    log_action(member_id, "contact_view", "admin_contact_reveal", request.client.host if request.client else None)
    return {
        "ok": True,
        "data": {
            "id": member["id"],
            "name": member["name"],
            "phone": phone,
            "phone_masked": member["phone_masked"],
            "email": email,
        },
    }


@app.put("/admin/members/{member_id}")
async def admin_update_member(member_id: str, body: MemberUpdateRequest, request: Request, _=Depends(require_admin)):
    if not get_member(member_id):
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    updates = body.model_dump(exclude_unset=True)
    if not updates:
        raise HTTPException(400, detail="변경할 값이 없습니다.")
    if updates.get("status") and updates["status"] not in {"pending", "approved", "rejected", "blacklist", "erased"}:
        raise HTTPException(400, detail="상태 값이 올바르지 않습니다.")
    if updates.get("plan_type") and updates["plan_type"] not in {"free", "full", "basic", "consultation", "lead_email", "lead_phone"}:
        raise HTTPException(400, detail="신청 유형 값이 올바르지 않습니다.")
    ok = update_member(member_id, updates)
    if not ok:
        raise HTTPException(400, detail="변경할 값이 없습니다.")
    log_action(
        member_id,
        "member_update",
        json.dumps({"fields": sorted(updates.keys())}, ensure_ascii=False),
        request.client.host if request.client else None,
    )
    member = get_member(member_id)
    member.pop("phone_encrypted", None)
    member.pop("email_encrypted", None)
    member.pop("access_code", None)
    return {"ok": True, "data": member}


@app.post("/admin/members/{member_id}/contact-registered")
async def admin_member_contact_registered(member_id: str, body: ContactRegisteredRequest, request: Request, _=Depends(require_admin)):
    member = get_member(member_id)
    if not member:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    detail = {
        "registered": bool(body.registered),
        "note": (body.note or "").strip(),
    }
    log_action(
        member_id,
        "contact_registered",
        json.dumps(detail, ensure_ascii=False),
        request.client.host if request.client else None,
    )
    updated = get_member(member_id)
    updated.pop("phone_encrypted", None)
    updated.pop("email_encrypted", None)
    updated.pop("access_code", None)
    return {"ok": True, "data": updated}


@app.post("/admin/members/{member_id}/kakao-unlink")
async def admin_member_kakao_unlink(member_id: str, request: Request, _=Depends(require_admin)):
    member = get_member(member_id)
    if not member:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    if not member.get("kakao_id"):
        raise HTTPException(400, detail="연결된 카카오 계정이 없습니다.")
    unlink_member_kakao(member_id)
    log_action(
        member_id,
        "kakao_unlinked_by_admin",
        "admin_manual_unlink",
        request.client.host if request.client else None,
    )
    updated = get_member(member_id)
    updated.pop("phone_encrypted", None)
    updated.pop("email_encrypted", None)
    updated.pop("access_code", None)
    return {"ok": True, "message": "카카오 계정 연결을 해제했습니다.", "data": updated}


@app.post("/admin/members/{member_id}/kick")
async def admin_kick_member_from_classes(member_id: str, body: MemberKickRequest, request: Request, _=Depends(require_admin)):
    member = get_member(member_id)
    if not member:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    reason = (body.reason or "운영자 강의 추방 처리").strip()
    targets = [
        item for item in list_member_bookings(member_id)
        if item.get("status") not in {"canceled", "rejected", "no_show", "completed"}
    ]
    for booking in targets:
        note = "\n".join(part for part in [booking.get("payment_note"), f"[강의 추방] {reason}"] if part)
        set_booking_state(booking["id"], status="canceled", payment_note=note)
    log_action(
        member_id,
        "member_kicked_from_classes",
        json.dumps({"count": len(targets), "reason": reason}, ensure_ascii=False),
        request.client.host if request.client else None,
    )
    return {"ok": True, "message": f"활성 강의 예약 {len(targets)}건을 취소 처리했습니다.", "data": {"member_id": member_id, "canceled": len(targets)}}


@app.post("/members/{member_id}/erase")
async def erase_member(
    member_id: str,
    body: MemberEraseRequest,
    request: Request,
    _=Depends(require_admin),
):
    result = erase_member_personal_data(member_id, cancel_bookings=body.cancel_bookings)
    if not result:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    for session_id in result.get("session_ids", []):
        refresh_session_counts(session_id)
    log_action(
        member_id,
        "member_personal_data_erased",
        json.dumps(
            {
                "cancel_bookings": result.get("cancel_bookings"),
                "bookings_updated": result.get("bookings_updated", 0),
                "bookings_canceled": result.get("bookings_canceled", 0),
            },
            ensure_ascii=False,
        ),
        request.client.host if request.client else None,
    )
    return {
        "ok": True,
        "message": "연락처와 개인정보를 삭제 처리했습니다.",
        "data": {
            "member_id": member_id,
            "status": "erased",
            "bookings_updated": result.get("bookings_updated", 0),
            "bookings_canceled": result.get("bookings_canceled", 0),
        },
    }


@app.post("/api/license/activate")
async def api_license_activate(body: LicenseActivateRequest, request: Request):
    result = activate_license(
        license_key=body.license_key,
        hwid=body.hwid,
        app_version=body.app_version,
        platform=body.platform,
        device_name=body.device_name,
        client_ip=_client_ip(request),
        user_agent=_user_agent(request),
    )
    return result


@app.post("/api/license/verify")
async def api_license_verify(body: LicenseVerifyRequest, request: Request):
    token = _bearer_token(request)
    result = verify_yoonbot_license(
        activation_token=token,
        hwid=body.hwid,
        app_version=body.app_version,
        platform=body.platform,
        client_ip=_client_ip(request),
        user_agent=_user_agent(request),
    )
    return result


@app.get("/admin/licenses")
async def admin_licenses(
    status: Optional[str] = None,
    member_id: Optional[str] = None,
    _=Depends(require_admin),
):
    return {
        "ok": True,
        "summary": license_summary(),
        "data": list_licenses(
            status=status.strip() if status else None,
            member_id=member_id.strip() if member_id else None,
        ),
    }


@app.post("/admin/licenses")
async def admin_create_license(
    body: AdminLicenseCreateRequest,
    request: Request,
    _=Depends(require_admin),
):
    try:
        result = create_license(
            member_id=body.member_id.strip() if body.member_id else None,
            plan_code=body.plan_code,
            expires_at=body.expires_at,
            max_devices=body.max_devices,
            app_min_version=body.app_min_version,
            note=body.note,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    log_action(
        "system",
        "yoonbot_license_created",
        result["license"]["license_key_hint"],
        _client_ip(request),
    )
    return result


@app.get("/admin/licenses/summary")
async def admin_license_summary(_=Depends(require_admin)):
    return {"ok": True, "data": license_summary()}


@app.get("/admin/licenses/{license_id}")
async def admin_get_license(license_id: str, _=Depends(require_admin)):
    license_item = get_license(license_id)
    if not license_item:
        raise HTTPException(status_code=404, detail="라이선스를 찾을 수 없습니다.")
    return {"ok": True, "data": license_item}


@app.post("/admin/licenses/{license_id}/revoke")
async def admin_revoke_license(
    license_id: str,
    body: AdminLicenseRevokeRequest,
    request: Request,
    _=Depends(require_admin),
):
    result = revoke_license(license_id, body.reason)
    if not result.get("ok"):
        raise HTTPException(status_code=404, detail=result.get("message", "라이선스를 찾을 수 없습니다."))
    log_action("system", "yoonbot_license_revoked", license_id, _client_ip(request))
    return result


@app.post("/admin/licenses/{license_id}/reset-device")
async def admin_reset_license_device(
    license_id: str,
    body: AdminLicenseResetDeviceRequest,
    request: Request,
    _=Depends(require_admin),
):
    result = reset_license_device(license_id, body.reason)
    if not result.get("ok"):
        raise HTTPException(status_code=400, detail=result.get("message", "기기 초기화에 실패했습니다."))
    log_action("system", "yoonbot_license_device_reset", license_id, _client_ip(request))
    return result


@app.post("/admin/licenses/{license_id}/extend")
async def admin_extend_license(
    license_id: str,
    body: AdminLicenseExtendRequest,
    request: Request,
    _=Depends(require_admin),
):
    result = extend_license(license_id, body.expires_at)
    if not result.get("ok"):
        raise HTTPException(status_code=400, detail=result.get("message", "만료일 변경에 실패했습니다."))
    log_action("system", "yoonbot_license_extended", license_id, _client_ip(request))
    return result


@app.get("/api/yoonbot/products")
async def api_yoonbot_products():
    return {"ok": True, **yoonbot_products()}


@app.post("/api/yoonbot/orders")
async def api_yoonbot_create_order(body: YoonbotOrderCreateRequest, request: Request):
    try:
        result = create_yoonbot_order(
            buyer_name=body.buyer_name,
            buyer_email=body.buyer_email,
            buyer_phone=body.buyer_phone,
            product_code=body.product_code,
            plan_code=body.plan_code,
            customer_message=body.customer_message,
            consent_privacy=body.consent_privacy,
            consent_terms=body.consent_terms,
            discount_code=body.discount_code,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    # Override payment payload only when Toss is fully configured (client + secret both set)
    config = get_toss_payment_config()
    if config["provider"] == "toss_payments" and config["client_key_set"] and config["secret_key_set"]:
        result["payment"] = build_toss_payment_payload(result["data"])
    log_action("system", "yoonbot_order_created", result["data"]["id"], _client_ip(request))
    return result


@app.post("/api/yoonbot/orders/{order_id}/payments/toss/confirm")
async def api_yoonbot_toss_confirm(order_id: str, body: TossPaymentConfirmRequest, request: Request):
    try:
        result = confirm_yoonbot_toss_payment(
            order_id=order_id,
            payment_key=body.payment_key,
            client_amount=body.amount,
            toss_order_id=body.order_id,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    log_action("system", "yoonbot_toss_payment_confirmed", order_id, _client_ip(request))
    return result


@app.post("/api/yoonbot/orders/by-toss-id/{toss_order_id}/payments/toss/confirm")
async def api_yoonbot_toss_confirm_by_toss_id(toss_order_id: str, body: TossPaymentConfirmRequest, request: Request):
    order = get_yoonbot_order_by_toss_id(toss_order_id)
    if not order:
        raise HTTPException(status_code=404, detail="주문을 찾을 수 없습니다.")
    try:
        result = confirm_yoonbot_toss_payment(
            order_id=order["id"],
            payment_key=body.payment_key,
            client_amount=body.amount,
            toss_order_id=body.order_id,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    log_action("system", "yoonbot_toss_payment_confirmed", order["id"], _client_ip(request))
    return result


@app.get("/admin/yoonbot/orders")
async def admin_yoonbot_orders(
    status: Optional[str] = None,
    plan_code: Optional[str] = None,
    _=Depends(require_admin),
):
    return {
        "ok": True,
        "summary": yoonbot_order_summary(),
        "data": list_yoonbot_orders(
            status=status.strip() if status else None,
            plan_code=plan_code.strip() if plan_code else None,
        ),
    }


@app.get("/admin/yoonbot/orders/{order_id}")
async def admin_yoonbot_order(order_id: str, _=Depends(require_admin)):
    order = get_yoonbot_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="주문을 찾을 수 없습니다.")
    return {"ok": True, "data": order}


@app.post("/admin/yoonbot/orders/{order_id}/mark-paid")
async def admin_yoonbot_mark_paid(
    order_id: str,
    body: AdminYoonbotOrderPaidRequest,
    request: Request,
    _=Depends(require_admin),
):
    try:
        result = mark_yoonbot_order_paid(
            order_id,
            payment_provider=body.payment_provider,
            payment_ref=body.payment_ref,
            note=body.note,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    log_action("system", "yoonbot_order_mark_paid", order_id, _client_ip(request))
    return result


@app.post("/admin/yoonbot/orders/{order_id}/issue-license")
async def admin_yoonbot_issue_license(order_id: str, request: Request, _=Depends(require_admin)):
    try:
        result = issue_yoonbot_order_license(order_id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    log_action("system", "yoonbot_order_license_issued", order_id, _client_ip(request))
    return result


@app.post("/admin/yoonbot/orders/{order_id}/cancel")
async def admin_yoonbot_cancel_order(
    order_id: str,
    body: AdminYoonbotOrderNoteRequest,
    request: Request,
    _=Depends(require_admin),
):
    try:
        result = cancel_yoonbot_order(order_id, note=body.note)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    log_action("system", "yoonbot_order_canceled", order_id, _client_ip(request))
    return result


@app.post("/admin/yoonbot/orders/{order_id}/refund-note")
async def admin_yoonbot_refund_order(
    order_id: str,
    body: AdminYoonbotOrderNoteRequest,
    request: Request,
    _=Depends(require_admin),
):
    try:
        result = refund_yoonbot_order(order_id, note=body.note)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    log_action("system", "yoonbot_order_refunded", order_id, _client_ip(request))
    return result


@app.get("/admin/yoonbot/discounts")
async def admin_yoonbot_list_discounts(
    _=Depends(require_admin),
):
    codes = list_yoonbot_discount_codes()
    return {"ok": True, "data": codes, "total": len(codes)}


@app.post("/admin/yoonbot/discounts")
async def admin_yoonbot_create_discount(
    body: AdminYoonbotDiscountCreateRequest,
    request: Request,
    _=Depends(require_admin),
):
    try:
        result = create_yoonbot_discount_code(
            code=body.code,
            label=body.label,
            plan_code=body.plan_code,
            discount_type=body.discount_type,
            discount_value=body.discount_value,
            max_redemptions=body.max_redemptions,
            starts_at=body.starts_at,
            expires_at=body.expires_at,
            note=body.note,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    log_action("system", "yoonbot_discount_created", result["code"], _client_ip(request))
    return {"ok": True, "data": result}


@app.post("/admin/yoonbot/discounts/{code}/disable")
async def admin_yoonbot_disable_discount(
    code: str,
    request: Request,
    _=Depends(require_admin),
):
    try:
        result = disable_yoonbot_discount_code(code)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    log_action("system", "yoonbot_discount_disabled", code, _client_ip(request))
    return {"ok": True, "data": result}


@app.get("/stats")
async def stats(_=Depends(require_admin)):
    data = get_stats()
    data["expiring_7d"] = len(get_expiring_soon(days=7))
    return {"ok": True, "data": data}


@app.get("/operator-health")
async def operator_health():
    return {"ok": True, "data": get_operator_health()}


@app.get("/health")
async def health(request: Request):
    return {
        "ok": True,
        "service": "member-system",
        "version": SYSTEM_VERSION,
        "local_admin_preview": is_local_admin_preview(request),
        "data": get_operator_health(),
    }


@app.get("/api/daf/manifest")
async def public_launcher_manifest(request: Request):
    return _public_launcher_manifest(request)


@app.get("/api/daf/programs")
async def public_launcher_programs(request: Request):
    data = _public_launcher_manifest(request)
    return {
        "schema_version": data.get("schema_version"),
        "updated_at": data.get("updated_at"),
        "served_at": data.get("served_at"),
        "programs": data.get("programs", []),
    }


@app.get("/api/daf/notices")
async def public_launcher_notices(
    request: Request,
    audience: Optional[str] = None,
    level: Optional[str] = None,
):
    if audience not in (None, "launcher", "website"):
        raise HTTPException(status_code=422, detail="invalid_audience")
    if level not in (None, "info", "warning", "critical"):
        raise HTTPException(status_code=422, detail="invalid_level")
    data = _load_launcher_manifest()
    return {
        "schema_version": data.get("schema_version"),
        "updated_at": data.get("updated_at"),
        "served_at": datetime.now(timezone.utc).isoformat(),
        "notices": _public_launcher_notices(data.get("notices", []), audience=audience, level=level),
    }


@app.get("/api/daf/launcher/release")
async def public_daf_launcher_release(request: Request):
    data = _load_launcher_manifest()
    return _public_launcher_release(data.get("launcher", {}), request)


@app.get("/api/launcher/release")
async def public_launcher_release(request: Request):
    return await public_daf_launcher_release(request)


@app.get("/api/daf/launcher/artifacts/{artifact_name}")
async def public_launcher_artifact(artifact_name: str):
    if not _safe_launcher_artifact_name(artifact_name):
        raise HTTPException(status_code=400, detail="invalid_artifact_name")
    artifact_path = LAUNCHER_ARTIFACT_DIR / artifact_name
    if not artifact_path.is_file():
        raise HTTPException(status_code=404, detail="launcher_artifact_missing")
    return FileResponse(
        str(artifact_path),
        media_type="application/zip",
        filename=artifact_name,
    )


@app.get("/api/site-theme")
async def public_site_theme():
    return {"ok": True, "data": _load_site_theme()}


@app.get("/admin/site-theme")
async def admin_site_theme(_=Depends(require_admin)):
    return {"ok": True, "data": _load_site_theme()}


@app.get("/admin/launcher-status")
async def admin_launcher_status(request: Request, _=Depends(require_admin)):
    return {"ok": True, "data": _admin_launcher_status(request)}


@app.put("/admin/site-theme")
async def admin_update_site_theme(body: SiteThemeRequest, request: Request, _=Depends(require_admin)):
    payload = _save_site_theme(body.active_theme_id)
    log_action(
        "system",
        "site_theme_update",
        payload.get("active_theme_id", ""),
        request.client.host if request.client else None,
    )
    return {"ok": True, "data": payload}


@app.get("/admin/implementation-status")
async def admin_implementation_status(_=Depends(require_admin)):
    return {"ok": True, "data": build_implementation_status()}


@app.get("/admin/storage-status")
async def admin_storage_status(_=Depends(require_admin)):
    return {"ok": True, "data": get_storage_status()}


@app.get("/admin/security-status")
async def admin_security_status(_=Depends(require_admin)):
    return {"ok": True, "data": build_admin_security_status()}


@app.get("/admin/payment-accounts")
async def admin_payment_accounts(_=Depends(require_admin)):
    return {"ok": True, "data": _load_payment_accounts()}


@app.put("/admin/payment-accounts")
async def admin_update_payment_accounts(body: PaymentAccountsRequest, request: Request, _=Depends(require_admin)):
    accounts = []
    seen: set[str] = set()
    for item in body.accounts[:20]:
        normalized = _normalize_payment_account(item.model_dump())
        if not normalized:
            continue
        if normalized["id"] in seen:
            normalized["id"] = f"acct-{uuid.uuid4().hex[:12]}"
        seen.add(normalized["id"])
        accounts.append(normalized)
    payload = _save_payment_accounts(accounts, body.active_id)
    log_action(
        "system",
        "payment_accounts_update",
        json.dumps({"count": len(accounts), "active_set": bool(payload.get("active_id"))}, ensure_ascii=False),
        request.client.host if request.client else None,
    )
    return {"ok": True, "data": payload}


@app.get("/admin/preparation-guide")
async def admin_preparation_guide(_=Depends(require_admin)):
    return {"ok": True, "data": _load_preparation_guide(), **_admin_no_send_delivery("manual_copy")}


@app.put("/admin/preparation-guide")
async def admin_update_preparation_guide(body: PreparationGuideRequest, request: Request, _=Depends(require_admin)):
    payload = _save_preparation_guide(body.message)
    log_action(
        "system",
        "preparation_guide_update",
        json.dumps({"length": len(payload["message"])}, ensure_ascii=False),
        request.client.host if request.client else None,
    )
    return {"ok": True, "data": payload, **_admin_no_send_delivery("manual_copy")}


@app.get("/api/review-board")
async def public_review_board():
    return {"ok": True, "data": list_review_board(public_only=True)}


@app.get("/api/review-board/submit/{token}")
async def public_review_submission_form(token: str):
    invite = get_review_invite_by_token(token)
    if not invite:
        raise HTTPException(404, detail="유효하지 않은 후기 작성 링크입니다.")
    if not invite.get("is_open"):
        raise HTTPException(400, detail="현재 사용할 수 없는 후기 작성 링크입니다.")
    return {"ok": True, "data": {"invite": invite, "instructors": list_review_board(public_only=True).get("instructors", [])}}


@app.post("/api/review-board/submit/{token}")
async def public_submit_review(token: str, body: ReviewSubmissionRequest, request: Request):
    data = body.model_dump()
    if data.get("instructor_id") and not get_review_instructor(data["instructor_id"]):
        raise HTTPException(400, detail="선택한 강사를 찾을 수 없습니다.")
    try:
        entry = submit_review_from_invite(token, data)
    except ValueError as exc:
        raise HTTPException(400, detail=str(exc)) from exc
    log_action(
        "review_board",
        "review_submission_received",
        json.dumps({"entry_id": entry["id"], "status": entry["status"], "source": "student_link"}, ensure_ascii=False),
        request.client.host if request.client else None,
    )
    return {
        "ok": True,
        "message": "후기가 접수되었습니다. 관리자가 개인정보를 확인하고 승인하면 후기보드에 공개됩니다.",
        "data": {"id": entry["id"], "status": entry["status"]},
    }


@app.get("/admin/review-board")
async def admin_review_board(_=Depends(require_admin)):
    return {"ok": True, "data": list_review_board(public_only=False)}


@app.get("/admin/review-board/invites")
async def admin_review_invites(_=Depends(require_admin)):
    return {"ok": True, "data": list_review_invites()}


@app.post("/admin/review-board/invites")
async def admin_create_review_invite(body: ReviewInviteRequest, request: Request, _=Depends(require_admin)):
    data = body.model_dump()
    if data.get("instructor_id") and not get_review_instructor(data["instructor_id"]):
        raise HTTPException(400, detail="선택한 강사를 찾을 수 없습니다.")
    invite = create_review_invite(data)
    log_action(
        "review_board",
        "review_invite_create",
        json.dumps({"id": invite["id"], "status": invite["status"]}, ensure_ascii=False),
        request.client.host if request.client else None,
    )
    return {"ok": True, "id": invite["id"], "data": invite}


@app.post("/admin/review-board/invites/{invite_id}/revoke")
async def admin_revoke_review_invite(invite_id: str, request: Request, _=Depends(require_admin)):
    if not get_review_invite(invite_id):
        raise HTTPException(404, detail="후기 작성 링크를 찾을 수 없습니다.")
    ok = revoke_review_invite(invite_id)
    if not ok:
        raise HTTPException(404, detail="후기 작성 링크를 찾을 수 없습니다.")
    log_action(
        "review_board",
        "review_invite_revoke",
        json.dumps({"id": invite_id}, ensure_ascii=False),
        request.client.host if request.client else None,
    )
    return {"ok": True, "data": get_review_invite(invite_id)}


@app.post("/admin/review-board/instructors")
async def admin_create_review_instructor(body: ReviewInstructorRequest, request: Request, _=Depends(require_admin)):
    try:
        instructor_id = create_review_instructor(body.model_dump())
    except ValueError as exc:
        raise HTTPException(400, detail=str(exc)) from exc
    log_action(
        "review_board",
        "review_instructor_create",
        json.dumps({"id": instructor_id, "status": body.status}, ensure_ascii=False),
        request.client.host if request.client else None,
    )
    return {"ok": True, "id": instructor_id, "data": get_review_instructor(instructor_id)}


@app.put("/admin/review-board/instructors/{instructor_id}")
async def admin_update_review_instructor(
    instructor_id: str,
    body: ReviewInstructorUpdateRequest,
    request: Request,
    _=Depends(require_admin),
):
    updates = body.model_dump(exclude_unset=True)
    if not updates:
        raise HTTPException(400, detail="변경할 값이 없습니다.")
    if not get_review_instructor(instructor_id):
        raise HTTPException(404, detail="강사를 찾을 수 없습니다.")
    ok = update_review_instructor(instructor_id, updates)
    if not ok:
        raise HTTPException(400, detail="변경할 값이 없습니다.")
    log_action(
        "review_board",
        "review_instructor_update",
        json.dumps({"id": instructor_id, "fields": sorted(updates.keys())}, ensure_ascii=False),
        request.client.host if request.client else None,
    )
    return {"ok": True, "data": get_review_instructor(instructor_id)}


@app.delete("/admin/review-board/instructors/{instructor_id}")
async def admin_delete_review_instructor(instructor_id: str, request: Request, _=Depends(require_admin)):
    ok = delete_review_instructor(instructor_id)
    if not ok:
        raise HTTPException(404, detail="강사를 찾을 수 없습니다.")
    log_action(
        "review_board",
        "review_instructor_delete",
        json.dumps({"id": instructor_id}, ensure_ascii=False),
        request.client.host if request.client else None,
    )
    return {"ok": True, "data": {"id": instructor_id}}


@app.post("/admin/review-board/entries")
async def admin_create_review_entry(body: ReviewEntryRequest, request: Request, _=Depends(require_admin)):
    data = body.model_dump()
    if data.get("instructor_id") and not get_review_instructor(data["instructor_id"]):
        raise HTTPException(400, detail="선택한 강사를 찾을 수 없습니다.")
    try:
        entry_id = create_review_entry(data)
    except ValueError as exc:
        raise HTTPException(400, detail=str(exc)) from exc
    log_action(
        "review_board",
        "review_entry_create",
        json.dumps({"id": entry_id, "status": body.status, "privacy_checked": body.privacy_checked}, ensure_ascii=False),
        request.client.host if request.client else None,
    )
    return {"ok": True, "id": entry_id, "data": get_review_entry(entry_id)}


@app.put("/admin/review-board/entries/{entry_id}")
async def admin_update_review_entry(
    entry_id: str,
    body: ReviewEntryUpdateRequest,
    request: Request,
    _=Depends(require_admin),
):
    updates = body.model_dump(exclude_unset=True)
    if not updates:
        raise HTTPException(400, detail="변경할 값이 없습니다.")
    if not get_review_entry(entry_id):
        raise HTTPException(404, detail="후기를 찾을 수 없습니다.")
    if updates.get("instructor_id") and not get_review_instructor(updates["instructor_id"]):
        raise HTTPException(400, detail="선택한 강사를 찾을 수 없습니다.")
    ok = update_review_entry(entry_id, updates)
    if not ok:
        raise HTTPException(400, detail="변경할 값이 없습니다.")
    log_action(
        "review_board",
        "review_entry_update",
        json.dumps({"id": entry_id, "fields": sorted(updates.keys())}, ensure_ascii=False),
        request.client.host if request.client else None,
    )
    return {"ok": True, "data": get_review_entry(entry_id)}


@app.delete("/admin/review-board/entries/{entry_id}")
async def admin_delete_review_entry(entry_id: str, request: Request, _=Depends(require_admin)):
    ok = delete_review_entry(entry_id)
    if not ok:
        raise HTTPException(404, detail="후기를 찾을 수 없습니다.")
    log_action(
        "review_board",
        "review_entry_delete",
        json.dumps({"id": entry_id}, ensure_ascii=False),
        request.client.host if request.client else None,
    )
    return {"ok": True, "data": {"id": entry_id}}


@app.post("/admin/password")
async def admin_password(body: AdminPasswordRequest, request: Request, _=Depends(require_admin)):
    global ADMIN_API_KEY
    new_password = (body.new_password or "").strip()
    if len(new_password) < ADMIN_PASSWORD_MIN_LENGTH:
        raise HTTPException(400, detail=f"관리자 비밀번호는 최소 {ADMIN_PASSWORD_MIN_LENGTH}자 이상이어야 합니다.")
    if "\n" in new_password or "\r" in new_password:
        raise HTTPException(400, detail="관리자 비밀번호에는 줄바꿈을 넣을 수 없습니다.")
    _update_env_value(ADMIN_ENV_PATH, "ADMIN_API_KEY", new_password)
    ADMIN_API_KEY = new_password
    log_action("system", "admin_password_changed", "admin_api_key_updated", request.client.host if request.client else None)
    return {"ok": True, "data": build_admin_security_status()}


@app.post("/admin/admin-tools/backup")
async def admin_tools_backup(request: Request, _=Depends(require_admin)):
    result = backup_admin_password_tools()
    log_action(
        "system",
        "admin_tool_backup",
        json.dumps(
            {
                "ok_count": result.get("ok_count", 0),
                "failed_count": result.get("failed_count", 0),
                "targets": [
                    {"name": item.get("name"), "status": item.get("status")}
                    for item in result.get("targets", [])
                ],
            },
            ensure_ascii=False,
        ),
        request.client.host if request.client else None,
    )
    return {"ok": result.get("ok_count", 0) > 0, "data": result}


@app.get("/admin/storage-snapshot")
async def admin_storage_snapshot(limit: int = 50, _=Depends(require_admin)):
    return {"ok": True, "data": get_storage_snapshot(limit=limit)}


@app.get("/admin/storage-snapshot.csv")
async def admin_storage_snapshot_csv(limit: int = 50, _=Depends(require_admin)):
    snapshot = get_storage_snapshot(limit=limit)
    output = io.StringIO()
    fields = [
        "member_id",
        "applicant",
        "phone_masked",
        "plan_type",
        "participation_grade",
        "member_status",
        "member_created_at",
        "booking_id",
        "booking_status",
        "payment_status",
        "booking_created_at",
        "session_starts_at",
        "session_location",
    ]
    writer = csv.DictWriter(output, fieldnames=fields)
    writer.writeheader()
    for row in snapshot["recent"]:
        writer.writerow({field: row.get(field, "") for field in fields})
    return Response(
        content=output.getvalue(),
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": "attachment; filename=booking-storage-snapshot.csv"},
    )


@app.get("/admin/contacts.csv")
async def admin_contacts_csv(
    request: Request,
    status: Optional[str] = None,
    grade: Optional[str] = None,
    plan_type: Optional[str] = None,
    _=Depends(require_admin_key),
):
    rows = _contact_export_rows(status=status, grade=grade, plan_type=plan_type)
    log_action("system", "contact_export_csv", f"count={len(rows)}", request.client.host if request.client else None)
    return _contacts_csv_response(rows, "member-contacts.csv")


@app.get("/admin/contacts.vcf")
async def admin_contacts_vcf(
    request: Request,
    status: Optional[str] = None,
    grade: Optional[str] = None,
    plan_type: Optional[str] = None,
    _=Depends(require_admin_key),
):
    rows = _contact_export_rows(status=status, grade=grade, plan_type=plan_type)
    log_action("system", "contact_export_vcard", f"count={len(rows)}", request.client.host if request.client else None)
    return _contacts_vcard_response(rows, "member-contacts.vcf")


@app.get("/admin/contacts-export.csv")
async def admin_contacts_export_csv(
    request: Request,
    status: Optional[str] = None,
    grade: Optional[str] = None,
    plan_type: Optional[str] = None,
    _=Depends(require_admin_key),
):
    rows = _contact_export_rows(status=status, grade=grade, plan_type=plan_type)
    log_action(
        "system",
        "contacts_export",
        _contact_export_detail("csv", rows),
        request.client.host if request.client else None,
    )
    return _contacts_csv_response(rows, "contacts-export.csv")


@app.head("/admin/contacts-export.csv")
async def admin_contacts_export_csv_head(_=Depends(require_admin_key)):
    return Response(
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": "attachment; filename=contacts-export.csv"},
    )


@app.get("/admin/contacts-export.vcf")
async def admin_contacts_export_vcf(
    request: Request,
    status: Optional[str] = None,
    grade: Optional[str] = None,
    plan_type: Optional[str] = None,
    _=Depends(require_admin_key),
):
    rows = _contact_export_rows(status=status, grade=grade, plan_type=plan_type)
    log_action(
        "system",
        "contacts_export",
        _contact_export_detail("vcf", rows),
        request.client.host if request.client else None,
    )
    return _contacts_vcard_response(rows, "contacts-export.vcf")


@app.head("/admin/contacts-export.vcf")
async def admin_contacts_export_vcf_head(_=Depends(require_admin_key)):
    return Response(
        media_type="text/vcard; charset=utf-8",
        headers={"Content-Disposition": "attachment; filename=contacts-export.vcf"},
    )


@app.post("/admin/backup-now")
async def admin_backup_now(request: Request, _=Depends(require_admin)):
    result = backup_database(reason="manual")
    summary = {
        "ok_count": result.get("ok_count", 0),
        "failed_count": result.get("failed_count", 0),
        "targets": [
            {"name": item.get("name"), "status": item.get("status")}
            for item in result.get("targets", [])
        ],
    }
    log_action("system", "db_backup", json.dumps(summary, ensure_ascii=False), request.client.host if request.client else None)
    return {"ok": result.get("ok_count", 0) > 0, "data": result}


@app.get("/admin/sessions")
async def admin_sessions(status: Optional[str] = None, _=Depends(require_admin)):
    rows = list_sessions(status=status, include_closed=True)
    return {"ok": True, "data": rows, "total": len(rows)}


@app.post("/admin/sessions")
async def admin_create_session(body: SessionRequest, request: Request, _=Depends(require_admin)):
    data = body.model_dump()
    session_id = create_session(data)
    log_action(session_id, "session_create", data.get("title"), request.client.host if request.client else None)
    return {"ok": True, "id": session_id, "data": get_session(session_id)}


@app.post("/admin/sessions/seed-default-sunday")
async def admin_seed_sessions(body: SeedSessionsRequest, request: Request, _=Depends(require_admin)):
    result = seed_default_sunday_sessions(body.weeks)
    created_ids = result.get("created", [])
    updated_ids = result.get("updated", [])
    detail = f"created={len(created_ids)},updated={len(updated_ids)}"
    log_action("booking", "session_seed_default_sunday", detail, request.client.host if request.client else None)
    return {
        "ok": True,
        "created": len(created_ids),
        "updated": len(updated_ids),
        "total": len(created_ids) + len(updated_ids),
        "ids": created_ids + updated_ids,
    }


@app.post("/admin/sessions/seed-free-class")
async def admin_seed_free_class_sessions(body: SeedSessionsRequest, request: Request, _=Depends(require_admin)):
    result = seed_default_free_class_sessions(body.weeks)
    created_ids = result.get("created", [])
    updated_ids = result.get("updated", [])
    detail = f"created={len(created_ids)},updated={len(updated_ids)}"
    log_action("booking", "session_seed_free_class", detail, request.client.host if request.client else None)
    return {
        "ok": True,
        "created": len(created_ids),
        "updated": len(updated_ids),
        "total": len(created_ids) + len(updated_ids),
        "ids": created_ids + updated_ids,
    }


@app.post("/admin/sessions/{session_id}")
async def admin_update_session(session_id: str, body: SessionUpdateRequest, request: Request, _=Depends(require_admin)):
    updates = {k: v for k, v in body.model_dump().items() if v is not None}
    ok = update_session(session_id, updates)
    if not ok:
        raise HTTPException(404, detail="세션을 찾을 수 없거나 변경할 값이 없습니다.")
    log_action(session_id, "session_update", ",".join(sorted(updates)), request.client.host if request.client else None)
    return {"ok": True, "data": get_session(session_id)}


@app.delete("/admin/sessions/{session_id}")
async def admin_delete_session(session_id: str, request: Request, _=Depends(require_admin)):
    ok, message = delete_session(session_id)
    if not ok:
        raise HTTPException(409, detail=message)
    log_action(session_id, "session_delete", message, request.client.host if request.client else None)
    return {"ok": True, "message": message}


@app.get("/admin/bookings")
async def admin_bookings(
    status: Optional[str] = None,
    session_id: Optional[str] = None,
    _=Depends(require_admin),
):
    rows = list_bookings(status=status, session_id=session_id)
    return {"ok": True, "data": rows, "total": len(rows)}


@app.post("/admin/sessions/{session_id}/manual-booking")
async def admin_manual_booking(session_id: str, body: ManualBookingRequest, request: Request, _=Depends(require_admin)):
    session = get_session(session_id)
    if not session:
        raise HTTPException(404, detail="일정을 찾을 수 없습니다.")
    if session.get("status") == "canceled":
        raise HTTPException(400, detail="취소된 일정에는 수동 추가할 수 없습니다.")

    reused_member = False
    phone = _normalize_phone_for_storage(body.phone or "")
    selected_member_id = (body.member_id or "").strip()
    if not selected_member_id and not phone:
        raise HTTPException(400, detail="신청자 ID 또는 연락처를 입력하세요.")
    member = get_member(selected_member_id) if selected_member_id else _get_member_by_phone(phone)
    if selected_member_id and not member:
        raise HTTPException(404, detail="선택한 신청자를 찾을 수 없습니다.")
    if member and member.get("status") in {"blacklist", "erased"}:
        raise HTTPException(409, detail=f"현재 회원 상태가 {member.get('status')}라 수동 확정할 수 없습니다.")
    if member:
        reused_member = True
        member_id = member["id"]
        name = (body.applicant_name or "").strip() or member.get("name") or "신청자"
        phone_masked = member.get("phone_masked") or "-"
        if member.get("status") != "approved":
            update_status(member_id, "approved")
            log_action(member_id, "manual_member_approved", f"session_id={session_id}", request.client.host if request.client else None)
    else:
        name = (body.applicant_name or "").strip()
        if not name:
            raise HTTPException(400, detail="신청자 이름을 입력하세요.")
        if not phone:
            raise HTTPException(400, detail="연락처를 입력하세요.")
        member_id = _create_manual_member(name, phone, body.email, body.desired_outcome or body.payment_note)
        phone_masked = encrypt_data({"phone": phone, "email": body.email or f"manual-{uuid.uuid4().hex[:12]}@arsen.local"})["phone_masked"]
        log_action(member_id, "manual_member_create", f"session_id={session_id}", request.client.host if request.client else None)

    existing = find_active_member_booking(member_id, session_id)
    is_study = is_study_session(session)
    is_free = _is_free_session(session)
    is_participation = is_free or is_study
    payment_note = body.payment_note or (
        "운영자 수동 추가: 스터디 참여 확정" if is_study
        else "운영자 수동 추가: 무료강의 확정" if is_free
        else "운영자 수동 추가: 입금 확인 완료"
    )
    if existing:
        if is_participation:
            ok = set_booking_state(existing["id"], status="confirmed", payment_status="waived", payment_note=payment_note)
            if not ok:
                raise HTTPException(409, detail="기존 참여 예약 상태를 변경하지 못했습니다.")
            booking = get_booking(existing["id"])
            message = "이미 연결된 스터디 예약을 참여확정으로 변경했습니다. 자동 알림은 보내지 않았습니다." if is_study else "이미 연결된 무료강의 예약을 확정으로 변경했습니다. 자동 알림은 보내지 않았습니다."
        else:
            ok, message, booking = confirm_payment_state(existing["id"], payment_note)
            if not ok:
                raise HTTPException(409, detail=message)
        log_action(member_id, "manual_booking_existing_confirmed", f"booking_id={existing['id']}", request.client.host if request.client else None)
        return {
            "ok": True,
            "message": message,
            "data": booking,
            "member_id": member_id,
            "reused_member": reused_member,
            **_admin_no_send_delivery("manual_booking"),
        }

    ok, reason = session_acceptance(session)
    if not ok:
        raise HTTPException(409, detail=reason)

    booking_id = create_booking({
        "session_id": session_id,
        "member_id": member_id,
        "applicant_name": name,
        "phone_masked": phone_masked,
        "desired_outcome": body.desired_outcome or "",
        "preparedness": "운영자 수동 추가",
        "status": "confirmed",
        "payment_status": "waived" if is_participation else "paid",
        "payment_amount_krw": int((session.get("price_krw") if body.payment_amount_krw is None else body.payment_amount_krw) or 0),
        "payment_note": payment_note,
        "confirmed_at": datetime.now(timezone.utc).isoformat(),
    })
    refresh_session_counts(session_id)
    booking = get_booking(booking_id)
    log_action(member_id, "manual_booking_confirmed", f"booking_id={booking_id}", request.client.host if request.client else None)
    return {
        "ok": True,
        "message": "스터디 예약을 일정에 수동 추가했습니다. 자동 알림은 보내지 않았습니다." if is_study else "무료강의 예약을 일정에 수동 추가했습니다. 자동 알림은 보내지 않았습니다." if is_free else "입금확정 예약을 일정에 수동 추가했습니다. 자동 알림은 보내지 않았습니다.",
        "data": booking,
        "member_id": member_id,
        "reused_member": reused_member,
        **_admin_no_send_delivery("manual_booking"),
    }


@app.post("/admin/bookings/{booking_id}/state")
async def admin_booking_state(booking_id: str, body: BookingStateRequest, request: Request, _=Depends(require_admin)):
    allowed_status = {"requested", "payment_guide_sent", "payment_pending", "payment_confirmed", "confirmed", "canceled", "rejected", "completed", "no_show"}
    allowed_payment = {"not_sent", "guide_sent", "pending", "paid", "waived", "refunded", "failed"}
    if body.status and body.status not in allowed_status:
        raise HTTPException(400, detail=f"status 가능 값: {sorted(allowed_status)}")
    if body.payment_status and body.payment_status not in allowed_payment:
        raise HTTPException(400, detail=f"payment_status 가능 값: {sorted(allowed_payment)}")
    ok = set_booking_state(
        booking_id,
        status=body.status,
        payment_status=body.payment_status,
        payment_note=body.payment_note,
    )
    if not ok:
        raise HTTPException(404, detail="예약 신청을 찾을 수 없습니다.")
    log_action(booking_id, "booking_state_update", f"status={body.status}, payment={body.payment_status}", request.client.host if request.client else None)
    return {"ok": True, "data": get_booking(booking_id)}


@app.get("/admin/bookings/{booking_id}")
async def admin_booking_detail(booking_id: str, _=Depends(require_admin)):
    booking = get_booking(booking_id)
    if not booking:
        raise HTTPException(404, detail="예약 신청을 찾을 수 없습니다.")
    return {"ok": True, "data": booking}


@app.post("/admin/bookings/{booking_id}/move-session")
async def admin_move_booking_session(booking_id: str, body: BookingMoveRequest, request: Request, _=Depends(require_admin)):
    ok, message, booking = move_booking_to_session(booking_id, body.session_id, body.note)
    if not ok:
        status_code = 404 if booking is None else 409
        raise HTTPException(status_code, detail=message)
    detail = f"target_session_id={body.session_id}"
    log_action(booking_id, "booking_session_move", detail, request.client.host if request.client else None)
    return {
        "ok": True,
        "message": f"{message} 자동 알림은 보내지 않았습니다.",
        "data": booking,
        **_admin_no_send_delivery("session_move"),
    }


@app.delete("/admin/bookings/{booking_id}")
async def admin_delete_booking(booking_id: str, request: Request, _=Depends(require_admin)):
    ok, message, data = delete_booking(booking_id)
    if not ok:
        status_code = 404 if data is None else 409
        raise HTTPException(status_code, detail=message)
    log_action(booking_id, "booking_delete", "inactive_booking", request.client.host if request.client else None)
    return {"ok": True, "message": message, "data": data}


@app.post("/admin/bookings/{booking_id}/send-payment-guide")
async def admin_send_payment_guide(booking_id: str, body: PaymentGuideRequest, request: Request, _=Depends(require_admin)):
    payment_account = _selected_payment_account(body.payment_account_id)
    updated = send_payment_guide_state(booking_id, body.payment_note, payment_account)
    if not updated:
        raise HTTPException(404, detail="예약 신청을 찾을 수 없습니다.")
    log_action(booking_id, "booking_payment_guide_sent", "manual_copy", request.client.host if request.client else None)
    return {
        "ok": True,
        "message": "입금 안내 상태로 변경했습니다. 신청자에게 자동 전송하지 않았습니다. 아래 문구를 복사해 카카오톡/문자로 직접 전달하세요.",
        **_admin_no_send_delivery("manual_copy"),
        "payment_account_included": bool(payment_account),
        "payment_guide": updated.get("payment_note") or default_payment_guide(None, updated, payment_account),
        "data": updated,
    }


@app.post("/admin/bookings/{booking_id}/confirm-payment")
async def admin_confirm_payment(booking_id: str, body: PaymentGuideRequest, request: Request, _=Depends(require_admin)):
    ok, message, booking = confirm_payment_state(booking_id, body.payment_note)
    if not ok:
        raise HTTPException(400, detail=message)
    log_action(booking_id, "booking_payment_confirmed", "manual_confirm", request.client.host if request.client else None)
    return {
        "ok": True,
        "message": f"{message}. 자동 알림은 보내지 않았습니다.",
        "data": booking,
        **_admin_no_send_delivery("manual_confirm"),
    }


@app.post("/admin/bookings/{booking_id}/location-guide")
async def admin_location_guide(booking_id: str, request: Request, _=Depends(require_admin)):
    booking = get_booking(booking_id)
    if not booking:
        raise HTTPException(404, detail="예약 신청을 찾을 수 없습니다.")
    guide = default_location_guide(booking)
    log_action(booking_id, "booking_location_guide_viewed", "manual_copy", request.client.host if request.client else None)
    return {
        "ok": True,
        "message": "장소 안내 문구를 만들었습니다. 신청자에게 자동 전송하지 않았습니다.",
        **_admin_no_send_delivery("manual_copy"),
        "location_guide": guide,
        "data": booking,
    }


@app.post("/admin/bookings/{booking_id}/free-guide")
async def admin_free_class_guide(booking_id: str, request: Request, _=Depends(require_admin)):
    booking = get_booking(booking_id)
    if not booking:
        raise HTTPException(404, detail="예약 신청을 찾을 수 없습니다.")
    guide = default_free_class_guide(booking)
    log_action(booking_id, "booking_free_guide_viewed", "manual_copy", request.client.host if request.client else None)
    return {
        "ok": True,
        "message": "무료강의 안내 문구를 만들었습니다. 신청자에게 자동 전송하지 않았습니다.",
        **_admin_no_send_delivery("manual_copy"),
        "free_guide": guide,
        "data": booking,
    }


@app.post("/admin/bookings/{booking_id}/refund-guide")
async def admin_refund_guide(booking_id: str, request: Request, _=Depends(require_admin)):
    booking = get_booking(booking_id)
    if not booking:
        raise HTTPException(404, detail="예약 신청을 찾을 수 없습니다.")
    guide = default_refund_guide(booking)
    log_action(booking_id, "booking_refund_guide_viewed", "manual_copy", request.client.host if request.client else None)
    return {
        "ok": True,
        "message": "환불 안내 문구를 만들었습니다. 신청자에게 자동 전송하지 않았습니다. 실제 환불 처리 여부는 운영자가 별도로 확인해야 합니다.",
        **_admin_no_send_delivery("manual_copy"),
        "refund_guide": guide,
        "data": booking,
    }


@app.get("/scheduler/status")
async def scheduler_status(_=Depends(require_admin)):
    jobs = []
    for job in scheduler.get_jobs():
        jobs.append({
            "id": job.id,
            "next_run": str(job.next_run_time) if job.next_run_time else None,
            "trigger": str(job.trigger),
        })
    return {"ok": True, "running": scheduler.running, "jobs": jobs}


@app.post("/scheduler/run")
async def scheduler_run(body: RunJobRequest, _=Depends(require_admin)):
    job_map = {
        "cleanup": job_cleanup,
        "expiry_warn": job_expiry_warning,
        "unlock_check": job_unlock_check,
        "weekly_report": job_weekly_report,
    }
    fn = job_map.get(body.job_id)
    if not fn:
        raise HTTPException(400, detail=f"알 수 없는 job_id: {body.job_id}. 가능: {list(job_map)}")
    fn()
    log.info(f"[manual-run] {body.job_id} 수동 실행")
    return {"ok": True, "message": f"{body.job_id} 실행 완료"}
