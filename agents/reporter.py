"""
주간 리포트 에이전트
매주 월요일 오전 9시 실행 (APScheduler 또는 cron으로 호출)
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path.home() / "member-system"))

from agents.db_manager import get_stats
from agents.telegram_notifier import send_weekly_report


def run_weekly_report():
    stats = get_stats()
    ok = send_weekly_report(stats)
    return {"ok": ok, "stats": stats}


if __name__ == "__main__":
    result = run_weekly_report()
    print(result)
