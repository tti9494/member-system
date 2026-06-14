# 관리자 페이지 접속 / 비밀번호 변경

## 접속

- 온라인 관리자: `https://apply.arsen-ai.com/frontend/admin.html`
- 로컬 관리자: `http://127.0.0.1:8100/frontend/admin.html`
- 신청/예약 확인 페이지 하단의 작은 `운영자` 링크로도 진입할 수 있습니다.

## 인증 방식

- 관리자 화면은 공개 URL로 열릴 수 있지만, 운영 데이터 조회/수정은 관리자 비밀번호가 있어야 동작합니다.
- 외부 도메인에서는 `/stats`, `/members`, `/admin/*`, `/scheduler/*` 같은 운영자 API가 비밀번호 없이 열리지 않아야 합니다.
- 실제 값은 `/Users/yoon/member-system/.env`의 `ADMIN_API_KEY`에 저장됩니다.
- 화면, 문서, 로그, 채팅에는 관리자 비밀번호 값을 출력하지 않습니다.

## 비밀번호 변경

권장 방식은 관리자 페이지의 `시스템/백업` 탭에서 `관리자 보안 관리` 패널을 여는 것입니다.

1. `https://apply.arsen-ai.com/frontend/admin.html` 접속
2. 현재 관리자 비밀번호로 연결
3. `시스템/백업` 탭 이동
4. `새 관리자 비밀번호`와 `새 비밀번호 확인` 입력
5. `비밀번호 변경` 클릭

이 방식은 현재 관리자 비밀번호로 인증된 세션에서만 동작하며, 변경 즉시 실행 중 서버의 관리자 키와 `.env` 값을 함께 갱신합니다. 실제 비밀번호 값은 화면, 문서, 로그에 출력하지 않습니다.

터미널 fallback이 필요하면 Mac에서 아래 명령을 실행해 새 비밀번호를 입력합니다.

```bash
cd /Users/yoon/member-system
python3 scripts/set_admin_password.py
launchctl kickstart -k gui/$(id -u)/com.arsen.member-system
```

터미널 방식으로 변경한 경우에는 member-system 서비스를 재시작해야 합니다. 브라우저의 기존 저장 비밀번호는 관리자 화면의 `비밀번호 지우기`로 삭제한 뒤 새 비밀번호로 연결합니다.

## 비밀번호 관리 도구 백업

관리자 페이지 `시스템/백업` 탭의 `비밀번호 도구 백업` 버튼은 다음 파일을 로컬/iCloud/OneDrive 도구 백업 위치로 복사합니다.

- `scripts/set_admin_password.py`
- `docs/admin_access_runbook_ko.md`

이 백업은 프로그램과 운영 문서만 복사하며, `.env`나 관리자 비밀번호 값은 복사하지 않습니다.
