#!/usr/bin/env python3
"""Claim approved ARSEN Kakao notice jobs and send them from this Mac."""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import subprocess
import sys
import time
import uuid
from pathlib import Path
from urllib import error, request


ROOT = Path(__file__).resolve().parents[1]
# 경로 하드코딩 금지 규칙: 사용자 홈 기준으로 계산 (KAKAO_GROUP_DB 환경변수로 재정의 가능)
DEFAULT_GROUP_DBS = [
    Path.home() / "Desktop" / "kakao_auto_sender" / "data" / "kakao.db",
    Path.home() / "Desktop" / "kakao_auto_gg" / "data" / "kakao.db",
]


class SenderError(RuntimeError):
    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


def read_env_file(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    values: dict[str, str] = {}
    for raw in path.read_text(errors="ignore").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def env() -> dict[str, str]:
    values: dict[str, str] = {}
    values.update(read_env_file(ROOT / ".env"))
    values.update(read_env_file(ROOT / "cloudflare" / ".secrets.local"))
    values.update(os.environ)
    return values


class Client:
    def __init__(self, base_url: str, admin_key: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.admin_key = admin_key

    def json(self, method: str, path: str, payload: dict | None = None) -> dict:
        body = None if payload is None else json.dumps(payload).encode("utf-8")
        req = request.Request(
            f"{self.base_url}{path}",
            data=body,
            method=method,
            headers={
                "content-type": "application/json",
                "x-admin-key": self.admin_key,
                "user-agent": "arsen-kakao-notice-sender/2",
            },
        )
        with request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))

    def claimable_jobs(self) -> list[dict]:
        payload = self.json("GET", "/admin/kakao-notice/jobs?status=all")
        return [
            job for job in list(payload.get("data") or [])
            if job.get("status") in {"prepare_requested", "approved", "group_manage_requested"}
        ]

    def job(self, job_id: str) -> dict:
        return self.json("GET", f"/admin/kakao-notice/jobs/{job_id}").get("data") or {}

    def claim(self, job_id: str) -> dict:
        return self.json("POST", f"/admin/kakao-notice/jobs/{job_id}/claim").get("data") or {}

    def finish(self, job_id: str, status: str, recipients: list[dict], summary: str = "") -> None:
        payload = {"status": status, "recipients": recipients}
        if summary:
            payload["summary"] = summary
        self.json("POST", f"/admin/kakao-notice/jobs/{job_id}/result", payload)

    def progress(self, job_id: str, status: str, recipients: list[dict]) -> None:
        self.json("POST", f"/admin/kakao-notice/jobs/{job_id}/result", {
            "progress": True,
            "status": status,
            "recipients": recipients,
        })


def run_osascript(script: str, timeout: float = 10) -> str:
    try:
        result = subprocess.run(["osascript", "-e", script], text=True, capture_output=True, timeout=timeout, check=True)
        return result.stdout.strip()
    except subprocess.TimeoutExpired as exc:
        raise SenderError("osascript_timeout") from exc
    except subprocess.CalledProcessError as exc:
        raise SenderError("osascript_failed") from exc


def preflight_ui(dry_run: bool) -> tuple[bool, str]:
    if dry_run:
        return True, ""
    try:
        activate_kakao()
        return True, ""
    except SenderError as exc:
        return False, exc.reason


def should_stop(client: Client, job_id: str) -> bool:
    try:
        return client.job(job_id).get("status") in {"stop_requested", "stopped", "rejected"}
    except Exception:
        return False


def ui_timeout(env_key: str, default: float, minimum: float, maximum: float) -> float:
    raw = os.environ.get(env_key, str(default))
    try:
        return max(minimum, min(maximum, float(raw)))
    except ValueError:
        return default


def search_wait() -> float:
    return ui_timeout("KAKAO_SEARCH_WAIT", 1.4, 0.2, 5.0)


def chat_open_wait() -> float:
    return ui_timeout("KAKAO_CHAT_OPEN_WAIT", 1.0, 0.2, 8.0)


