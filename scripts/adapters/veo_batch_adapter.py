"""Google Veo Batch Adapter (Production Engine Adapter).

Connects to the multi-account Veo pipeline specifications used for
'혈화의 궐' EP01~EP10 production.

Historical Production Provenance:
- 10부작 전편(EP01~EP10) 80씬 전수 실사 렌더링 제작 및 검수 통과 (MacBook Air M2 6계정 브릿지 실증 이력)

Adapter Implementation Status:
- ADAPTER_IMPLEMENTED: BaseVideoAdapter 인터페이스 구현 및 로컬 태스크 스펙 생성/경로 탐색 코드 완비.
"""
import os
import glob
from typing import Dict, Any, Optional
from .base_adapter import BaseVideoAdapter, EngineStatus


class VeoBatchAdapter(BaseVideoAdapter):
    """Adapter for Google Veo 16:9 cinematic batch generation."""

    def __init__(self):
        super().__init__(
            name="Google Veo",
            status=EngineStatus.ADAPTER_IMPLEMENTED,
            production_provenance=(
                "사극 10부작 전편(EP01~EP10) 80씬 전수 실사 렌더링 제작 및 검수 통과 "
                "(MacBook Air M2 Ego 6계정 브릿지 파이프라인 실증 이력)"
            )
        )

    def get_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "status": self.status.value,
            "production_provenance": self.production_provenance,
            "adapter_verification": (
                "어댑터 코드 구현 완료: BaseVideoAdapter 인터페이스 구현, 씬별 렌더 태스크 페이로드(prepare_render_spec) "
                "및 로컬/원격 클립 경로 탐색(resolve_clip_path) 단위 테스트 검증 완료. "
                "(참고: 80씬 실증 이력은 MacAir 멀티프로필 브릿지 운영 결과물이며, 본 파이썬 클래스는 해당 규격을 추상화한 어댑터임)"
            ),
            "input_mode": "Image-to-Video (1:1 Canonical Storyboard + Prompt)",
            "native_aspect_ratio": "16:9 (1920x1080)",
            "native_fps": 24,
            "default_raw_duration_sec": 7.0,
            "recommended_cutoff_sec": 1.35,
            "clean_cutoff_range_sec": [1.35, 9.75],
            "supports_audio": False  # Native -an clean video
        }

    def prepare_render_spec(
        self,
        scene_spec: Dict[str, Any],
        storyboard_path: str,
        output_dir: str
    ) -> Dict[str, Any]:
        """Generate render task payload for Veo runner."""
        scene_id = scene_spec["scene_id"]
        return {
            "engine": "google_veo",
            "scene_id": scene_id,
            "storyboard_image": storyboard_path,
            "prompt": scene_spec["prompt"],
            "camera_motion": scene_spec.get("camera_motion", "cinematic"),
            "aspect_ratio": "16:9",
            "target_resolution": "1920x1080",
            "fps": 24,
            "expected_raw_output": os.path.join(output_dir, f"raw_{scene_id}.mp4")
        }

    def resolve_clip_path(
        self,
        scene_id: str,
        input_directory: str
    ) -> Optional[str]:
        """Find existing clip for the scene in local directory or assets."""
        patterns = [
            os.path.join(input_directory, f"raw_{scene_id}.mp4"),
            os.path.join(input_directory, f"{scene_id}.mp4"),
            os.path.join(input_directory, f"*_{scene_id}_*.mp4"),
            os.path.join(input_directory, f"clip_{scene_id}.mp4"),
        ]
        for pat in patterns:
            matches = glob.glob(pat)
            if matches:
                return sorted(matches)[0]
        return None
