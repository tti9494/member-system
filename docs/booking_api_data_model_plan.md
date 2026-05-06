---
title: 예약 시스템 API · 데이터 모델 설계안 (Booking)
project: member-system
version: v0.1 (draft)
created_at: 2026-05-07 KST
author: 에어코드 (Claude Code, Mac Air)
scope: read-only 분석 + 제안서. DB / 코드 직접 수정 없음.
status: 제안 (사용자 검토 대기)
related_specs:
  - /Users/yoon/member-system/db.py
  - /Users/yoon/member-system/main.py
  - /Users/yoon/member-system/agents/db_manager.py
  - /Users/yoon/member-system/agents/code_generator.py
  - /Users/yoon/member-system/agents/encryptor.py
---

# 예약 시스템 설계안 (member-system Booking)

## 0. 본 문서 위치

본 문서는 **제안서**이며 코드 / DB 변경 0. `member-system` 본진에 예약 (1:1 코칭 / 그룹 모임 / 강의 슬롯) 기능을 붙일 때의 데이터 모델·API·단계 분리 계획만 담는다.

- 결정 권한: 사용자 (윤상욱)
- 본 문서 채택 시 별도 task (`docs/tasks/pending/T???.md`) 발행 후 단계별 구현 진입
- 본 문서는 1차 초안이며, 사용자 결정 후 v0.2 로 보강 (open question 영역 § 9 참조)

---

## 1. 배경 / 목적

### 1.1 현재 `member-system` 본질
- 멤버십 신청 → 검증 → 승인 → 코드 발급 → 만료 관리 파이프라인 (FastAPI + SQLite + APScheduler)
- 기존 SSOT 테이블: `members`, `member_logs`
- ID = `uuid4` 문자열, 시간 = `ISO 8601 UTC`, 개인정보 = AES 암호화 (`encryptor.py`)
- 인증 layer: `X-Admin-Key` (ADMIN_API_KEY) — 관리자 전용 엔드포인트
- 텔레그램 알림 hook (`telegram_notifier.py`)

### 1.2 예약 시스템 추가 목적
1. 승인된 멤버 (`status=approved`) 가 **세션 슬롯**을 직접 예약
2. 외부 (비멤버) 도 결제 완료 후 슬롯 예약 가능 (옵션, § 9.1)
3. 운영자가 슬롯을 미리 발행·취소·변경 (관리자 콘솔)
4. 결제 (선택) → 캘린더 발행 → 알림 (텔레그램 + 이메일) 일관 흐름

### 1.3 통합 수준 (3가지 선택지, § 9.4 결정 영역)
| 옵션 | 본질 | 장점 | 단점 |
|---|---|---|---|
| A. 같은 DB, 같은 앱 | `members.db` 에 `slots` / `applications` / `payments` 테이블 추가 | 단일 deploy, FK 무결성 | 코드 비대, 멤버 영역 외 트래픽 영향 |
| B. 같은 DB, 별 라우터 모듈 | 같은 SQLite, `routers/booking.py` 분리 | 코드 분리, 단일 deploy | 같은 프로세스 영향 영역 잔존 |
| C. 별 앱 / 별 DB | `booking-system/` 신 레포 + 별 SQLite | 완전 분리 | FK 끊김, 멤버 인증 호출 layer 필요 |

**1차 추천**: 옵션 B (라우터 분리, 같은 DB). 사유 = 멤버 → 슬롯 FK 가 가장 자연스럽고, 운영자도 한 곳에서 관리. § 9.4 에서 사용자 결정 대기.

---

## 2. 도메인 모델 (4개 entity)

### 2.1 entity 개요

| entity | 본질 | 누가 생성 | 누가 수정 |
|---|---|---|---|
| `slot` | 예약 가능한 시간 슬롯 (1:1 / 그룹 / 강의) | 운영자 | 운영자 (취소·시간 변경) |
| `booking` (=application) | 슬롯에 대한 예약 신청 | 멤버 / 외부 신청자 | 시스템 (status 전이) + 운영자 (취소) |
| `payment` | 예약 1건에 대한 결제 (옵션) | 시스템 (결제 게이트웨이 webhook) | 시스템 (refund / cancel) |
| `calendar_event` | 캘린더 발행 결과 (Google Calendar / iCal 링크) | 시스템 (예약 확정 후) | 시스템 (취소 시 cancel) |

