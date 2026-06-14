import importlib
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
            return None

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


class ReviewBoardContractTest(unittest.TestCase):
    ADMIN_KEY = "unit-test-review-board-key"

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.tmpdir.name) / "members.db"
        self.original_db_path = db.DB_PATH
        self.original_manager_db_path = db_manager.DB_PATH
        db.DB_PATH = self.db_path
        db_manager.DB_PATH = self.db_path
        db.init_db()

        _install_scheduler_stub()
        self.main = importlib.import_module("main")
        self.original_admin_key = self.main.ADMIN_API_KEY
        self.main.ADMIN_API_KEY = self.ADMIN_KEY
        self.client = TestClient(self.main.app)

    def tearDown(self):
        self.main.ADMIN_API_KEY = self.original_admin_key
        db.DB_PATH = self.original_db_path
        db_manager.DB_PATH = self.original_manager_db_path
        self.tmpdir.cleanup()

    def _admin_headers(self):
        return {"X-Admin-Key": self.ADMIN_KEY}

    def test_admin_can_manage_review_board_and_public_only_sees_checked_public_entries(self):
        no_auth = self.client.get("/admin/review-board")
        self.assertEqual(no_auth.status_code, 401)

        instructor_response = self.client.post(
            "/admin/review-board/instructors",
            headers=self._admin_headers(),
            json={
                "name": "테스트 강사",
                "role": "AI 자동화",
                "specialties": ["LLM", "업무 자동화"],
                "status": "active",
                "sort_order": 1,
            },
        )
        self.assertEqual(instructor_response.status_code, 200)
        instructor_id = instructor_response.json()["id"]

        entry_response = self.client.post(
            "/admin/review-board/entries",
            headers=self._admin_headers(),
            json={
                "instructor_id": instructor_id,
                "class_title": "테스트 수업",
                "class_date": "2026-06-10",
                "title": "검수 전 후기",
                "summary": "공개 전에는 보이지 않아야 합니다.",
                "tags": ["후기", "자동화"],
                "status": "public",
                "privacy_checked": False,
                "featured": True,
            },
        )
        self.assertEqual(entry_response.status_code, 200)
        entry_id = entry_response.json()["id"]

        public_before = self.client.get("/api/review-board").json()["data"]
        self.assertEqual(public_before["entries"], [])

        update_response = self.client.put(
            f"/admin/review-board/entries/{entry_id}",
            headers=self._admin_headers(),
            json={"privacy_checked": True},
        )
        self.assertEqual(update_response.status_code, 200)

        public_after = self.client.get("/api/review-board").json()["data"]
        self.assertEqual(len(public_after["entries"]), 1)
        self.assertEqual(public_after["entries"][0]["title"], "검수 전 후기")
        self.assertTrue(public_after["entries"][0]["privacy_checked"])

        admin_board = self.client.get("/admin/review-board", headers=self._admin_headers()).json()["data"]
        self.assertEqual(admin_board["stats"]["entries"], 1)
        self.assertEqual(admin_board["stats"]["instructors"], 1)

    def test_review_entry_accepts_class_title_without_title_like_worker(self):
        instructor_id = self.client.post(
            "/admin/review-board/instructors",
            headers=self._admin_headers(),
            json={"name": "계약 테스트 강사"},
        ).json()["id"]

        response = self.client.post(
            "/admin/review-board/entries",
            headers=self._admin_headers(),
            json={
                "instructor_id": instructor_id,
                "class_title": "제목 보정 수업",
                "status": "draft",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"]["title"], "제목 보정 수업")

    def test_review_update_noop_returns_400_and_missing_target_returns_404(self):
        no_fields = self.client.put(
            "/admin/review-board/entries/missing",
            headers=self._admin_headers(),
            json={},
        )
        self.assertEqual(no_fields.status_code, 400)

        missing = self.client.put(
            "/admin/review-board/entries/missing",
            headers=self._admin_headers(),
            json={"title": "없음"},
        )
        self.assertEqual(missing.status_code, 404)

        instructor_no_fields = self.client.put(
            "/admin/review-board/instructors/missing",
            headers=self._admin_headers(),
            json={},
        )
        self.assertEqual(instructor_no_fields.status_code, 400)

        instructor_missing = self.client.put(
            "/admin/review-board/instructors/missing",
            headers=self._admin_headers(),
            json={"name": "없음"},
        )
        self.assertEqual(instructor_missing.status_code, 404)

    def test_student_review_invite_submission_requires_admin_approval_before_public(self):
        invite_response = self.client.post(
            "/admin/review-board/invites",
            headers=self._admin_headers(),
            json={
                "label": "초대 테스트",
                "class_title": "후기 링크 수업",
                "class_date": "2026-06-12",
            },
        )
        self.assertEqual(invite_response.status_code, 200)
        invite = invite_response.json()["data"]
        self.assertIn("token", invite)
        self.assertNotIn("token_hash", invite)

        token = invite["token"]
        form_response = self.client.get(f"/api/review-board/submit/{token}")
        self.assertEqual(form_response.status_code, 200)
        self.assertEqual(form_response.json()["data"]["invite"]["class_title"], "후기 링크 수업")

        submit_response = self.client.post(
            f"/api/review-board/submit/{token}",
            json={
                "display_name": "후기작성자",
                "class_title": "후기 링크 수업",
                "class_date": "2026-06-12",
                "rating": 5,
                "summary": "승인 전에는 공개되면 안 됩니다.",
                "body": "관리자 승인 후 공개되어야 하는 후기입니다.",
                "tags": ["테스트", "링크제출"],
                "consent_public_review": True,
            },
        )
        self.assertEqual(submit_response.status_code, 200)
        entry_id = submit_response.json()["data"]["id"]

        public_before = self.client.get("/api/review-board").json()["data"]
        self.assertEqual(public_before["entries"], [])

        admin_board = self.client.get("/admin/review-board", headers=self._admin_headers()).json()["data"]
        self.assertEqual(len(admin_board["entries"]), 1)
        self.assertEqual(admin_board["entries"][0]["status"], "draft")
        self.assertTrue(admin_board["entries"][0]["source"].startswith("student_link:"))
        self.assertEqual(admin_board["invites"][0]["submitted_count"], 1)

        approve_response = self.client.put(
            f"/admin/review-board/entries/{entry_id}",
            headers=self._admin_headers(),
            json={"status": "public", "privacy_checked": True},
        )
        self.assertEqual(approve_response.status_code, 200)

        public_after = self.client.get("/api/review-board").json()["data"]
        self.assertEqual(len(public_after["entries"]), 1)
        self.assertEqual(public_after["entries"][0]["title"], "후기작성자님의 수업 후기")


if __name__ == "__main__":
    unittest.main()
