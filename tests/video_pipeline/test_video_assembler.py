"""Tests for Video Assembler, Schemas, and Adapters (Modular Pipeline v1.2)."""
import os
import json
import pytest
from scripts.video_assembler import VideoAssembler, VideoProbe, run_counterexample_diagnostics
from scripts.adapters import get_adapter, list_engines, EngineStatus


def test_engine_registry_statuses_and_provenance():
    """Verify that Google Veo adapter separates code implementation from historical production provenance."""
    veo = get_adapter("google_veo")
    assert veo.status == EngineStatus.ADAPTER_IMPLEMENTED
    info = veo.get_info()
    assert info["status"] == "adapter_implemented"
    assert "80씬 전수 실사 렌더링 제작 및 검수 통과" in info["production_provenance"]
    assert "BaseVideoAdapter 인터페이스 구현" in info["adapter_verification"]
    assert info["recommended_cutoff_sec"] == 1.35

    kling = get_adapter("kling_1.5")
    assert kling.status == EngineStatus.INTERFACE_ONLY

    runway = get_adapter("runway_gen3")
    assert runway.status == EngineStatus.INTERFACE_ONLY

    sora = get_adapter("openai_sora")
    assert sora.status == EngineStatus.PLANNED


def test_schema_and_scene_order_validation():
    """Verify that scenes must be S01~S08 without duplicates, omissions, or bad order."""
    assembler = VideoAssembler()

    # Missing S08 (only 7 scenes)
    bad_plan = {
        "episode": 1,
        "title": "Bad Plan",
        "target_fps": 24,
        "target_resolution": {"width": 1920, "height": 1080},
        "duration_mode": {"type": "fixed_exact", "target_seconds": 60.0, "target_frames": 1440},
        "scenes": [
            {"scene_id": f"S{i:02d}", "canonical_storyboard": "a.jpg", "trim_start_sec": 1.35, "trim_end_sec": 8.0, "camera_motion": "pan", "prompt": "p"}
            for i in range(1, 8)
        ]
    }
    with pytest.raises(ValueError, match="must contain exactly 8 scenes"):
        assembler.validate_plan_structure(bad_plan)

    # Inverted order
    bad_order_plan = dict(bad_plan)
    scenes = [
        {"scene_id": f"S{i:02d}", "canonical_storyboard": "a.jpg", "trim_start_sec": 1.35, "trim_end_sec": 8.0, "camera_motion": "pan", "prompt": "p"}
        for i in range(1, 9)
    ]
    scenes[0], scenes[1] = scenes[1], scenes[0]  # swap S01 and S02
    bad_order_plan["scenes"] = scenes
    with pytest.raises(ValueError, match="Scene order violation"):
        assembler.validate_plan_structure(bad_order_plan)


def test_counterexample_diagnostics():
    """Run full diagnostic test verifying fixes for Counterexamples A, B, C, D and EP01."""
    results = run_counterexample_diagnostics()

    # Counterexample A: 7s raw clips under EP01 (55~65s) MUST FAIL and abort
    a = results["counterexample_a_7s_production_check"]
    assert a["status"] == "FAIL"
    assert "Flexible range violation" in a["diagnostics"][0]
    assert a["total_planned_duration_sec"] == 45.2

    # Counterexample B: 160x90 resolution mismatch against 1920x1080 MUST FAIL
    b = results["counterexample_b_resolution_mismatch"]
    assert b["status"] == "FAIL"
    assert any("resolution mismatch" in d for d in b["diagnostics"])

    # Counterexample C: Corrupted MP4 MUST be caught without fake fallback
    c = results["counterexample_c_corrupted_mp4"]
    assert c["corrupted_caught"] is True

    # Counterexample D: 10s clips S08 0-frame bug resolution MUST PASS
    d = results["counterexample_d_10s_s08_zero_frame_fix"]
    assert d["status"] == "PASS"
    assert d["s08_allocated_frames"] == 180
    assert d["all_scenes_have_frames"] is True
    assert d["total_frames"] == 1440

    # EP01 solution check: 58.54s, planned discrete frames 1,406 vs actual air master 1,405
    ep01 = results["ep01_canonical_solution"]
    assert ep01["status"] == "PASS"
    assert ep01["planned_total_duration_sec"] == 58.54
    assert ep01["planned_discrete_frames_sum"] == 1406
    air = ep01["air_physical_master_measurement"]
    assert air["actual_frames"] == 1405
    assert air["file_size_bytes"] == 61512282