def paste_wait(message: str) -> float:
    base = 0.25 if len(message) > 200 else 0.15
    return ui_timeout("KAKAO_PASTE_WAIT", base, 0.05, 3.0)


def progress_every() -> int:
    raw = os.environ.get("KAKAO_NOTICE_PROGRESS_EVERY", "10")
    try:
        return max(1, min(50, int(raw)))
    except ValueError:
        return 10


def normalize_title(value: str) -> str:
    return " ".join(str(value or "").strip().split())


def validate_search_name(search_name: str) -> str:
    target = normalize_title(search_name)
    if not target:
        raise SenderError("empty_search_name")
    return target


def fatal_sender_error(reason: str) -> bool:
    return reason in {
        "kakao_open_failed",
        "kakao_not_frontmost",
        "kakao_main_window_not_front",
        "kakao_search_failed",
        "kakao_input_failed",
        "kakao_paste_failed",
        "kakao_send_failed",
        "clipboard_failed",
        "osascript_timeout",
        "osascript_failed",
    }


def group_db_path() -> Path:
    configured = os.environ.get("KAKAO_GROUP_DB", "").strip()
    candidates = [Path(configured)] if configured else []
    candidates.extend(DEFAULT_GROUP_DBS)
    for path in candidates:
        if path.exists():
            return path
    raise SenderError("group_db_not_found")


def render_group_message(template: str, friend: dict) -> str:
    nickname = str(friend.get("nickname") or "").strip()
    name = str(friend.get("name") or "").strip()
    return (
        str(template or "")
        .replace("[[호칭]]", nickname)
        .replace("[[이름]]", name)
        .strip()
    )


def load_local_group_recipients(group_name: str, message: str) -> list[dict]:
    target_group = normalize_title(group_name)
    if not target_group:
        raise SenderError("empty_group_name")
    template = str(message or "").strip()
    if not template:
        raise SenderError("empty_group_message")
    path = group_db_path()
    with sqlite3.connect(path) as conn:
        conn.row_factory = sqlite3.Row
        group = conn.execute(
            "SELECT id, name FROM groups WHERE name = ? COLLATE NOCASE",
            (target_group,),
        ).fetchone()
        if not group:
            raise SenderError("group_not_found")
        rows = conn.execute(
            """
            SELECT f.id, f.name, f.nickname, f.memo
            FROM friends f
            INNER JOIN group_members gm ON f.id = gm.friend_id
            WHERE gm.group_id = ?
            ORDER BY f.name
            """,
            (group["id"],),
        ).fetchall()
    if not rows:
        raise SenderError("group_empty")
    recipients = []
    for row in rows:
        friend = dict(row)
        search_name = validate_search_name(str(friend.get("name") or ""))
        rendered = render_group_message(template, friend)
        if not rendered:
            raise SenderError("empty_group_message")
        recipients.append({
            "id": f"kg_{uuid.uuid4().hex}",
            "member_id": "",
            "booking_id": "",
            "name": search_name,
            "kakao_display_name": search_name,
            "message": rendered,
            "status": "pending",
            "error": "",
            "sent_at": "",
        })
    return recipients


def group_by_name(conn: sqlite3.Connection, group_name: str) -> sqlite3.Row | None:
    return conn.execute("SELECT id, name FROM groups WHERE name = ? COLLATE NOCASE", (normalize_title(group_name),)).fetchone()


def friend_rows_by_name(conn: sqlite3.Connection, friend_name: str) -> list[sqlite3.Row]:
    name = normalize_title(friend_name)
    return conn.execute(
        "SELECT id, name, nickname FROM friends WHERE name = ? COLLATE NOCASE OR nickname = ? COLLATE NOCASE ORDER BY name",
        (name, name),
    ).fetchall()


def local_group_summary(action: str) -> str:
    labels = {
        "list": "그룹 목록",
        "view": "그룹 보기",
        "create": "그룹 생성",
        "delete": "그룹 삭제",
        "rename": "그룹 이름변경",
        "add_member": "그룹 멤버 추가",
        "remove_member": "그룹 멤버 제거",
    }
    return labels.get(action, action or "그룹 관리")


