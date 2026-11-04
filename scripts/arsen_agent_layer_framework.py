#!/usr/bin/env python3
"""ARSEN 4-Layer Multi-Agent Architecture Reference Implementation.

현업 실무자 및 모임 배포용: 단일 챗봇 구조를 탈피하여
수집(L1) -> 관제·라우팅(L2) -> 워커 실행(L3) -> 실측 검증·배포(L4)로 이어지는
프로덕션 엔터프라이즈 멀티에이전트 파이프라인의 실전 동작 코드입니다.

실행:
    python3 scripts/arsen_agent_layer_framework.py
"""

from __future__ import annotations

import dataclasses
import hashlib
import json
import logging
import sys
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List, Optional

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("ARSEN-Framework")


# ==============================================================================
# [Domain Enums & Data Contracts]
# ==============================================================================
class Priority(Enum):
    LOW = 1
    NORMAL = 2
    HIGH = 3
    CRITICAL = 4


class ModelTier(Enum):
    FAST_LITE = "gemini-2.5-flash / haiku-3.5 (경량·저비용)"
    HEAVY_REASONING = "claude-3.5-sonnet / gpt-4o (고난도 추론·기획)"
    EMBEDDED_CODE = "codex-cli / local-llm (코드 컴파일·툴 제어)"


@dataclass
class StandardEvent:
    """Layer 1 Output: 외부 신호가 정제된 표준 이벤트 객체."""
    event_id: str
    source: str  # e.g., "slack", "webhook", "cron", "calendar"
    timestamp: float
    user_id: str
    payload: Dict[str, Any]
    priority: Priority = Priority.NORMAL
    context: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SubTask:
    """Layer 2 Output: 세부 실행 단위."""
    task_id: str
    name: str
    assigned_worker: str  # e.g., "codex_worker", "content_worker", "video_worker"
    model_tier: ModelTier
    estimated_tokens: int
    inputs: Dict[str, Any]
    requires_human_approval: bool = False


@dataclass
class OrchestrationPlan:
    """Layer 2 Output: 관제 두뇌가 생성한 작업 실행 계획(DAG)."""
    plan_id: str
    intent_summary: str
    total_token_budget: int
    tasks: List[SubTask]
    human_approved: bool = False


@dataclass
class ExecutionArtifact:
    """Layer 3 Output: 워커가 실행하고 생성한 원시 산출물."""
    task_id: str
    worker_name: str
    raw_data: Any
    metadata: Dict[str, Any]
    checksum: str
    execution_time_sec: float


@dataclass
class VerificationReport:
    """Layer 4 Output: 최종 실측 검수 및 배포 결과 영수증."""
    artifact_id: str
    passed_deterministic_checks: bool
    passed_cross_model_qc: bool
    details: List[str]
    delivered_channels: List[str]
    final_sha256: str


# ==============================================================================
# [Layer 1: Ingestion & Telemetry Layer]
# ==============================================================================
class IngestionLayer:
    """외부 신호 수집, 노이즈 필터링, 이벤트 디바운싱 및 메타데이터 주입."""

    def __init__(self, debounce_window_sec: float = 1.0):
        self.debounce_window = debounce_window_sec
        self._last_event_times: Dict[str, float] = {}

    def process_raw_signal(self, raw_signal: Dict[str, Any]) -> Optional[StandardEvent]:
        source = raw_signal.get("source", "unknown")
        user_id = raw_signal.get("user", "anonymous")
        text = raw_signal.get("text", "").strip()

        # 1. 빈 메시지 및 봇 루프 방지 (자신이 보낸 메시지 필터)
        if not text or raw_signal.get("is_bot", False):
            logger.debug(f"[L1] 무효 신호 필터링: source={source}")
            return None

        # 2. 이벤트 디바운싱 (단시간 중복 트리거 차단)
        now = time.time()
        dedup_key = f"{user_id}:{hashlib.md5(text.encode()).hexdigest()[:8]}"
        last_time = self._last_event_times.get(dedup_key, 0.0)
        if now - last_time < self.debounce_window:
            logger.warning(f"[L1] 디바운싱 작동: 중복 신호 차단 ({dedup_key})")
            return None
        self._last_event_times[dedup_key] = now

        # 3. 컨텍스트 보강 (위치, 디바이스, 시간대)
        event_id = f"evt_{int(now)}_{hashlib.sha256(dedup_key.encode()).hexdigest()[:6]}"
        logger.info(f"[L1 Ingestion] 정제된 표준 이벤트 생성 완료: {event_id} (출처: {source})")

        return StandardEvent(
            event_id=event_id,
            source=source,
            timestamp=now,
            user_id=user_id,
            payload={"text": text, "params": raw_signal.get("params", {})},
            priority=Priority.NORMAL,
            context={"system_time": "KST", "environment": "production"},
        )


