# member-system Codex Guide

## Role

`member-system` is a separate FastAPI/member-management project on Mac Air.

## Safety

- Treat member data and local SQLite files as sensitive operational data.
- Do not output `.env`, `ADMIN_API_KEY`, tokens, passwords, or database contents.
- Do not edit database files directly.
- Do not change running services or launchd state without explicit user approval.
- Legal/privacy stop gate:
  - Any new application, member, review, consultation, Kakao, Telegram, payment, or newsletter flow must state purpose, required/optional fields, retention, deletion path, and privacy-policy link before collecting personal data.
  - Keep under-14 handling explicit. If a flow cannot handle legal guardian consent, block under-14 users before submission.
  - Never log plaintext passwords, approval codes, secrets, resident registration numbers, full phone numbers, raw email addresses, Kakao identifiers, or raw message contents in server logs, Telegram notifications, test output, or exported reports.
  - Marketing messages require explicit opt-in, opt-out wording, and separate night-time consent for 21:00-08:00 sends. Service notices and advertising must be separated.
  - Location-based features require a location-law review before launch. Do not collect or infer personal location by default.
  - Withdrawal/deletion flows must delete or anonymize personal data unless a legal retention duty applies; retained payment/dispute records must be separated from active member data.
  - Resident registration numbers are forbidden unless a clear statutory basis is documented. Consent is not sufficient.

## Work Rules

- Check `git status --short` before edits.
- Keep this project separate from `ai-tools` and Control Tower work.
- Use tests or dry-run checks before commit suggestions.
- Do not push unless explicitly requested.
- At the start of substantial member-system work, explicitly choose `direct Codex`, `Orca delegation`, or `Work Bus delegation`.
- Use direct Codex for narrow, local, immediately verifiable fixes.
- Use Orca for parallel QA, UI review, research/audit, or delegated Claude/Antigravity work. Consumer Gemini-family work must use `agy`, not the legacy `gemini` CLI.
- Use Work Bus for Windows, scheduled, durable, headless, or cross-machine work that must survive the current session.
- Do not create Work Bus tasks just to create activity. Default to 0 new tasks; create at most 1-2 narrow tasks unless the user explicitly approves more.
- Every new Work Bus task must include purpose, target files/paths, whether mutation is allowed, external send/publish/deploy forbidden, expected `final_status_code`, verification method, and result storage location.
- Auto/refill mode stays off by default. Use `prepare` or a bounded short `auto --max-tasks` run only after explicit operator approval.
- After worker results return, Codex must classify them as applied/tested/proposal/stale/duplicate/blocked and decide whether they actually changed the usable member-system flow.

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