def perform_local_group_admin(job: dict) -> str:
    action = str(job.get("group_action") or "").strip()
    group_name = str(job.get("local_group_name") or "").strip()
    new_group_name = str(job.get("new_group_name") or "").strip()
    friend_name = str(job.get("friend_name") or "").strip()
    path = group_db_path()
    with sqlite3.connect(path) as conn:
        conn.row_factory = sqlite3.Row
        if action == "list":
            rows = conn.execute(
                """
                SELECT g.name, COUNT(gm.friend_id) AS member_count
                FROM groups g
                LEFT JOIN group_members gm ON gm.group_id = g.id
                GROUP BY g.id
                ORDER BY g.name
                """
            ).fetchall()
            if not rows:
                return "등록된 그룹이 없습니다."
            lines = [f"{idx}. {row['name']} ({row['member_count']}명)" for idx, row in enumerate(rows[:80], start=1)]
            if len(rows) > 80:
                lines.append(f"... 외 {len(rows) - 80}개")
            return "\n".join(lines)

        group = group_by_name(conn, group_name)
        if action == "create":
            if group:
                raise SenderError("group_already_exists")
            conn.execute("INSERT INTO groups (name) VALUES (?)", (normalize_title(group_name),))
            conn.commit()
            return f"그룹 생성 완료: {normalize_title(group_name)}"

        if not group:
            raise SenderError("group_not_found")

        if action == "view":
            rows = conn.execute(
                """
                SELECT f.name, f.nickname
                FROM friends f
                INNER JOIN group_members gm ON f.id = gm.friend_id
                WHERE gm.group_id = ?
                ORDER BY f.name
                """,
                (group["id"],),
            ).fetchall()
            if not rows:
                return f"{group['name']}: 멤버 0명"
            lines = [f"{group['name']}: {len(rows)}명"]
            lines.extend(f"- {row['name']}" + (f" ({row['nickname']})" if row["nickname"] else "") for row in rows[:120])
            if len(rows) > 120:
                lines.append(f"... 외 {len(rows) - 120}명")
            return "\n".join(lines)

        if action == "delete":
            conn.execute("DELETE FROM group_members WHERE group_id = ?", (group["id"],))
            conn.execute("DELETE FROM groups WHERE id = ?", (group["id"],))
            conn.commit()
            return f"그룹 삭제 완료: {group['name']}"

        if action == "rename":
            next_name = normalize_title(new_group_name)
            if not next_name:
                raise SenderError("empty_new_group_name")
            if group_by_name(conn, next_name):
                raise SenderError("group_already_exists")
            conn.execute("UPDATE groups SET name = ? WHERE id = ?", (next_name, group["id"]))
            conn.commit()
            return f"그룹 이름변경 완료: {group['name']} -> {next_name}"

        if action in {"add_member", "remove_member"}:
            friends = friend_rows_by_name(conn, friend_name)
            if not friends:
                raise SenderError("friend_not_found")
            unique_ids = {row["id"] for row in friends}
            if len(unique_ids) > 1:
                raise SenderError("friend_ambiguous")
            friend = friends[0]
            if action == "add_member":
                conn.execute(
                    "INSERT OR IGNORE INTO group_members (group_id, friend_id) VALUES (?, ?)",
                    (group["id"], friend["id"]),
                )
                conn.commit()
                return f"그룹 멤버 추가 완료: {group['name']} / {friend['name']}"
            conn.execute("DELETE FROM group_members WHERE group_id = ? AND friend_id = ?", (group["id"], friend["id"]))
            conn.commit()
            return f"그룹 멤버 제거 완료: {group['name']} / {friend['name']}"

    raise SenderError("unknown_group_action")


