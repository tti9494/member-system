---
title: 예약 운영자 워크플로우 / 운영자 요약 — member-system 구현자 인덱스 v1
project: member-system
created_at: 2026-05-09 KST
machine: macair
channel: 에어웹
worker: claude-ui
work_id: AUTOPLAN-100
status: implementation_index
scope: read-only 인덱스. DB / 코드 직접 수정 0
external_publish: false
external_payment: false
external_calendar_write: false
db_change: false
public_site_change: false
parent_specs:
  - /Users/yoon/ai-tools/docs/design/booking_operator_workflow_v1.md
  - /Users/yoon/ai-tools/docs/design/booking_operator_summary_v1.md
  - /Users/yoon/ai-tools/docs/design/booking_pre_calendar_consolidation_v1.md
  - /Users/yoon/ai-tools/docs/design/booking_admin_dashboard_mockup.md
related_specs:
  - /Users/yoon/member-system/docs/booking_api_data_model_plan.md
  - /Users/yoon/member-system/docs/arsen_ai_web_course_cta_review.md
related_code:
  - /Users/yoon/member-system/main.py
  - /Users/yoon/member-system/db.py
  - /Users/yoon/member-system/agents/booking_manager.py
  - /Users/yoon/member-system/agents/encryptor.py
  - /Users/yoon/member-system/agents/security_checker.py
  - /Users/yoon/member-system/agents/telegram_notifier.py
  - /Users/yoon/member-system/frontend/admin.html
final_status_code: AUTOPLAN_BOOKING_MEMBER_010_READY
---

# 예약 운영자 워크플로우 / 운영자 요약 — member-system 구현자 인덱스 v1

## 0. 본 문서 위치

본 문서는 **AUTOPLAN-100 운영자 요약 v1 의 member-system 측 인덱스**입니다. 부모 spec 4건 (092 워크플로우 / 100 운영자 요약 / 096 캘린더 연동 전 통합 / mockup) 의 본문을 복제하지 않고, **member-system 구현자가 어디를 봐야 하는지 / 어디를 건드려야 하는지** 만 1 페이지로 압축한 index 영역입니다.

본 문서가 **하지 않는 것**:
- 부모 spec 본문 정정 / 갱신 0 (참조만)
- DB / 코드 / `frontend/` / `.env` 직접 수정 0
- 외부 발행 / 결제 / 캘린더 / 알림 API 호출 0
- 신규 SSOT 정의 0 — index 영역만

본 문서가 **하는 것**:
- 부모 spec 4건 → member-system 구현 파일 매핑 1건
- Phase 1 / 2 / 3 진입 시 member-system 측 작업 영역 1줄 단위 정리
- 보호 대상 / 변경 0 검증 매트릭스
- 후속 task 7건 (T-BS-1 ~ T-BS-7) 의 member-system 측 영역 표기

---

## 1. 핵심 결정 본문 (인덱스)

| 결정 | 값 |
|---|---|
| 운영자 단위 | 1 운영자 (상욱님 단독) |
| 진입 화면 | 1 화면 (`frontend/admin.html`) — 별 화면 0 |
| 운영자 진입 시각 cut | 4단 (0~3초 / 3~10초 / 10~30초 / 30초~3분) — `booking_operator_summary_v1.md` § 2 |
| 5 시나리오 | 평일 아침 / 점심 / 강의 직전 / 강의 직후 / 주간 회고 — `booking_operator_workflow_v1.md` § 1 |
| 캘린더 미접촉 영역 | Phase 1 + 2 + 3 (캘린더 OAuth = Phase 5 게이트, 본 v1 영역 외) |
| 신설 endpoint 수 | 10건 (`booking_operator_workflow_v1.md` § 5.2) |
| 신설 DB 컬럼 수 | 3건 (`payment_guide_sent_at` / `cancel_token` / `feedback_status`) |
| 신설 `frontend/admin.html` 섹션 수 | 4건 (publish 게이트 / 4-state 큐 / Week 보드 / KPI strip 확장) |
| LLM 자동 카피 영역 | 0 (운영자 1줄 / 다음 결정 = 결정론 매핑 단독) |
| dashboard 005 카드 | 단방향 read 통과 영역 — `arsen-dashboard` frontend 영역 변경 = 별 task (T-BS-7) |

---