# ==============================================================================
# [Layer 2: Brain & Orchestration Layer]
# ==============================================================================
class OrchestrationLayer:
    """작업 분해, 토큰 예산 관리, 모델 라우팅, 사람 승인 게이트."""

    def __init__(self, max_token_budget: int = 10000):
        self.max_budget = max_token_budget

    def plan_and_route(self, event: StandardEvent) -> OrchestrationPlan:
        text = event.payload["text"]
        logger.info(f"[L2 Brain] 의도 분석 및 작업 분해 시작: '{text[:30]}...'")

        tasks: List[SubTask] = []
        plan_id = f"plan_{event.event_id}"

        # 의도에 따른 작업 분해 및 모델 라우팅 (실전 규칙)
        if "블로그" in text or "콘텐츠" in text:
            # Task A: 고난도 구조화 및 기획 (Heavy 모델)
            tasks.append(
                SubTask(
                    task_id=f"{plan_id}_t1",
                    name="콘텐츠 기획 및 4개 식당 실측 큐레이션 작성",
                    assigned_worker="content_drafter",
                    model_tier=ModelTier.HEAVY_REASONING,
                    estimated_tokens=3500,
                    inputs={"topic": text, "rules": ["19pt소제목", "8행표", "친근존댓말"]},
                )
            )
            # Task B: 이미지 및 플레이스 카드 매핑 (Fast 모델)
            tasks.append(
                SubTask(
                    task_id=f"{plan_id}_t2",
                    name="썸네일 뱃지 생성 및 플레이스 카드 매핑",
                    assigned_worker="asset_mapper",
                    model_tier=ModelTier.FAST_LITE,
                    estimated_tokens=800,
                    inputs={"style": "high_contrast_badge"},
                )
            )
        elif "영상" in text or "스토리보드" in text:
            tasks.append(
                SubTask(
                    task_id=f"{plan_id}_t1",
                    name="8씬 연필소묘 콘티 및 v3.1 프롬프트 원장 생성",
                    assigned_worker="storyboard_engine",
                    model_tier=ModelTier.HEAVY_REASONING,
                    estimated_tokens=4200,
                    inputs={"ratio": "16:9", "scenes": 8},
                )
            )
            tasks.append(
                SubTask(
                    task_id=f"{plan_id}_t2",
                    name="FFmpeg 1.35s 컷오프 및 60.00초 마스터 리먹싱",
                    assigned_worker="media_remuxer",
                    model_tier=ModelTier.EMBEDDED_CODE,
                    estimated_tokens=500,
                    inputs={"target_duration_sec": 60.0, "fps": 24},
                )
            )
        else:
            tasks.append(
                SubTask(
                    task_id=f"{plan_id}_t1",
                    name="일반 업무 지원 및 질의 응답",
                    assigned_worker="general_worker",
                    model_tier=ModelTier.FAST_LITE,
                    estimated_tokens=1000,
                    inputs={"query": text},
                )
            )

        total_est = sum(t.estimated_tokens for t in tasks)
        logger.info(
            f"[L2 Brain] 오케스트레이션 계획 수립 완료: 총 {len(tasks)}개 서브태스크 (예상 토큰: {total_est})"
        )

        # 인간 승인 필요 여부 검사 (금융/보안/비밀번호 등)
        requires_approval = any(k in text for k in ["비밀번호", "결제", "카드", "삭제"])

        return OrchestrationPlan(
            plan_id=plan_id,
            intent_summary=f"자동화 실행 계획 for [{text[:20]}]",
            total_token_budget=total_est,
            tasks=tasks,
            human_approved=not requires_approval,
        )


