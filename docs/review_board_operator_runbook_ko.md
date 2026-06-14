# ARSEN 후기보드 운영 문서

작성일: 2026-06-10 KST
대상 프로젝트: `/Users/yoon/member-system`

## 목적

ARSEN 후기보드는 수업 후기, 수업 결과물, 강사별 기록을 별도 페이지로 관리하기 위한 기능입니다.
기존 회원 신청, 예약, 텔레그램 신청 알림, Kakao/Blog Studio/Work Bus 업무와 분리되어 동작합니다.

## 주요 화면

- 공개 페이지: `/frontend/class-stories.html`
- 공개 데모 모드: `/frontend/class-stories.html?demo=1`
- 수강생 후기 작성 페이지: `/frontend/review-submit.html?token={작성링크토큰}`
- 관리자 페이지: `/frontend/admin.html`의 `후기보드` 탭

## 데이터 정책

공개 페이지에 노출되는 후기는 아래 조건을 모두 만족해야 합니다.

- 후기 상태: `public`
- 개인정보 확인: `privacy_checked = true`
- 강사 상태: `active` 또는 강사 미지정

초안, 비공개, 개인정보 미확인 후기는 관리자 페이지에서만 보이며 공개 페이지에는 나오지 않습니다.

## 관리자 기능

관리자 `후기보드` 탭에서 가능한 작업:

- 후기 작성 링크 발급
- 후기 작성 링크 폐기
- 강사 추가
- 강사 수정
- 강사 삭제
- 후기 추가
- 후기 수정
- 후기 공개/초안 전환
- 개인정보 검수 완료/해제
- 추천 후기 지정/해제
- 후기 삭제

후기를 공개로 전환하면 공개 실수를 줄이기 위해 `privacy_checked`도 함께 켜집니다.

## API

공개 API:

- `GET /api/review-board`
- `GET /api/review-board/submit/{token}`
- `POST /api/review-board/submit/{token}`

관리자 API:

- `GET /admin/review-board`
- `GET /admin/review-board/invites`
- `POST /admin/review-board/invites`
- `POST /admin/review-board/invites/{invite_id}/revoke`
- `POST /admin/review-board/instructors`
- `PUT /admin/review-board/instructors/{instructor_id}`
- `DELETE /admin/review-board/instructors/{instructor_id}`
- `POST /admin/review-board/entries`
- `PUT /admin/review-board/entries/{entry_id}`
- `DELETE /admin/review-board/entries/{entry_id}`

관리자 API는 관리자 인증 또는 로컬 관리자 미리보기 조건에서만 동작합니다.

## DB 테이블

SQLite와 Cloudflare D1 모두 동일한 테이블을 사용합니다.

- `review_instructors`
- `review_entries`
- `review_invites`

배포 전에는 Cloudflare D1에 `cloudflare/schema.sql`이 적용되어야 합니다.
기존 D1이 오래된 스키마라면 `members.available_time_slots` 컬럼 보정도 필요합니다.
`cloudflare/scripts/deploy-cloudflare.mjs`는 `schema.sql` 적용과 `available_time_slots` 보정을 수행합니다.

## 운영 순서

1. 관리자 페이지 접속
2. `후기보드` 탭 열기
3. 필요하면 강사 추가
4. `작성 링크 만들기` 클릭
5. 수업명, 수업일, 강사, 최대 제출 수 입력
6. 생성된 링크를 모임원에게 전달
7. 모임원이 후기 작성 페이지에서 제출
8. 제출된 후기는 `draft` 상태로 관리자 후기보드에 저장됨
9. 개인정보와 문구 확인
10. 공개 상태로 전환하면 `privacy_checked`가 함께 켜지고 공개 페이지에 노출됨
11. 공개 페이지에서 노출 확인

## 사진/텔레그램/카톡 확장 위치

현재 구현은 사진 URL 목록 입력 방식입니다.
후기 작성 링크에서 사진 URL을 받을 수 있지만, 파일 업로드 자체는 아직 연동하지 않았습니다.
나중에 텔레그램으로 사진과 문구를 보내면 자동 등록하는 흐름을 붙일 경우, 아래 구조가 적합합니다.

- 텔레그램 수신: 별도 intake 루틴
- 임시 저장: `review_entries.status = draft`
- 사진 URL: `review_entries.image_urls`
- 개인정보 검수: 관리자 수동 확인
- 공개: 관리자 승인 후 `status = public`

## 링크 보안 정책

- 작성 링크 토큰 원문은 DB에 저장하지 않습니다.
- DB에는 `review_invites.token_hash`만 저장합니다.
- 생성된 링크는 생성 직후 화면에 한 번 표시되며 자동 복사를 시도합니다.
- 기존 링크를 잃어버리면 새 링크를 발급하는 방식으로 운영합니다.
- 링크를 더 이상 쓰지 않을 경우 관리자 화면에서 폐기합니다.

카톡 자동 안내는 현재 미연동입니다.
추후 카톡 자동화 프로그램과 연결할 때는 후기 공개와 별개로 수업 신청/예약 안내 루틴에 붙이는 편이 안전합니다.

## 로컬 검증 명령

```bash
cd /Users/yoon/member-system
/Users/yoon/member-system/venv/bin/python -m pytest -q
cd /Users/yoon/member-system/cloudflare
npm run check
```

## 배포 주의사항

- 사용자 승인 전 `git push` 금지
- 사용자 승인 전 Cloudflare/DNS/WordPress 변경 금지
- D1 스키마 적용 없이 Worker만 배포 금지
- `.env`, 토큰, 비밀번호, 원문 개인정보 출력 금지
- 로컬 테스트용 후기/강사 데이터는 검증 후 삭제