def expand_local_group_job(client: Client, claimed: dict) -> dict:
    if claimed.get("target") != "local_group" or claimed.get("recipients"):
        return claimed
    recipients = load_local_group_recipients(
        str(claimed.get("local_group_name") or ""),
        str(claimed.get("custom_message") or ""),
    )
    expanded = {**claimed, "recipients": recipients}
    try:
        client.progress(str(claimed["id"]), "preparing", recipients)
    except Exception as exc:  # noqa: BLE001 - final result will still sync recipients.
        print(f"group_progress_failed: {claimed.get('id', '-')} ({type(exc).__name__})", file=sys.stderr)
    return expanded


def set_clipboard(text: str) -> None:
    try:
        subprocess.run(["pbcopy"], input=text, text=True, capture_output=True, timeout=5, check=True)
    except subprocess.TimeoutExpired as exc:
        raise SenderError("clipboard_failed") from exc
    except subprocess.CalledProcessError as exc:
        raise SenderError("clipboard_failed") from exc


def frontmost_app_name() -> str:
    return run_osascript(
        'tell application "System Events"\n'
        '  return name of first application process whose frontmost is true\n'
        'end tell',
        timeout=5,
    )


def ensure_kakao_frontmost() -> None:
    if frontmost_app_name() != "KakaoTalk":
        raise SenderError("kakao_not_frontmost")


def activate_kakao() -> None:
    try:
        subprocess.run(["open", "-a", "KakaoTalk"], text=True, capture_output=True, timeout=10, check=True)
    except subprocess.TimeoutExpired as exc:
        raise SenderError("kakao_open_failed") from exc
    except subprocess.CalledProcessError as exc:
        raise SenderError("kakao_open_failed") from exc
    run_osascript(
        'tell application "KakaoTalk" to activate\n'
        'delay 0.2\n'
        'tell application "System Events"\n'
        '  tell process "KakaoTalk"\n'
        '    set frontmost to true\n'
        '    if (count of windows) = 0 then\n'
        '      key code 18 using command down\n'
        '      delay 0.3\n'
        '    end if\n'
        '    set raisedMain to false\n'
        '    repeat with w in windows\n'
        '      try\n'
        '        if (name of w is "KakaoTalk") or (name of w is "카카오톡") then\n'
        '          perform action "AXRaise" of w\n'
        '          set raisedMain to true\n'
        '          exit repeat\n'
        '        end if\n'
        '      end try\n'
        '    end repeat\n'
        '    if raisedMain is false and (count of windows) > 0 then perform action "AXRaise" of window 1\n'
        '  end tell\n'
        'end tell',
        timeout=10,
    )
    time.sleep(0.4)
    ensure_kakao_frontmost()
    if normalize_title(front_kakao_window_name()) not in {"KakaoTalk", "카카오톡"}:
        raise SenderError("kakao_main_window_not_front")


def focused_search_value() -> str | None:
    value = run_osascript(
        'tell application "System Events"\n'
        '  tell process "KakaoTalk"\n'
        '    try\n'
        '      set focusedElem to value of attribute "AXFocusedUIElement"\n'
        '      if role of focusedElem is not "AXTextField" then return "__KAKAO_SEARCH_FIELD_MISSING__"\n'
        '      try\n'
        '        set elemDesc to description of focusedElem as text\n'
        '      on error\n'
        '        set elemDesc to ""\n'
        '      end try\n'
        '      if elemDesc does not contain "검색" then return "__KAKAO_SEARCH_FIELD_MISSING__"\n'
        '      try\n'
        '        return value of focusedElem as text\n'
        '      on error\n'
        '        return ""\n'
        '      end try\n'
        '    on error\n'
        '      return "__KAKAO_SEARCH_FIELD_MISSING__"\n'
        '    end try\n'
        '  end tell\n'
        'end tell',
        timeout=5,
    )
    if value == "__KAKAO_SEARCH_FIELD_MISSING__":
        return None
    return value


def focus_existing_search_field() -> bool:
    return run_osascript(
        'tell application "System Events"\n'
        '  tell process "KakaoTalk"\n'
        '    try\n'
        '      set searchField to first text field of front window whose description contains "검색"\n'
        '      set focused of searchField to true\n'
        '      return "1"\n'
        '    on error\n'
        '      return "0"\n'
        '    end try\n'
        '  end tell\n'
        'end tell',
        timeout=5,
    ) == "1"


