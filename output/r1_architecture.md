# 아키텍트 — 1라운드 구조 검토

## 발견 문제

### 1. 동일 로직 중복 [심각]
- `db.py:calculate_grade()` 와 `main.py:_grade_count()` 가 완전히 동일한 등급 계산 로직
- `calculate_grade`는 `_can_code_provided` 같은 존재하지 않는 키를 참조하다가 결국 미실행됨
- 실제로 호출되는 건 `_grade_count`만. `calculate_grade`는 데드 코드

### 2. 패키지 구조 없음 [중간]
- 모든 파일이 `sys.path.insert(0, ...)` 로 경로를 직접 주입
- `agents/` 가 실제 Python 패키지가 아님 (`__init__.py` 있지만 상대 import 안 씀)
- 환경 따라 import 충돌 가능

### 3. 스케줄러 모듈이 main.py에 혼재 [중간]
- `job_cleanup`, `job_expiry_warning` 등 스케줄 함수가 main.py 안에 인라인
- 독립 `scheduler.py` 로 분리해야 단독 실행/테스트 가능

### 4. DB 연결 풀 없음 [중간]
- `get_conn()` 호출할 때마다 새 연결 생성, 매 요청마다 열고 닫음
- 동시 요청 증가 시 SQLite 파일 잠금 경합 발생 가능

### 5. 설정값 분산 [낮음]
- `MIN_AGE`가 `validator.py`와 `meta_validator.py` 양쪽에서 각각 `os.getenv` 로 읽음
- 중앙 config 모듈 없음

## 긍정 평가
- agent 단일 책임 원칙은 잘 지켜짐
- `Path.home()` 사용으로 하드코딩 없음
- AES + HMAC 이중 구조 (암호화/중복확인 분리)는 올바른 설계
