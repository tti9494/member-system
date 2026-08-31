import os
import sys
import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
from fastapi.testclient import TestClient

WORKSPACE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WORKSPACE_DIR))

import db

@pytest.fixture(scope="module")
def setup_db():
    with TemporaryDirectory() as temp_dir:
        temp_db_path = Path(temp_dir) / "members.db"
        original_db_path = db.DB_PATH
        db.DB_PATH = temp_db_path
        db.init_db()
        yield temp_db_path
        db.DB_PATH = original_db_path

@pytest.fixture(scope="module")
def client(setup_db):
    import main
    main.ADMIN_API_KEY = "test_admin_key"
    with TestClient(main.app) as c:
        yield c

@pytest.fixture
def admin_headers():
    return {"X-Admin-Key": "test_admin_key"}

def _create_device(client, headers):
    resp = client.post("/admin/yoonbot/lab/devices", json={"name": "test_mac", "platform": "macos"}, headers=headers)
    return resp.json()["id"], resp.json()["token"]

def _create_template(client, headers):
    resp = client.post("/admin/yoonbot/lab/templates", json={"name": "tpl1", "content": "hello"}, headers=headers)
    return resp.json()["id"]

def test_missing_admin_auth(client):
    resp = client.post("/admin/yoonbot/lab/devices", json={"name": "test_mac", "platform": "macos"})
    assert resp.status_code == 401

def test_device_extra_fields(client, admin_headers):
    resp = client.post("/admin/yoonbot/lab/devices", json={"name": "test_mac", "platform": "macos", "extra": "field"}, headers=admin_headers)
    assert resp.status_code == 400

def test_template_extra_fields(client, admin_headers):
    resp = client.post("/admin/yoonbot/lab/templates", json={"name": "tpl1", "content": "hello", "extra": "field"}, headers=admin_headers)
    assert resp.status_code == 400

def test_boundary_validation(client, admin_headers):
    dev_id, _ = _create_device(client, admin_headers)
    assert client.post(
        "/admin/yoonbot/lab/templates",
        json={"name": "blank", "content": "   ", "version": 1},
        headers=admin_headers,
    ).status_code == 400
    assert client.post(
        "/admin/yoonbot/lab/jobs",
        json={
            "idempotency_key": "bad key",
            "device_id": dev_id,
            "target_alias": "target1",
            "action": "simulate_schedule",
            "execution_mode": "dry_run",
        },
        headers=admin_headers,
    ).status_code == 400
    assert client.post(
        "/admin/yoonbot/lab/jobs",
        json={
            "idempotency_key": "held_without_reason",
            "device_id": dev_id,
            "target_alias": "target1",
            "action": "simulate_schedule",
            "execution_mode": "dry_run",
            "quality_status": "blocked",
        },
        headers=admin_headers,
    ).status_code == 400

def test_device_list_no_secrets(client, admin_headers):
    dev_id, _ = _create_device(client, admin_headers)
    resp = client.get("/admin/yoonbot/lab/devices", headers=admin_headers)
    assert resp.status_code == 200
    devices = resp.json()["devices"]
    assert any(d["id"] == dev_id for d in devices)
    assert all("token" not in d for d in devices)
    assert all("token_hash" not in d for d in devices)

def test_template_list_no_secrets(client, admin_headers):
    tpl_id = _create_template(client, admin_headers)
    resp = client.get("/admin/yoonbot/lab/templates", headers=admin_headers)
    assert resp.status_code == 200
    templates = resp.json()["templates"]
    assert any(t["id"] == tpl_id for t in templates)
    assert all("content" not in t for t in templates)

def test_job_lists_no_secrets(client, admin_headers):
    dev_id, _ = _create_device(client, admin_headers)
    resp = client.post("/admin/yoonbot/lab/jobs", json={
        "idempotency_key": "list_jobs_test",
        "device_id": dev_id,
        "target_alias": "target1",
        "action": "simulate_schedule",
        "execution_mode": "dry_run"
    }, headers=admin_headers)
    job_id = resp.json()["id"]

    resp = client.get("/admin/yoonbot/lab/jobs", headers=admin_headers)
    assert resp.status_code == 200
    jobs = resp.json()["jobs"]
    assert any(j["id"] == job_id for j in jobs)

    resp = client.get(f"/admin/yoonbot/lab/jobs/{job_id}/results", headers=admin_headers)
    assert resp.status_code == 200