### 2.2 entity 간 관계
```
member 1 ─ N booking N ─ 1 slot
              │
              ├─ 1 payment      (선택, plan_type / slot.price > 0 일 때)
              │
              └─ 1 calendar_event (확정 후)
```

- `booking` ↔ `slot`: N:1 (한 슬롯에 여러 신청 가능, 단 `confirmed=1` 인 booking 은 `slot.capacity` 까지)
- `booking` ↔ `member`: N:1 (옵션, 외부 신청자도 허용 시 `member_id` nullable)
- `booking` ↔ `payment`: 1:1 (결제 미사용 슬롯이면 0)
- `booking` ↔ `calendar_event`: 1:1 (확정된 booking만 발행)

---

## 3. 상태 모델 (state machine)

### 3.1 `slot.status`
```
draft ──publish──▶ open ──fill──▶ full ──end──▶ closed
                    │
                    └─cancel──▶ canceled
```

| 상태 | 본질 |
|---|---|
| `draft` | 운영자 작성 중, 멤버에게 미노출 |
| `open` | 예약 가능, 멤버 / 외부 신청 가능 |
| `full` | `confirmed_count >= capacity`, 신규 신청 차단 (대기열 § 9.5) |
| `closed` | 시작 시각 경과, 신규 신청 차단 |
| `canceled` | 운영자 취소, 모든 booking → `slot_canceled` |

전이 트리거:
- `draft → open`: 운영자 publish API
- `open → full`: booking confirm 시 시스템 자동
- `full → open`: booking cancel / no-show 시 시스템 자동
- `open|full → closed`: APScheduler `job_close_past_slots` (매 10분)
- `* → canceled`: 운영자 cancel API (강제)

### 3.2 `booking.status`
```
                 ┌──admin_reject──▶ rejected
                 │
requested ──auto│screen ──ok──▶ pending_payment ──pay──▶ confirmed
                 │                     │                     │
                 │                     └──timeout──▶ expired │
                 │                                            │
                 └──ok (free slot)──▶ confirmed              ├─user_cancel──▶ canceled
                                                              │
                                                              ├─slot_canceled──▶ canceled
                                                              │
                                                              ├─attended──▶ completed
                                                              │
                                                              └─no_show──▶ no_show
```

| 상태 | 본질 |
|---|---|
| `requested` | 신청 직후, 자동 검증 진행 중 |
| `pending_payment` | 결제 필요 슬롯, 결제 대기 (TTL 30분 § 9.6) |
| `confirmed` | 예약 확정, 캘린더 발행 완료 |
| `expired` | 결제 미완료로 자동 만료 |
| `rejected` | 운영자 거절 (악성 / 중복 등) |
| `canceled` | 사용자 또는 슬롯 취소로 종료 |
| `completed` | 세션 완료, 출석 처리 |
| `no_show` | 세션 시작 후 미출석 처리 |

### 3.3 `payment.status` (옵션, 결제 도입 시)
```
created ──checkout──▶ pending ──succeed──▶ paid ──refund_request──▶ refunded
                          │                  │
                          └──fail──▶ failed └──charge_back──▶ disputed
```

### 3.4 `calendar_event.status`
```
queued ──publish──▶ published ──cancel──▶ canceled
                       │
                       └──update──▶ updated
```

---

## 4. 스키마 제안 (SQL DDL — 제안만)

> ⚠ 본 DDL 은 **제안서**이며 적용 0. 채택 시 별도 migration task 발행.

### 4.1 `slots` 테이블
```sql
CREATE TABLE IF NOT EXISTS slots (
    id              TEXT PRIMARY KEY,            -- uuid4
    title           TEXT NOT NULL,
    description     TEXT,
    slot_type       TEXT NOT NULL,               -- '1on1' | 'group' | 'lecture'
    starts_at       TEXT NOT NULL,               -- ISO 8601 UTC
    ends_at         TEXT NOT NULL,
    timezone        TEXT NOT NULL DEFAULT 'Asia/Seoul',
    capacity        INTEGER NOT NULL DEFAULT 1,
    confirmed_count INTEGER NOT NULL DEFAULT 0,  -- materialized for fast filter
    price_krw       INTEGER NOT NULL DEFAULT 0,  -- 0 = 무료 슬롯
    plan_required   TEXT,                        -- NULL | 'basic' | 'full'
    location        TEXT,                        -- 'online' | 'offline:address'
    meeting_url     TEXT,                        -- Zoom / Meet, 확정 후 노출
    status          TEXT NOT NULL DEFAULT 'draft',
    canceled_reason TEXT,
    created_by      TEXT NOT NULL,               -- admin id (logical)
    created_at      TEXT NOT NULL,
    updated_at      TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_slots_status_starts ON slots(status, starts_at);
CREATE INDEX IF NOT EXISTS idx_slots_starts ON slots(starts_at);
```

