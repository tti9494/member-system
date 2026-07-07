# 전체 검증 + 안전 리팩토링 세션 기록 (2026-07-07)

Claude Code 세션에서 member-system 전체 기능 검증(신청/회원/관리자/카카오/스터디/후기/YoonBot)과
안전 범위 리팩토링을 진행한 기록. 코덱스 등 다른 채널이 이어서 작업할 때 참고한다.

## 커밋 목록 (이 세션, 오래된 것 → 최신 순)

Claude Code 채널이 작성한 커밋(★)과 병렬 세션(코덱스 채널) 작업물을 반영/포함한 커밋을 함께 적는다.

| hash | 작성 | 내용 |
|---|---|---|
| `bf428a2` | ★ Claude Code | fix: 테마 버튼 disabled 스타일 고착 해소 + YOONBOT 브랜드 표기 통일 |
| `2a8121a` | ★ Claude Code | feat: 무료강의 신청 백엔드 검증 + status.html 테마 정합 |
| `81c1daf` | 코덱스 작업물, Claude Code 커밋 | feat: 스터디/카카오 공지/회원 레벨 (병렬 세션 작업물 반영) |
| `2c8c1f4` | ★ Claude Code | chore: 발송 스크립트 경로 하드코딩 제거 + 세션 규칙 문서화 |
| `5babe30` | 코덱스 채널 | feat(kakao-notice): 발송 전 승인 단계 AI 문구 다듬기 + 승인 미리보기 개선 |
| `0edbfe0` | 코덱스 채널 | docs(kakao-notice): AI 문구 다듬기 설정 변수 문서화 |
| `30f6566` | ★ Claude Code | polish: 안내 명칭 구분 + 예약 상태색 복원 + 테마 자산 캐시 키 갱신 |
| `0791e11` | ★ Claude Code | docs: 2026-07-07 운영 배포 기록 추가 |

배포 시점 기준 main = codex 브랜치 = origin 모두 `0791e11` (또는 이후) 로 동기화됨.
병렬 세션(코덱스)이 계속 작업 중일 수 있으니 그 채널에서 `git pull` 로 동기화 후 이어갈 것.

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

6. **테마 자산 캐시 키** — 테마 CSS(`arsen-theme.css` / `themes/*.css`)를 수정하면 반드시
   `theme-loader.js`의 `THEME_ASSET_VERSION`과 전 페이지의 `?v=` 쿼리 키를 같은 값으로 올린다.
   현재 값은 `button-state-colors-v3`. 안 올리면 재방문 브라우저가 구버전 CSS를 캐시에서 계속 쓴다.

7. **예약 카드 상태색 예외** — 테마는 `.state-label`을 blue로 통일하지만, 예약 카드의 상태 라벨만
   예외로 상태색을 유지한다 (`.booking-card.confirmed .state-label`=green,
   `.booking-card.pending .state-label`=amber). 상태 구분이 운영 판단에 쓰이므로 이 예외는 유지할 것.

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

## 후속 다듬기 (커밋 `30f6566` 에서 처리 완료)

이전에 "남은 관찰 사항"으로 적었던 3건은 모두 처리했다. 재작업 불필요.

- **안내 명칭 구분** — "준비물 안내"(유료 준비물)와 "무료강의 안내"(무료)는 서로 다른 기능이라
  통일이 아니라 구분이 맞다. 무료 쪽 모달 명칭에서 "준비물"을 제거(`무료강의 준비물 안내 문구`
  → `무료강의 안내 문구`)하고 `tests/test_admin_frontend_contract.py` 문구 기대값도 함께 갱신.
- **상담 마스킹 문구 명확화** — admin.html 상담 탭 helper 문구를 "관리자 인증 상태에서 원문 표시"
  → "관리자 권한으로 원문을 조회해 표시합니다 (조회 기록이 남습니다)"로 수정. 조회 감사 로그는 실기능.
- **예약 상태색 복원** — `arsen-theme.css`/`arsen-modern.css`에 예외 규칙 추가:
  `.booking-card.confirmed .state-label` = green, `.booking-card.pending .state-label` = amber.
  (기본 `.state-label`은 여전히 blue 통일 규칙을 따르되, 예약 카드 상태 라벨만 상태색 유지.)
- **테마 자산 캐시 키 통일** — 전 프론트 페이지의 `theme-loader.js?v=` / `arsen-theme.css?v=` 키를
  `button-state-colors-v3`로 통일(`theme-loader.js`의 `THEME_ASSET_VERSION`도 동일). 재방문
  브라우저의 구버전 CSS 캐시(버튼 고착 버그 포함)를 무효화하기 위함. 테마 CSS를 바꿀 때는
  이 키도 함께 올려야 사용자 브라우저에 반영된다.

## 현재 남은 관찰 사항 (수정 안 함)

- 없음. 이번 세션에서 발견한 안전 수정 범위 항목은 모두 처리했다.
  추가 개선(예: 대규모 파일 분리, DB 스키마 변경, 인증 방식 변경)은 승인 범위 밖이라 손대지 않았다.

## 운영 배포 기록 (2026-07-07)

- main 병합: `14f4566` → `30f6566` (fast-forward) 후 push, 이어 배포 기록 커밋 `0791e11`까지 push 완료.
  main = codex 브랜치 = origin 모두 동일 HEAD로 동기화.
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