## 2. 부모 spec → member-system 구현 파일 매핑

### 2.1 spec 본문 → 코드 영역

| 부모 spec § | 본문 영역 | member-system 파일 | 진입 함수 / 라인 |
|---|---|---|---|
| 092 § 3.1 (현 자산) | `members` / `sessions` / `bookings` / `member_logs` 테이블 | `db.py` | § 17-116 |
| 092 § 3.1 | 신청 입수 + 자동 검증 7단계 | `main.py` | `POST /apply` § 294-381 |
| 092 § 3.1 | 운영자 검토 + 승인 / 거절 | `main.py` | `POST /approve/{id}` § 384-401 / `POST /reject/{id}` § 404-415 |
| 092 § 3.1 | 슬롯 신규 등록 / 시드 / 수정 | `main.py` | `POST /admin/sessions` § 486-491 / seed-default-sunday § 494-498 / `POST /admin/sessions/{id}` § 501-508 |
| 092 § 3.1 | 신청 큐 조회 / 상태 전이 | `main.py` | `GET /admin/bookings` § 511-518 / `POST /admin/bookings/{id}/state` § 521-538 |
| 092 § 3.1 | 정원 자동 전이 | `agents/booking_manager.py` | `refresh_session_counts` |
| 092 § 3.1 | PII 암호화 + 보안 검사 + 텔레그램 알림 | `agents/encryptor.py` / `agents/security_checker.py` / `telegram_notifier.py` |
| 092 § 6.1~6.5 | 관리자 콘솔 추가 섹션 4건 | `frontend/admin.html` | 17524 bytes 본문 (디자인 토큰 § 7-31 재사용) |
| 100 § 8.1 | view contract 본문 schema | `frontend/admin.html` | 신설 영역 (T-BS-1) |
| 100 § 2.1~2.4 | 진입 시각 cut 4단 | `frontend/admin.html` | 신설 영역 (T-BS-1) |
| 100 § 4 | 운영자 1줄 / 다음 결정 결정론 매핑 | `frontend/admin.html` (클라이언트 JS) | 신설 함수 (T-BS-2) |

### 2.2 신설 endpoint → 진입 파일

| Endpoint | Method | 인증 | 진입 파일 | Phase |
|---|---|---|---|---|
| `/admin/sessions/{id}/publish` | POST | admin | `main.py` 신설 | 1 |
| `/admin/sessions/{id}/unpublish` | POST | admin | `main.py` 신설 | 1 |
| `/admin/sessions/{id}/cancel` | POST | admin | `main.py` 신설 | 2 |
| `/admin/sessions/{id}/notify-applicants` | POST | admin | `main.py` 신설 + `telegram_notifier.py` 보강 | 2 |
| `/admin/sessions/{id}/mark-attended-bulk` | POST | admin | `main.py` 신설 | 2 |
| `/admin/bookings/{id}/send-payment-guide` | POST | admin | `main.py` 신설 + `db.py` `payment_guide_sent_at` 컬럼 | 2 |
| `/admin/feedback/queue` | GET | admin | `main.py` 신설 + `db.py` `feedback_status` 컬럼 | 3 |
| `/admin/feedback/{id}/done` | POST | admin | `main.py` 신설 | 3 |
| `/booking/{id}/cancel` | POST | cancel_token | `main.py` 신설 + `db.py` `cancel_token` 컬럼 | 3 |
| `/booking/{id}/me` | GET | cancel_token | `main.py` 신설 | 3 |

---

## 3. Phase 별 member-system 작업 영역

### 3.1 Phase 1 — 슬롯 publish/unpublish + 공개 응답 마스킹 (저위험)

| 작업 | 진입 파일 | 본질 |
|---|---|---|
| `sessions.status='draft'` 옵션 추가 검증 | `db.py` § 79-98 | 상태 화이트리스트 검증 (현 코드에 `draft` 통과 영역 검증 필요) |
| `POST /admin/sessions/{id}/publish` / `unpublish` | `main.py` 신설 | draft → open / open → draft (booking 0 시) |
| `GET /sessions` 응답 필드 화이트리스트 | `main.py` § 283-291 | `payment_guide` 제외 / `location` 정책 적용 (10.1 결정) |
| `frontend/admin.html` 슬롯 카드에 publish 버튼 | `frontend/admin.html` | 디자인 토큰 재사용 |
| 단위 테스트 | `tests/test_session_publish.py` 신설 | publish / unpublish / 공개 응답 마스킹 검증 |
| view contract 4단 (운영자 1줄 / 다음 결정 / KPI strip / Week 보드) | `frontend/admin.html` | 100 § 8.1 schema |
| 결정론 매핑 함수 (KO_1LINE_60_MAP / KO_DECISION_40_MAP) | `frontend/admin.html` (클라이언트 JS) | 100 § 2.1~2.2 |

