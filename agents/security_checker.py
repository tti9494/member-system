import re
from typing import Any

# SQL injection 패턴 (단어 경계 + 실제 위험 패턴 위주)
SQL_PATTERNS = re.compile(
    r"(--|\/\*|\*\/|xp_|\bUNION\b|\bSELECT\b.{0,30}\bFROM\b|\bINSERT\b.{0,20}\bINTO\b"
    r"|\bUPDATE\b.{0,20}\bSET\b|\bDELETE\b.{0,20}\bFROM\b|\bDROP\b.{0,10}\bTABLE\b"
    r"|\bEXEC\b|\bEXECUTE\b|\bDECLARE\b|\bWAITFOR\b)",
    re.IGNORECASE | re.DOTALL,
)

# XSS 패턴
XSS_PATTERNS = re.compile(
    r"(<script|javascript:|on\w+=|<iframe|<object|<embed|<link|<meta|vbscript:)",
    re.IGNORECASE,
)

# 의심 이메일 도메인
SUSPICIOUS_DOMAINS = {"mailinator.com", "guerrillamail.com", "10minutemail.com", "throwam.com", "yopmail.com"}

# 필드별 최대 길이
MAX_LENGTHS = {
    "name": 50,
    "email": 100,
    "phone": 20,
    "job": 100,
    "reason": 2000,
    "ai_subscription": 200,
    "ai_weekly_hours": 50,
    "short_term_goal": 1000,
    "preferred_schedule": 200,
    "region": 100,
    "skills": 1000,
    "contribution": 1000,
}


def check_security(data: dict) -> dict:
    threats = []

    def scan_value(key: str, val: Any):
        if not isinstance(val, str):
            return
        if SQL_PATTERNS.search(val):
            threats.append(f"SQL 인젝션 의심 패턴 감지: {key}")
        if XSS_PATTERNS.search(val):
            threats.append(f"XSS 의심 패턴 감지: {key}")
        max_len = MAX_LENGTHS.get(key, 2000)
        if len(val) > max_len:
            threats.append(f"입력값 초과: {key} (최대 {max_len}자, 입력 {len(val)}자)")

    for key, val in data.items():
        if isinstance(val, list):
            for item in val:
                scan_value(key, str(item))
        else:
            scan_value(key, val)

    # 의심 이메일 도메인 확인
    email = str(data.get("email", ""))
    domain = email.split("@")[-1].lower() if "@" in email else ""
    if domain in SUSPICIOUS_DOMAINS:
        threats.append(f"의심스러운 이메일 도메인: {domain}")

    return {"ok": len(threats) == 0, "threats": threats}
