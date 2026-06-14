#!/usr/bin/env python3
"""Set the member-system admin password without printing it.

The password is stored as ADMIN_API_KEY in ~/member-system/.env because the
running API still authenticates admin requests through the X-Admin-Key header.
"""

from __future__ import annotations

import getpass
from pathlib import Path


ENV_PATH = Path.home() / "member-system" / ".env"
KEY_NAME = "ADMIN_API_KEY"
MIN_LENGTH = 8


def update_env_value(path: Path, key: str, value: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
    updated = False
    output: list[str] = []

    for line in lines:
        if line.startswith(f"{key}="):
            output.append(f"{key}={value}")
            updated = True
        else:
            output.append(line)

    if not updated:
        if output and output[-1].strip():
            output.append("")
        output.append(f"{key}={value}")

    path.write_text("\n".join(output) + "\n", encoding="utf-8")
    path.chmod(0o600)


def main() -> int:
    print("member-system 관리자 비밀번호를 새 값으로 고정합니다.")
    password = getpass.getpass("새 관리자 비밀번호: ").strip()
    confirm = getpass.getpass("새 관리자 비밀번호 확인: ").strip()

    if password != confirm:
        print("오류: 입력한 비밀번호가 서로 다릅니다.")
        return 1
    if len(password) < MIN_LENGTH:
        print(f"오류: 관리자 비밀번호는 최소 {MIN_LENGTH}자 이상이어야 합니다.")
        return 1

    update_env_value(ENV_PATH, KEY_NAME, password)
    print("완료: 관리자 비밀번호를 .env에 저장했습니다.")
    print("반영하려면 member-system 서비스를 재시작하세요.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
