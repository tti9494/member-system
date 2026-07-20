import importlib
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import db
from agents import db_manager


def _install_scheduler_stub():
    if "apscheduler.schedulers.asyncio" in sys.modules:
        return
    try:
        import apscheduler.schedulers.asyncio  # noqa: F401
        import apscheduler.triggers.cron  # noqa: F401
        return
    except ModuleNotFoundError:
        pass

    apscheduler = types.ModuleType("apscheduler")
    schedulers = types.ModuleType("apscheduler.schedulers")
    asyncio_module = types.ModuleType("apscheduler.schedulers.asyncio")
    triggers = types.ModuleType("apscheduler.triggers")
    cron_module = types.ModuleType("apscheduler.triggers.cron")

    class AsyncIOScheduler:
        def __init__(self, *args, **kwargs):
            self.jobs = []

        def add_job(self, *args, **kwargs):
            self.jobs.append((args, kwargs))

        def start(self):
            return None

        def shutdown(self):
            return None

    class CronTrigger:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    asyncio_module.AsyncIOScheduler = AsyncIOScheduler
    cron_module.CronTrigger = CronTrigger
    sys.modules["apscheduler"] = apscheduler
    sys.modules["apscheduler.schedulers"] = schedulers
    sys.modules["apscheduler.schedulers.asyncio"] = asyncio_module
    sys.modules["apscheduler.triggers"] = triggers
    sys.modules["apscheduler.triggers.cron"] = cron_module


