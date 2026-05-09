# 멤버/예약 시스템 저장소와 백업 전략

작성일: 2026-05-09

## 현재 상태

- 원본 DB: `/Users/yoon/member-system/members.db`
- 운영 화면: `http://127.0.0.1:8100/frontend/admin.html`
- 관리자 키: `/Users/yoon/member-system/.env`의 `ADMIN_API_KEY`
- 관리자 키 값은 화면, 문서, 로그에 출력하지 않는다.

현재 시스템은 맥에어 로컬 SQLite를 원본으로 사용한다. 신청서가 접수되면 DB 저장, Google Sheets 전송 시도, Hermes/Telegram 알림 시도, DB 백업을 순서대로 실행한다.

## 백업 위치

신청 DB는 개인정보가 포함된 민감 운영 데이터다. 백업 파일도 공개 공유 폴더에 두지 않는다.

현재 자동 백업 대상:

| 대상 | 위치 | 용도 |
| --- | --- | --- |
| Mac Air local | `/Users/yoon/member-system/backups` | 즉시 복구용 로컬 백업 |
| iCloud Drive | `/Users/yoon/Library/Mobile Documents/com~apple~CloudDocs/Arsen/member-system/backups` | 노트북 변경/분실 대비 개인 클라우드 백업 |
| OneDrive | `/Users/yoon/OneDrive/Arsen/member-system/backups` | iCloud 외 보조 클라우드 백업 |
| Mac Pro | `/Users/sanguk/member-system/backups` | 24시간 장비 보조 백업 |

관리자 화면의 `저장 / Hermes 알림 확인` 패널에서 DB 원본 위치, 최근 백업, 신청별 DB/백업/Sheets/Hermes 상태를 확인한다.

## 권장 운영 단계

### 오늘 운영

맥에어 로컬 SQLite를 원본으로 유지하고, 신청 때마다 iCloud/OneDrive/Mac Pro에 백업한다. 오늘처럼 신청 접수와 인원 확인이 우선인 경우 가장 빠르고 안전하다.

### 단기 안정화

Google Sheets는 운영자가 보기 쉬운 미러로 사용한다. 단, Sheets를 개인정보 원본 저장소로 삼지는 않는다. GAS URL 설정 여부는 관리자 화면에서 확인한다.

### 장기 운영

VPS 또는 클라우드 서버를 원본 저장소로 승격한다. 이 단계에서는 맥에어/맥프로가 작업자 역할을 하고, 서버 DB가 단일 원본이 된다. 외부 공개 신청서, 관리자 인증, 백업 정책, 접근 로그를 함께 정리해야 한다.

## 복구 기준

1. 서버 장애: 최신 `members-YYYYMMDD-HHMMSS.db` 백업을 선택한다.
2. 맥에어 교체: iCloud 또는 OneDrive의 `Arsen/member-system/backups`에서 최신 DB를 복사한다.
3. 맥에어 접근 불가: Mac Pro의 `/Users/sanguk/member-system/backups`에서 최신 DB를 가져온다.
4. 복구 전에는 기존 DB를 덮어쓰지 말고 별도 파일명으로 보관한다.

## 보안 원칙

- `.env`, 관리자 키, Telegram 토큰, GAS URL 값은 문서/화면/채팅에 출력하지 않는다.
- DB와 백업 파일은 공개 링크로 공유하지 않는다.
- Google Sheets 또는 Drive 공유는 최소 권한으로 제한한다.
- 실제 결제/입금 자동화는 별도 승인 후 연결한다.