def test_template_missing(client, admin_headers):
    dev_id, _ = _create_device(client, admin_headers)
    resp = client.post("/admin/yoonbot/lab/jobs", json={
        "idempotency_key": "k_miss",
        "device_id": dev_id,
        "template_id": "invalid_tpl",
        "target_alias": "target1",
        "action": "simulate_schedule",
        "execution_mode": "dry_run"
    }, headers=admin_headers)
    assert resp.status_code == 400

def test_idempotency_conflict(client, admin_headers):
    dev_id, _ = _create_device(client, admin_headers)
    dev_id_2, _ = _create_device(client, admin_headers)
    
    resp = client.post("/admin/yoonbot/lab/jobs", json={
        "idempotency_key": "idemp_test",
        "device_id": dev_id,
        "target_alias": "target1",
        "action": "simulate_schedule",
        "execution_mode": "dry_run"
    }, headers=admin_headers)
    assert resp.status_code == 200
    job_id = resp.json()["id"]
    
    # Matching params
    resp2 = client.post("/admin/yoonbot/lab/jobs", json={
        "idempotency_key": "idemp_test",
        "device_id": dev_id,
        "target_alias": "target1",
        "action": "simulate_schedule",
        "execution_mode": "dry_run"
    }, headers=admin_headers)
    assert resp2.status_code == 200
    assert resp2.json()["id"] == job_id
    
    # Conflict params
    resp3 = client.post("/admin/yoonbot/lab/jobs", json={
        "idempotency_key": "idemp_test",
        "device_id": dev_id_2,
        "target_alias": "target1",
        "action": "simulate_schedule",
        "execution_mode": "dry_run"
    }, headers=admin_headers)
    assert resp3.status_code == 409

def test_agent_heartbeat(client, admin_headers):
    dev_id, token = _create_device(client, admin_headers)
    agent_headers = {"Authorization": f"Bearer {token}"}
    resp = client.post("/api/yoonbot/agent/heartbeat", headers=agent_headers)
    assert resp.status_code == 200
    assert resp.json()["ok"] is True