class EducationContractSmokeTest(unittest.TestCase):
    ADMIN_KEY = "unit-test-admin-key"

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.tmpdir.name) / "members.db"
        self.education_path = Path(self.tmpdir.name) / "education_resources.json"

        self.original_db_path = db.DB_PATH
        self.original_manager_db_path = db_manager.DB_PATH
        db.DB_PATH = self.db_path
        db_manager.DB_PATH = self.db_path
        db.init_db()

        _install_scheduler_stub()
        self.main = importlib.import_module("main")
        self.original_admin_key = self.main.ADMIN_API_KEY
        self.original_education_path = self.main.EDUCATION_DATA_PATH
        self.original_local_open = self.main.MEMBER_ADMIN_LOCAL_OPEN
        self.original_local_flag = self.main.LOCAL_ADMIN_OPEN_FLAG

        self.main.ADMIN_API_KEY = self.ADMIN_KEY
        self.main.EDUCATION_DATA_PATH = self.education_path
        self.main.MEMBER_ADMIN_LOCAL_OPEN = False
        self.main.LOCAL_ADMIN_OPEN_FLAG = Path(self.tmpdir.name) / ".local_admin_open"
        self._write_seed()
        self.client = TestClient(self.main.app)

    def tearDown(self):
        self.main.ADMIN_API_KEY = self.original_admin_key
        self.main.EDUCATION_DATA_PATH = self.original_education_path
        self.main.MEMBER_ADMIN_LOCAL_OPEN = self.original_local_open
        self.main.LOCAL_ADMIN_OPEN_FLAG = self.original_local_flag
        db.DB_PATH = self.original_db_path
        db_manager.DB_PATH = self.original_manager_db_path
        self.tmpdir.cleanup()

    def _admin_headers(self):
        return {"X-Admin-Key": self.ADMIN_KEY}

    def _write_seed(self):
        payload = {
            "updated_at": "2026-05-18T00:00:00+00:00",
            "resources": [
                {
                    "section": "설치 링크",
                    "title": "Visible Resource",
                    "status": "official",
                    "description": "public",
                    "url": "https://example.com/visible",
                    "copy_text": "",
                    "visible": True,
                },
                {
                    "section": "수업 프롬프트",
                    "title": "Hidden Template",
                    "status": "template",
                    "description": "operator only",
                    "url": "",
                    "copy_text": "hidden copy",
                    "visible": False,
                    "template_id": "template-smoke",
                },
            ],
        }
        self.education_path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def test_public_get_returns_visible_resources_only(self):
        response = self.client.get("/api/education")
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["visible_count"], payload["total_count"])
        self.assertEqual(payload["hidden_count"], 0)
        self.assertTrue(payload["resources"])
        self.assertTrue(all(item.get("visible") is not False for item in payload["resources"]))
        self.assertNotIn("Hidden Template", {item["title"] for item in payload["resources"]})

    def test_admin_hidden_get_requires_key_and_preserves_template_id(self):
        blocked = self.client.get("/api/education?include_hidden=1")
        self.assertEqual(blocked.status_code, 401)

        response = self.client.get(
            "/api/education?include_hidden=1",
            headers=self._admin_headers(),
        )
        self.assertEqual(response.status_code, 200)
        resources = response.json()["resources"]
        hidden = [item for item in resources if item.get("visible") is False]
        self.assertEqual(len(resources), 2)
        self.assertEqual(hidden[0]["template_id"], "template-smoke")

    def test_put_save_add_delete_persists_contract(self):
        response = self.client.get(
            "/api/education?include_hidden=1",
            headers=self._admin_headers(),
        )
        resources = response.json()["resources"]
        baseline_total = len(resources)

        resources[0]["description"] = "updated public description"
        resources.append(
            {
                "section": "수업 프롬프트",
                "title": "Temporary Hidden Smoke",
                "status": "template",
                "description": "temporary",
                "url": "",
                "copy_text": "temporary copy",
                "visible": False,
                "template_id": "temporary-hidden-smoke",
            }
        )
        saved = self.client.put(
            "/api/education",
            headers=self._admin_headers(),
            json={"resources": resources},
        )
        self.assertEqual(saved.status_code, 200)
        self.assertEqual(saved.json()["total_count"], baseline_total + 1)

        admin_reload = self.client.get(
            "/api/education?include_hidden=1",
            headers=self._admin_headers(),
        ).json()
        by_title = {item["title"]: item for item in admin_reload["resources"]}
        self.assertEqual(by_title["Visible Resource"]["description"], "updated public description")
        self.assertEqual(by_title["Temporary Hidden Smoke"]["template_id"], "temporary-hidden-smoke")
        self.assertEqual(by_title["Hidden Template"]["template_id"], "template-smoke")

        public_reload = self.client.get("/api/education").json()
        self.assertNotIn("Temporary Hidden Smoke", {item["title"] for item in public_reload["resources"]})

        deleted = [
            item
            for item in admin_reload["resources"]
            if item["title"] != "Temporary Hidden Smoke"
        ]
        delete_response = self.client.put(
            "/api/education",
            headers=self._admin_headers(),
            json={"resources": deleted},
        )
        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(delete_response.json()["total_count"], baseline_total)

    def test_static_student_and_dashboard_contracts(self):
        web_page = ROOT.parent / "arsen-ai-web" / "education.html"
        dashboard_page = ROOT.parent / "arsen-dashboard" / "frontend" / "index.html"
        if not web_page.exists() or not dashboard_page.exists():
            self.skipTest("sibling web/dashboard repos are not available")

        web_html = web_page.read_text(encoding="utf-8")
        self.assertIn("https://apply.arsen-ai.com", web_html)
        self.assertIn("강의/교육 - ARSEN AI", web_html)
        self.assertIn("AI 결과물 제작 초급 4주반", web_html)
        self.assertIn("https://apply.arsen-ai.com/frontend/join-full.html", web_html)
        self.assertNotIn("https://apply.arsen-ai.com/frontend/join-free.html", web_html)
        self.assertIn("https://apply.arsen-ai.com/frontend/status.html", web_html)
        self.assertNotIn("'X-Admin-Key'", web_html)

        dashboard_html = dashboard_page.read_text(encoding="utf-8")
        self.assertIn("/api/education?include_hidden=true", dashboard_html)
        self.assertTrue(
            "fetch(API + '/api/education?include_hidden=true')" in dashboard_html
            or "fetch(apiUrl('/api/education?include_hidden=true'))" in dashboard_html
        )
        self.assertIn("toggleEducationHidden()", dashboard_html)
        self.assertIn("숨김 자료 표시", dashboard_html)
        save_start = dashboard_html.index("function saveEducationResources()")
        save_end = dashboard_html.index("function renderEducationEditor()", save_start)
        save_block = dashboard_html[save_start:save_end]
        self.assertNotIn("fetch(", save_block)
        self.assertIn("openEducationEditor()", save_block)


if __name__ == "__main__":
    unittest.main()
