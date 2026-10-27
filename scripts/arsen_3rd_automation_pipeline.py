#!/usr/bin/env python3
"""ARSEN 3기 수강생 접수·운영 자동화 파이프라인 (Automated Enrollment & Ops).

기능:
1. 3기 4주 정규 세션 생성 및 시드 (토요일 14:00~17:00, 180분, 25만 원)
2. 수강 신청서 접수, 데이터 정규화, AES-256 암호화 및 DB 등록
3. 슬랙 #ai 채널 실시간 신청 알림 생성 및 연동
4. 입금 확인 및 수강 확정 처리
5. 수강생 명부(Roster) 요약 및 통계 리포트
"""

from __future__ import annotations

import argparse
import json
import sys
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import db
from agents import booking_manager, db_manager
from agents.encryptor import (
    encrypt_email,
    encrypt_phone,
    hash_email,
    hash_phone,
    mask_phone,
)

KST = ZoneInfo("Asia/Seoul")

# ARSEN 3기 공식 메타데이터
ARSEN_3RD_TITLE = "ARSEN AI 결과물 제작 실전 초급 3기 (4주 완성)"
ARSEN_3RD_DESCRIPTION = (
    "AI 도구를 활용해 4주 만에 나만의 블로그, 숏폼 영상, 자동화 파이프라인, 포트폴리오 웹페이지까지 "
    "실전 결과물을 완성하는 소수정예 실습 코칭반입니다.\n"
    "1주차: Claude Artifacts 블로그 초안 및 프롬프트 구조화\n"
    "2주차: Creator Radar 숏폼 영상 기획 및 AI 이미지 생성\n"
    "3주차: n8n 기초 자동화 파이프라인 및 비디오 합성\n"
    "4주차: 나만의 웹페이지 배포 및 AI 에이전트 쇼케이스"
)
ARSEN_3RD_PRICE = 250000
ARSEN_3RD_CAPACITY_MIN = 3
ARSEN_3RD_CAPACITY_MAX = 8
ARSEN_3RD_LOCATION = "강남/영등포 오프라인 스튜디오 & 라이브 온라인 병행"
ARSEN_3RD_MATERIALS = "개인 노트북, 충전기, AI 서비스 계정(Claude, ChatGPT 등)"


def seed_arsen_3rd_sessions(
    weeks: int = 4,
    start_date: Optional[str] = None,
    time_slot: tuple[int, int] = (14, 17),
) -> List[Dict[str, Any]]:
    """ARSEN 3기 4주 토요일 세션을 생성하거나 조회합니다."""
    if start_date:
        base_dt = datetime.fromisoformat(start_date).replace(tzinfo=KST)
    else:
        # 가장 가까운 다가오는 토요일 계산
        now_local = datetime.now(KST)
        days_until_saturday = (5 - now_local.weekday()) % 7
        if days_until_saturday == 0:
            days_until_saturday = 7
        base_dt = now_local + timedelta(days=days_until_saturday)

    created_sessions: List[Dict[str, Any]] = []
    existing = booking_manager.list_sessions(include_closed=True)
    existing_by_start = {s["starts_at"]: s for s in existing}

    for week_idx in range(weeks):
        session_day = base_dt + timedelta(days=7 * week_idx)
        start_h, end_h = time_slot
        starts_at = session_day.replace(hour=start_h, minute=0, second=0, microsecond=0).isoformat()
        ends_at = session_day.replace(hour=end_h, minute=0, second=0, microsecond=0).isoformat()

        session_title = f"{ARSEN_3RD_TITLE} - {week_idx + 1}주차"
        session_data = {
            "title": session_title,
            "description": ARSEN_3RD_DESCRIPTION,
            "program_type": "arsen_paid_beginner_3",
            "audience_level": "beginner",
            "starts_at": starts_at,
            "ends_at": ends_at,
            "timezone": "Asia/Seoul",
            "capacity_min": ARSEN_3RD_CAPACITY_MIN,
            "capacity_max": ARSEN_3RD_CAPACITY_MAX,
            "price_krw": ARSEN_3RD_PRICE,
            "location": ARSEN_3RD_LOCATION,
            "materials": ARSEN_3RD_MATERIALS,
            "status": "open",
        }

        existing_sess = existing_by_start.get(starts_at)
        if existing_sess:
            created_sessions.append(existing_sess)
        else:
            sess_id = booking_manager.create_session(session_data)
            full_sess = booking_manager.get_session(sess_id) or {"id": sess_id, **session_data}
            created_sessions.append(full_sess)
            existing_by_start[starts_at] = full_sess

    return created_sessions


