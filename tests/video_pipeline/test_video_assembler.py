"""Tests for Video Assembler, Schemas, and Adapters (Modular Pipeline v1.1)."""
import os
import json
import pytest
from scripts.video_assembler import VideoAssembler, VideoProbe, run_counterexample_diagnostics
from scripts.adapters import get_adapter, list_engines, EngineStatus


def test_engine_registry_statuses():
    """Verify that Google Veo is VERIFIED, others are INTERFACE_ONLY or PLANNED."""
    veo = get_adapter("google_veo")
    assert veo.status == EngineStatus.VERIFIED
    info = veo.get_info()
    assert info["status"] == "verified"
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
    """Run full diagnostic test verifying fixes for Counterexamples A and B."""
    results = run_counterexample_diagnostics()

    # Counterexample A check
    a = results["counterexample_a_7s"]
    assert a["old_naive_check"]["status"] == "FAIL"
    assert "14.800s" in a["old_naive_check"]["diagnostics"][0]
    assert a["flexible_range_check"]["status"] == "PASS"

    # Counterexample B check
    b = results["counterexample_b_10s"]
    assert b["old_flaw_explanation"]["s08_frames_in_old_script"] == 0
    assert b["new_fixed_check"]["status"] == "PASS"
    assert b["new_fixed_check"]["s08_frames"] == 180
    assert b["new_fixed_check"]["all_scenes_have_frames"] is True
    assert b["new_fixed_check"]["total_frames"] == 1440

    # EP01 solution check
    ep01 = results["ep01_canonical_solution"]
    assert ep01["status"] == "PASS"
    assert ep01["total_duration_sec"] == 58.54
    assert len(ep01["scene_table"]) == 8