def ensure_search_field_focused() -> None:
    if focused_search_value() is None:
        raise SenderError("kakao_search_failed")


def wait_for_search_field(timeout: float = 1.5) -> None:
    deadline = time.time() + timeout
    while time.time() <= deadline:
        if focused_search_value() is not None:
            return
        time.sleep(0.1)
    raise SenderError("kakao_search_failed")


def wait_for_search_value(target: str) -> None:
    deadline = time.time() + search_wait()
    normalized_target = normalize_title(target)
    while time.time() <= deadline:
        ensure_kakao_frontmost()
        if normalize_title(front_kakao_window_name()) != "카카오톡" and normalize_title(front_kakao_window_name()) != "KakaoTalk":
            raise SenderError("kakao_search_failed")
        if normalize_title(focused_search_value() or "") == normalized_target:
            return
        time.sleep(0.1)
    raise SenderError("kakao_search_failed")


def focus_friend_search(target: str) -> None:
    activate_kakao()
    if focused_search_value() is None:
        if not focus_existing_search_field():
            run_osascript(
                'tell application "System Events"\n'
                '  tell process "KakaoTalk"\n'
                '    set frontmost to true\n'
                '    try\n'
                '      perform action "AXPress" of (first button of front window whose description contains "검색")\n'
                '    on error\n'
                '      error "kakao_search_button_missing"\n'
                '    end try\n'
                '    delay 0.25\n'
                '  end tell\n'
                'end tell',
                timeout=10,
            )
            ensure_kakao_frontmost()
        wait_for_search_field()
    set_clipboard(target)
    run_osascript(
        'tell application "System Events"\n'
        '  tell process "KakaoTalk"\n'
        '    key code 0 using command down\n'
        '    key code 51\n'
        '    key code 9 using command down\n'
        '  end tell\n'
        'end tell',
        timeout=10,
    )
    wait_for_search_value(target)


def front_kakao_window_name() -> str:
    return run_osascript(
        'tell application "System Events"\n'
        '  tell process "KakaoTalk"\n'
        '    if (count of windows) > 0 then\n'
        '      return name of front window\n'
        '    else\n'
        '      return ""\n'
        '    end if\n'
        '  end tell\n'
        'end tell\n'
        'return ""',
        timeout=5,
    )


def chat_window_is_open(target: str) -> bool:
    title = normalize_title(
        front_kakao_window_name()
        .replace(" - KakaoTalk", "")
        .replace(" - 카카오톡", "")
    )
    if not title or title in {"KakaoTalk", "카카오톡"}:
        return False
    normalized_target = normalize_title(target)
    return normalized_target in title or title in normalized_target


def close_kakao_chat() -> None:
    try:
        title = normalize_title(front_kakao_window_name())
        if title and title not in {"KakaoTalk", "카카오톡"}:
            run_osascript(
                'tell application "System Events" to tell process "KakaoTalk"\n'
                '  key code 13 using command down\n'
                'end tell',
                timeout=5,
            )
            time.sleep(0.3)
            return
        if focused_search_value() is None:
            return
        run_osascript(
            'tell application "System Events" to tell process "KakaoTalk"\n'
            '  key code 53\n'
            'end tell',
            timeout=5,
        )
    except SenderError:
        return
    time.sleep(0.25)


def open_friend_chat(search_name: str, close_after_check: bool = False) -> None:
    target = validate_search_name(search_name)
    focus_friend_search(target)
    run_osascript(
        'tell application "System Events" to tell process "KakaoTalk"\n'
        '  key code 125\n'
        '  delay 0.15\n'
        '  key code 125\n'
        '  delay 0.25\n'
        '  key code 36\n'
        'end tell',
        timeout=10,
    )
    time.sleep(chat_open_wait())
    if not chat_window_is_open(target):
        run_osascript(
            'tell application "System Events" to tell process "KakaoTalk"\n'
            '  key code 36\n'
            'end tell',
            timeout=5,
        )
        time.sleep(chat_open_wait())
    if not chat_window_is_open(target):
        close_kakao_chat()
        raise SenderError("chat_window_not_opened")
    if close_after_check:
        close_kakao_chat()


