import os
import sys
import json
import logging
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

load_dotenv(dotenv_path=str(Path.home() / "member-system" / ".env"))
sys.path.insert(0, str(Path.home() / "member-system"))

from db import init_db
from agents.validator import validate
from agents.duplicate_checker import check_duplicate
from agents.consent_checker import check_consent
from agents.db_manager import (
    create_member, get_member, list_members, update_status,
    blacklist_member, get_stats, save_to_sheets, log_action,
    backup_database, cleanup_expired_codes, get_expiring_soon, get_storage_status,
    release_expired_locks,
)
from agents.booking_manager import (
    DEFAULT_PRICE, confirm_payment_state, create_booking, create_session, default_payment_guide,
    get_booking, get_session, list_bookings, list_sessions, refresh_session_counts,
    seed_default_sunday_sessions, send_payment_guide_state, session_acceptance, set_booking_state,
    update_session,
)
from agents.code_generator import generate_code, verify_code, revoke_code, regenerate_code
from agents.telegram_notifier import (
    notify_admin_new_apply, notify_member_approved, notify_member_rejected,
    notify_expiring_codes, notify_cleanup_result, send_weekly_report,
)
from agents.meta_validator import meta_validate
from agents.security_checker import check_security
from agents.encryptor import encrypt_data, decrypt_phone  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("member-system")

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
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

FRONTEND_DIR = Path.home() / "member-system" / "frontend"
app.mount("/frontend", StaticFiles(directory=str(FRONTEND_DIR)), name="frontend")

# ── 관리자 인증 ──────────────────────────────────────

ADMIN_API_KEY = os.getenv("ADMIN_API_KEY", "")


def require_admin(request: Request):
    key = request.headers.get("X-Admin-Key", "")
    if not ADMIN_API_KEY:
        log.error("ADMIN_API_KEY 미설정 — 관리자 엔드포인트 차단")
        raise HTTPException(status_code=503, detail="관리자 인증 설정이 필요합니다.")
    if not key or key != ADMIN_API_KEY:
        raise HTTPException(status_code=401, detail="관리자 인증 필요 (X-Admin-Key 헤더)")


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


class RejectRequest(BaseModel):
    reason: str


class RunJobRequest(BaseModel):
    job_id: str  # cleanup | expiry_warn | unlock_check | weekly_report


class VerifyCodeRequest(BaseModel):
    code: str
    member_id: str


class SessionRequest(BaseModel):
    title: str = "AI 기초 셋팅 및 컨설팅 강의 1:4"
    description: Optional[str] = None
    program_type: str = "ai_basic_setup"
    audience_level: str = "all"
    starts_at: str
    ends_at: str
    timezone: str = "Asia/Seoul"
    capacity_min: int = 4
    capacity_max: int = 5
    price_krw: int = 50000
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


class PaymentGuideRequest(BaseModel):
    payment_note: Optional[str] = None


class SeedSessionsRequest(BaseModel):
    weeks: int = 4


# ── 유틸 ────────────────────────────────────────────

