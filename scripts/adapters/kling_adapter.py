"""Kling AI Adapter (Interface Only).

Parameter mapping for Kling 1.5 / Pro video generation.
Status: INTERFACE_ONLY (실연동 미확인, 규격 매핑만 정의됨).
"""
import os
import glob
from typing import Dict, Any, Optional
from .base_adapter import BaseVideoAdapter, EngineStatus


class KlingAdapter(BaseVideoAdapter):
    """Adapter interface for Kling 1.5."""

    def __init__(self):
        super().__init__(name="Kling AI 1.5", status=EngineStatus.INTERFACE_ONLY)

    def get_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "status": self.status.value,
            "verification_notes": (
                "인터페이스 및 파라미터 매핑 규격만 정의됨. "
                "실제 API 연동 및 프로덕션 파이프라인 실측 미확인 상태."
            ),
            "input_mode": "Image + Text Prompt",
            "native_aspect_ratio": "16:9",
            "native_fps": 24,
            "default_raw_duration_sec": 10.0,
            "recommended_cutoff_sec": 1.00,
            "clean_cutoff_range_sec": [1.00, 9.50]
        }

    def prepare_render_spec(
        self,
        scene_spec: Dict[str, Any],
        storyboard_path: str,
        output_dir: str
    ) -> Dict[str, Any]:
        return {
            "engine": "kling_1.5",
            "scene_id": scene_spec["scene_id"],
            "image": storyboard_path,
            "prompt": scene_spec["prompt"],
            "mode": "pro",
            "duration": 10,
            "motion_brush_intensity": 3,
            "expected_raw_output": os.path.join(output_dir, f"raw_{scene_spec['scene_id']}.mp4")
        }

    def resolve_clip_path(
        self,
        scene_id: str,
        input_directory: str
    ) -> Optional[str]:
        patterns = [
            os.path.join(input_directory, f"kling_{scene_id}.mp4"),
            os.path.join(input_directory, f"raw_{scene_id}.mp4")
        ]
        for pat in patterns:
            matches = glob.glob(pat)
            if matches:
                return sorted(matches)[0]
        return None
