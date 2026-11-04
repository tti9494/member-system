"""OpenAI Sora Adapter (Planned / Speculative).

Status: PLANNED (향후 공식 API 릴리즈 시 연동 계획).
"""
from typing import Dict, Any, Optional
from .base_adapter import BaseVideoAdapter, EngineStatus


class SoraAdapter(BaseVideoAdapter):
    """Adapter interface for OpenAI Sora."""

    def __init__(self):
        super().__init__(name="OpenAI Sora", status=EngineStatus.PLANNED)

    def get_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "status": self.status.value,
            "verification_notes": (
                "상용 대량 생성 API 정식 출시 대기 중. "
                "추상화 인터페이스 사전 정의 상태."
            ),
            "input_mode": "Multi-modal Prompt (Text + Image Anchor)",
            "native_aspect_ratio": "16:9",
            "native_fps": 24,
            "default_raw_duration_sec": 10.0,
            "recommended_cutoff_sec": 0.50,
            "clean_cutoff_range_sec": [0.50, 9.90]
        }

    def prepare_render_spec(
        self,
        scene_spec: Dict[str, Any],
        storyboard_path: str,
        output_dir: str
    ) -> Dict[str, Any]:
        return {
            "engine": "openai_sora",
            "scene_id": scene_spec["scene_id"],
            "prompt": scene_spec["prompt"],
            "anchor_image": storyboard_path,
            "status": "planned_unsupported"
        }

    def resolve_clip_path(
        self,
        scene_id: str,
        input_directory: str
    ) -> Optional[str]:
        return None
