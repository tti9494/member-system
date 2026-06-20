import os
import httpx
import logging
import html
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

load_dotenv(dotenv_path=str(Path.home() / "member-system" / ".env"))

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
ADMIN_CHAT_ID = os.getenv("TELEGRAM_ADMIN_CHAT_ID", "")
TELEGRAM_NOTIFY_ENABLED = os.getenv("TELEGRAM_NOTIFY_ENABLED", "").lower() in {"1", "true", "yes", "on"}
TELEGRAM_BOOKING_NOTIFY_ENABLED = os.getenv(
    "TELEGRAM_BOOKING_NOTIFY_ENABLED",
    os.getenv("TELEGRAM_NOTIFY_ENABLED", ""),
).lower() in {"1", "true", "yes", "on"}
TELEGRAM_APPLICATION_NOTIFY_ENABLED = os.getenv(
    "TELEGRAM_APPLICATION_NOTIFY_ENABLED",
    os.getenv("TELEGRAM_BOOKING_NOTIFY_ENABLED", os.getenv("TELEGRAM_NOTIFY_ENABLED", "")),
).lower() in {"1", "true", "yes", "on"}
SERVICE_NAME = os.getenv("SERVICE_NAME", "AI 모임")
PUBLIC_BASE_URL = os.getenv("PUBLIC_BASE_URL", "https://apply.arsen-ai.com").rstrip("/")
KST = ZoneInfo("Asia/Seoul")

log = logging.getLogger("member-system")


def _configured_value(value: str | None) -> bool:
    text = (value or "").strip()
    if not text:
        return False
    lowered = text.lower()
    placeholders = (
        "your_",
        "placeholder",
        "token_here",
        "chat_id_here",
        "telegram_bot_token",
        "telegram_admin_chat_id",
        "telegram_chat_id",
    )
    return not any(marker in lowered for marker in placeholders)


def _is_configured() -> bool:
    return _configured_value(BOT_TOKEN) and _configured_value(ADMIN_CHAT_ID)


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


def _html(value: object) -> str:
    text = str(value or "").strip()
    return html.escape(text) if text else "-"


def _compact(value: object, limit: int = 160) -> str:
    text = str(value or "").replace("\r", "\n").strip()
    text = "\n".join(line.strip() for line in text.splitlines() if line.strip())
    if not text:
        return "-"
    if len(text) > limit:
        return f"{text[:limit].rstrip()}..."
    return text


def _presence(value: object) -> str:
    text = str(value or "").strip()
    return "입력 있음" if text else "-"


def _display(value: object, limit: int = 220) -> str:
    if isinstance(value, (list, tuple, set)):
        text = ", ".join(str(item).strip() for item in value if str(item).strip())
    else:
        text = str(value or "").replace("\r", "\n").strip()
    text = "\n".join(line.strip() for line in text.splitlines() if line.strip())
    if not text:
        return "-"
    if len(text) > limit:
        text = f"{text[:limit].rstrip()}..."
    return _html(text)


def _yes_no(value: object) -> str:
    if value is True or value == 1 or value == "1" or value == "true":
        return "예"
    if value is False or value == 0 or value == "0" or value == "false":
        return "아니오"
    return "-"


def _plan_type_label(plan_type: object) -> str:
    normalized = str(plan_type or "").strip().lower()
    return {
        "free": "무료강의",
        "full": "유료강의",
        "basic": "기본강의",
    }.get(normalized) or str(plan_type or "").strip() or "-"


def _contact_summary(name: object = None, phone: object = None) -> str:
    return f"{_html(_mask_name(str(name or '')))} ({_html(_mask_phone(str(phone or '')))})"


def _admin_url() -> str:
    return f"{PUBLIC_BASE_URL}/frontend/admin.html"


def _member_keyboard(member_id: str | None) -> dict | None:
    if not member_id:
        return None
    return {
        "inline_keyboard": [
            [
                {"text": "승인 + 코드 발급", "callback_data": f"arsen:approve:{member_id}"},
                {"text": "관리자 열기", "url": _admin_url()},
            ]
        ]
    }


def _booking_keyboard(booking_id: str | None) -> dict | None:
    if not booking_id:
        return None
    return {
        "inline_keyboard": [
            [
                {"text": "입금 안내", "callback_data": f"arsen:payguide:{booking_id}"},
                {"text": "입금 확인", "callback_data": f"arsen:confirm:{booking_id}"},
            ],
            [
                {"text": "장소 안내", "callback_data": f"arsen:location:{booking_id}"},
                {"text": "관리자 열기", "url": _admin_url()},
            ],
        ]
    }


