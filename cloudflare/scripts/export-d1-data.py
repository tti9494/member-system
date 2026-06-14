#!/usr/bin/env python3
"""Export member-system SQLite rows into a D1 seed SQL file.

The output can contain operational member records, so write it only under the
ignored cloudflare/.data directory and never print it to chat/logs.
"""

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path


TABLES = ("members", "member_logs", "sessions", "bookings", "operator_settings")


def sql_quote(conn: sqlite3.Connection, value) -> str:
    return conn.execute("SELECT quote(?)", (value,)).fetchone()[0]


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: export-d1-data.py <members.db> <output.sql>", file=sys.stderr)
        return 2

    db_path = Path(sys.argv[1]).expanduser()
    out_path = Path(sys.argv[2]).expanduser()
    if not db_path.exists():
        print(f"missing sqlite db: {db_path}", file=sys.stderr)
        return 1

    out_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    lines = [
        "-- Generated member-system D1 seed. Contains operational records.",
        "PRAGMA foreign_keys=OFF;",
    ]
    try:
        existing_tables = {
            row["name"]
            for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        }
        for table in TABLES:
            if table not in existing_tables:
                continue
            rows = conn.execute(f"SELECT * FROM {table}").fetchall()
            if not rows:
                continue
            columns = rows[0].keys()
            quoted_columns = ", ".join(f'"{column}"' for column in columns)
            for row in rows:
                values = ", ".join(sql_quote(conn, row[column]) for column in columns)
                lines.append(f'INSERT OR IGNORE INTO "{table}" ({quoted_columns}) VALUES ({values});')
        lines.append("PRAGMA foreign_keys=ON;")
        out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    finally:
        conn.close()

    print(f"wrote seed sql: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