def test_claim_includes_assigned_template_only(client, admin_headers):
    dev_id, token = _create_device(client, admin_headers)
    tpl_id = _create_template(client, admin_headers)
    created = client.post("/admin/yoonbot/lab/jobs", json={
        "idempotency_key": "claim_template_contract",
        "device_id": dev_id,
        "template_id": tpl_id,
        "target_alias": "self-test",
        "action": "preview_message",
        "execution_mode": "dry_run",
        "quality_status": "pass",
    }, headers=admin_headers)
    job_id = created.json()["id"]
    client.post(f"/admin/yoonbot/lab/jobs/{job_id}/approve", headers=admin_headers)
    claimed = client.post(
        "/api/yoonbot/agent/claim",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert claimed.status_code == 200
    job = claimed.json()["job"]
    assert job["id"] == job_id
    assert job["template_id"] == tpl_id
    assert job["template_name"] == "tpl1"
    assert job["template_content"] == "hello"
    assert job["template_version"] == 1
    assert "token" not in job and "token_hash" not in job

def test_job_and_agent_flow(client, admin_headers):
    dev_id, token = _create_device(client, admin_headers)
    
    resp = client.post("/admin/yoonbot/lab/jobs", json={
        "idempotency_key": "k1",
        "device_id": dev_id,
        "target_alias": "target1",
        "action": "simulate_schedule",
        "execution_mode": "dry_run",
        "quality_status": "pass"
    }, headers=admin_headers)
    assert resp.status_code == 200
    job_id = resp.json()["id"]
    
    client.post(f"/admin/yoonbot/lab/jobs/{job_id}/approve", headers=admin_headers)
    
    agent_headers = {"Authorization": f"Bearer {token}"}
    client.post("/api/yoonbot/agent/claim", headers=agent_headers)
    
    # Unknown result status
    resp = client.post(f"/api/yoonbot/agent/jobs/{job_id}/result", json={
        "status": "unknown_status",
        "quality_status": "pass"
    }, headers=agent_headers)
    assert resp.status_code == 400
    
    # success hold_reason mapping
    resp = client.post(f"/api/yoonbot/agent/jobs/{job_id}/result", json={
        "status": "dry_run_completed",
        "quality_status": "pass"
    }, headers=agent_headers)
    assert resp.status_code == 200
    
    # check if it mapped to held
    resp = client.get("/admin/yoonbot/lab/jobs", headers=admin_headers)
    job_info = next((j for j in resp.json()["jobs"] if j["id"] == job_id), None)
    assert job_info["status"] == "held"
    assert job_info["hold_reason"] == "dry_run_completed"
    
def test_wrong_assigned_device(client, admin_headers):
    dev_id1, token1 = _create_device(client, admin_headers)
    dev_id2, token2 = _create_device(client, admin_headers)
    
    resp = client.post("/admin/yoonbot/lab/jobs", json={
        "idempotency_key": "k_dev_wrong",
        "device_id": dev_id1,
        "target_alias": "target1",
        "action": "simulate_schedule",
        "execution_mode": "dry_run",
        "quality_status": "pass"
    }, headers=admin_headers)
    job_id = resp.json()["id"]
    client.post(f"/admin/yoonbot/lab/jobs/{job_id}/approve", headers=admin_headers)
    
    agent_headers1 = {"Authorization": f"Bearer {token1}"}
    client.post("/api/yoonbot/agent/claim", headers=agent_headers1)
    
    # Try report result with wrong device token
    agent_headers2 = {"Authorization": f"Bearer {token2}"}
    resp = client.post(f"/api/yoonbot/agent/jobs/{job_id}/result", json={
        "status": "dry_run_completed",
        "quality_status": "pass"
    }, headers=agent_headers2)
    assert resp.status_code == 404

def test_held_requires_safe_hold_reason(client, admin_headers):
    dev_id, token = _create_device(client, admin_headers)
    resp = client.post("/admin/yoonbot/lab/jobs", json={
        "idempotency_key": "k_held_test",
        "device_id": dev_id,
        "target_alias": "t_held",
        "action": "simulate_schedule",
        "execution_mode": "dry_run",
        "quality_status": "pass"
    }, headers=admin_headers)
    job_id = resp.json()["id"]
    client.post(f"/admin/yoonbot/lab/jobs/{job_id}/approve", headers=admin_headers)
    
    agent_headers = {"Authorization": f"Bearer {token}"}
    client.post("/api/yoonbot/agent/claim", headers=agent_headers)
    
    # empty hold_reason for held
    resp = client.post(f"/api/yoonbot/agent/jobs/{job_id}/result", json={
        "status": "held",
        "quality_status": "review_needed"
    }, headers=agent_headers)
    assert resp.status_code == 400
    
    # invalid quality_status for held
    resp = client.post(f"/api/yoonbot/agent/jobs/{job_id}/result", json={
        "status": "held",
        "quality_status": "pass",
        "hold_reason": "safe reason"
    }, headers=agent_headers)
    assert resp.status_code == 400
    
    # valid
    resp = client.post(f"/api/yoonbot/agent/jobs/{job_id}/result", json={
        "status": "held",
        "quality_status": "review_needed",
        "hold_reason": "safe reason"
    }, headers=agent_headers)
    assert resp.status_code == 200


def test_lab_ui_auto_connects_and_builds_safe_one_click_jobs():
    html = (WORKSPACE_DIR / "frontend" / "yoonbot-lab.html").read_text(encoding="utf-8")

    assert 'id="auth-section" hidden' in html
    assert "async function autoConnect()" in html
    assert '<select id="job-device">' in html
    assert 'id="job-idempotency"' not in html
    assert 'id="job-mode"' not in html
    assert "crypto.randomUUID()" in html
    assert 'execution_mode: "dry_run"' in html
    assert "quality_status: \"pass\"" in html
    assert "`/jobs/${data.id}/approve`" in html