def process_arsen_3rd_application(
    name: str,
    phone: str,
    email: str,
    session_id: str,
    job: str = "미입력",
    ai_level: str = "입문",
    desired_outcome: str = "AI 실전 결과물 완성",
    ip_address: str = "127.0.0.1",
) -> Dict[str, Any]:
    """수강 신청 접수, DB 등록, 마스킹 및 슬랙 알림 페이로드를 생성합니다."""
    clean_phone = phone.strip()
    clean_email = email.strip()
    clean_name = name.strip()

    now_utc = datetime.now(timezone.utc).isoformat()
    p_masked = mask_phone(clean_phone)
    p_enc = encrypt_phone(clean_phone)
    p_hash = hash_phone(clean_phone)
    e_enc = encrypt_email(clean_email)
    e_hash = hash_email(clean_email)

    # 1. 회원 등록 (또는 기존 회원 조회)
    existing_member = db_manager.get_latest_member_by_phone_hash(p_hash)
    if existing_member:
        member_id = existing_member["id"]
        db_manager.update_member(
            member_id,
            {
                "name": clean_name,
                "job": job,
                "ai_level": ai_level,
                "desired_outcome": desired_outcome,
            },
        )
    else:
        member_id = db_manager.create_member(
            {
                "name": clean_name,
                "email_encrypted": e_enc,
                "email_hash": e_hash,
                "phone_masked": p_masked,
                "phone_encrypted": p_enc,
                "phone_hash": p_hash,
                "gender": "미지정",
                "age": 30,
                "job": job,
                "referral_source": "ARSEN_3RD_RECRUIT",
                "reason": f"ARSEN 3기 수강 신청: {desired_outcome}",
                "ai_level": ai_level,
                "plan_type": "paid_course",
                "consent_personal": True,
                "consent_marketing": False,
                "consent_at": now_utc,
                "consent_version": "arsen-3rd-v1",
                "participation_grade": "신청",
                "desired_outcome": desired_outcome,
                "preparedness": "노트북 준비 완료",
            }
        )
        db_manager.log_action(member_id, "apply", "ARSEN 3기 신청 접수", ip_address)

    # 2. 예약/수강신청 생성
    session = booking_manager.get_session(session_id)
    if not session:
        raise ValueError(f"세션을 찾을 수 없습니다: {session_id}")

    booking_id = booking_manager.create_booking(
        {
            "session_id": session_id,
            "member_id": member_id,
            "applicant_name": clean_name,
            "phone_masked": p_masked,
            "desired_outcome": desired_outcome,
            "preparedness": "노트북 준비 완료",
            "status": "requested",
            "payment_status": "not_sent",
            "payment_amount_krw": session.get("price_krw", ARSEN_3RD_PRICE),
        }
    )
    booking_manager.refresh_session_counts(session_id)
    db_manager.log_action(member_id, "booking_requested", f"booking_id={booking_id}", ip_address)

    # 3. 입금 안내 상태 전환
    booking_manager.send_payment_guide_state(booking_id)

    # 4. 슬랙 채널 알림 메시지 (보안 게이트 준수: 마스킹 연락처만 사용)
    slack_notification = (
        f"🎉 *[ARSEN 3기 신규 수강 신청 접수]*\n"
        f"• *신청자*: {clean_name} 님\n"
        f"• *연락처*: `{p_masked}`\n"
        f"• *강의*: {session.get('title')}\n"
        f"• *수강료*: {int(session.get('price_krw', ARSEN_3RD_PRICE)):,}원\n"
        f"• *수강 목적*: {desired_outcome}\n"
        f"• *상태*: 💳 입금 안내 발송 완료 (입금 대기)\n"
        f"• *예약 ID*: `{booking_id}`"
    )

    # 5. 수강생용 입금 및 사전 준비 안내 텍스트
    guide_for_student = (
        f"안녕하세요, {clean_name} 님! ARSEN AI 결과물 제작 실전 초급 3기에 신청해 주셔서 감사합니다.\n\n"
        f"📌 [신청 내역]\n"
        f"- 과정: {session.get('title')}\n"
        f"- 수강료: {int(session.get('price_krw', ARSEN_3RD_PRICE)):,}원\n"
        f"- 장소: {session.get('location')}\n\n"
        f"💳 [입금 안내]\n"
        f"- 계좌: 카카오뱅크 (운영자 계좌)\n"
        f"- 입금자명: {clean_name}\n"
        f"- 입금 확인 후 최종 수강 확정 안내 및 1주차 사전 준비 체크리스트를 전달드립니다."
    )

    return {
        "ok": True,
        "member_id": member_id,
        "booking_id": booking_id,
        "session_id": session_id,
        "applicant_name": clean_name,
        "phone_masked": p_masked,
        "slack_notification": slack_notification,
        "student_guide": guide_for_student,
    }


