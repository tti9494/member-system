# 전체 검증 + 안전 리팩토링 세션 기록 (2026-07-07)

Claude Code 세션에서 member-system 전체 기능 검증(신청/회원/관리자/카카오/스터디/후기/YoonBot)과
안전 범위 리팩토링을 진행한 기록. 코덱스 등 다른 채널이 이어서 작업할 때 참고한다.

## 커밋 목록 (이 세션)

| hash | 내용 |
|---|---|
| `bf428a2` | fix: 테마 버튼 disabled 스타일 고착 해소 + YOONBOT 브랜드 표기 통일 |
| `2a8121a` | feat: 무료강의 신청 백엔드 검증 + status.html 테마 정합 |
| `81c1daf` | feat: 스터디/카카오 공지/회원 레벨 (병렬 세션 코덱스 작업물 반영 커밋) |
| (이후) | chore: 발송 스크립트 경로 하드코딩 제거 + 본 문서 |

## 확립된 규칙 (계약 테스트로 보호됨 — 어기면 pytest 실패)

1. **테마 CSS transition 규칙** — `frontend/assets/arsen-theme.css` / `themes/arsen-modern.css`의
   버튼 계열 규칙에서 `!important`로 선언된 색상 속성(background/opacity/border-color)을
   transition 대상으로 두지 않는다. `transition: transform 0.18s ease;`만 유지.
   - 근거: Chromium에서 `!important` 속성이 transition 대상이면 버튼 disabled 해제 후에도
     저대비 회색 상태로 계산값이 고정되는 문제 실측 (kakao-members.html 목록 불러오기 버튼에서 발견).
     버튼을 로딩 중 disabled로 토글하는 모든 페이지에서 재현 가능했다.
   - 보호: `tests/test_admin_frontend_contract.py::test_yoonbot_brand_copy_and_theme_button_state_contracts`

2. **브랜드 표기** — 공개 페이지·관리자 화면 모두 `YOONBOT` 대문자 통일.
   `윤봇`, `YoonBot` 혼용 금지. 공개 판매 페이지(yoonbot.html)에 `MVP` 같은 내부 개발 용어 노출 금지.
   (운영자 전용 페이지 license-admin.html 등은 예외.)
   - 보호: 위와 동일 테스트

3. **main.py ↔ worker.js 동등성(parity)** — 신청/검증/정책 로직을 한쪽에만 추가하지 않는다.
   운영은 Cloudflare worker, 로컬은 FastAPI 양쪽 모두 실행 경로다.
   - 사례: 무료강의 신청 시 참여 가능 지역·시간대 필수 검증을
     `agents/validator.py`(main.py 경로)와 `cloudflare/src/worker.js` `handleApply`에 동일 문구로 추가.
     join-free.html 프론트 필수 항목과 같은 기준 (API 직접 호출 우회 방지 목적).
   - 보호: `test_apply_free_plan_backend_validation_contracts` (양쪽 소스에 동일 에러 문구 존재 검증)

4. **status.html 색상은 테마 변수 사용** — status.html은 `arsen-theme.css` + `theme-loader.js`
   체계를 따른다. 카드/칩/복사 박스 등 동적 요소에 하드코딩 다크 색상(`#0c131b`, `#d9e5f2` 등) 금지,
   `var(--chip)` / `var(--ink)` 등 공용 변수 사용. 테마가 body에서 동일 변수명을 `!important`로
   재정의하는 구조이므로 변수만 쓰면 테마 전환이 자동 반영된다.
   - 근거: 로그인 후 예약 카드 제목이 "테마 흰 카드 위 밝은 글씨"로 렌더링되던 저대비 결함 수정.
   - 보호: 위 계약 테스트 (`#d9e5f2`, `#0c131b` 문자열 부재 검증)

5. **경로 하드코딩 금지** — `scripts/kakao_notice_sender.py`의 `/Users/yoon/...` 절대경로를
   `Path.home()` 기준으로 정리. 신규 스크립트도 동일 원칙 (`KAKAO_GROUP_DB` 환경변수 재정의 지원).

