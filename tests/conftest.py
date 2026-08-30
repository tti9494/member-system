"""이 작업 트리의 코드를 테스트가 확실히 import하도록 고정한다.

main.py와 agents/* 모듈은 런타임 배포 경로(~/member-system)를 sys.path 맨 앞에
삽입한다. worktree에서 pytest를 돌리면 그 삽입이 우선되어 agents 패키지가
본 저장소(다른 브랜치일 수 있음)에서 로드되는 문제가 있었다. 여기서 worktree의
db/agents 패키지를 먼저 sys.modules에 올려 이 작업 트리 코드가 검증되게 한다.
런타임 코드는 변경하지 않는다.
"""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) in sys.path:
    sys.path.remove(str(ROOT))
sys.path.insert(0, str(ROOT))

# 운영 코드의 예측 가능한 dev fallback secret은 전부 제거(fail-closed)되었다.
# 테스트 환경에만 명시적 더미 secret을 설정한다 — 운영 fallback이 아니다.
os.environ.setdefault("CODE_SECRET_KEY", "pytest-dummy-code-secret-key-32ch!!")
os.environ.setdefault("LICENSE_SECRET_KEY", "pytest-dummy-license-secret-32ch!!")
os.environ.setdefault("KAKAO_SESSION_SECRET", "pytest-dummy-kakao-session-secret!")
os.environ.setdefault("PHONE_SECRET_KEY", "pytest-dummy-phone-secret-key-32c!!")
os.environ.setdefault("EMAIL_SECRET_KEY", "pytest-dummy-email-secret-key-32c!!")

import db  # noqa: E402,F401  — worktree db 모듈 고정
import agents  # noqa: E402,F401  — worktree agents 패키지 고정 (하위 모듈 포함)
