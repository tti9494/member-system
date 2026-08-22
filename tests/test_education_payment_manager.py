import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import db
from agents import education_payment_manager as payments


def _seed_paid_booking():
    conn = db.get_conn()
    try:
        conn.execute(
            """
            INSERT INTO members (
                id, name, email_encrypted, phone_masked, phone_encrypted, gender, age, job,
                referral_source, reason, ai_level, plan_type, consent_at, consent_version, created_at
            ) VALUES ('member-1', '테스트', '', '010-****-0000', '', 'x', 0, 'test', 'test', 'test', 'beginner', 'full', ?, 'test', ?)
            """,
            ("2026-07-28T00:00:00+00:00", "2026-07-28T00:00:00+00:00"),
        )
        conn.execute(
            """
            INSERT INTO sessions (
                id, title, program_type, audience_level, starts_at, ends_at, capacity_min,
                capacity_max, price_krw, location, status, created_at, updated_at
            ) VALUES ('session-1', '유료 강의', 'ai_basic_setup', 'beginner', ?, ?, 4, 8, 100000, '영등포', 'open', ?, ?)
            """,
            ("2026-08-01T10:00:00+00:00", "2026-08-01T12:00:00+00:00", "2026-07-28T00:00:00+00:00", "2026-07-28T00:00:00+00:00"),
        )
        conn.execute(
            """
            INSERT INTO bookings (
                id, session_id, member_id, applicant_name, phone_masked, status,
                payment_status, payment_amount_krw, created_at, updated_at
            ) VALUES ('booking-1', 'session-1', 'member-1', '테스트', '010-****-0000', 'requested', 'not_sent', 100000, ?, ?)
            """,
            ("2026-07-28T00:00:00+00:00", "2026-07-28T00:00:00+00:00"),
        )
        conn.commit()
    finally:
        conn.close()


def test_education_payment_order_uses_server_amount_and_hashes_payment_key(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        original_db_path = db.DB_PATH
        db.DB_PATH = Path(temp_dir) / "members.db"
        try:
            db.init_db()
            _seed_paid_booking()
            monkeypatch.setenv("YOONBOT_PAYMENT_PROVIDER", "manual_bank_transfer")
            order = payments.create_or_reuse_order(booking_id="booking-1", member_id="member-1")["data"]
            assert order["amount_krw"] == 100000
            assert order["status"] == "payment_pending"
            assert payments.create_or_reuse_order(booking_id="booking-1", member_id="member-1").get("reused") is True

            class FakeToss:
                def confirm(self, payment_key, toss_order_id, amount):
                    assert amount == 100000
                    return {"status": "DONE", "totalAmount": amount}

            monkeypatch.setenv("TOSS_PAYMENTS_SECRET_KEY", "test-secret")
            result = payments.confirm_toss_payment(
                order_id=order["id"],
                payment_key="payment-key-for-test-only",
                client_amount=100000,
                toss_order_id=order["toss_order_id"],
                confirm_client=FakeToss(),
            )
            assert result["data"]["status"] == "paid"
            conn = db.get_conn()
            try:
                payment_ref = conn.execute("SELECT payment_ref FROM education_payment_orders WHERE id=?", (order["id"],)).fetchone()[0]
                booking = conn.execute("SELECT status, payment_status FROM bookings WHERE id='booking-1'").fetchone()
            finally:
                conn.close()
            assert payment_ref.startswith("toss:")
            assert "payment-key-for-test-only" not in payment_ref
            assert tuple(booking) == ("confirmed", "paid")
        finally:
            db.DB_PATH = original_db_path
