"""Engine Registry for Video Generation Adapters.

Manages registration and lookup of video generation engines,
providing explicit visibility into verification status.
"""
from typing import Dict, List, Any
from .base_adapter import BaseVideoAdapter, EngineStatus
from .veo_batch_adapter import VeoBatchAdapter
from .kling_adapter import KlingAdapter
from .runway_adapter import RunwayAdapter
from .sora_adapter import SoraAdapter


_REGISTRY: Dict[str, BaseVideoAdapter] = {
    "google_veo": VeoBatchAdapter(),
    "veo": VeoBatchAdapter(),
    "kling_1.5": KlingAdapter(),
    "kling": KlingAdapter(),
    "runway_gen3": RunwayAdapter(),
    "runway": RunwayAdapter(),
    "openai_sora": SoraAdapter(),
    "sora": SoraAdapter()
}


def get_adapter(engine_name: str) -> BaseVideoAdapter:
    """Retrieve an adapter by engine name or alias."""
    key = engine_name.strip().lower()
    if key not in _REGISTRY:
        supported = list(_REGISTRY.keys())
        raise ValueError(f"Unknown engine '{engine_name}'. Available engines: {supported}")
    return _REGISTRY[key]


def list_engines() -> List[Dict[str, Any]]:
    """List all registered engines with metadata and verification status."""
    seen = set()
    result = []
    for adapter in _REGISTRY.values():
        if adapter.name in seen:
            continue
        seen.add(adapter.name)
        result.append(adapter.get_info())
    return result