def confirm_arsen_3rd_payment(
    booking_id: str,
    operator_note: str = "운영자 입금 확인",
) -> Dict[str, Any]:
    """수강료 입금을 확인하고 수강을 공식 확정합니다."""
    ok, message, confirmed_booking = booking_manager.confirm_payment_state(
        booking_id,
        operator_note,
    )
    if not ok or not confirmed_booking:
        return {"ok": False, "message": message}

    session_id = confirmed_booking["session_id"]
    session = booking_manager.get_session(session_id) or {}
    confirmed_count = session.get("confirmed_booking_count", 0)

    applicant_name = confirmed_booking.get("applicant_name", "수강생")

    confirmation_notice = (
        f"✅ *[ARSEN 3기 수강 확정 완료]*\n"
        f"• *수강생*: {applicant_name} 님\n"
        f"• *과정*: {session.get('title')}\n"
        f"• *현재 확정 인원*: {confirmed_count}/{session.get('capacity_max', 8)}명\n"
        f"• *메모*: {operator_note}\n"
        f"• *다음 조치*: 1주차 Claude 실습 사전 가이드 발송"
    )

    return {
        "ok": True,
        "message": message,
        "booking_id": booking_id,
        "applicant_name": applicant_name,
        "confirmed_count": confirmed_count,
        "confirmation_notice": confirmation_notice,
    }


def get_arsen_3rd_roster(session_id: Optional[str] = None) -> List[Dict[str, Any]]:
    """수강생 명단을 안전하게 조회합니다."""
    bookings = booking_manager.list_bookings(session_id=session_id)
    roster = []
    for b in bookings:
        roster.append({
            "booking_id": b["id"],
            "session_id": b["session_id"],
            "applicant_name": b.get("applicant_name"),
            "phone_masked": b.get("phone_masked"),
            "status": b.get("status"),
            "payment_status": b.get("payment_status"),
            "payment_amount_krw": b.get("payment_amount_krw"),
            "created_at": b.get("created_at"),
        })
    return roster


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ARSEN 3기 수강생 운영 자동화 파이프라인")
    parser.add_argument("--action", choices=["seed", "apply", "confirm", "roster"], default="seed")
    parser.add_argument("--weeks", type=int, default=4)
    parser.add_argument("--booking-id", type=str, default="")
    parser.add_argument("--name", type=str, default="테스트 수강생")
    parser.add_argument("--phone", type=str, default="010-1234-5678")
    parser.add_argument("--email", type=str, default="test@example.com")
    parser.add_argument("--session-id", type=str, default="")

    args = parser.parse_args()
    db.init_db()

    if args.action == "seed":
        sessions = seed_arsen_3rd_sessions(weeks=args.weeks)
        print(json.dumps({"ok": True, "count": len(sessions), "sessions": sessions}, ensure_ascii=False, indent=2))
    elif args.action == "apply":
        if not args.session_id:
            sess_list = seed_arsen_3rd_sessions(weeks=1)
            args.session_id = sess_list[0]["id"]
        res = process_arsen_3rd_application(args.name, args.phone, args.email, args.session_id)
        print(json.dumps(res, ensure_ascii=False, indent=2))
    elif args.action == "confirm":
        if not args.booking_id:
            print(json.dumps({"ok": False, "error": "--booking-id 필요"}, ensure_ascii=False))
            sys.exit(1)
        res = confirm_arsen_3rd_payment(args.booking_id)
        print(json.dumps(res, ensure_ascii=False, indent=2))
    elif args.action == "roster":
        roster = get_arsen_3rd_roster(args.session_id or None)
        print(json.dumps({"ok": True, "count": len(roster), "roster": roster}, ensure_ascii=False, indent=2))