### 4.2 `bookings` 테이블 (=applications)
```sql
CREATE TABLE IF NOT EXISTS bookings (
    id                TEXT PRIMARY KEY,
    slot_id           TEXT NOT NULL REFERENCES slots(id),
    member_id         TEXT REFERENCES members(id),  -- NULL = 외부 신청자
    -- 외부 신청자 정보 (member_id NULL 일 때만 채움)
    external_name     TEXT,
    external_email_encrypted TEXT,
    external_email_hash      TEXT,
    external_phone_masked    TEXT,
    external_phone_encrypted TEXT,
    external_phone_hash      TEXT,
    note              TEXT,                        -- 신청 사유
    status            TEXT NOT NULL DEFAULT 'requested',
    payment_id        TEXT REFERENCES payments(id),
    calendar_event_id TEXT REFERENCES calendar_events(id),
    payment_due_at    TEXT,                        -- pending_payment TTL
    confirmed_at      TEXT,
    canceled_at       TEXT,
    canceled_reason   TEXT,                        -- 'user_cancel'|'slot_canceled'|'expired'|'admin_reject'
    completed_at      TEXT,
    no_show_at        TEXT,
    consent_at        TEXT NOT NULL,               -- 신청 시점 동의
    consent_version   TEXT NOT NULL,
    created_at        TEXT NOT NULL,
    updated_at        TEXT NOT NULL,

    UNIQUE(slot_id, member_id)                     -- 멤버는 같은 슬롯 1회만 (외부 신청자는 NULL 이라 UNIQUE 영향 0)
);

CREATE INDEX IF NOT EXISTS idx_bookings_slot ON bookings(slot_id);
CREATE INDEX IF NOT EXISTS idx_bookings_member ON bookings(member_id);
CREATE INDEX IF NOT EXISTS idx_bookings_status ON bookings(status);
CREATE INDEX IF NOT EXISTS idx_bookings_external_phone_hash ON bookings(external_phone_hash);
```

> NOTE: SQLite 의 `UNIQUE(slot_id, member_id)` 는 NULL 다중 허용 → 외부 신청자 자동 OK, 멤버 중복 차단.

### 4.3 `payments` 테이블 (옵션)
```sql
CREATE TABLE IF NOT EXISTS payments (
    id              TEXT PRIMARY KEY,
    booking_id      TEXT NOT NULL REFERENCES bookings(id),
    amount_krw      INTEGER NOT NULL,
    method          TEXT,                          -- 'toss'|'kakao'|'bank'|'manual'
    provider_tx_id  TEXT,                          -- 외부 결제 ID
    status          TEXT NOT NULL DEFAULT 'created',
    paid_at         TEXT,
    refunded_at     TEXT,
    refund_amount   INTEGER DEFAULT 0,
    failure_reason  TEXT,
    raw_payload     TEXT,                          -- webhook 원문 (JSON, 마스킹 후 저장)
    created_at      TEXT NOT NULL,
    updated_at      TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_payments_booking ON payments(booking_id);
CREATE INDEX IF NOT EXISTS idx_payments_status ON payments(status);
```

### 4.4 `calendar_events` 테이블
```sql
CREATE TABLE IF NOT EXISTS calendar_events (
    id              TEXT PRIMARY KEY,
    booking_id      TEXT NOT NULL REFERENCES bookings(id),
    provider        TEXT NOT NULL,                 -- 'google'|'ical'|'manual'
    provider_event_id TEXT,                        -- Google Calendar event ID
    ics_path        TEXT,                          -- 로컬 .ics 파일 (옵션)
    invite_email_sent INTEGER DEFAULT 0,
    status          TEXT NOT NULL DEFAULT 'queued',
    last_error      TEXT,
    created_at      TEXT NOT NULL,
    updated_at      TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_cal_booking ON calendar_events(booking_id);
CREATE INDEX IF NOT EXISTS idx_cal_status ON calendar_events(status);
```

