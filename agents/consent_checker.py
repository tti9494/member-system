import os
from datetime import datetime, timezone
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=str(Path.home() / "member-system" / ".env"))

PRIVACY_VERSION = os.getenv("PRIVACY_VERSION", "1.0")


def check_consent(data: dict) -> dict:
    errors = []

    if not data.get("consent_personal"):
        errors.append("개인정보 수집·이용 동의는 필수입니다.")

    if errors:
        return {"ok": False, "errors": errors, "consent_data": None}

    consent_data = {
        "at": datetime.now(timezone.utc).isoformat(),
        "version": PRIVACY_VERSION,
        "marketing": bool(data.get("consent_marketing", False)),
    }

    return {"ok": True, "errors": [], "consent_data": consent_data}
