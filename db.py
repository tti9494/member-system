import sqlite3
from pathlib import Path

DB_PATH = Path.home() / "member-system" / "members.db"


def get_conn():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
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

        CREATE INDEX IF NOT EXISTS idx_members_phone_hash ON members(phone_hash);
        CREATE INDEX IF NOT EXISTS idx_members_email_hash ON members(email_hash);
        CREATE INDEX IF NOT EXISTS idx_members_status ON members(status);
        CREATE INDEX IF NOT EXISTS idx_members_grade ON members(participation_grade);
        CREATE INDEX IF NOT EXISTS idx_logs_member ON member_logs(member_id);
    """)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print(f"DB 초기화 완료: {DB_PATH}")
