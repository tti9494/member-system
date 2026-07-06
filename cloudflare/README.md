# member-system Cloudflare target

This folder is the Cloudflare migration target for `apply.arsen-ai.com`.

It keeps the current frontend pages as Cloudflare Pages static assets and moves
the API surface to Pages Functions / Workers with D1.

Local checks:

```bash
cd /Users/yoon/member-system/cloudflare
npm run check
npm run smoke:production
npm run compare:production
```

One-command deploy after Wrangler is authenticated:

```bash
cd /Users/yoon/member-system/cloudflare
npm run deploy:cloudflare
```

The deploy script builds static assets, creates/reuses D1, applies schema,
deploys the Worker with assets, attaches the `apply.arsen-ai.com/*` Worker
route, and sets required secrets without printing them.

Schema/migration notes before deployment:

- `schema.sql` must be applied before deploying the Worker when new tables are
  added. The review board uses `review_instructors` and `review_entries`.
- The deploy script also runs a guarded `ALTER TABLE members ADD COLUMN
  available_time_slots TEXT` for older D1 databases and ignores the duplicate
  column case. If deployment is done manually, run the same schema/migration
  step first or new application submissions can fail on older D1 schemas.
- Kakao Login adds guarded `members.kakao_id`, `members.kakao_profile`, and
  `members.kakao_connected_at` migrations plus `idx_members_kakao_id`. Register
  `https://apply.arsen-ai.com/auth/kakao/callback` in Kakao Developers before
  enabling `KAKAO_REST_API_KEY`.
- Do not run manual D1 imports over live operational data unless explicitly
  approved. The default deploy path preserves existing D1 rows.

It does not import local SQLite data by default, so live admin edits in D1 such
as booking schedule moves are not overwritten by deployment. For a first-time
migration only, run with `MEMBER_SYSTEM_IMPORT_LOCAL_DATA=1` or
`node scripts/deploy-cloudflare.mjs --import-local-data`; exported seed rows use
`INSERT OR IGNORE` and will not replace existing D1 rows.
It reuses the local `ADMIN_API_KEY`, `PHONE_SECRET_KEY`, and `EMAIL_SECRET_KEY`
from `/Users/yoon/member-system/.env`.

Smoke test `https://apply.arsen-ai.com/health` and the public/admin pages after
deployment.

Kakao notice AI polish (optional):

- Telegram `카톡공지`/`카톡그룹` 명령의 운영자 멘트를 발송 전 승인 단계에서 AI로
  다듬는다. 승인 미리보기와 실제 발송 문구는 동일한 다듬어진 텍스트를 쓴다.
- `wrangler secret put ANTHROPIC_API_KEY`(또는 `GEMINI_API_KEY`)를 설정해야
  활성화되며, 미설정 시 `polish_status=unavailable`로 원문 그대로 발송된다.
- 회원 이름/확인 코드/연락처는 AI로 전송되지 않는다. `[[호칭]]`/`[[이름]]`
  자리표시자는 다듬기 후에도 보존 검증된다.
- 조정 변수: `KAKAO_POLISH_PROVIDER`, `KAKAO_POLISH_MODEL`,
  `KAKAO_POLISH_ENABLED=0` — 상세는 `wrangler.toml.example` 주석 참조.

Private D1 backup:

```bash
cd /Users/yoon/member-system/cloudflare
npm run backup:d1
```

Backups are written under ignored `cloudflare/.data/backups/` and can contain
operational member data. Keep them private.

Operator QA after each deployment:

- Open `https://apply.arsen-ai.com/frontend/join-full` and confirm the public application page renders.
- Open `https://apply.arsen-ai.com/frontend/status` and confirm the booking status page renders.
- Open `https://apply.arsen-ai.com/frontend/admin`, connect with the admin key, and confirm Cloudflare status shows Worker + D1.
- Move one non-production test booking between two open sessions and confirm the selected target date is shown after refresh.
- Confirm cancel/payment actions refresh the dashboard without browser-level reload or admin key re-entry.

Do not print secrets or export raw member data in logs.