**STOP 게이트 1**: 사용자 검수 (UI · 흐름).

### 3.2 Phase 2 — 슬롯 cancel + 결제 안내 + 출석 일괄 (중간)

| 작업 | 진입 파일 | 본질 |
|---|---|---|
| `bookings.payment_guide_sent_at` 컬럼 신설 | `db.py` 마이그레이션 | DB 컬럼 1건 추가 (사용자 OK 게이트) |
| `/admin/sessions/{id}/cancel` | `main.py` 신설 | 슬롯 cancel + booking 일괄 canceled + 텔레그램 |
| `/admin/sessions/{id}/notify-applicants` | `main.py` 신설 | 코드 화이트리스트 (10.11 B 결정) |
| `/admin/sessions/{id}/mark-attended-bulk` | `main.py` 신설 | confirmed 일괄 completed |
| `/admin/bookings/{id}/send-payment-guide` | `main.py` 신설 | 결제 안내 발송 + 시각 갱신 |
| 4-state 큐 1·2 + Week 보드 | `frontend/admin.html` | 100 § 2.4 |
| `telegram_notifier.notify_booking_*` hook | `agents/telegram_notifier.py` | mock 검증 우선 |

**STOP 게이트 2**: ① DB 컬럼 신설 사전 OK ② 실 알림 발송 전 mock 검증.

### 3.3 Phase 3 — 후속 피드백 + 본인 취소 (중간)

| 작업 | 진입 파일 | 본질 |
|---|---|---|
| `bookings.feedback_status` 컬럼 신설 | `db.py` 마이그레이션 | 1건 (10.7 A 결정) |
| `bookings.cancel_token` 컬럼 신설 | `db.py` 마이그레이션 | uuid4 발급 (1건) |
| `/admin/feedback/queue` / `/admin/feedback/{id}/done` | `main.py` 신설 | 피드백 큐 |
| `/booking/{id}/cancel` / `/booking/{id}/me` | `main.py` 신설 | cancel_token 인증 |
| `frontend/booking-me.html` 신설 | `frontend/booking-me.html` 신규 | 신청자 본인 화면 |
| 4-state 큐 4 (피드백 대기) | `frontend/admin.html` | 100 § 2.4 |
| weekly_report 확장 (5건 메트릭) | `main.py` `job_weekly_report` § 47-91 영역 | 092 § 5.4 |

**STOP 게이트 2**: ① DB 컬럼 신설 사전 OK ② 본인 인증 token 분실 / 재발급 흐름 검증.

### 3.4 Phase 4 / 5 / 6 — 본 인덱스 영역 외

- Phase 4 (결제 통합) → `booking_api_data_model_plan.md` § 8 위임
- Phase 5 (캘린더 OAuth) → `reservation-system-v1.md` § 7 위임
- Phase 6 (자동 알림 / 리마인더) → `booking_api_data_model_plan.md` § 8 위임

---

## 4. 보안 QA × member-system 영역 (28건 정합)

부모 spec 092 § 7 + 096 § 6 = 28건 보안 QA 위 member-system 측 진입 영역 매핑.

### 4.1 PII 노출 영역 (8건)

| 점검 | 진입 파일 | 통과 검증 |
|---|---|---|
| `GET /sessions` 응답 `payment_guide` 미포함 | `main.py` § 283-291 | 응답 필드 화이트리스트 검증 |
| `GET /sessions` 응답 `location` 노출 정책 (10.1) | 같은 | publish 시 운영자 직접 결정 (per-slot flag) |
| `GET /admin/bookings` 응답 `email_encrypted` / `phone_encrypted` 미포함 | `main.py` § 511-518 | join 결과 phone_masked 만 |
| `GET /admin/bookings` raw `applicant_name` 노출 | 같은 | 외부 신청자 진입 시 마스킹 (Phase 4+ 영역) |
| `POST /apply` 응답 PII 0 | `main.py` § 294-381 | `member_id` / `booking_id` 만 |
| `frontend/admin.html` localStorage PII 캐싱 0 | `frontend/admin.html` | 정적 검증 |
| 신청자 카드 본명 raw 노출 0 | 같은 | 마스킹 이름 (`박**`) |
| 알림 템플릿 본문 PII 0 | `agents/telegram_notifier.py` | 변수 단독 (`{slot_title}` 등) |