def _stats_lines(stats: dict | None) -> list[str]:
    if not stats:
        return []
    return [
        "현황:",
        f"- 대기 인원: {int(stats.get('pending', 0) or 0)}명",
        f"- 승인 인원: {int(stats.get('approved', 0) or 0)}명",
        f"- 전체 신청: {int(stats.get('total', 0) or 0)}명",
        f"- 예약 신청: {int(stats.get('requested_bookings', stats.get('requested', 0)) or 0)}명",
        f"- 활성 예약: {int(stats.get('active_bookings', stats.get('active', 0)) or 0)}명",
    ]


def _parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    text = str(value).strip()
    if text.endswith("Z"):
        text = f"{text[:-1]}+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=KST)
    return parsed.astimezone(KST)


def _korean_time(value: datetime) -> str:
    ampm = "오전" if value.hour < 12 else "오후"
    hour = value.hour % 12 or 12
    minute = f" {value.minute:02d}분" if value.minute else ""
    return f"{ampm} {hour}시{minute}"


def _format_korean_datetime_range(starts_at: str | None, ends_at: str | None = None) -> str:
    start = _parse_datetime(starts_at)
    end = _parse_datetime(ends_at)
    if not start:
        return starts_at or "-"
    weekdays = "월화수목금토일"
    date_text = f"{start.year}년 {start.month}월 {start.day}일 ({weekdays[start.weekday()]})"
    time_text = _korean_time(start)
    if end:
        end_text = _korean_time(end)
        if end.date() != start.date():
            end_date = f"{end.month}월 {end.day}일 ({weekdays[end.weekday()]})"
            time_text = f"{time_text} - {end_date} {end_text}"
        else:
            time_text = f"{time_text} - {end_text}"
    return f"{date_text} {time_text}"


def _send_status(
    chat_id: str,
    text: str,
    enabled: bool | None = None,
    reply_markup: dict | None = None,
) -> str:
    is_enabled = TELEGRAM_NOTIFY_ENABLED if enabled is None else enabled
    if not is_enabled:
        log.info("[Telegram skip] disabled")
        return "disabled"
    if not _is_configured() or not chat_id:
        log.info("[Telegram skip] not_configured")
        return "not_configured"
    try:
        resp = httpx.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": text,
                "parse_mode": "HTML",
                "disable_web_page_preview": True,
                **({"reply_markup": reply_markup} if reply_markup else {}),
            },
            timeout=10,
        )
        return "ok" if resp.status_code == 200 else "failed"
    except Exception as e:
        print(f"[Telegram 오류] {e.__class__.__name__}")
        return "failed"


def _send(chat_id: str, text: str) -> bool:
    return _send_status(chat_id, text) == "ok"


def send_admin_message(text: str, reply_markup: dict | None = None, enabled: bool | None = None) -> str:
    return _send_status(ADMIN_CHAT_ID, text, enabled=enabled, reply_markup=reply_markup)


def answer_callback_query(callback_query_id: str, text: str, show_alert: bool = False) -> str:
    if not callback_query_id:
        return "missing_callback_id"
    if not TELEGRAM_NOTIFY_ENABLED and not TELEGRAM_APPLICATION_NOTIFY_ENABLED and not TELEGRAM_BOOKING_NOTIFY_ENABLED:
        return "disabled"
    if not _configured_value(BOT_TOKEN):
        return "not_configured"
    try:
        resp = httpx.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/answerCallbackQuery",
            json={
                "callback_query_id": callback_query_id,
                "text": text,
                "show_alert": show_alert,
            },
            timeout=10,
        )
        return "ok" if resp.status_code == 200 else "failed"
    except Exception as e:
        print(f"[Telegram 오류] {e.__class__.__name__}")
        return "failed"