def send_button_enabled() -> bool:
    return run_osascript(
        'tell application "System Events"\n'
        '  tell process "KakaoTalk"\n'
        '    try\n'
        '      repeat with b in buttons of front window\n'
        '        try\n'
        '          if (description of b as text) is "버튼" then\n'
        '            if enabled of b is true then return "1"\n'
        '          end if\n'
        '        end try\n'
        '      end repeat\n'
        '      return "0"\n'
        '    on error\n'
        '      return "0"\n'
        '    end try\n'
        '  end tell\n'
        'end tell',
        timeout=5,
    ) == "1"


def focus_chat_input() -> None:
    result = run_osascript(
        'tell application "System Events"\n'
        '  tell process "KakaoTalk"\n'
        '    try\n'
        '      set frontmost to true\n'
        '      set w to front window\n'
        '      set p to position of w\n'
        '      set sz to size of w\n'
        '      click at {(item 1 of p) + ((item 1 of sz) / 2), (item 2 of p) + (item 2 of sz) - 48}\n'
        '      delay 0.15\n'
        '      return "1"\n'
        '    on error\n'
        '      return "0"\n'
        '    end try\n'
        '  end tell\n'
        'end tell',
        timeout=8,
    )
    if result != "1":
        raise SenderError("kakao_input_failed")


def wait_for_send_button(expected_enabled: bool, timeout: float = 2.0) -> None:
    deadline = time.time() + timeout
    while time.time() <= deadline:
        if send_button_enabled() is expected_enabled:
            return
        time.sleep(0.1)
    raise SenderError("kakao_send_failed" if not expected_enabled else "kakao_paste_failed")


def click_send_button() -> None:
    run_osascript(
        'tell application "System Events"\n'
        '  tell process "KakaoTalk"\n'
        '    repeat with b in buttons of front window\n'
        '      try\n'
        '        if ((description of b as text) is "버튼") and (enabled of b is true) then\n'
        '          click b\n'
        '          return\n'
        '        end if\n'
        '      end try\n'
        '    end repeat\n'
        '    error "kakao_send_button_missing"\n'
        '  end tell\n'
        'end tell',
        timeout=8,
    )


def paste_chat_message(text: str) -> None:
    focus_chat_input()
    set_clipboard(text)
    run_osascript(
        'tell application "System Events" to tell process "KakaoTalk"\n'
        '  key code 9 using command down\n'
        'end tell',
        timeout=10,
    )
    time.sleep(paste_wait(text))
    wait_for_send_button(True, timeout=2.0)


def send_kakao_message(search_name: str, message: str, dry_run: bool) -> None:
    text = str(message or "").strip()
    if not text:
        raise SenderError("empty_message")
    if dry_run:
        open_friend_chat(search_name, close_after_check=True)
        return
    open_friend_chat(search_name, close_after_check=False)
    paste_chat_message(text)
    run_osascript(
        'tell application "System Events" to tell process "KakaoTalk"\n'
        '  key code 36\n'
        'end tell',
        timeout=10,
    )
    time.sleep(0.35)
    if send_button_enabled():
        click_send_button()
    wait_for_send_button(False, timeout=2.0)
    if os.environ.get("KAKAO_CLOSE_CHAT_AFTER_SEND", "1") != "0":
        close_kakao_chat()


def prepare_kakao_target(search_name: str) -> None:
    open_friend_chat(search_name, close_after_check=True)