### 4.2 인증 / 권한 영역 (5건)

| 점검 | 진입 파일 | 통과 검증 |
|---|---|---|
| `X-Admin-Key` 미설정 시 503 | `main.py` § 137-139 | 현 자산 통과 |
| cancel_token 길이 ≥ 32자 + uuid4 | `main.py` Phase 3 신설 영역 | uuid4.hex 통과 검증 |
| cancel_token 검증 fail 시 401 | 같은 | 보안 알림 옵션 (10.13 A 결정 = lock 0 MVP) |
| 관리자 액션 `member_logs` append | `db.py` `log_action` | 모든 endpoint 통과 검증 |
| 본인 화면 URL 추측 차단 | `frontend/booking-me.html` | URL leak 위험 (096 § 9 신규 위험) |

### 4.3 입력 검증 영역 (6건)

| 점검 | 진입 파일 | 통과 검증 |
|---|---|---|
| `POST /apply` 보안 검사 | `agents/security_checker.py` | 현 자산 통과 (`main.py` § 304) |
| `POST /admin/sessions` `starts_at < ends_at` | `main.py` § 486-491 | 신설 검증 |
| `POST /admin/sessions` `capacity_min ≤ capacity_max` | 같은 | 신설 검증 |
| `POST /admin/bookings/{id}/state` 화이트리스트 | `main.py` § 521-538 | 현 자산 통과 (§ 523-528) |
| `POST /apply` rate limit | `main.py` § 294-381 | 10.8 C (MVP 0) |
| 알림 템플릿 코드 화이트리스트 | `agents/telegram_notifier.py` | 10.11 B (자유 입력 차단) |

### 4.4 동시성 / 외부 통신 / 로그 영역 (9건)

| 점검 | 진입 파일 | 통과 검증 |
|---|---|---|
| `refresh_session_counts` 트랜잭션 격리 | `agents/booking_manager.py` § 263 | `BEGIN IMMEDIATE` 보강 (Phase 1 사이드) |
| 결제 webhook idempotency | (Phase 4 영역 외) | 게이트 |
| 텔레그램 알림 발송 (테스트 시 mock) | `agents/telegram_notifier.py` | mock 우선 |
| 외부 결제 webhook 0 | (Phase 4 영역 외) | 게이트 |
| Google Calendar API 0 | (Phase 5 영역 외) | 게이트 |
| 모든 status 전이 `member_logs` append | `db.py` `log_action` | 검증 통과 |
| 슬롯 cancel 영향 booking 수 로그 | `main.py` 신설 endpoint | 로그 본문 정합 |
| 관리자 IP 기록 | `main.py` § 357 등 | 현 자산 통과 |
| 자동 알림 (Phase 6) | (Phase 6 영역 외) | 게이트 |

---

## 5. 후속 task 7건 (T-BS-1 ~ T-BS-7) → member-system 측 영역

부모 spec 100 § 11 의 T-BS-1 ~ T-BS-7 를 member-system 진입 영역으로 매핑.

| # | task | member-system 영역 | 진입 파일 | Phase |
|---|---|---|---|---|
| T-BS-1 | view contract HTML schema | `frontend/admin.html` 신설 영역 (운영자 1줄 / 다음 결정 / KPI strip 12 / STOP gate 4종) | `frontend/admin.html` | 1 |
| T-BS-2 | 결정론 매핑 함수 | 클라이언트 자바스크립트 1건 (KO_1LINE_60_MAP / KO_DECISION_40_MAP) | `frontend/admin.html` | 1 |
| T-BS-3 | STOP gate 4종 시각화 | 4-state 큐 + STOP gate badge | `frontend/admin.html` | 1·2·3 |
| T-BS-4 | 카피 표준 검증 스크립트 | 한국어 cut / 어미 / "박힘" 계열 / 색상 단독 / 톤 정적 검증 | `scripts/check_operator_copy.sh` 신설 | 1 사이드 |
| T-BS-5 | 보안 QA × 운영자 시각 분리 | 시각 영역별 마스킹 / 인증 / audit 검증 | `tests/test_operator_summary_pii.py` 신설 | 1·2·3 사이드 |
| T-BS-6 | dashboard 005 카드 정합 매핑 본문 | dashboard 005 카드 read API 명세 + admin.html 본문 정합 매트릭스 | (별 spec) | 1·2·3 통과 후 |
| T-BS-7 | dashboard 005 카드 신설 | `arsen-dashboard` frontend / backend 영역 신설 = **member-system 영역 외** | (`arsen-dashboard` 별 spec) | 별 영역 |