### 4.5 `booking_logs` 테이블 (감사 append-only)
```sql
CREATE TABLE IF NOT EXISTS booking_logs (
    id          TEXT PRIMARY KEY,
    booking_id  TEXT,
    slot_id     TEXT,
    actor       TEXT NOT NULL,                     -- 'member:{id}'|'admin'|'system'|'external:{phone_hash}'
    action      TEXT NOT NULL,                     -- 'request'|'confirm'|'cancel'|'pay'|'refund'|...
    detail      TEXT,
    ip          TEXT,
    created_at  TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_blog_booking ON booking_logs(booking_id);
CREATE INDEX IF NOT EXISTS idx_blog_slot ON booking_logs(slot_id);
```

---

## 5. API 설계

### 5.1 공개 (인증 0 또는 멤버 인증)

| Method | Path | 인증 | 본질 |
|---|---|---|---|
| GET | `/booking/slots` | 0 | open / full 슬롯 목록 (publish 영역만) |
| GET | `/booking/slots/{slot_id}` | 0 | 슬롯 상세 (meeting_url 마스킹) |
| POST | `/booking/request` | 옵션 | 슬롯 신청 (멤버: `member_id` 추출 / 외부: 입력값 검증) |
| POST | `/booking/{booking_id}/cancel` | 신청자 본인 (token / member key) | 사용자 취소 (시작 24h 전까지) |
| POST | `/booking/payment/webhook` | provider signature | 결제 webhook (Toss / Kakao) |
| GET | `/booking/{booking_id}/calendar.ics` | 신청자 본인 | iCal 다운로드 |

### 5.2 관리자 (`X-Admin-Key`)

| Method | Path | 본질 |
|---|---|---|
| POST | `/admin/booking/slots` | 슬롯 신규 등록 (draft) |
| POST | `/admin/booking/slots/{id}/publish` | draft → open |
| POST | `/admin/booking/slots/{id}/cancel` | * → canceled (모든 booking 자동 취소) |
| PATCH | `/admin/booking/slots/{id}` | 시간 / 가격 / capacity 수정 (booking 영향 시 알림) |
| GET | `/admin/booking/slots` | 전체 슬롯 (draft 포함) |
| GET | `/admin/booking/bookings` | 전체 booking (status 필터) |
| POST | `/admin/booking/bookings/{id}/approve` | requested → confirmed (수동 승인 모드, § 9.7) |
| POST | `/admin/booking/bookings/{id}/reject` | requested → rejected |
| POST | `/admin/booking/bookings/{id}/mark-no-show` | confirmed → no_show |
| POST | `/admin/booking/bookings/{id}/mark-completed` | confirmed → completed |
| POST | `/admin/booking/payments/{id}/refund` | 환불 처리 (provider API 호출) |

### 5.3 시스템 (스케줄러 작업)

| job_id | 주기 | 본질 |
|---|---|---|
| `booking_close_past_slots` | 매 10분 | starts_at 경과 슬롯 → closed |
| `booking_expire_pending_payment` | 매 5분 | payment_due_at 경과 → expired |
| `booking_send_reminder` | 매시간 | 시작 24h / 1h 전 알림 |
| `booking_mark_no_show` | 매 30분 | ends_at 경과 + completed 0 → no_show 후보 (운영자 검토) |

---

## 6. Pydantic 모델 제안 (FastAPI)

```python
# routers/booking_models.py (제안)
class SlotCreate(BaseModel):
    title: str
    description: Optional[str] = None
    slot_type: Literal["1on1", "group", "lecture"]
    starts_at: datetime
    ends_at: datetime
    timezone: str = "Asia/Seoul"
    capacity: int = 1
    price_krw: int = 0
    plan_required: Optional[Literal["basic", "full"]] = None
    location: str = "online"
    meeting_url: Optional[str] = None

class BookingRequest(BaseModel):
    slot_id: str
    member_id: Optional[str] = None  # 멤버 인증 시 자동
    external_name: Optional[str] = None
    external_email: Optional[EmailStr] = None
    external_phone: Optional[str] = None
    note: Optional[str] = None
    consent_personal: bool

class BookingCancel(BaseModel):
    reason: Optional[str] = None

class PaymentWebhook(BaseModel):
    provider: Literal["toss", "kakao"]
    provider_tx_id: str
    booking_id: str
    amount_krw: int
    status: Literal["paid", "failed", "refunded"]
    signature: str
    raw: dict
```

---

## 7. 보안 / 컴플라이언스