def _grade_count(data: dict) -> str:
    """선택 항목 입력 개수 기반 등급 계산"""
    optional_fields = [
        "ai_tools", "ai_subscription", "ai_weekly_hours", "ai_use_cases",
        "group_goals", "short_term_goal", "participation_type", "preferred_schedule",
        "region", "main_device", "can_code", "can_present", "skills", "contribution",
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


# ── 엔드포인트 ──────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <html><body>
    <h2>Member System</h2>
    <ul>
      <li><a href="/frontend/join-basic.html">체험 신청 (Basic)</a></li>
      <li><a href="/frontend/join-full.html">정식 신청 (Full)</a></li>
      <li><a href="/frontend/privacy.html">개인정보처리방침</a></li>
    </ul>
    </body></html>
    """


@app.get("/sessions")
async def public_sessions():
    rows = list_sessions(include_closed=False)
    safe_rows = []
    for row in rows:
        safe = dict(row)
        safe.pop("payment_guide", None)
        safe_rows.append(safe)
    return {
        "ok": True,
        "data": safe_rows,
        "total": len(safe_rows),
        "workflow": "신청 → 운영자 확인 → 자리 확정 안내",
    }


@app.post("/apply")
async def apply(req: ApplyRequest, request: Request):
    data = req.model_dump()
    client_ip = request.client.host if request.client else "unknown"
    selected_session = get_session(data.get("session_id")) if data.get("session_id") else None
    if data.get("session_id"):
        ok, reason = session_acceptance(selected_session)
        if not ok:
            raise HTTPException(400, detail=reason)

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

    # 4. 중복 확인
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

    booking_id = None
    booking_next_steps = [
        "운영자가 신청 내용과 정원을 확인합니다.",
        "자리 확정 여부와 다음 안내를 개별 전달합니다.",
    ]
    if data.get("session_id") or data.get("desired_outcome") or data.get("preparedness"):
        amount = int(selected_session["price_krw"]) if selected_session else DEFAULT_PRICE
        booking_id = create_booking({
            "session_id": data.get("session_id"),
            "member_id": member_id,
            "applicant_name": data["name"],
            "phone_masked": member.get("phone_masked", ""),
            "desired_outcome": data.get("desired_outcome") or data.get("short_term_goal") or data.get("reason"),
            "preparedness": data.get("preparedness") or "",
            "status": "requested",
            "payment_status": "not_sent",
            "payment_amount_krw": amount,
        })
        refresh_session_counts(data.get("session_id"))
        log_action(member_id, "booking_requested", f"booking_id={booking_id}", client_ip)

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

    # 13. Hermes/Telegram 알림
    booking = get_booking(booking_id) if booking_id else None
    hermes_ok = notify_admin_new_apply(
        member,
        booking=booking,
        storage_status={
            "db": "ok",
            "sheets": "ok" if sheets_ok else "not_configured_or_failed",
            "backup": f"{backup_result.get('ok_count', 0)} ok / {backup_result.get('failed_count', 0)} failed",
        },
    )
    log_action(member_id, "hermes_notify", "ok" if hermes_ok else "not_configured_or_failed", client_ip)

    return {
        "ok": True,
        "message": "신청이 접수되었습니다.",
        "member_id": member_id,
        "booking_id": booking_id,
        "next_steps": booking_next_steps,
        "reservation": {
            "status": "requested",
            "message": "신청이 접수되었습니다. 운영자가 인원과 일정을 확인한 뒤 자리 확정 안내를 드립니다.",
            "amount_krw": int(selected_session["price_krw"]) if selected_session else DEFAULT_PRICE,
        } if booking_id else None,
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
    notify_member_approved(member, code, member["code_expires_at"], phone)
    log_action(member_id, "approve", f"code_issued", request.client.host if request.client else None)

    return {"ok": True, "message": "승인 완료", "code": code, "expires_at": member["code_expires_at"]}


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


@app.post("/verify-code")
async def verify(body: VerifyCodeRequest, request: Request):
    result = verify_code(body.code, body.member_id)
    action = "code_used" if result["ok"] else "code_failed"
    log_action(body.member_id, action, None, request.client.host if request.client else None)
    return result


@app.post("/regen-code/{member_id}")
async def regen(member_id: str, request: Request, _=Depends(require_admin)):
    member = get_member(member_id)
    if not member:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    code = regenerate_code(member_id)
    member = get_member(member_id)
    phone = decrypt_phone(member["phone_encrypted"])
    notify_member_approved(member, code, member["code_expires_at"], phone)
    log_action(member_id, "code_issued", "재발급", request.client.host if request.client else None)
    return {"ok": True, "code": code, "expires_at": member["code_expires_at"]}


@app.post("/blacklist/{member_id}")
async def add_blacklist(member_id: str, request: Request, _=Depends(require_admin)):
    member = get_member(member_id)
    if not member:
        raise HTTPException(404, detail="신청자를 찾을 수 없습니다.")
    blacklist_member(member_id)
    log_action(member_id, "blacklist", None, request.client.host if request.client else None)
    return {"ok": True, "message": "블랙리스트 등록 완료"}


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
    return {"ok": True, "data": member}


@app.get("/stats")
async def stats():
    data = get_stats()
    data["expiring_7d"] = len(get_expiring_soon(days=7))
    return {"ok": True, "data": data}


@app.get("/admin/storage-status")
async def admin_storage_status(_=Depends(require_admin)):
    return {"ok": True, "data": get_storage_status()}


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
    ids = seed_default_sunday_sessions(body.weeks)
    log_action("booking", "session_seed_default_sunday", f"created={len(ids)}", request.client.host if request.client else None)
    return {"ok": True, "created": len(ids), "ids": ids}


@app.post("/admin/sessions/{session_id}")
async def admin_update_session(session_id: str, body: SessionUpdateRequest, request: Request, _=Depends(require_admin)):
    updates = {k: v for k, v in body.model_dump().items() if v is not None}
    ok = update_session(session_id, updates)
    if not ok:
        raise HTTPException(404, detail="세션을 찾을 수 없거나 변경할 값이 없습니다.")
    log_action(session_id, "session_update", ",".join(sorted(updates)), request.client.host if request.client else None)
    return {"ok": True, "data": get_session(session_id)}


@app.get("/admin/bookings")
async def admin_bookings(
    status: Optional[str] = None,
    session_id: Optional[str] = None,
    _=Depends(require_admin),
):
    rows = list_bookings(status=status, session_id=session_id)
    return {"ok": True, "data": rows, "total": len(rows)}


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
    return {"ok": True, "data": list_bookings()}


@app.get("/admin/bookings/{booking_id}")
async def admin_booking_detail(booking_id: str, _=Depends(require_admin)):
    booking = get_booking(booking_id)
    if not booking:
        raise HTTPException(404, detail="예약 신청을 찾을 수 없습니다.")
    return {"ok": True, "data": booking}


@app.post("/admin/bookings/{booking_id}/send-payment-guide")
async def admin_send_payment_guide(booking_id: str, body: PaymentGuideRequest, request: Request, _=Depends(require_admin)):
    updated = send_payment_guide_state(booking_id, body.payment_note)
    if not updated:
        raise HTTPException(404, detail="예약 신청을 찾을 수 없습니다.")
    log_action(booking_id, "booking_payment_guide_sent", "manual_copy", request.client.host if request.client else None)
    return {
        "ok": True,
        "message": "입금 안내 상태로 변경했습니다. 아래 문구를 신청자에게 전달하세요.",
        "payment_guide": updated.get("payment_note") or default_payment_guide(None, updated),
        "data": updated,
    }


@app.post("/admin/bookings/{booking_id}/confirm-payment")
async def admin_confirm_payment(booking_id: str, body: PaymentGuideRequest, request: Request, _=Depends(require_admin)):
    ok, message, booking = confirm_payment_state(booking_id, body.payment_note)
    if not ok:
        raise HTTPException(400, detail=message)
    log_action(booking_id, "booking_payment_confirmed", "manual_confirm", request.client.host if request.client else None)
    return {"ok": True, "message": message, "data": booking}


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
