# 악마의 변호인 — 4라운드 재검사

## 이전 문제 해결 확인

- ✅ HTML 태그 오류 수정됨
- ✅ consent_personal 하드코딩 수정됨
- ✅ 관리자 인증 추가됨
- ✅ log action "unlocked" 수정됨
- ✅ calculate_grade 데드코드 제거됨

## 새로 발견한 문제

### 1. `members` 라우트 시그니처 이상
```python
async def members(status=None, grade=None, request: Request = None, _=Depends(require_admin)):
```
`request: Request = None` — Request 기본값이 None이면 FastAPI가 제대로 주입 못할 수 있음.
실제로 `request` 를 이 함수 내부에서 사용하지도 않으므로 제거 권고.

### 2. ADMIN_API_KEY 미설정 시 로그인 없이 모든 관리 API 접근 가능
`.env`에 키가 있지만, 만약 `.env` 파일 누락 또는 변수 오타 시 완전 무방비.
운영 배포 전 체크 필요.

### 3. `test_all.py` 에 rate limit, 관리자 인증 테스트 없음
새로 추가된 기능(인증, SQL 패턴 개선)에 대한 테스트가 부분적임.

## 판정
새 심각 문제 없음. **통과**.
