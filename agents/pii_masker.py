"""PII 마스킹 / sanitize 표준 모듈.

본 모듈은 응답 schema / log / 외부 채널 페이로드에서 평문 PII 노출을 회피하기 위한
순수 함수 집합입니다. DB / .env / 외부 호출 의존 0, stdlib 단독.

대상:
- mask_name: 한글/영문 이름 first-char + asterisk 마스킹 (보안 QA v1 §2.2 정합)
- mask_phone: dash 분할 의존성 제거 + 마지막 4자리 보존 fallback 강화
- mask_email: local + domain 마스킹 + TLD 보존
- sanitize_payment_note: length 200 절단 + 계좌/이메일/전화/token 패턴 치환
- mask_location_to_grade: 동/구 단위 grade 추출 (공개 schema 용)

선행 spec: /Users/yoon/ai-tools/docs/reports/work_bus/2026-05-09_member_applicant_pii_masking_preimplementation_check_autoplan_164.md §4
"""

from __future__ import annotations

import re
from typing import Optional

_NAME_LEN_MIN_FOR_MASK = 2
_PAYMENT_NOTE_MAX_LEN = 200

_RE_PHONE_DIGITS_ONLY = re.compile(r"^(\d{2,3})(\d{3,4})(\d{4})$")
_RE_PHONE_INTL = re.compile(r"^\+?(\d{1,3})[\s\-]?(\d{1,3})[\s\-]?(\d{3,4})[\s\-]?(\d{4})$")
_RE_EMAIL = re.compile(r"^([^@]+)@([^@]+)$")
_RE_DIGITS = re.compile(r"\D+")

_RE_PAYMENT_ACCOUNT = re.compile(r"\b\d{2,6}-\d{2,6}-\d{2,8}\b|\b\d{11,16}\b")
_RE_PAYMENT_EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
_RE_PAYMENT_PHONE = re.compile(r"\b01\d[\s\-]?\d{3,4}[\s\-]?\d{4}\b")
_RE_PAYMENT_TOKEN = re.compile(
    r"(?:Bearer\s+[A-Za-z0-9._\-]{8,})|(?:sk-[A-Za-z0-9_\-]{16,})|(?:ghp_[A-Za-z0-9]{16,})|(?:xoxb-[A-Za-z0-9\-]{16,})"
)


def mask_name(name: Optional[str]) -> str:
    """이름 마스킹 — first 1자 + 나머지 `*`. 빈 입력은 `""`."""
    if not name:
        return ""
    text = str(name).strip()
    if not text:
        return ""
    if " " in text:
        return " ".join(_mask_token(token) for token in text.split() if token)
    return _mask_token(text)


def _mask_token(token: str) -> str:
    if len(token) < _NAME_LEN_MIN_FOR_MASK:
        return token
    return token[0] + "*" * (len(token) - 1)


def mask_phone(phone: Optional[str]) -> str:
    """전화번호 마스킹 — 마지막 4자리 보존 + dash 비분할 입력 fallback.

    - `010-1234-5678` → `010-****-5678`
    - `01012345678` → `010-****-5678`
    - `+82-10-1234-5678` → `+82-10-****-5678`
    - `010 1234 5678` → `010-****-5678`
    - 빈 입력 → `""`
    """
    if not phone:
        return ""
    text = str(phone).strip()
    if not text:
        return ""

    if text.startswith("+"):
        m = _RE_PHONE_INTL.match(text)
        if m:
            cc, area, _mid, last = m.groups()
            return f"+{cc}-{area}-****-{last}"

    parts = text.split("-")
    if len(parts) == 3 and all(p.isdigit() for p in parts):
        return f"{parts[0]}-****-{parts[2]}"

    digits = _RE_DIGITS.sub("", text)
    m = _RE_PHONE_DIGITS_ONLY.match(digits)
    if m:
        head, _mid, last = m.groups()
        return f"{head}-****-{last}"

    if len(digits) >= 4:
        return f"***-****-{digits[-4:]}"
    return "***-****-****"


def mask_email(email: Optional[str]) -> str:
    """이메일 마스킹 — local first 1자 + 나머지 `*`, domain first 1자 + 나머지 `*`, TLD 보존.

    - `holong@example.com` → `h*****@e******.com`
    - `a@b.com` → `a@b.com`
    - `not_an_email` → `""`
    """
    if not email:
        return ""
    text = str(email).strip().lower()
    if not text or "@" not in text:
        return ""
    m = _RE_EMAIL.match(text)
    if not m:
        return ""
    local, domain = m.groups()
    if "." in domain:
        host, tld = domain.rsplit(".", 1)
    else:
        host, tld = domain, ""
    masked_local = _mask_token(local) if local else ""
    masked_host = _mask_token(host) if host else ""
    if tld:
        return f"{masked_local}@{masked_host}.{tld}"
    return f"{masked_local}@{masked_host}"


def sanitize_payment_note(note: Optional[str], max_len: int = _PAYMENT_NOTE_MAX_LEN) -> str:
    """입금자명 / 거래 메모 sanitize — 패턴 치환 + length 절단.

    치환 우선순위: TOKEN → ACCOUNT → EMAIL → PHONE.
    250자 초과 시 250자 절단 + `...` 표기.
    """
    if not note:
        return ""
    text = str(note)
    text = _RE_PAYMENT_TOKEN.sub("<TOKEN>", text)
    text = _RE_PAYMENT_PHONE.sub("<PHONE>", text)
    text = _RE_PAYMENT_ACCOUNT.sub("<ACCT>", text)
    text = _RE_PAYMENT_EMAIL.sub("<EMAIL>", text)
    if len(text) > max_len:
        text = text[:max_len] + "..."
    return text


_LOCATION_DISTRICT_PATTERN = re.compile(r"([가-힣]{2,6}(?:구|시|군))")
_LOCATION_DONG_PATTERN = re.compile(r"([가-힣]{2,6}동)")


def mask_location_to_grade(location: Optional[str]) -> str:
    """장소 평문 → 동/구 단위 grade 추출.

    매칭 실패 시 빈 문자열 반환 (평문 fallback 회피).
    """
    if not location:
        return ""
    text = str(location).strip()
    if not text:
        return ""
    m = _LOCATION_DISTRICT_PATTERN.search(text)
    if m:
        return m.group(1).rstrip("구시군")
    m = _LOCATION_DONG_PATTERN.search(text)
    if m:
        return m.group(1).rstrip("동")
    return ""
