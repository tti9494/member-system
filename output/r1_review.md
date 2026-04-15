# 리뷰어 — 1라운드 코드 품질 검토

## 발견 문제

### 1. `decrypt_phone` 중복 import [낮음]
`main.py` 상단:
```python
from agents.encryptor import encrypt_data      # 20번째 줄
from agents.encryptor import decrypt_phone     # 28번째 줄
```
같은 모듈에서 두 번 import. 하나로 합쳐야 함.

### 2. `release_expired_locks` 의 log_action action 값 오류 [중간]
`db_manager.py`:
```python
log_action(mid, "locked", "잠금 자동 해제")
```
잠금 **해제** 처리인데 action이 `"locked"`. `"unlocked"` 이어야 함.
로그 분석 시 잠금/해제 구분 불가.

### 3. `get_expiring_soon` 내 `_now()` 이중 호출 [낮음]
```python
def get_expiring_soon(days: int = 7) -> list:
    now = _now()
    deadline = (datetime.fromisoformat(now) + timedelta(days=days)).isoformat() ...
    rows = conn.execute(
        "... WHERE code_expires_at > ? AND code_expires_at < ?",
        (_now(), deadline)   # ← _now() 재호출
    )
```
`now` 를 저장해뒀는데 쿼리에서 `_now()` 다시 호출. 미세한 시간 차이 발생.

### 4. `join-full.html` HTML 태그 오류 [중간]
```html
<h1>🤖 AI 모임 정식 신청</html>
```
`</h1>` 대신 `</html>` 로 잘못 닫힘. 브라우저가 자동 복구하더라도 명백한 오류.

### 5. `join-full.html` consent_personal 하드코딩 [중간]
```javascript
consent_personal: true,   // submitForm() 내부, 548번째 줄 근처
```
체크박스 실제 값 대신 무조건 `true`. 클라이언트 측 검증(`if (!checkbox.checked) return`)이 있어서
실제로 우회되진 않지만, JS 오류/조작으로 우회 가능.

### 6. `calculate_grade` 의 `_can_code_provided` 키 [심각]
`db.py:calculate_grade()`:
```python
if data.get(f"_{field}_provided"):
    count += 1
```
`_can_code_provided`, `_can_present_provided` 라는 키를 보는데
이 키를 세팅하는 코드가 어디에도 없음. can_code/can_present는 항상 카운트 0.
(어차피 `_grade_count`만 실제 호출되므로 실서비스엔 영향 없지만 코드 혼란)

### 7. `security_checker.py` 정상 데이터 차단 위험 [중간]
```python
SQL_PATTERNS = re.compile(r"(--|;|'|\"|...|SELECT|INSERT|...)")
```
`reason` 필드에 "SELECT 버튼을 눌렀더니..." 같은 정상 문장도 차단됨.
대소문자 구분 없이 단어 경계 없이 매칭 — false positive 높음.