def _application_lines(member: dict, raw_application: dict | None = None) -> list[str]:
    raw = raw_application or {}
    plan_label = _plan_type_label(raw.get("plan_type") or member.get("plan_type"))
    return [
        f"신청자: {_display(raw.get('name') or member.get('name'))}",
        f"이메일: {_display(raw.get('email'))}",
        f"연락처: {_display(raw.get('phone') or member.get('phone_masked'))}",
        f"신청ID: <code>{_html(member.get('id'))}</code>",
        f"상태: {_html(member.get('status', 'pending'))}",
        f"신청 구분: {_display(plan_label)}",
        f"등급: {_html(member.get('participation_grade'))}",
        f"성별/나이: {_display(raw.get('gender') or member.get('gender'))} / {_display(raw.get('age') or member.get('age'))}",
        f"직업/소속: {_display(raw.get('job') or member.get('job'))}",
        f"유입 경로: {_display(raw.get('referral_source') or member.get('referral_source'))}",
        f"AI 레벨: {_display(raw.get('ai_level') or member.get('ai_level'))}",
        f"사용 AI 도구: {_display(raw.get('ai_tools') or member.get('ai_tools'))}",
        f"AI 구독: {_display(raw.get('ai_subscription') or member.get('ai_subscription'))}",
        f"주당 AI 사용 시간: {_display(raw.get('ai_weekly_hours') or member.get('ai_weekly_hours'))}",
        f"AI 활용 분야: {_display(raw.get('ai_use_cases') or member.get('ai_use_cases'))}",
        f"모임 목적: {_display(raw.get('group_goals') or member.get('group_goals'))}",
        f"참여 방식: {_display(raw.get('participation_type') or member.get('participation_type'))}",
        f"참여 가능 지역: {_display(raw.get('region') or member.get('region'))}",
        f"참여 가능 시간: {_display(raw.get('available_time_slots') or member.get('available_time_slots'))}",
        f"선호 일정: {_display(raw.get('preferred_schedule') or member.get('preferred_schedule'))}",
        f"주 사용 기기: {_display(raw.get('main_device') or member.get('main_device'))}",
        f"코딩 가능: {_yes_no(raw.get('can_code') if 'can_code' in raw else member.get('can_code'))}",
        f"발표/강의 가능: {_yes_no(raw.get('can_present') if 'can_present' in raw else member.get('can_present'))}",
        f"보유 스킬: {_display(raw.get('skills') or member.get('skills'))}",
        f"기여 방식: {_display(raw.get('contribution') or member.get('contribution'))}",
        f"신청 이유: {_display(raw.get('reason') or member.get('reason'))}",
        f"단기 목표: {_display(raw.get('short_term_goal') or member.get('short_term_goal'))}",
        f"강의에서 해보고 싶은 내용: {_display(raw.get('desired_outcome') or member.get('desired_outcome'))}",
        f"준비 상태: {_display(raw.get('preparedness') or member.get('preparedness'))}",
        f"마케팅 동의: {_yes_no(raw.get('consent_marketing') if 'consent_marketing' in raw else member.get('consent_marketing'))}",
    ]


def notify_admin_new_apply(
    member: dict,
    booking: dict | None = None,
    storage_status: dict | None = None,
    stats: dict | None = None,
    raw_application: dict | None = None,
    lead_upgrade_from: str | None = None,
) -> str:
    plan_label = _plan_type_label((raw_application or {}).get("plan_type") or member.get("plan_type"))
    booking_id = booking.get("id") if booking else "-"
    booking_status = booking.get("status") if booking else "not_requested"
    source_label = "소식받기" if str(lead_upgrade_from or "").startswith("lead_") else _plan_type_label(lead_upgrade_from)
    heading = (
        f"<b>ARSEN {_html(source_label)}에서 {_html(plan_label)} 신청으로 변경</b>"
        if lead_upgrade_from
        else f"<b>ARSEN 신규 {_html(plan_label)} 신청</b>"
    )
    lines = [
        heading,
        *_application_lines(member, raw_application=raw_application),
        f"예약ID: {_html(booking_id)}",
        f"예약상태: {_html(booking_status)}",
    ]
    if lead_upgrade_from:
        lines.insert(1, f"전환 안내: 기존 {_html(source_label)} 리드를 신청자/멤버 목록의 {_html(plan_label)} 신청으로 승격했습니다.")
    if storage_status:
        lines.extend([
            "저장 상태:",
            f"- DB: {_html(storage_status.get('db'))}",
            f"- Sheets: {_html(storage_status.get('sheets'))}",
            f"- Backup: {_html(storage_status.get('backup'))}",
        ])
    lines.extend(_stats_lines(stats))
    return _send_status(
        ADMIN_CHAT_ID,
        "\n".join(lines),
        enabled=TELEGRAM_APPLICATION_NOTIFY_ENABLED,
        reply_markup=_member_keyboard(member.get("id")),
    )


