import sqlite3
from pathlib import Path

DB_PATH = Path.home() / "member-system" / "members.db"


def get_conn():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS members (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email_encrypted TEXT NOT NULL,
            email_hash TEXT,
            phone_hash TEXT,
            phone_masked TEXT NOT NULL,
            phone_encrypted TEXT NOT NULL,
            kakao_id TEXT,
            kakao_profile TEXT,
            kakao_connected_at TEXT,
            gender TEXT NOT NULL,
            age INTEGER NOT NULL,
            job TEXT NOT NULL,
            referral_source TEXT NOT NULL,
            reason TEXT NOT NULL,
            ai_level TEXT NOT NULL,
            plan_type TEXT NOT NULL,

            -- 선택 항목
            ai_tools TEXT,
            ai_subscription TEXT,
            ai_weekly_hours TEXT,
            ai_use_cases TEXT,
            group_goals TEXT,
            short_term_goal TEXT,
            participation_type TEXT,
            preferred_schedule TEXT,
            region TEXT,
            main_device TEXT,
            can_code INTEGER DEFAULT 0,
            can_present INTEGER DEFAULT 0,
            skills TEXT,
            contribution TEXT,

            -- 참여 등급
            participation_grade TEXT DEFAULT '🌱 새싹',

            -- 동의
            consent_personal INTEGER NOT NULL DEFAULT 0,
            consent_marketing INTEGER DEFAULT 0,
            consent_at TEXT NOT NULL,
            consent_version TEXT NOT NULL,

            -- 상태
            status TEXT DEFAULT 'pending',
            rejection_reason TEXT,
            access_code TEXT,
            code_expires_at TEXT,
            code_issued_at TEXT,
            code_fail_count INTEGER DEFAULT 0,
            code_locked_until TEXT,
            approved_at TEXT,
            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS member_logs (
            id TEXT PRIMARY KEY,
            member_id TEXT NOT NULL,
            action TEXT NOT NULL,
            detail TEXT,
            ip TEXT,
            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS sessions (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            program_type TEXT NOT NULL DEFAULT 'ai_basic_setup',
            audience_level TEXT NOT NULL DEFAULT 'all',
            starts_at TEXT NOT NULL,
            ends_at TEXT NOT NULL,
            timezone TEXT NOT NULL DEFAULT 'Asia/Seoul',
            capacity_min INTEGER NOT NULL DEFAULT 4,
            capacity_max INTEGER NOT NULL DEFAULT 5,
            confirmed_count INTEGER NOT NULL DEFAULT 0,
            price_krw INTEGER NOT NULL DEFAULT 50000,
            location TEXT NOT NULL,
            materials TEXT,
            status TEXT NOT NULL DEFAULT 'draft',
            payment_guide TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS bookings (
            id TEXT PRIMARY KEY,
            session_id TEXT REFERENCES sessions(id),
            member_id TEXT REFERENCES members(id),
            applicant_name TEXT NOT NULL,
            phone_masked TEXT NOT NULL,
            desired_outcome TEXT,
            preparedness TEXT,
            status TEXT NOT NULL DEFAULT 'requested',
            payment_status TEXT NOT NULL DEFAULT 'not_sent',
            payment_amount_krw INTEGER NOT NULL DEFAULT 50000,
            payment_note TEXT,
            confirmed_at TEXT,
            canceled_at TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS review_instructors (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            role TEXT,
            bio TEXT,
            specialties TEXT,
            status TEXT NOT NULL DEFAULT 'active',
            sort_order INTEGER NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS review_entries (
            id TEXT PRIMARY KEY,
            instructor_id TEXT REFERENCES review_instructors(id) ON DELETE SET NULL,
            class_title TEXT NOT NULL,
            class_date TEXT,
            title TEXT NOT NULL,
            summary TEXT,
            body TEXT,
            tags TEXT,
            image_urls TEXT,
            status TEXT NOT NULL DEFAULT 'draft',
            source TEXT NOT NULL DEFAULT 'manual',
            privacy_checked INTEGER NOT NULL DEFAULT 0,
            featured INTEGER NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS review_invites (
            id TEXT PRIMARY KEY,
            token_hash TEXT UNIQUE NOT NULL,
            label TEXT,
            instructor_id TEXT REFERENCES review_instructors(id) ON DELETE SET NULL,
            class_title TEXT,
            class_date TEXT,
            status TEXT NOT NULL DEFAULT 'active',
            max_submissions INTEGER NOT NULL DEFAULT 0,
            submitted_count INTEGER NOT NULL DEFAULT 0,
            expires_at TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS consultations (
            id TEXT PRIMARY KEY,
            source TEXT NOT NULL DEFAULT 'public_site',
            topic TEXT NOT NULL DEFAULT '',
            name TEXT NOT NULL DEFAULT '',
            email_hash TEXT,
            email_masked TEXT NOT NULL DEFAULT '',
            email_encrypted TEXT NOT NULL DEFAULT '',
            phone_hash TEXT,
            phone_masked TEXT NOT NULL DEFAULT '',
            phone_encrypted TEXT NOT NULL DEFAULT '',
            product_interest TEXT,
            message TEXT,
            status TEXT NOT NULL DEFAULT 'new',
            admin_note TEXT,
            page_url TEXT,
            referrer TEXT,
            user_agent TEXT,
            member_id TEXT REFERENCES members(id) ON DELETE SET NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS licenses (
            id TEXT PRIMARY KEY,
            member_id TEXT REFERENCES members(id) ON DELETE SET NULL,
            license_key_hash TEXT UNIQUE NOT NULL,
            license_key_hint TEXT NOT NULL,
            plan_code TEXT NOT NULL DEFAULT 'basic',
            status TEXT NOT NULL DEFAULT 'unused',
            max_devices INTEGER NOT NULL DEFAULT 1,
            bound_hwid_hash TEXT,
            app_min_version TEXT,
            expires_at TEXT NOT NULL,
            activated_at TEXT,
            last_verified_at TEXT,
            revoked_at TEXT,
            revoke_reason TEXT,
            note TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS license_activations (
            id TEXT PRIMARY KEY,
            license_id TEXT NOT NULL REFERENCES licenses(id) ON DELETE CASCADE,
            token_hash TEXT UNIQUE NOT NULL,
            hwid_hash TEXT NOT NULL,
            platform TEXT NOT NULL DEFAULT 'windows',
            device_name TEXT,
            app_version TEXT,
            status TEXT NOT NULL DEFAULT 'active',
            first_seen_at TEXT NOT NULL,
            last_seen_at TEXT NOT NULL,
            expires_at TEXT NOT NULL,
            revoked_at TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS license_events (
            id TEXT PRIMARY KEY,
            license_id TEXT,
            activation_id TEXT,
            event_type TEXT NOT NULL,
            result TEXT NOT NULL,
            reason_code TEXT,
            ip_hash TEXT,
            user_agent TEXT,
            app_version TEXT,
            platform TEXT,
            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS orders (
            id TEXT PRIMARY KEY,
            buyer_name TEXT NOT NULL,
            buyer_email_hash TEXT,
            buyer_email_masked TEXT NOT NULL DEFAULT '',
            buyer_phone_hash TEXT,
            buyer_phone_masked TEXT NOT NULL DEFAULT '',
            product_code TEXT NOT NULL DEFAULT 'yoonbot',
            plan_code TEXT NOT NULL,
            amount_krw INTEGER NOT NULL,
            original_amount_krw INTEGER,
            discount_code TEXT,
            discount_label TEXT,
            discount_amount_krw INTEGER NOT NULL DEFAULT 0,
            status TEXT NOT NULL DEFAULT 'payment_pending',
            payment_provider TEXT NOT NULL DEFAULT 'manual_bank_transfer',
            payment_ref TEXT,
            member_id TEXT REFERENCES members(id) ON DELETE SET NULL,
            license_id TEXT REFERENCES licenses(id) ON DELETE SET NULL,
            note TEXT,
            customer_message TEXT,
            paid_at TEXT,
            canceled_at TEXT,
            refunded_at TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS yoonbot_discount_codes (
            id TEXT PRIMARY KEY,
            code TEXT NOT NULL UNIQUE,
            label TEXT,
            plan_code TEXT,
            discount_type TEXT NOT NULL,
            discount_value INTEGER NOT NULL,
            max_redemptions INTEGER,
            redeemed_count INTEGER NOT NULL DEFAULT 0,
            starts_at TEXT,
            expires_at TEXT,
            enabled INTEGER NOT NULL DEFAULT 1,
            note TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE INDEX IF NOT EXISTS idx_members_phone_hash ON members(phone_hash);
        CREATE INDEX IF NOT EXISTS idx_members_email_hash ON members(email_hash);
        CREATE INDEX IF NOT EXISTS idx_members_status ON members(status);
        CREATE INDEX IF NOT EXISTS idx_members_grade ON members(participation_grade);
        CREATE INDEX IF NOT EXISTS idx_logs_member ON member_logs(member_id);
        CREATE INDEX IF NOT EXISTS idx_sessions_status_start ON sessions(status, starts_at);
        CREATE INDEX IF NOT EXISTS idx_bookings_session ON bookings(session_id);
        CREATE INDEX IF NOT EXISTS idx_bookings_member ON bookings(member_id);
        CREATE INDEX IF NOT EXISTS idx_bookings_status ON bookings(status);
        CREATE INDEX IF NOT EXISTS idx_review_instructors_status_sort ON review_instructors(status, sort_order);
        CREATE INDEX IF NOT EXISTS idx_review_entries_status_date ON review_entries(status, class_date);
        CREATE INDEX IF NOT EXISTS idx_review_entries_instructor ON review_entries(instructor_id);
        CREATE INDEX IF NOT EXISTS idx_review_invites_status_created ON review_invites(status, created_at);
        CREATE INDEX IF NOT EXISTS idx_review_invites_token ON review_invites(token_hash);
        CREATE INDEX IF NOT EXISTS idx_consultations_status_created ON consultations(status, created_at);
        CREATE INDEX IF NOT EXISTS idx_consultations_source_created ON consultations(source, created_at);
        CREATE INDEX IF NOT EXISTS idx_licenses_member ON licenses(member_id);
        CREATE INDEX IF NOT EXISTS idx_licenses_status_expires ON licenses(status, expires_at);
        CREATE INDEX IF NOT EXISTS idx_license_activations_license_status ON license_activations(license_id, status);
        CREATE INDEX IF NOT EXISTS idx_license_events_license_created ON license_events(license_id, created_at);
        CREATE INDEX IF NOT EXISTS idx_orders_status_created ON orders(status, created_at);
        CREATE INDEX IF NOT EXISTS idx_orders_plan_created ON orders(plan_code, created_at);
        CREATE INDEX IF NOT EXISTS idx_orders_license ON orders(license_id);
        CREATE INDEX IF NOT EXISTS idx_discount_codes_code ON yoonbot_discount_codes(code);
        CREATE INDEX IF NOT EXISTS idx_discount_codes_enabled_created ON yoonbot_discount_codes(enabled, created_at);
    """)
    _ensure_column(conn, "members", "available_time_slots", "TEXT")
    _ensure_column(conn, "members", "kakao_id", "TEXT")
    _ensure_column(conn, "members", "kakao_profile", "TEXT")
    _ensure_column(conn, "members", "kakao_connected_at", "TEXT")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_members_kakao_id ON members(kakao_id)")
    _ensure_column(conn, "orders", "toss_order_id", "TEXT")
    _ensure_column(conn, "orders", "original_amount_krw", "INTEGER")
    _ensure_column(conn, "orders", "discount_code", "TEXT")
    _ensure_column(conn, "orders", "discount_label", "TEXT")
    _ensure_column(conn, "orders", "discount_amount_krw", "INTEGER NOT NULL DEFAULT 0")
    _ensure_column(conn, "consultations", "member_id", "TEXT REFERENCES members(id) ON DELETE SET NULL")
    conn.commit()
    conn.close()


def _ensure_column(conn: sqlite3.Connection, table: str, column: str, definition: str):
    existing = {
        row["name"]
        for row in conn.execute(f"PRAGMA table_info({table})").fetchall()
    }
    if column not in existing:
        conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")


if __name__ == "__main__":
    init_db()
    print(f"DB 초기화 완료: {DB_PATH}")
