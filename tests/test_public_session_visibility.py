import asyncio
from datetime import datetime, timedelta, timezone
from types import SimpleNamespace

import main
import pytest
from fastapi import HTTPException


def _session(session_id: str, starts_at: str, timezone_name: str = "Asia/Seoul") -> dict:
    return {
        "id": session_id,
        "starts_at": starts_at,
        "timezone": timezone_name,
        "status": "open",
    }


def test_public_sessions_exclude_past_and_invalid_dates(monkeypatch):
    now = datetime.now(timezone.utc)
    monkeypatch.setattr(
        main,
        "list_sessions",
        lambda include_closed=False: [
            _session("past", (now - timedelta(days=1)).isoformat(), "UTC"),
            _session("future", (now + timedelta(days=1)).isoformat(), "UTC"),
            _session("invalid", "not-a-date"),
        ],
    )

    payload = asyncio.run(main.public_sessions())

    assert payload["total"] == 1
    assert [row["id"] for row in payload["data"]] == ["future"]


def test_public_study_sessions_exclude_past_naive_kst_date(monkeypatch):
    now_kst = datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=9)))
    monkeypatch.setattr(
        main,
        "list_study_sessions",
        lambda include_closed=False: [
            _session("past", (now_kst - timedelta(hours=1)).replace(tzinfo=None).isoformat()),
            _session("future", (now_kst + timedelta(hours=1)).replace(tzinfo=None).isoformat()),
        ],
    )

    payload = asyncio.run(main.public_study_sessions())

    assert payload["total"] == 1
    assert [row["id"] for row in payload["data"]] == ["future"]


def test_admin_schedule_guard_rejects_past_or_invalid_start_time():
    now = datetime.now(timezone.utc)

    with pytest.raises(HTTPException, match="현재 이후"):
        main._require_future_session_start(_session("past", (now - timedelta(minutes=1)).isoformat(), "UTC"))

    with pytest.raises(HTTPException, match="현재 이후"):
        main._require_future_session_start(_session("invalid", "not-a-date"))

    main._require_future_session_start(_session("future", (now + timedelta(minutes=1)).isoformat(), "UTC"))


def test_admin_schedule_guard_rejects_invalid_time_range():
    now = datetime.now(timezone.utc)
    session = _session("future", (now + timedelta(hours=1)).isoformat(), "UTC")
    session["ends_at"] = (now + timedelta(hours=1)).isoformat()

    with pytest.raises(HTTPException, match="종료 시각"):
        main._require_session_time_order(session)

    session["ends_at"] = (now + timedelta(hours=2)).isoformat()
    main._require_session_time_order(session)


def test_admin_session_routes_reject_past_start_before_any_write(monkeypatch):
    now = datetime.now(timezone.utc)
    past = (now - timedelta(minutes=1)).isoformat()
    request = SimpleNamespace(client=None)
    create_body = main.SessionRequest(
        starts_at=past,
        ends_at=(now + timedelta(hours=1)).isoformat(),
        location="test",
    )

    with pytest.raises(HTTPException, match="현재 이후"):
        asyncio.run(main.admin_create_session(create_body, request, _=None))

    monkeypatch.setattr(
        main,
        "get_session",
        lambda session_id: _session("existing", (now + timedelta(hours=2)).isoformat(), "UTC")
        | {"ends_at": (now + timedelta(hours=3)).isoformat()},
    )
    with pytest.raises(HTTPException, match="현재 이후"):
        asyncio.run(
            main.admin_update_session(
                "not-written",
                main.SessionUpdateRequest(starts_at=past),
                request,
                _=None,
            )
        )


def test_admin_create_route_rejects_end_before_start_before_any_write():
    now = datetime.now(timezone.utc)
    request = SimpleNamespace(client=None)
    body = main.SessionRequest(
        starts_at=(now + timedelta(hours=2)).isoformat(),
        ends_at=(now + timedelta(hours=1)).isoformat(),
        location="test",
    )

    with pytest.raises(HTTPException, match="종료 시각"):
        asyncio.run(main.admin_create_session(body, request, _=None))