def notify_admin_duplicate_apply(
    existing_member: dict,
    attempted: dict | None = None,
    stats: dict | None = None,
) -> str:
    attempted = attempted or {}
    plan_label = _plan_type_label(attempted.get("plan_type") or existing_member.get("plan_type"))
    lines = [
        f"<b>ARSEN 중복 신청 감지 - {_html(plan_label)}</b>",
        f"기존 신청ID: <code>{_html(existing_member.get('id'))}</code>",
        f"기존 신청자: {_contact_summary(existing_member.get('name'), existing_member.get('phone_masked'))}",
        f"기존 상태: {_html(existing_member.get('status'))}",
        f"중복 기준: {_html(existing_member.get('duplicate_source'))}",
        "",
        "이번 입력:",
        *_application_lines(existing_member, raw_application=attempted),
    ]
    lines.extend(_stats_lines(stats))
    return _send_status(
        ADMIN_CHAT_ID,
        "\n".join(lines),
        enabled=TELEGRAM_APPLICATION_NOTIFY_ENABLED,
        reply_markup=_member_keyboard(existing_member.get("id")),
    )


def _booking_summary_lines(booking: dict) -> list[str]:
    amount = booking.get("payment_amount_krw")
    amount_text = f"{int(amount):,}원" if isinstance(amount, (int, float)) else "-"
    request_rank = booking.get("request_rank")
    paid_rank = booking.get("paid_rank")
    schedule_time = _format_korean_datetime_range(
        booking.get("session_starts_at"),
        booking.get("session_ends_at"),
    )
    return [
        f"예약ID: {booking.get('id', '-')}",
        f"신청자: {_contact_summary(booking.get('applicant_name') or booking.get('member_name'), booking.get('phone_masked'))}",
        f"회원ID: {_html(booking.get('member_id'))}",
        f"일정: {_html(booking.get('session_title') or '-')}",
        f"시간: {schedule_time}",
        f"예약상태: {_html(booking.get('status', '-'))}",
        f"입금상태: {_html(booking.get('payment_status', '-'))}",
        f"금액: {amount_text}",
        f"순서: 신청 {request_rank or '-'} / 입금확정 {paid_rank or '-'}",
        f"목표/내용: {_presence(booking.get('desired_outcome'))}",
        f"준비상태: {_presence(booking.get('preparedness'))}",
    ]


def notify_booking_requested(member: dict, booking: dict, stats: dict | None = None) -> str:
    lines = ["<b>ARSEN 신규 예약 신청</b>", *(_booking_summary_lines(booking)), *_stats_lines(stats)]
    return _send_status(
        ADMIN_CHAT_ID,
        "\n".join(lines),
        enabled=TELEGRAM_BOOKING_NOTIFY_ENABLED,
        reply_markup=_booking_keyboard(booking.get("id")),
    )


def notify_booking_payment_guide(booking: dict) -> str:
    text = "<b>ARSEN 입금 안내 처리</b>\n" + "\n".join(_booking_summary_lines(booking))
    return _send_status(ADMIN_CHAT_ID, text, enabled=TELEGRAM_BOOKING_NOTIFY_ENABLED)


def notify_booking_payment_confirmed(booking: dict) -> str:
    text = "<b>ARSEN 입금 확인/예약 확정</b>\n" + "\n".join(_booking_summary_lines(booking))
    return _send_status(ADMIN_CHAT_ID, text, enabled=TELEGRAM_BOOKING_NOTIFY_ENABLED)


def notify_member_approved(member: dict, code: str, expires_at: str | None, phone: str) -> bool:
    """승인 시 신청자에게 알림 (전화번호 기반 텔레그램은 불가 → 관리자에게 전달 메시지로 대체)"""
    text = (
        f"<b>ARSEN 승인 + 코드 발급 완료</b>\n"
        f"수신: {_html(member.get('name'))}님 ({_html(phone)})\n\n"
        f"안녕하세요 {_html(member.get('name'))}님!\n"
        f"{_html(SERVICE_NAME)} 신청이 승인되었습니다.\n"
        f"접속 코드: <code>{_html(code)}</code>\n"
        f"유효기간: 없음"
    )
    return send_admin_message(text, enabled=TELEGRAM_APPLICATION_NOTIFY_ENABLED) == "ok"


def notify_member_rejected(member: dict, reason: str, phone: str) -> bool:
    text = (
        f"❌ 거절 처리\n"
        f"수신: {_html(member.get('name'))}님 ({_html(phone)})\n\n"
        f"안녕하세요 {_html(member.get('name'))}님.\n"
        f"이번에는 승인이 어렵습니다.\n"
        f"사유: {_html(reason)}"
    )
    return send_admin_message(text, enabled=TELEGRAM_APPLICATION_NOTIFY_ENABLED) == "ok"


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