---

## 6. 보호 영역 변경 0 검증

본 작업 영역 = read-only 인덱스 신설 1건만. 보호 영역 7종 변경 0 검증.

| 보호 영역 | 본 작업 시점 변경 영역 | 검증 |
|---|---|---|
| `auto_agent/` (콘텐츠 자동화) | 0 | 본 작업 read 0 |
| `SYSTEM_MAP.md` | 0 | 본 작업 read 0 |
| `/Users/yoon/arsen-ai-web/` (공개 홈페이지) | 0 | 제안서만, 실 변경 0 |
| `.env` / token / API key / password / cookie / auth | 0 | 본 작업 read 0 |
| `git push` | 0 | 본 작업 영역 외 |
| `launchctl` / cron / tmux 상주 프로세스 | 0 | 본 작업 영역 외 |
| DB 직접 수정 | 0 | 본 작업 영역 외 (Phase 1·2·3 진입 = 별 task + 사용자 OK) |

### 6.1 본 작업 영역 변경 영역

| 파일 | 영역 | 본질 |
|---|---|---|
| `/Users/yoon/member-system/docs/booking_operator_workflow_summary_v1.md` | 신규 | 본 인덱스 본문 |
| `/Users/yoon/ai-tools/docs/daily/2026-05-09.md` | 갱신 (append) | 본 세션 기록 |

### 6.2 외부 발행 / 전송 / 예약 / 댓글 / DM 0 검증

| 채널 | 본 작업 시점 호출 영역 |
|---|---|
| Telegram API | 0 |
| Kakao API | 0 |
| WordPress API | 0 |
| Threads API | 0 |
| 이메일 발송 | 0 |
| Google Calendar API | 0 |
| 결제 게이트웨이 (Toss / Kakao Pay) | 0 |

---

## 7. 본 인덱스 채택 후 다음 액션

1. 부모 spec 100 § 10 의 22 결정 영역 사용자 응답 수집 → 부모 spec v1.1 보강
2. T-BC-1 (096 publish 게이트) 통과 후 T-BS-1 (view contract HTML) + T-BS-2 (결정론 매핑) 1차 진입
3. T-BS-7 (`arsen-dashboard` 005 카드) = 별 spec 발행 후 진입 (10.20 결정 통과 게이트, member-system 영역 외)
4. 본 인덱스를 `~/ai-tools/reviews/self/architecture/2026-05-09_booking-operator-workflow-summary-member-system.md` 미러링 = 사용자 합의 후 별 commit
5. `member-system/docs/booking_api_data_model_plan.md` v0.2 보강 시 본 인덱스 § 2 매핑 표 인용 동기화 (단방향 참조)

---

## 8. 한줄 결론

부모 spec 4건 (092 워크플로우 / 100 운영자 요약 / 096 캘린더 연동 전 통합 / mockup) 을 그대로 두고, **member-system 구현자 진입 영역만 1 페이지로 압축한 인덱스 1건** 을 추가하면, Phase 1·2·3 진입 시 어느 파일을 어떤 본질로 건드려야 하는지 1줄 단위로 통과 + 보안 QA 28건 → member-system 측 진입 영역 매핑 + 후속 task 7건 (T-BS-1 ~ T-BS-7) 의 member-system 영역 / 영역 외 분리까지 통과. 부모 spec 본문 정정 0 / DB 직접 수정 0 / 외부 발행 / 결제 / 캘린더 / 알림 0.

---

## 9. 최종 상태 코드

`AUTOPLAN_BOOKING_MEMBER_010_READY`
