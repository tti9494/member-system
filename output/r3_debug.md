# 디버거 — 3라운드 수정 내역

## 수정 1: 중복 import 제거
- **파일**: `main.py`
- **전**: `from agents.encryptor import encrypt_data` (23번째) + `from agents.encryptor import decrypt_phone` (28번째) 두 줄
- **후**: `from agents.encryptor import encrypt_data, decrypt_phone` 한 줄

## 수정 2: release_expired_locks log action 오타
- **파일**: `agents/db_manager.py`
- **전**: `log_action(mid, "locked", "잠금 자동 해제")`
- **후**: `log_action(mid, "unlocked", "잠금 자동 해제")`

## 수정 3: get_expiring_soon 이중 _now() 호출
- **파일**: `agents/db_manager.py`
- **전**: `(_now(), deadline)` — now 변수 저장해놓고 재호출
- **후**: `(now, deadline)` — 저장된 now 사용

## 수정 4: join-full.html h1 태그 오류
- **파일**: `frontend/join-full.html`
- **전**: `<h1>🤖 AI 모임 정식 신청</html>`
- **후**: `<h1>🤖 AI 모임 정식 신청</h1>`

## 수정 5: consent_personal 하드코딩 → 실제 체크박스 값으로
- **파일**: `frontend/join-full.html`
- **전**: `consent_personal: true,`
- **후**: `consent_personal: document.getElementById('consent_personal').checked,`

## 수정 6: calculate_grade 데드코드 제거
- **파일**: `db.py`
- 미사용 `calculate_grade` 함수 전체 제거 (40줄)
- 관련 import `from db import init_db, calculate_grade` → `from db import init_db`

## 수정 7: security_checker SQL 패턴 — 단어 경계 추가
- **파일**: `agents/security_checker.py`
- **전**: `SELECT`, `DELETE` 등 단어 그대로 매칭 → 정상 문장도 차단
- **후**: `\bSELECT\b.{0,30}\bFROM\b` 등 실제 SQL 구문 패턴으로 수정

## 수정 8: 관리자 엔드포인트 인증 추가
- **파일**: `main.py`
- `require_admin` 함수 추가 (`X-Admin-Key` 헤더 검증)
- ADMIN_API_KEY 환경변수 추가 (`.env`)
- 적용 엔드포인트: `/approve`, `/reject`, `/regen-code`, `/blacklist`, `/members`, `/members/{id}`, `/scheduler/status`, `/scheduler/run`

## 수정 9: CORS 제한
- **파일**: `main.py`
- **전**: `allow_origins=["*"]`
- **후**: `allow_origins=["http://localhost:8100", "http://127.0.0.1:8100"]`

## 수정 못한 것
- **Rate limiting**: `slowapi` 별도 패키지 필요. 현재 설치 안 됨. 권고사항으로 남김.
