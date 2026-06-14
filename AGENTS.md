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
