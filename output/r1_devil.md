# 악마의 변호인 — 1라운드 최악의 시나리오 검토

## 1. `consent_personal: true` 하드코딩 → 동의 없이 신청 가능

`join-full.html submitForm()`:
```javascript
consent_personal: true,  // ← 체크박스 무시하고 하드코딩
```
클라이언트 측에 `if (!checkbox.checked) return` 가드가 있지만
Burp Suite / curl로 `{"consent_personal": false}` 직접 POST하면
서버 `consent_checker.py` 는 `data.get("consent_personal")` 가 `False` 이므로 거부됨.
그러나 `{"consent_personal": true}`로 조작 전송 시 JS 가드 완전 우회.
**개인정보 동의 없이 데이터 수집 가능 → 법적 위험.**

## 2. `GET /members` 인증 없음 → 전체 신청자 개인정보 조회

```bash
curl http://localhost:8100/members
```
`phone_masked`, `name`, `job`, `age`, `gender`, `reason` 전부 반환됨.
phone_encrypted, access_code 는 제거되지만 나머지 개인정보는 평문 노출.

## 3. `POST /blacklist/{any_valid_uuid}` → 합법 신청자 영구 차단

인증 없이 임의 member_id로 블랙리스트 등록 가능.
한 번 blacklist가 되면 같은 phone_hash로 재신청 불가 → 서비스 거부 공격.

## 4. 스케줄러 수동 실행 무제한

```bash
curl -X POST http://localhost:8100/scheduler/run -d '{"job_id":"weekly_report"}'
```
텔레그램에 리포트 무한 발송 가능. Bot API rate limit 걸리면 실제 알림 차단됨.

## 5. `reason` 필드에 "SELECT" 한 글자로 신청 차단

`security_checker.py` 가 `SELECT` 를 SQL injection으로 감지.
정상적인 내용 ("AI SELECT 기능을 배우고 싶어요")도 차단.
사용자는 왜 거부됐는지 모름. 에러 메시지도 "보안 위협"으로 나와서 혼란.

## 6. `code_fail_count` 리셋이 성공 시만 됨

`verify_code` 에서 성공하면 `code_fail_count=0` 리셋.
그런데 **코드 재발급(`/regen-code`)** 시에는 `revoke_code → generate_code` 순서인데
`generate_code` 에서 `code_fail_count=0` 리셋함. 양호.
그러나 잠금(`code_locked_until`) 상태에서 재발급 해도 잠금이 풀리지 않음:
`generate_code` 에서 `code_fail_count=0` 은 하지만 `code_locked_until=NULL` 은 하지 않음.

**재현**: 5회 실패 → 잠금 → `/regen-code` 호출 → 새 코드 발급됨 → 잠금은 그대로
→ 새 코드로 verify 시도 시 즉시 "잠겨있음" 반환.

## 7. `join-full.html` 에 `</html>` 잘못된 태그

```html
<h1>🤖 AI 모임 정식 신청</html>
```
h1 닫기 태그 누락. 브라우저 자동 복구되지만 이후 DOM 파싱이 예상과 다를 수 있음.
특히 `<title>` 내 텍스트가 잘못 파싱될 가능성.
