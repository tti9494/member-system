import os
import sys
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
    cleanup_expired_codes, get_expiring_soon, release_expired_locks,
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


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    log.info("스케줄러 시작 — cleanup(일00:00) / expiry_warn(일10:00) / unlock(매시) / weekly_report(월09:00)")
    # 서버 시작 직후 잠금 해제 1회 즉시 실행
    job_unlock_check()
    yield
    scheduler.shutdown()
    log.info("스케줄러 종료")


app = FastAPI(title="Member System", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8100", "http://127.0.0.1:8100"],
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
        log.warning("ADMIN_API_KEY 미설정 — 관리자 인증 비활성화 (개발 모드)")
        return
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


# ── 유틸 ────────────────────────────────────────────

def _grade_count(data: dict) -> str:
    """선택 항목 입력 개수 기반 등급 계산"""
    optional_fields = [
        "ai_tools", "ai_subscription", "ai_weekly_hours", "ai_use_cases",
        "group_goals", "short_term_goal", "participation_type", "preferred_schedule",
        "region", "main_device", "can_code", "can_present", "skills", "contribution",
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
      <li><a href="/docs">API 문서</a></li>
    </ul>
    </body></html>
    """


@app.post("/apply")
async def apply(req: ApplyRequest, request: Request):
    data = req.model_dump()
    client_ip = request.client.host if request.client else "unknown"

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
    save_to_sheets(sheets_data)

    # 11. 텔레그램 알림
    member = get_member(member_id)
    notify_admin_new_apply(member)

    # 12. 이력 기록
    log_action(member_id, "apply", f"plan={data['plan_type']}, grade={grade}", client_ip)

    return {"ok": True, "message": "신청이 접수되었습니다.", "member_id": member_id}


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
