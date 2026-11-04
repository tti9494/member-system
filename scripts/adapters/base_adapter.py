"""Base Video Generation Engine Adapter Interface.

Defines the abstract interface, verification status, and production provenance
for all AI video models (Veo, Kling, Runway, Sora, etc.) in the modular pipeline.
"""
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Any, Optional


class EngineStatus(str, Enum):
    """Engine integration and verification status."""
    ADAPTER_IMPLEMENTED = "adapter_implemented"  # 어댑터 인터페이스 및 작업 스펙 생성 코드 구현 완료
    INTERFACE_ONLY = "interface_only"            # 파라미터 규격 정의 단계 (실연동 미확인)
    PLANNED = "planned"                          # 향후 연동 계획 단계 (상용 API 대기 등)
    DEPRECATED = "deprecated"                    # 지원 중단


class BaseVideoAdapter(ABC):
    """Abstract Base Class for Video Generation Model Adapters."""

    def __init__(self, name: str, status: EngineStatus, production_provenance: Optional[str] = None):
        self.name = name
        self.status = status
        self.production_provenance = production_provenance

    @abstractmethod
    def get_info(self) -> Dict[str, Any]:
        """Return engine metadata, capabilities, and verification status."""
        pass

    @abstractmethod
    def prepare_render_spec(
        self,
        scene_spec: Dict[str, Any],
        storyboard_path: str,
        output_dir: str
    ) -> Dict[str, Any]:
        """Generate engine-specific render specification / request payload."""
        pass

    @abstractmethod
    def resolve_clip_path(
        self,
        scene_id: str,
        input_directory: str
    ) -> Optional[str]:
        """Resolve the raw rendered clip file for the scene from the input directory."""
        pass
