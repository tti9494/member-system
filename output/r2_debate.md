# 2라운드 — 반박 및 합의

## architect vs reviewer

**reviewer 지적**: `calculate_grade` 데드코드  
**architect 동의**: 맞음. `main.py`의 `_grade_count`만 실제 사용. `calculate_grade` 제거 권장.

**architect 지적**: DB 연결 풀 없음  
**reviewer 보완**: SQLite는 단일 파일 DB라 연결 풀 효과가 제한적. 그러나 WAL 모드 활성화로 동시성 개선 가능.

## reviewer vs security

**security 지적**: `consent_personal: true` 하드코딩은 서버에서 `consent_checker`가 막음  
**devil 반박**: 서버가 막는 건 맞지만 **JS 측이 `true` 하드코딩이면 동의 안 한 사람도 폼 제출이 됨**. 클라이언트 가드만 믿으면 위험. 수정 필요.

## security vs devil

**security 지적**: Rate limiting 없음 → 최우선 수정 필요  
**devil 동의**: `/apply`에 IP당 분당 5회 제한 최소 필요.

**devil 추가 발견**: `regen-code` 후 잠금 유지 버그  
**security 동의**: `generate_code` 에서 `code_locked_until=NULL` 추가 필요. 명백한 버그.

## 최종 합의 — 우선순위

| 우선순위 | 문제 | 담당 |
|---------|------|------|
| 1 | 관리자 엔드포인트 무인증 | debugger |
| 2 | regen-code 후 잠금 유지 버그 | debugger |
| 3 | consent_personal 하드코딩 | debugger |
| 4 | release_expired_locks log action 오타 | debugger |
| 5 | HTML h1 태그 오류 | debugger |
| 6 | decrypt_phone 중복 import | debugger |
| 7 | calculate_grade 데드코드 제거 | debugger |
| 8 | security_checker 단어 경계 추가 | debugger |
| 9 | CORS 제한 | debugger |
| 10 | Rate limiting (별도 패키지 필요) | 권고사항으로 기록 |
