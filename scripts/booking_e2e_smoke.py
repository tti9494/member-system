#!/usr/bin/env python3
"""Local smoke test for apply -> booking -> admin count visibility.

Default mode uses a temporary SQLite database, so the smoke can be repeated
without touching operational data. Pass --use-live-db to insert explicit TEST
rows into the configured local DB.
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import db
from agents import booking_manager, db_manager
from agents.encryptor import encrypt_email, encrypt_phone, hash_email, hash_phone, mask_phone


TEST_NAME = "TEST_BOOKING_E2E_SMOKE"
TEST_PHONE = "010-0000-9001"
TEST_EMAIL = "test.booking.e2e.smoke@example.invalid"


def _patch_db_path(path: Path) -> None:
    db.DB_PATH = path
    db_manager.DB_PATH = path


@contextmanager
def smoke_database(use_live_db: bool) -> Iterator[Path]:
    original_db_path = db.DB_PATH
    original_manager_db_path = db_manager.DB_PATH
    if use_live_db:
        db.init_db()
        try:
            yield db.DB_PATH
        finally:
            _patch_db_path(original_db_path)
            db_manager.DB_PATH = original_manager_db_path
        return

    with tempfile.TemporaryDirectory(prefix="member-system-smoke-") as tmpdir:
        path = Path(tmpdir) / "members.db"
        _patch_db_path(path)
        db.init_db()
        try:
            yield path
        finally:
            _patch_db_path(original_db_path)
            db_manager.DB_PATH = original_manager_db_path


def count_tables() -> dict[str, int]:
    conn = db.get_conn()
    try:
        return {
            "members": conn.execute("SELECT COUNT(*) FROM members").fetchone()[0],
            "bookings": conn.execute("SELECT COUNT(*) FROM bookings").fetchone()[0],
            "sessions": conn.execute("SELECT COUNT(*) FROM sessions").fetchone()[0],
        }
    finally:
        conn.close()


def admin_counts() -> dict[str, int | str | bool]:
    health = db_manager.get_operator_health()
    storage = db_manager.get_storage_status(limit=1)
    return {
        "members": storage["counts"]["members"],
        "bookings": storage["counts"]["bookings"],
        "sessions": storage["counts"]["sessions"],
        "public_sessions": health["public_sessions"]["count"],
        "open_sessions": health["public_sessions"]["open_count"],
        "requested_bookings": health["application_system"]["requested_booking_count"],
        "active_bookings": health["application_system"]["active_booking_count"],
        "accepting_applications": health["application_system"]["accepting_applications"],
    }


def external_status() -> dict[str, str | bool]:
    storage = db_manager.get_storage_status(limit=1)
    return {
        "sheets_configured": storage["sheets"]["configured"],
        "sheets_mode": storage["sheets"]["mode"],
        "hermes_configured": storage["hermes"]["configured"],
        "hermes_mode": storage["hermes"]["mode"],
    }


def create_test_application() -> dict[str, str]:
    now = datetime.now(timezone.utc)
    starts_at = (now + timedelta(days=3)).replace(microsecond=0).isoformat()
    ends_at = (now + timedelta(days=3, hours=2)).replace(microsecond=0).isoformat()
    session_id = booking_manager.create_session(
        {
            "title": "TEST E2E Smoke Session",
            "description": "TEST data for local booking smoke verification.",
            "starts_at": starts_at,
            "ends_at": ends_at,
            "location": "TEST Local Only",
            "status": "open",
            "capacity_min": 1,
            "capacity_max": 5,
            "price_krw": booking_manager.DEFAULT_PRICE,
        }
    )
    member_id = db_manager.create_member(
        {
            "name": TEST_NAME,
            "email_encrypted": encrypt_email(TEST_EMAIL),
            "email_hash": hash_email(TEST_EMAIL),
            "phone_masked": mask_phone(TEST_PHONE),
            "phone_encrypted": encrypt_phone(TEST_PHONE),
            "phone_hash": hash_phone(TEST_PHONE),
            "gender": "테스트",
            "age": 30,
            "job": "TEST_OPERATOR_SMOKE",
            "referral_source": "TEST_LOCAL_SMOKE",
            "reason": "TEST local smoke verifies apply booking admin counts only.",
            "ai_level": "입문",
            "plan_type": "basic",
            "consent_personal": True,
            "consent_marketing": False,
            "consent_at": now.isoformat(),
            "consent_version": "smoke-test",
            "participation_grade": "TEST",
            "desired_outcome": "TEST booking count increase",
            "preparedness": "TEST local only",
        }
    )
    db_manager.log_action(member_id, "apply", "TEST booking_e2e_smoke", "127.0.0.1")
    db_manager.log_action(member_id, "sheets_sync", "not_configured_or_failed", "127.0.0.1")
    booking_id = booking_manager.create_booking(
        {
            "session_id": session_id,
            "member_id": member_id,
            "applicant_name": TEST_NAME,
            "phone_masked": mask_phone(TEST_PHONE),
            "desired_outcome": "TEST booking count increase",
            "preparedness": "TEST local only",
            "status": "requested",
            "payment_status": "not_sent",
            "payment_amount_krw": booking_manager.DEFAULT_PRICE,
        }
    )
    booking_manager.refresh_session_counts(session_id)
    db_manager.log_action(member_id, "booking_requested", f"booking_id={booking_id}", "127.0.0.1")
    db_manager.log_action(member_id, "hermes_notify", "not_configured", "127.0.0.1")
    return {"session_id": session_id, "member_id": member_id, "booking_id": booking_id}


def assert_increments(before: dict[str, int], after: dict[str, int]) -> list[str]:
    errors = []
    expected = {"members": 1, "bookings": 1, "sessions": 1}
    for key, delta in expected.items():
        actual = after[key] - before[key]
        if actual != delta:
            errors.append(f"{key} delta expected {delta}, got {actual}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Run local apply -> booking -> admin count smoke.")
    parser.add_argument(
        "--use-live-db",
        action="store_true",
        help="Insert explicit TEST rows into the configured local DB instead of a temporary DB.",
    )
    args = parser.parse_args()

    with smoke_database(args.use_live_db) as db_path:
        before = count_tables()
        before_admin = admin_counts()
        ids = create_test_application()
        after = count_tables()
        after_admin = admin_counts()
        status = external_status()

    errors = assert_increments(before, after)
    admin_errors = assert_increments(
        {
            "members": int(before_admin["members"]),
            "bookings": int(before_admin["bookings"]),
            "sessions": int(before_admin["sessions"]),
        },
        {
            "members": int(after_admin["members"]),
            "bookings": int(after_admin["bookings"]),
            "sessions": int(after_admin["sessions"]),
        },
    )
    errors.extend(f"admin {item}" for item in admin_errors)
    if int(after_admin["requested_bookings"]) - int(before_admin["requested_bookings"]) != 1:
        errors.append("admin requested_bookings delta expected 1")
    if int(after_admin["active_bookings"]) - int(before_admin["active_bookings"]) != 1:
        errors.append("admin active_bookings delta expected 1")

    report = {
        "ok": not errors,
        "mode": "live_db_TEST_insert" if args.use_live_db else "temp_db",
        "db_path": str(db_path),
        "test_identity": {
            "name": TEST_NAME,
            "phone": TEST_PHONE,
            "email": TEST_EMAIL,
        },
        "ids": ids,
        "counts": {"before": before, "after": after},
        "admin_counts": {"before": before_admin, "after": after_admin},
        "external_status": status,
        "errors": errors,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