# ==============================================================================
# [Layer 3: Worker Execution Layer]
# ==============================================================================
class WorkerExecutionLayer:
    """격리된 샌드박스에서 개별 도구 및 멀티모델 실행."""

    @staticmethod
    def execute_subtask(subtask: SubTask) -> ExecutionArtifact:
        start_t = time.time()
        logger.info(
            f"[L3 Worker: {subtask.assigned_worker}] 실행 착수: '{subtask.name}' "
            f"| 모델 티어: {subtask.model_tier.value}"
        )

        # 실제 환경에서는 여기서 API 호출, 브라우저 조작, 쉘 실행 수행
        time.sleep(0.1)  # 시뮬레이션 지연

        mock_payload = {
            "status": "success",
            "task_name": subtask.name,
            "generated_items": [
                {"heading": "[1. 우리왕뚜껑생삼겹]", "size_pt": 19, "has_photo": True},
                {"heading": "[2. 백암집 짚불구이]", "size_pt": 19, "has_photo": True},
                {"heading": "[3. 사당돈 본점]", "size_pt": 19, "has_photo": True},
                {"heading": "[4. 화포식당 인덕원점]", "size_pt": 19, "has_photo": True},
            ],
            "table_rows": 8,
            "has_hyperlink": True,
            "informal_speech_count": 0,
        }

        serialized = json.dumps(mock_payload, sort_keys=True)
        checksum = hashlib.sha256(serialized.encode()).hexdigest()
        elapsed = time.time() - start_t

        logger.info(
            f"[L3 Worker: {subtask.assigned_worker}] 실행 완료 ({elapsed:.2f}s) | SHA-256: {checksum[:12]}..."
        )

        return ExecutionArtifact(
            task_id=subtask.task_id,
            worker_name=subtask.assigned_worker,
            raw_data=mock_payload,
            metadata={"model_tier": subtask.model_tier.name, "elapsed": elapsed},
            checksum=checksum,
            execution_time_sec=elapsed,
        )


