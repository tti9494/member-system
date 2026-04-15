# 보안검사관 — 1라운드 보안 검토

## [높음] 관리자 엔드포인트 무인증

**파일**: `main.py`
**대상 엔드포인트**:
- `POST /approve/{member_id}`
- `POST /reject/{member_id}`
- `POST /blacklist/{member_id}`
- `POST /regen-code/{member_id}`
- `GET /members`
- `GET /members/{id}`
- `POST /scheduler/run`

**문제**: HTTP 요청 누구든 가능. member_id(UUID)를 모르면 무작위 공격은 어렵지만
`GET /members` 로 전체 목록 + member_id 조회 → 이후 승인/블랙리스트 임의 조작 가능.

**재현 조건**:
```bash
# 전체 member_id 조회
curl http://localhost:8100/members
# 임의 승인
curl -X POST http://localhost:8100/approve/UUID_HERE
```

**수정 방향**: API Key 헤더 검증 (최소), 또는 FastAPI Depends로 admin 토큰 확인

---

## [높음] Rate Limiting 없음

**파일**: `main.py`
**엔드포인트**: `POST /apply`

**문제**: 동일 IP에서 무제한 반복 호출 가능.
security_checker가 XSS/SQLi는 막지만 신청 스팸은 미차단.
중복 체크는 phone_hash 기준이므로 전화번호만 바꾸면 DB 무한 적재.

**수정 방향**: `slowapi` 또는 미들웨어로 IP당 분당 호출 제한

---

## [중간] CORS 전체 허용

**파일**: `main.py:36`
```python
allow_origins=["*"]
```
내부 서비스임에도 모든 도메인에서 API 직접 호출 가능.
개인정보 엔드포인트(`/members`)에 CORS 무제한은 위험.

**수정 방향**: `allow_origins=["http://localhost:8100"]` 또는 명시적 도메인

---

## [중간] .env 파일 암호화 키 평문 저장

**파일**: `.env`
```
CODE_SECRET_KEY=7c3b95f2fb23d97859a5ce030d5b48f0
PHONE_SECRET_KEY=0ae95db3f8a4e8610fd07a5a115d8fa9
```
iCloud에 업로드 시 키 노출. `.gitignore`/`.cloudignore` 미설정 시 동기화됨.

**수정 방향**: `.env`를 iCloud 동기화 제외 경로에 두거나, `.gitignore`에 명시

---

## [중간] `security_checker` SQL 패턴 — 단어 경계 없음

**파일**: `agents/security_checker.py:8-14`
```python
SQL_PATTERNS = re.compile(r"(SELECT|INSERT|...)", re.IGNORECASE)
```
`reason` 필드에 "나는 SELECT 하고 싶다" 같은 정상 문장 차단.
반대로 `sElEcT/**/1` 같은 우회 패턴은 통과 가능.
실제 SQLi 방어는 parameterized query가 담당 — 이 필터는 보조 수단임을 명확히 해야 함.

---

## [낮음] 코드 검증 시 timing attack 가능

**파일**: `agents/code_generator.py:122`
```python
if secrets.compare_digest(input_code.upper(), stored):
```
`secrets.compare_digest` 사용으로 timing attack 방어는 됨. 양호.

---

## [낮음] member_id 노출

`/members` 에서 모든 member_id가 평문 노출됨.
UUID라서 예측은 어렵지만 목록 조회 → 개별 조작 경로가 열림.
인증 추가 시 해결됨.