def process_prepare_job(client: Client, claimed: dict, delay: float) -> None:
    job_id = str(claimed["id"])
    results: list[dict] = []
    try:
        claimed = expand_local_group_job(client, claimed)
    except SenderError as exc:
        results.append({"id": f"kg_error_{uuid.uuid4().hex}", "status": "blocked", "error": exc.reason, "sent_at": ""})
        client.finish(job_id, "prepare_blocked", results)
        print(f"prepare_blocked: {job_id} {exc.reason}", file=sys.stderr)
        return
    ok, reason = preflight_ui(False)
    if not ok:
        for recipient in claimed.get("recipients") or []:
            results.append({"id": recipient.get("id"), "status": "blocked", "error": reason, "sent_at": ""})
        client.finish(job_id, "prepare_blocked", results)
        print(f"prepare_blocked: {job_id} {reason}")
        return

    recipients = claimed.get("recipients") or []
    report_every = progress_every()
    for recipient in recipients:
        if should_stop(client, job_id):
            results.append({"id": recipient.get("id"), "status": "stopped", "error": "stop_requested", "sent_at": ""})
            print(f"prepare_stopped: {job_id}")
            break
        result = {"id": recipient.get("id"), "status": "prepare_failed", "error": "", "sent_at": ""}
        try:
            prepare_kakao_target(str(recipient.get("kakao_display_name") or ""))
            result["status"] = "ready"
            print(f"ready: {job_id}:{recipient.get('id', '-')}")
        except SenderError as exc:
            result["error"] = exc.reason
            print(f"prepare_failed: {job_id}:{recipient.get('id', '-')} ({exc.reason})", file=sys.stderr)
            if fatal_sender_error(exc.reason):
                result["status"] = "blocked"
                results.append(result)
                for remaining in recipients[len(results):]:
                    results.append({"id": remaining.get("id"), "status": "blocked", "error": exc.reason, "sent_at": ""})
                break
        results.append(result)
        if len(results) < len(recipients) and len(results) % report_every == 0:
            try:
                client.progress(job_id, "preparing", results)
            except Exception as exc:  # noqa: BLE001 - progress reporting must not stop local checks.
                print(f"progress_failed: {job_id} ({type(exc).__name__})", file=sys.stderr)
        if delay > 0:
            time.sleep(delay)

    ready = any(item["status"] == "ready" for item in results)
    blocked = any(item["status"] == "blocked" for item in results)
    stopped = any(item["status"] == "stopped" for item in results)
    status = "stopped" if stopped else "prepared" if ready else "prepare_blocked" if blocked else "prepare_failed"
    client.finish(job_id, status, results)