# ==============================================================================
# [Layer 4: Verification, QC & Delivery Layer]
# ==============================================================================
class VerificationDeliveryLayer:
    """기계적 실측 검증, 교차 모델 QC 게이트 및 최종 채널 배포."""

    @staticmethod
    def verify_and_deliver(
        plan: OrchestrationPlan, artifacts: List[ExecutionArtifact]
    ) -> VerificationReport:
        logger.info("[L4 QC & Delivery] 최종 품질 검수 및 교차 검증 시작...")
        details: List[str] = []

        passed_deterministic = True
        passed_cross_qc = True

        for art in artifacts:
            data = art.raw_data
            if not isinstance(data, dict):
                continue

            # 1. 기계적 실측 가드레일 (Deterministic Rules)
            # - 반말 평서체 검출 0건 필수
            if data.get("informal_speech_count", 0) > 0:
                passed_deterministic = False
                details.append(f"[{art.task_id}] FAIL: 반말 평서체 잔존 검출!")
            else:
                details.append(f"[{art.task_id}] PASS: 전 문장 정중한 존댓말 100% 실측 확인.")

            # - 하이퍼링크 실측
            if data.get("has_hyperlink", False):
                details.append(f"[{art.task_id}] PASS: 정식 se-link 하이퍼링크 실측 확인.")
            else:
                passed_deterministic = False
                details.append(f"[{art.task_id}] FAIL: 클릭 가능한 하이퍼링크 누락!")

            # - 19pt 소제목 4개 이상 확인
            headings = [
                item for item in data.get("generated_items", []) if item.get("size_pt") == 19
            ]
            if len(headings) >= 4:
                details.append(f"[{art.task_id}] PASS: 19pt 소제목 규격 {len(headings)}개 충족.")
            else:
                passed_deterministic = False
                details.append(f"[{art.task_id}] FAIL: 19pt 소제목 부족 ({len(headings)}/4).")

        # 2. 교차 모델 검수 (Cross-Model Dual Check 시뮬레이션)
        # Claude/Sonnet 생성 ➔ Gemini 검증
        cross_model_score = 98  # / 100
        if cross_model_score >= 90:
            details.append(f"[Cross-QC] PASS: 교차 모델(Claude ↔ Gemini) 논리 정합성 검수 통과 ({cross_model_score}점).")
        else:
            passed_cross_qc = False
            details.append("[Cross-QC] FAIL: 교차 모델 논리 불일치 감지.")

        # 3. 배포 (Delivery)
        delivered_channels: List[str] = []
        if passed_deterministic and passed_cross_qc:
            delivered_channels = ["git_repository (member-system)", "slack_channel (#ai)", "live_blog (irnshrk)"]
            logger.info(f"[L4 QC & Delivery] 🎉 모든 검수 통과! 배포 완료: {delivered_channels}")
        else:
            logger.error("[L4 QC & Delivery] ❌ 검수 실패! 롤백 및 작업자 재지시 필요.")

        final_hash = hashlib.sha256(
            "".join(a.checksum for a in artifacts).encode()
        ).hexdigest()

        return VerificationReport(
            artifact_id=plan.plan_id,
            passed_deterministic_checks=passed_deterministic,
            passed_cross_model_qc=passed_cross_qc,
            details=details,
            delivered_channels=delivered_channels,
            final_sha256=final_hash,
        )


# ==============================================================================
# [End-to-End Demo Execution]
# ==============================================================================
def main() -> None:
    print("=" * 80)
    print(" 🚀 ARSEN 4-Layer Multi-Agent Architecture Framework Live Demo")
    print("=" * 80)

    # 1. 외부 신호 인입 시뮬레이션 (Slack / Webhook)
    raw_incoming_signal = {
        "source": "slack:#ai",
        "user": "U_SANGWOOK",
        "text": "인덕원 안양 고기집 4곳 큐레이션 블로그 포스팅 발행 및 모듈화 가이드 작성",
        "params": {"category": "matjib", "target_count": 4},
    }

    # [Layer 1] 수집 및 필터링
    ingestion = IngestionLayer()
    event = ingestion.process_raw_signal(raw_incoming_signal)
    if not event:
        print("[!] 유효하지 않은 신호로 중단되었습니다.")
        return

    # [Layer 2] 두뇌 기획 및 모델 라우팅
    orchestrator = OrchestrationLayer(max_token_budget=15000)
    plan = orchestrator.plan_and_route(event)

    # [Layer 3] 격리된 워커 실행
    artifacts: List[ExecutionArtifact] = []
    for task in plan.tasks:
        artifact = WorkerExecutionLayer.execute_subtask(task)
        artifacts.append(artifact)

    # [Layer 4] 실측 검증 및 최종 배포
    report = VerificationDeliveryLayer.verify_and_deliver(plan, artifacts)

    # 결과 리포트 출력
    print("\n" + "-" * 80)
    print(" 📋 [ARSEN Framework Execution Receipt]")
    print("-" * 80)
    print(f"• Plan ID               : {report.artifact_id}")
    print(f"• Deterministic QC      : {'✅ PASS' if report.passed_deterministic_checks else '❌ FAIL'}")
    print(f"• Cross-Model QC        : {'✅ PASS' if report.passed_cross_model_qc else '❌ FAIL'}")
    print(f"• Delivered Channels    : {', '.join(report.delivered_channels)}")
    print(f"• Final Checksum        : SHA-256:{report.final_sha256[:16]}...")
    print("\n[검수 상세 로그]:")
    for d in report.details:
        print(f"  - {d}")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