## 검증 절차 (수정 후 필수)

```bash
./venv/bin/python -m pytest -q tests/          # 전체 (2026-07-07 기준 247 passed)
npm --prefix cloudflare run check              # worker 문법 + copy/launcher 계약 + build inputs
```

로컬 UI 확인:

```bash
./venv/bin/uvicorn main:app --host 127.0.0.1 --port 8124
# http://127.0.0.1:8124/frontend/admin.html (localhost는 로컬 테스트 DB 미리보기 자동 적용)
```

운영 읽기 전용 확인: `npm --prefix cloudflare run smoke:production`.
`compare:production`의 로컬 vs D1 카운트 mismatch는 로컬이 테스트 전용 DB라서 나는 정상 차이다
— mismatch만으로 실패 판정하지 않는다.

## 검증 완료 항목 (2026-07-07 기준, 재작업 불필요)

- 무료 세션 중복 예약 방지: main.py `find_active_member_booking` + worker.js SQL 가드로
  이미 양쪽 구현되어 있음 (canceled/rejected/no_show 제외 후 기존 예약 재사용).
- `isFreeSession`의 스터디 세션 제외: main.py/worker.js parity 일치 확인.
- 카카오만 로그인한 미신청자는 `linked=false`·member=null로 회원 취급되지 않음 (정책 준수).
- UI 실측: 데스크톱 1440/모바일 390 전 페이지 + admin 9탭 — 대비 결함 0건, body 가로 overflow 0건.
- build-pages.mjs에 kakao-members.html / study.html 포함됨.
- .gitignore: *.db / *.log / private/ 등 추적 0건 확인.

## 남은 관찰 사항 (수정 안 함 — 후속 판단 필요)

- admin.html 내 "무료강의 안내 복사" vs "준비물 안내 복사" 명칭 혼용 — 통일하려면
  `cloudflare/scripts/check-admin-copy-contracts.mjs`의 고정 문구와 함께 움직여야 한다.
- 상담 목록의 "관리자 인증 상태에서 원문 표시" 문구가 모호하다는 관찰 (기능은 정상).
- status.html의 `.state-label` 색상이 테마 `!important` 규칙에 의해 상태별 색(green/amber) 대신
  blue로 통일 렌더링됨 — 저대비는 아니고 일관성 문제. 상태색 복원이 필요하면 테마 쪽 규칙 조정.

## 운영 배포 기록 (2026-07-07)

- main 병합: `14f4566` → `30f6566` (fast-forward, 12커밋) 후 push 완료.
- 배포 전 D1 백업: `cloudflare/.data/backups/arsen_member_system-2026-07-06T23-55-53-891Z.sql` (565KB, git 미추적).
- `npm --prefix cloudflare run deploy:cloudflare` 실행 — 7단계 전부 성공,
  로컬 데이터 import는 건너뜀 (운영 D1 데이터 보존), 마이그레이션은 추가형 ALTER만.
- 배포 후 검증:
  - `smoke:production` 전 항목 정상 (health/페이지 200, 무키 401, 회원 98명, launcher 0.1.0)
  - 무료강의 검증 실동작: region 없는 free `/apply` → 400 "참여 가능 지역을 입력해야 합니다."
    (거절이 중복 확인·DB 기록·알림보다 먼저라 부작용 없음)
  - 정적 자산 반영: yoonbot 구 문구 0건, 테마 신규 규칙 서빙 확인, status 구 색상 0건
- 배포 범위에 병렬 세션 커밋 2건 포함: `5babe30` (kakao-notice AI 문구 다듬기 — 승인 단계,
  키 미설정 시 원문 사용), `0edbfe0` (관련 문서). 테스트 247건 통과 상태로 배포함.
- 캐시 키 `button-state-colors-v3` 통일 배포 — 재방문 브라우저도 새 테마 CSS 수신.