def process_send_job(client: Client, claimed: dict, dry_run: bool, delay: float) -> None:
    job_id = str(claimed["id"])
    results: list[dict] = []
    ok, reason = preflight_ui(dry_run)
    if not ok:
        for recipient in claimed.get("recipients") or []:
            results.append({"id": recipient.get("id"), "status": "blocked", "error": reason, "sent_at": ""})
        client.finish(job_id, "blocked", results)
        print(f"blocked: {job_id} {reason}")
        return

    recipients = claimed.get("recipients") or []
    prepared_mode = any(recipient.get("status") == "ready" for recipient in recipients)
    for recipient in recipients:
        if recipient.get("status") == "sent":
            results.append({
                "id": recipient.get("id"),
                "status": "sent",
                "error": "",
                "sent_at": recipient.get("sent_at") or "",
            })
            print(f"skip_sent: {job_id}:{recipient.get('id', '-')}")
            continue
        if prepared_mode and recipient.get("status") != "ready":
            results.append({"id": recipient.get("id"), "status": "skipped", "error": "not_prepared", "sent_at": ""})
            print(f"skip_not_ready: {job_id}:{recipient.get('id', '-')}")
            continue
        if should_stop(client, job_id):
            results.append({"id": recipient.get("id"), "status": "stopped", "error": "stop_requested", "sent_at": ""})
            print(f"stopped: {job_id}")
            break
        result = {"id": recipient.get("id"), "status": "failed", "error": "", "sent_at": ""}
        try:
            send_kakao_message(
                str(recipient.get("kakao_display_name") or ""),
                str(recipient.get("message") or ""),
                dry_run,
            )
            result["status"] = "dry_run" if dry_run else "sent"
            result["sent_at"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
            print(f"{result['status']}: {job_id}:{recipient.get('id', '-')}")
        except SenderError as exc:
            result["error"] = exc.reason
            print(f"failed: {job_id}:{recipient.get('id', '-')} ({exc.reason})", file=sys.stderr)
            if fatal_sender_error(exc.reason):
                result["status"] = "blocked"
                results.append(result)
                for remaining in recipients[len(results):]:
                    results.append({"id": remaining.get("id"), "status": "blocked", "error": exc.reason, "sent_at": ""})
                break
        except Exception as exc:  # noqa: BLE001 - preserve automation failure reason for operator.
            result["error"] = type(exc).__name__
            print(f"failed: {job_id}:{recipient.get('id', '-')} ({type(exc).__name__})", file=sys.stderr)
        if result not in results:
            results.append(result)
        if delay > 0:
            time.sleep(delay)

    blocked = any(item["status"] == "blocked" for item in results)
    failed = any(item["status"] == "failed" for item in results)
    skipped = any(item["status"] == "skipped" for item in results)
    stopped = any(item["status"] == "stopped" for item in results)
    status = "stopped" if stopped else "blocked" if blocked else "dry_run_done" if dry_run else ("failed" if failed or skipped else "done")
    client.finish(job_id, status, results)


def process_group_admin_job(client: Client, claimed: dict) -> None:
    job_id = str(claimed["id"])
    action = str(claimed.get("group_action") or "")
    try:
        summary = perform_local_group_admin(claimed)
        client.finish(job_id, "group_manage_done", [], summary=f"{local_group_summary(action)}\n{summary}")
        print(f"group_manage_done: {job_id}:{action}")
    except SenderError as exc:
        client.finish(job_id, "group_manage_failed", [], summary=f"{local_group_summary(action)} 실패: {exc.reason}")
        print(f"group_manage_failed: {job_id}:{action} ({exc.reason})", file=sys.stderr)
    except Exception as exc:  # noqa: BLE001 - keep sender alive and report the local failure.
        client.finish(job_id, "group_manage_failed", [], summary=f"{local_group_summary(action)} 실패: {type(exc).__name__}")
        print(f"group_manage_failed: {job_id}:{action} ({type(exc).__name__})", file=sys.stderr)


def process_job(client: Client, job: dict, dry_run: bool, delay: float) -> None:
    claimed = client.claim(str(job["id"]))
    if claimed.get("status") == "group_managing" or claimed.get("claim_phase") == "group_manage":
        process_group_admin_job(client, claimed)
        return
    if claimed.get("status") == "preparing" or claimed.get("claim_phase") == "prepare":
        process_prepare_job(client, claimed, delay)
        return
    process_send_job(client, claimed, dry_run, delay)


def run_once(client: Client, dry_run: bool, delay: float) -> int:
    jobs = client.claimable_jobs()
    if not jobs:
        print("no claimable jobs")
        return 0
    process_job(client, jobs[0], dry_run, delay)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Send approved ARSEN Kakao notice jobs from Mac Air.")
    parser.add_argument("--send", action="store_true", help="Actually send messages through KakaoTalk UI automation. Default is dry-run.")
    parser.add_argument("--loop", action="store_true", help="Poll for approved jobs until stopped.")
    parser.add_argument("--interval", type=float, default=10.0, help="Polling interval seconds for --loop.")
    parser.add_argument("--delay", type=float, default=2.0, help="Delay between Kakao recipients.")
    args = parser.parse_args()

    values = env()
    admin_key = values.get("ADMIN_API_KEY", "")
    if not admin_key:
        print("ADMIN_API_KEY is not configured", file=sys.stderr)
        return 2
    base_url = values.get("PUBLIC_BASE_URL", "https://apply.arsen-ai.com")
    client = Client(base_url, admin_key)
    dry_run = not args.send
    while True:
        try:
            run_once(client, dry_run=dry_run, delay=args.delay)
        except error.HTTPError as exc:
            print(f"http error: {exc.code}", file=sys.stderr)
        if not args.loop:
            return 0
        time.sleep(max(1.0, args.interval))


if __name__ == "__main__":
    raise SystemExit(main())