| 항목 | 처리 |
|---|---|
| 외부 신청자 PII | `email_encrypted` / `phone_encrypted` (기존 `encryptor.py` 재사용), `*_hash` 로 중복 검사 |
| 결제 webhook | HMAC signature 검증 + replay 방지 (provider_tx_id UNIQUE) |
| meeting_url | confirmed booking 본인에게만 노출 (public GET 에선 마스킹) |
| 관리자 작업 | `require_admin` 재사용 (`X-Admin-Key`) |
| 본인 취소 인증 | booking 생성 시 `cancel_token` (uuid4) 발급 → URL 파라미터로 검증 |
| 감사 로그 | 모든 status 전이 → `booking_logs` append (member_logs 패턴 정합) |
| GDPR / 동의 | booking 생성 시 `consent_at` / `consent_version` 기록 (members 패턴 정합) |
| Rate limit | 외부 신청자 IP 기준 (분당 5회 권장, § 9.8) |

---

## 8. 단계별 구현 계획 (Phase 분리)

> 본 phase 분리는 전역 CLAUDE.md "Phase 차등화 기준" 정합. 각 phase = 1 task = 1 commit 묶음.

### Phase 1 — 데이터 모델 + 슬롯 CRUD (저위험)
**산출물**: `slots` 테이블 + `booking_logs` + 관리자 슬롯 CRUD API
1. `db.py` 에 `slots` / `booking_logs` DDL 추가 (기존 `members` 영향 0)
2. `routers/booking_admin.py` 신설 (slot CRUD, publish, cancel)
3. `frontend/admin-booking.html` 신설 (기존 `admin.html` 디자인 토큰 재사용)
4. 단위 테스트 (`test_booking_slots.py`)
5. STOP 게이트 1개: 사용자 검수 (UI · 흐름)

### Phase 2 — 멤버 신청 흐름 (무료 슬롯) (중간)
**산출물**: `bookings` 테이블 + 멤버 신청 / 취소 API + 공개 슬롯 목록 페이지
1. `bookings` DDL + `consent_at` / `consent_version` 정합
2. `POST /booking/request` (member_id 추출 + 무료 슬롯 한정 → 즉시 confirmed)
3. `POST /booking/{id}/cancel` (cancel_token 검증)
4. `frontend/booking.html` (멤버 인증 후 슬롯 목록 + 신청 폼)
5. APScheduler `booking_close_past_slots` job 추가
6. 텔레그램 알림 hook (`telegram_notifier.notify_booking_*`)
7. STOP 게이트 2개: ① 데이터 무결성 검증 (UNIQUE 제약, status 전이) ② UI 검수

### Phase 3 — 외부 신청자 (회원가입 0) (중간)
**산출물**: 외부 신청자 PII 암호화 + 공개 신청 폼
1. `bookings.external_*` 컬럼 활성 + `encryptor` 재사용
2. `frontend/booking-public.html` (외부 신청자 폼, 동의 체크)
3. 보안 검토 (`security_checker` 재사용, IP rate limit 추가)
4. STOP 게이트 1개: 보안 검수 (PII 노출 영역 0 검증)

### Phase 4 — 결제 통합 (Toss / Kakao) (고위험)
**산출물**: `payments` 테이블 + webhook + pending_payment 흐름
1. `payments` DDL + provider 추상화 (`agents/payment_provider.py`)
2. `POST /booking/payment/webhook` + signature 검증
3. `booking_expire_pending_payment` job
4. `POST /admin/booking/payments/{id}/refund`
5. 환불 정책 (시작 24h 전 100%, 24h 내 50%, § 9.9)
6. STOP 게이트 5개 (풀 왕복): ① provider 계약 검증 ② signature 검증 ③ webhook idempotency ④ refund flow ⑤ E2E 테스트

### Phase 5 — 캘린더 발행 (Google Calendar / iCal) (중간)
**산출물**: `calendar_events` + 자동 발행 + .ics 다운로드
1. `calendar_events` DDL
2. Google Calendar API integration (선택, OAuth 게이트)
3. `.ics` 생성 (서드파티 0, 직접 작성)
4. confirmed 트리거 → calendar_event publish
5. STOP 게이트 2개: ① OAuth scope 검증 ② 이벤트 update / cancel 정합

### Phase 6 — 알림 + 리마인더 (저위험)
**산출물**: 24h / 1h 전 텔레그램 + 이메일 리마인더
1. `booking_send_reminder` job
2. 멤버 = 기존 텔레그램 / 외부 = 이메일
3. STOP 게이트 1개: 발송 빈도 검증 (중복 발송 0)

### 단계 게이트 요약
- Phase 1·2 완료 = MVP (무료 슬롯 멤버 예약)
- Phase 3 = 외부 채널 진입
- Phase 4·5 = 유료 코칭 / 강의 가능
- Phase 6 = 운영 안정화

