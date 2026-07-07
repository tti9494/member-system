# member-system Codex Guide

## Role

`member-system` is a separate FastAPI/member-management project on Mac Air.

## Safety

- Treat member data and local SQLite files as sensitive operational data.
- Do not output `.env`, `ADMIN_API_KEY`, tokens, passwords, or database contents.
- Do not edit database files directly.
- Do not change running services or launchd state without explicit user approval.

## Work Rules

- Check `git status --short` before edits.
- Keep this project separate from `ai-tools` and Control Tower work.
- Use tests or dry-run checks before commit suggestions.
- Do not push unless explicitly requested.

## Conventions (enforced by contract tests — see docs/refactor_session_2026-07-07_ko.md)

- Brand copy is `YOONBOT` everywhere (no `윤봇`, no `YoonBot`); never expose internal
  terms like `MVP` on public sales pages.
- Keep main.py and cloudflare/src/worker.js in parity: any new validation or policy
  must land in both (example: free-plan apply requires region + time slots).
- Theme CSS button rules must transition `transform` only — transitioning
  `!important` color properties leaves buttons stuck in disabled styling on Chromium.
- Page colors use shared theme variables (`var(--chip)`, `var(--ink)`, ...);
  no hardcoded dark hex values in theme-managed pages such as status.html.
- No hardcoded `/Users/...` paths in scripts; use `Path.home()` with env overrides.
- Kakao notice AI polish: only the operator custom message is sent to the AI; member
  names/access codes/contacts are inserted deterministically in worker.js after polish.
  `[[호칭]]`/`[[이름]]` placeholders must be preserved (count-checked); any failure
  falls back to the original text. See docs/kakao_notice_polish_session_2026-07-07_ko.md.
- Verify with: `./venv/bin/python -m pytest -q tests/` and `npm --prefix cloudflare run check`.
  `compare:production` count mismatches are expected (local test DB vs production D1).
