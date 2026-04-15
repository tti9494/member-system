# 테스터 — 3라운드 테스트 결과

| 항목 | 결과 | 비고 |
|------|------|------|
| 27개 단위 테스트 | ✅ 통과 | 27/27 |
| 인증 없이 /members | ✅ 통과 | 401 반환 |
| 인증 있이 /members | ✅ 통과 | 200 반환 |
| /apply 인증 불필요 | ✅ 통과 | 200 반환 |
| h1 태그 수정 | ✅ 통과 | `</h1>` 정상 닫힘 |
| consent_personal 실제값 | ✅ 통과 | checkbox.checked 사용 |
| log action "unlocked" | ✅ 통과 | 코드 확인 |
| get_expiring_soon now 단일 | ✅ 통과 | 코드 확인 |
| calculate_grade 제거 | ✅ 통과 | import 오류 없음 |
| SQL 패턴 정상문장 통과 | ✅ 통과 | "SELECT 버튼" → 차단 안 됨 |
| SQL injection 패턴 차단 | ✅ 통과 | `SELECT * FROM` → 차단 |
| 서버 기동 | ✅ 통과 | uvicorn 정상 시작 |

**전체 통과. 4라운드로 진행.**