---

## 9. 사용자 결정 영역 (open questions)

| # | 항목 | 옵션 |
|---|---|---|
| 9.1 | 외부 신청자 (비멤버) 허용 여부 | A. 허용 (Phase 3) / B. 멤버 한정 |
| 9.2 | 슬롯 타입 범위 | A. 1on1 + group + lecture / B. 1on1 만 (MVP) |
| 9.3 | 결제 도입 시점 | A. Phase 4 즉시 / B. 무료 운영 후 별도 시점 |
| 9.4 | 통합 수준 (§ 1.3) | A. 같은 DB·앱 / B. 같은 DB·라우터 분리 / C. 별 앱·별 DB |
| 9.5 | 슬롯 full 시 대기열 | A. 대기열 X (full 차단) / B. waitlist 테이블 |
| 9.6 | pending_payment TTL | A. 30분 / B. 1시간 / C. 24시간 |
| 9.7 | booking 자동 승인 vs 수동 승인 | A. 무료 자동 / 유료 결제 후 자동 / B. 모두 운영자 수동 검토 |
| 9.8 | 외부 신청 rate limit | A. IP 분당 5회 / B. IP 시간당 20회 / C. 0 |
| 9.9 | 환불 정책 | A. 24h 전 100% / 24h 내 50% / 시작 후 0% / B. 별 정책 |
| 9.10 | 캘린더 provider | A. Google Calendar OAuth / B. .ics 다운로드만 / C. 둘 다 |
| 9.11 | 멤버 인증 방식 (booking) | A. 멤버 코드 (`access_code`) 재사용 / B. 별 token 발급 |

---

## 10. 위험 / 회귀 영역

| 영역 | 위험 | 대비 |
|---|---|---|
| 동시성 | 같은 슬롯 동시 신청 → over-booking | `BEGIN IMMEDIATE` 트랜잭션 + `confirmed_count < capacity` 검증 후 INSERT |
| webhook 중복 | provider 재시도 → 중복 결제 처리 | `payments.provider_tx_id` UNIQUE + idempotent INSERT |
| PII 노출 | meeting_url public 노출 | confirmed booking 본인만 (cancel_token 또는 멤버 인증) |
| 캘린더 sync 실패 | Google API 일시 오류 | `calendar_events.status='queued'` 재시도 큐 + `last_error` |
| 슬롯 시간 변경 | 기존 booking 영향 | UPDATE 시 `slot_changed` 알림 발송 + booking 본인 재확인 옵션 |
| 데이터 정합 | members 외래 키 누락 | FK + `ON DELETE RESTRICT` (멤버 삭제 차단), 테스트로 검증 |

---

## 11. 의존성 / 추가 라이브러리 (제안)

| 라이브러리 | 용도 | 필수성 |
|---|---|---|
| 기존 (`fastapi` / `apscheduler` / `cryptography` / `httpx`) | 재사용 | 필수 0 (기존 영역) |
| `icalendar` (선택) | .ics 생성 | Phase 5 |
| `google-api-python-client` (선택) | Google Calendar | Phase 5 옵션 |
| `tosspayments-server-sdk` 또는 raw `httpx` | 결제 | Phase 4 |
| `slowapi` 또는 직접 IP counter | rate limit | Phase 3 |

---

## 12. 본 문서 채택 후 다음 액션

1. § 9 의 11개 결정 항목 사용자 응답 수집 → 본 문서 v0.2 보강
2. `docs/tasks/pending/T???_booking-phase1-slots.md` 발행 (Phase 1 task)
3. `db.py` 수정 PR (slots / booking_logs DDL only) — STOP 게이트 사용자 검수
4. 단위 테스트 추가 + 검수 통과 후 Phase 2 진입
5. 본 문서를 `~/ai-tools/reviews/self/architecture/2026-05-07_booking-system-design.md` 로 미러링 (judgments 영역, snapshot 시점 명시)

---

## 13. 한줄 결론

`member-system` 의 멤버 / 코드 / 알림 / 암호화 / APScheduler 인프라를 그대로 재사용하면 **Phase 1·2 만으로 무료 슬롯 멤버 예약 MVP** 가 1주 이내 가동 가능. 결제·캘린더는 별 phase 로 분리하여 위험 영역 격리. § 9 의 11개 결정 영역만 사용자 응답 도달 시 v0.2 로 즉시 진입 가능.
