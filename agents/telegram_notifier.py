import os
import httpx
import logging
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=str(Path.home() / "member-system" / ".env"))

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
ADMIN_CHAT_ID = os.getenv("TELEGRAM_ADMIN_CHAT_ID", "")
TELEGRAM_NOTIFY_ENABLED = os.getenv("TELEGRAM_NOTIFY_ENABLED", "").lower() in {"1", "true", "yes", "on"}
SERVICE_NAME = os.getenv("SERVICE_NAME", "AI 모임")

log = logging.getLogger("member-system")


def _is_configured() -> bool:
    return bool(
        BOT_TOKEN
        and BOT_TOKEN != "your_bot_token_here"
        and ADMIN_CHAT_ID
        and ADMIN_CHAT_ID != "your_chat_id_here"
    )


def _mask_name(value: str | None) -> str:
    if not value:
        return "-"
    text = str(value).strip()
    if len(text) <= 1:
        return "*"
    if len(text) == 2:
        return f"{text[0]}*"
    return f"{text[0]}{'*' * (len(text) - 2)}{text[-1]}"


def _mask_phone(value: str | None) -> str:
    if not value:
        return "-"
    text = str(value).strip()
    if "*" in text:
        return text
    digits = "".join(ch for ch in text if ch.isdigit())
    if len(digits) < 4:
        return "****"
    return f"***-****-{digits[-4:]}"


def _send_status(chat_id: str, text: str) -> str:
    if not TELEGRAM_NOTIFY_ENABLED:
        log.info("[Telegram skip] disabled")
        return "disabled"
    if not _is_configured() or not chat_id:
        log.info("[Telegram skip] not_configured")
        return "not_configured"
    try:
        resp = httpx.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": text, "parse_mode": "HTML"},
            timeout=10,
        )
        return "ok" if resp.status_code == 200 else "failed"
    except Exception as e:
        print(f"[Telegram 오류] {e.__class__.__name__}")
        return "failed"


def _send(chat_id: str, text: str) -> bool:
    return _send_status(chat_id, text) == "ok"


def notify_admin_new_apply(member: dict, booking: dict | None = None, storage_status: dict | None = None) -> str:
    booking_id = booking.get("id") if booking else "-"
    booking_status = booking.get("status") if booking else "not_requested"
    text = (
        "Hermes 신규 신청\n"
        f"이름: {_mask_name(member.get('name'))}\n"
        f"연락처: {_mask_phone(member.get('phone_masked'))}\n"
        f"신청ID: {member.get('id')}\n"
        f"신청상태: {member.get('status', 'pending')}\n"
        f"예약ID: {booking_id}\n"
        f"예약상태: {booking_status}"
    )
    return _send_status(ADMIN_CHAT_ID, text)


def notify_member_approved(member: dict, code: str, expires_at: str, phone: str) -> bool:
    """승인 시 신청자에게 알림 (전화번호 기반 텔레그램은 불가 → 관리자에게 전달 메시지로 대체)"""
    text = (
        f"✅ 승인 완료\n"
        f"수신: {member.get('name')}님 ({phone})\n\n"
        f"안녕하세요 {member.get('name')}님!\n"
        f"{SERVICE_NAME} 신청이 승인되었습니다.\n"
        f"접속 코드: <code>{code}</code>\n"
        f"유효기간: {expires_at}"
    )
    return _send(ADMIN_CHAT_ID, text)


def notify_member_rejected(member: dict, reason: str, phone: str) -> bool:
    text = (
        f"❌ 거절 처리\n"
        f"수신: {member.get('name')}님 ({phone})\n\n"
        f"안녕하세요 {member.get('name')}님.\n"
        f"이번에는 승인이 어렵습니다.\n"
        f"사유: {reason}"
    )
    return _send(ADMIN_CHAT_ID, text)


def notify_expiring_codes(expiring: list) -> bool:
    if not expiring:
        return True
    lines = "\n".join(
        f"  • {m['name']} ({m['phone_masked']}) — {m['code_expires_at'][:10]}"
        for m in expiring
    )
    text = f"⏰ 코드 만료 7일 전 알림\n총 {len(expiring)}명\n{lines}"
    return _send(ADMIN_CHAT_ID, text)


def notify_cleanup_result(cleaned: int, released: int) -> bool:
    if cleaned == 0 and released == 0:
        return True
    text = (
        f"🧹 자동 정리 완료\n"
        f"만료 코드 무효화: {cleaned}건\n"
        f"코드 잠금 해제: {released}건"
    )
    return _send(ADMIN_CHAT_ID, text)


def send_weekly_report(stats: dict) -> bool:
    grade_lines = ""
    for grade, cnt in stats.get("grades", {}).items():
        grade_lines += f"  {grade}: {cnt}명\n"

    text = (
        f"📊 주간 멤버 리포트\n"
        f"신규 신청: {stats.get('pending', 0)}명 "
        f"(basic: {stats.get('basic', 0)} / full: {stats.get('full', 0)})\n"
        f"승인: {stats.get('approved', 0)}명 | 거절: {stats.get('rejected', 0)}명\n"
        f"누적: {stats.get('total', 0)}명\n\n"
        f"등급별 현황:\n{grade_lines}"
    )
    return _send(ADMIN_CHAT_ID, text)
