import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import db
from agents import booking_manager, db_manager


class BookingPaymentFlowTest(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.tmpdir.name) / "members.db"
        self.original_db_path = db.DB_PATH
        self.original_manager_db_path = db_manager.DB_PATH
        db.DB_PATH = self.db_path
        db_manager.DB_PATH = self.db_path
        db.init_db()
        for idx in range(1, 4):
            self._create_test_member(
                f"member-{idx}",
                name=f"TEST Member {idx}",
                phone_masked=f"010-****-{idx:04d}",
            )

    def tearDown(self):
        db.DB_PATH = self.original_db_path
        db_manager.DB_PATH = self.original_manager_db_path
        self.tmpdir.cleanup()

    def _create_test_member(self, member_id, name="TEST Member", phone_masked="010-****-0000"):
        now = datetime.now(timezone.utc).isoformat()
        conn = db.get_conn()
        conn.execute(
            """
            INSERT OR IGNORE INTO members (
                id, name, email_encrypted, email_hash, phone_hash, phone_masked, phone_encrypted,
                gender, age, job, referral_source, reason, ai_level, plan_type,
                consent_personal, consent_marketing, consent_at, consent_version,
                status, created_at
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                member_id,
                name,
                f"test-email-encrypted-{member_id}",
                f"test-email-hash-{member_id}",
                f"test-phone-hash-{member_id}",
                phone_masked,
                f"test-phone-encrypted-{member_id}",
                "테스트",
                30,
                "QA",
                "unit-test",
                "booking payment flow fixture",
                "입문",
                "basic",
                1,
                0,
                now,
                "test-fixture-v1",
                "approved",
                now,
            ),
        )
        conn.commit()
        conn.close()
        return member_id

    def _create_session_and_booking(self, capacity_max=5):
        now = datetime.now(timezone.utc)
        session_id = booking_manager.create_session(
            {
                "title": "TEST Payment Flow",
                "starts_at": (now + timedelta(days=7)).isoformat(),
                "ends_at": (now + timedelta(days=7, hours=2)).isoformat(),
                "location": "TEST Local",
                "status": "open",
                "capacity_max": capacity_max,
                "price_krw": 50000,
                "payment_guide": "TEST 계좌는 운영자가 별도 확인합니다.",
            }
        )
        booking_id = booking_manager.create_booking(
            {
                "session_id": session_id,
                "member_id": "member-1",
                "applicant_name": "TEST",
                "phone_masked": "010-****-1234",
                "status": "requested",
                "payment_status": "not_sent",
                "payment_amount_krw": 50000,
            }
        )
        booking_manager.refresh_session_counts(session_id)
        return session_id, booking_id

    def _create_session(self, *, days=8, capacity_max=5, status="open", title="TEST Target Session"):
        now = datetime.now(timezone.utc)
        return booking_manager.create_session(
            {
                "title": title,
                "starts_at": (now + timedelta(days=days)).isoformat(),
                "ends_at": (now + timedelta(days=days, hours=2)).isoformat(),
                "location": "TEST Local",
                "status": status,
                "capacity_max": capacity_max,
                "price_krw": 50000,
            }
        )

    def test_send_payment_guide_sets_manual_copy_state(self):
        _, booking_id = self._create_session_and_booking()

        updated = booking_manager.send_payment_guide_state(booking_id)

        self.assertIsNotNone(updated)
        self.assertEqual(updated["status"], "payment_guide_sent")
        self.assertEqual(updated["payment_status"], "guide_sent")
        self.assertIn("[입금 안내]", updated["payment_note"])
        self.assertIn("TEST Payment Flow", updated["payment_note"])
        schedule_line = next(line for line in updated["payment_note"].splitlines() if line.startswith("일정:"))
        time_line = next(line for line in updated["payment_note"].splitlines() if line.startswith("시간:"))
        self.assertNotIn("T", schedule_line)
        self.assertNotIn("+", schedule_line)
        self.assertRegex(time_line, r"시간: (오전|오후) \d+시")

    def test_send_payment_guide_can_include_selected_account(self):
        _, booking_id = self._create_session_and_booking()

        updated = booking_manager.send_payment_guide_state(
            booking_id,
            payment_account={
                "label": "주계좌",
                "bank": "테스트은행",
                "number": "123-456",
                "holder": "아르센",
                "memo": "입금자명과 신청자명이 다르면 알려주세요.",
            },
        )

        self.assertIn("입금 계좌: 테스트은행 123-456", updated["payment_note"])
        self.assertIn("예금주: 아르센", updated["payment_note"])
        self.assertIn("계좌 메모: 입금자명과 신청자명이 다르면 알려주세요.", updated["payment_note"])

    def test_location_and_refund_guides_use_korean_schedule(self):
        _, booking_id = self._create_session_and_booking()
        booking_manager.send_payment_guide_state(booking_id)
        _, _, booking = booking_manager.confirm_payment_state(booking_id, "입금 확인")

        location_guide = booking_manager.default_location_guide(booking)
        refund_guide = booking_manager.default_refund_guide(booking)

        self.assertIn("[장소 안내]", location_guide)
        self.assertIn("TEST Local", location_guide)
        self.assertGreaterEqual(len(location_guide.splitlines()), 10)
        self.assertIn("\n\n예약 정보\n", location_guide)
        self.assertIn("\n\n오시기 전 확인\n", location_guide)
        self.assertIn("[예약 취소 및 환불 안내]", refund_guide)
        self.assertIn("환불 계좌", refund_guide)
        location_schedule = [
            line for line in location_guide.splitlines() if line.startswith(("일정:", "시간:"))
        ]
        refund_schedule = [
            line for line in refund_guide.splitlines() if line.startswith(("일정:", "시간:"))
        ]
        self.assertFalse(any("T" in line for line in location_schedule))
        self.assertFalse(any("T" in line for line in refund_schedule))

    def test_payment_guide_sent_still_counts_as_pending_booking(self):
        session_id, booking_id = self._create_session_and_booking()

        booking_manager.send_payment_guide_state(booking_id)

        session = booking_manager.get_session(session_id)
        listed = booking_manager.list_sessions(include_closed=True)
        listed_session = next(row for row in listed if row["id"] == session_id)
        self.assertEqual(session["requested_count"], 1)
        self.assertEqual(listed_session["requested_count"], 1)
        self.assertEqual(session["confirmed_booking_count"], 0)

    def test_confirm_payment_confirms_booking_and_session_count(self):
        session_id, booking_id = self._create_session_and_booking()
        booking_manager.send_payment_guide_state(booking_id)

        ok, message, booking = booking_manager.confirm_payment_state(
            booking_id,
            "운영자 수동 입금 확인",
        )
        session = booking_manager.get_session(session_id)

        self.assertTrue(ok)
        self.assertEqual(message, "입금 확인 및 예약 확정 완료")
        self.assertEqual(booking["status"], "confirmed")
        self.assertEqual(booking["payment_status"], "paid")
        self.assertEqual(session["confirmed_booking_count"], 1)

    def test_move_confirmed_paid_booking_keeps_payment_state_and_updates_counts(self):
        source_session_id, booking_id = self._create_session_and_booking()
        target_session_id = self._create_session(days=10, capacity_max=2)
        booking_manager.send_payment_guide_state(booking_id)
        ok, _, confirmed = booking_manager.confirm_payment_state(
            booking_id,
            "운영자 수동 입금 확인",
        )
        self.assertTrue(ok)
        self.assertEqual(confirmed["session_id"], source_session_id)

        moved_ok, message, moved = booking_manager.move_booking_to_session(
            booking_id,
            target_session_id,
            "입금 후 일정 변경",
        )
        source = booking_manager.get_session(source_session_id)
        target = booking_manager.get_session(target_session_id)

        self.assertTrue(moved_ok)
        self.assertEqual(message, "예약 일정을 이동했습니다.")
        self.assertEqual(moved["session_id"], target_session_id)
        self.assertEqual(moved["status"], "confirmed")
        self.assertEqual(moved["payment_status"], "paid")
        self.assertIsNotNone(moved["confirmed_at"])
        self.assertIn("[일정 이동] 입금 후 일정 변경", moved["payment_note"])
        self.assertEqual(source["active_booking_count"], 0)
        self.assertEqual(source["confirmed_booking_count"], 0)
        self.assertEqual(target["active_booking_count"], 1)
        self.assertEqual(target["confirmed_booking_count"], 1)

    def test_move_booking_rejects_full_target_without_losing_original_state(self):
        source_session_id, booking_id = self._create_session_and_booking()
        target_session_id = self._create_session(days=10, capacity_max=1)
        blocker_id = booking_manager.create_booking(
            {
                "session_id": target_session_id,
                "member_id": "member-2",
                "applicant_name": "TEST 2",
                "phone_masked": "010-****-5678",
                "status": "requested",
                "payment_status": "not_sent",
                "payment_amount_krw": 50000,
            }
        )
        booking_manager.refresh_session_counts(target_session_id)
        booking_manager.send_payment_guide_state(booking_id)
        booking_manager.confirm_payment_state(booking_id, "운영자 수동 입금 확인")

        moved_ok, message, moved = booking_manager.move_booking_to_session(
            booking_id,
            target_session_id,
            "자리 없는 일정 이동 시도",
        )
        original = booking_manager.get_booking(booking_id)
        target = booking_manager.get_session(target_session_id)

        self.assertFalse(moved_ok)
        self.assertIn("마감", message)
        self.assertEqual(moved["session_id"], source_session_id)
        self.assertEqual(original["session_id"], source_session_id)
        self.assertEqual(original["status"], "confirmed")
        self.assertEqual(original["payment_status"], "paid")
        self.assertEqual(target["active_booking_count"], 1)
        self.assertEqual(target["status"], "full")
        self.assertIsNotNone(booking_manager.get_booking(blocker_id))

    def test_confirm_payment_rejects_when_session_is_full(self):
        session_id, first_booking_id = self._create_session_and_booking(capacity_max=1)
        second_booking_id = booking_manager.create_booking(
            {
                "session_id": session_id,
                "member_id": "member-2",
                "applicant_name": "TEST 2",
                "phone_masked": "010-****-5678",
                "status": "requested",
                "payment_status": "not_sent",
                "payment_amount_krw": 50000,
            }
        )

        booking_manager.send_payment_guide_state(first_booking_id)
        first_ok, _, first_booking = booking_manager.confirm_payment_state(
            first_booking_id,
            "첫 번째 입금 확인",
        )
        booking_manager.send_payment_guide_state(second_booking_id)
        second_ok, message, second_booking = booking_manager.confirm_payment_state(
            second_booking_id,
            "두 번째 입금 확인",
        )
        session = booking_manager.get_session(session_id)

        self.assertTrue(first_ok)
        self.assertEqual(first_booking["status"], "confirmed")
        self.assertFalse(second_ok)
        self.assertEqual(message, "정원이 이미 마감되어 확정할 수 없습니다.")
        self.assertEqual(second_booking["status"], "payment_guide_sent")
        self.assertEqual(second_booking["payment_status"], "guide_sent")
        self.assertEqual(session["confirmed_booking_count"], 1)
        self.assertEqual(session["status"], "full")

    def test_session_acceptance_rejects_when_requested_booking_fills_capacity(self):
        session_id, _ = self._create_session_and_booking(capacity_max=1)

        session = booking_manager.get_session(session_id)
        ok, message = booking_manager.session_acceptance(session)

        self.assertFalse(ok)
        self.assertEqual(message, "이미 마감된 세션입니다.")
        self.assertEqual(session["active_booking_count"], 1)
        self.assertEqual(session["remaining_capacity"], 0)
        self.assertTrue(session["is_request_full"])
        self.assertEqual(session["status"], "full")

    def test_canceling_booking_releases_session_capacity(self):
        session_id, booking_id = self._create_session_and_booking(capacity_max=1)
        full_session = booking_manager.get_session(session_id)

        changed = booking_manager.set_booking_state(
            booking_id,
            status="canceled",
            payment_status="canceled",
            payment_note="TEST operator cancellation",
        )
        session = booking_manager.get_session(session_id)
        ok, message = booking_manager.session_acceptance(session)
        booking = booking_manager.get_booking(booking_id)

        self.assertEqual(full_session["status"], "full")
        self.assertTrue(changed)
        self.assertTrue(ok)
        self.assertEqual(message, "")
        self.assertEqual(booking["status"], "canceled")
        self.assertIsNotNone(booking["canceled_at"])
        self.assertEqual(session["active_booking_count"], 0)
        self.assertEqual(session["remaining_capacity"], 1)
        self.assertFalse(session["is_request_full"])
        self.assertEqual(session["status"], "open")

    def test_booking_lists_include_request_and_paid_rank(self):
        session_id, first_booking_id = self._create_session_and_booking(capacity_max=5)
        second_booking_id = booking_manager.create_booking(
            {
                "session_id": session_id,
                "member_id": "member-2",
                "applicant_name": "TEST 2",
                "phone_masked": "010-****-5678",
                "status": "requested",
                "payment_status": "not_sent",
                "payment_amount_krw": 50000,
            }
        )
        booking_manager.send_payment_guide_state(first_booking_id)
        booking_manager.confirm_payment_state(first_booking_id, "첫 번째 입금 확인")

        rows = {
            row["id"]: row
            for row in booking_manager.list_bookings(session_id=session_id)
        }
        member_rows = booking_manager.list_member_bookings("member-1")

        self.assertEqual(rows[first_booking_id]["request_rank"], 1)
        self.assertEqual(rows[first_booking_id]["paid_rank"], 1)
        self.assertEqual(rows[second_booking_id]["request_rank"], 2)
        self.assertIsNone(rows[second_booking_id]["paid_rank"])
        self.assertEqual(member_rows[0]["id"], first_booking_id)
        self.assertEqual(member_rows[0]["request_rank"], 1)
        self.assertEqual(member_rows[0]["paid_rank"], 1)


    def test_waitlisted_booking_has_waitlist_rank(self):
        """대기자(waitlisted) 상태 예약은 waitlist_rank를 가지고, 일반 예약은 None이어야 한다."""
        session_id, first_booking_id = self._create_session_and_booking(capacity_max=1)

        second_booking_id = booking_manager.create_booking(
            {
                "session_id": session_id,
                "member_id": "member-2",
                "applicant_name": "TEST 대기자1",
                "phone_masked": "010-****-5678",
                "status": "waitlisted",
                "payment_status": "not_sent",
                "payment_amount_krw": 50000,
            }
        )
        third_booking_id = booking_manager.create_booking(
            {
                "session_id": session_id,
                "member_id": "member-3",
                "applicant_name": "TEST 대기자2",
                "phone_masked": "010-****-9999",
                "status": "waitlisted",
                "payment_status": "not_sent",
                "payment_amount_krw": 50000,
            }
        )

        rows = {
            row["id"]: row
            for row in booking_manager.list_bookings(session_id=session_id)
        }

        # 일반 신청자는 waitlist_rank 없음
        self.assertIsNone(rows[first_booking_id]["waitlist_rank"])
        # 대기자 순서 확인
        self.assertEqual(rows[second_booking_id]["waitlist_rank"], 1)
        self.assertEqual(rows[third_booking_id]["waitlist_rank"], 2)
        # request_rank는 전체 활성 예약 기준 순번 부여
        self.assertEqual(rows[first_booking_id]["request_rank"], 1)
        self.assertEqual(rows[second_booking_id]["request_rank"], 2)
        self.assertEqual(rows[third_booking_id]["request_rank"], 3)

    def test_canceled_waitlisted_booking_excluded_from_waitlist_rank(self):
        """취소된 대기자는 waitlist_rank 계산에서 제외되어야 한다."""
        session_id, _ = self._create_session_and_booking(capacity_max=1)

        wait1_id = booking_manager.create_booking(
            {
                "session_id": session_id,
                "member_id": "member-2",
                "applicant_name": "TEST 대기1",
                "phone_masked": "010-****-0001",
                "status": "waitlisted",
                "payment_status": "not_sent",
                "payment_amount_krw": 50000,
            }
        )
        wait2_id = booking_manager.create_booking(
            {
                "session_id": session_id,
                "member_id": "member-3",
                "applicant_name": "TEST 대기2",
                "phone_masked": "010-****-0002",
                "status": "waitlisted",
                "payment_status": "not_sent",
                "payment_amount_krw": 50000,
            }
        )

        # 첫 번째 대기자 취소
        booking_manager.set_booking_state(wait1_id, status="canceled")

        rows = {
            row["id"]: row
            for row in booking_manager.list_bookings(session_id=session_id)
        }

        # 취소된 대기자는 waitlist_rank 없음 (waitlist_order CTE 제외 대상)
        self.assertEqual(rows[wait1_id]["status"], "canceled")
        self.assertIsNone(rows[wait1_id]["waitlist_rank"])
        # 남은 대기자는 waitlist_rank=1로 재배정
        self.assertEqual(rows[wait2_id]["waitlist_rank"], 1)

    def test_seed_default_sunday_sessions_uses_fixed_office_location(self):
        result = booking_manager.seed_default_sunday_sessions(weeks=1)
        sessions = booking_manager.list_sessions(include_closed=True)

        self.assertEqual(len(result["created"]), 3)
        self.assertEqual(result["updated"], [])
        self.assertEqual({row["location"] for row in sessions}, {"영등포시장역 사무실"})

    def test_seed_default_sunday_sessions_reopens_existing_same_time(self):
        result = booking_manager.seed_default_sunday_sessions(weeks=1)
        first_id = result["created"][0]
        ok = booking_manager.update_session(first_id, {"location": "서울 공유오피스", "status": "canceled"})

        second_result = booking_manager.seed_default_sunday_sessions(weeks=1)
        sessions = booking_manager.list_sessions(include_closed=True)
        first = booking_manager.get_session(first_id)

        self.assertTrue(ok)
        self.assertEqual(second_result["created"], [])
        self.assertEqual(second_result["updated"], [first_id])
        self.assertEqual(len(sessions), 3)
        self.assertEqual(first["status"], "open")
        self.assertEqual(first["location"], "영등포시장역 사무실")

    def test_delete_empty_session_succeeds(self):
        now = datetime.now(timezone.utc)
        session_id = booking_manager.create_session(
            {
                "title": "TEST Empty Session",
                "starts_at": (now + timedelta(days=9)).isoformat(),
                "ends_at": (now + timedelta(days=9, hours=2)).isoformat(),
                "location": "영등포시장역 사무실",
                "status": "draft",
            }
        )

        ok, message = booking_manager.delete_session(session_id)

        self.assertTrue(ok)
        self.assertEqual(message, "일정을 삭제했습니다.")
        self.assertIsNone(booking_manager.get_session(session_id))

    def test_delete_session_rejects_when_active_booking_exists(self):
        session_id, _ = self._create_session_and_booking()

        ok, message = booking_manager.delete_session(session_id)

        self.assertFalse(ok)
        self.assertIn("신청 또는 확정 예약이 남은 일정은 삭제할 수 없습니다", message)
        self.assertIsNotNone(booking_manager.get_session(session_id))

    def test_delete_session_with_only_canceled_bookings_succeeds(self):
        session_id, booking_id = self._create_session_and_booking()
        booking_manager.set_booking_state(booking_id, status="canceled", payment_status="not_sent")

        ok, message = booking_manager.delete_session(session_id)
        rows = booking_manager.list_bookings()
        booking = next(row for row in rows if row["id"] == booking_id)

        self.assertTrue(ok)
        self.assertIn("취소된 예약 기록 1건은 보관했습니다", message)
        self.assertIsNone(booking_manager.get_session(session_id))
        self.assertIsNone(booking["session_id"])

    def test_delete_booking_requires_inactive_status(self):
        _, booking_id = self._create_session_and_booking()

        ok, message, data = booking_manager.delete_booking(booking_id)

        self.assertFalse(ok)
        self.assertIn("먼저 취소", message)
        self.assertIsNotNone(data)
        self.assertIsNotNone(booking_manager.get_booking(booking_id))

    def test_delete_canceled_booking_removes_record_and_releases_view(self):
        session_id, booking_id = self._create_session_and_booking(capacity_max=1)
        booking_manager.set_booking_state(booking_id, status="canceled", payment_status="not_sent")

        ok, message, data = booking_manager.delete_booking(booking_id)
        session = booking_manager.get_session(session_id)

        self.assertTrue(ok)
        self.assertEqual(message, "예약 신청 기록을 삭제했습니다.")
        self.assertEqual(data["booking_id"], booking_id)
        self.assertIsNone(booking_manager.get_booking(booking_id))
        self.assertEqual(session["active_booking_count"], 0)

    def test_move_payment_guide_sent_booking_preserves_payment_state(self):
        """입금 안내 발송 후(미확정) 예약을 이동해도 payment_status가 유지되어야 한다."""
        source_session_id, booking_id = self._create_session_and_booking()
        target_session_id = self._create_session(days=10, capacity_max=3)
        booking_manager.send_payment_guide_state(booking_id)

        moved_ok, message, moved = booking_manager.move_booking_to_session(
            booking_id,
            target_session_id,
            "입금 안내 후 일정 변경",
        )
        source = booking_manager.get_session(source_session_id)
        target = booking_manager.get_session(target_session_id)

        self.assertTrue(moved_ok)
        self.assertEqual(moved["session_id"], target_session_id)
        self.assertEqual(moved["status"], "payment_guide_sent")
        self.assertEqual(moved["payment_status"], "guide_sent")
        self.assertIn("[일정 이동] 입금 안내 후 일정 변경", moved["payment_note"])
        self.assertEqual(source["active_booking_count"], 0)
        self.assertEqual(target["active_booking_count"], 1)

    def test_move_booking_appends_note_to_existing_payment_note(self):
        """기존 payment_note가 있는 예약을 이동할 때 이동 메모가 기존 메모 뒤에 추가되어야 한다."""
        source_session_id, booking_id = self._create_session_and_booking()
        target_session_id = self._create_session(days=10, capacity_max=3)
        booking_manager.send_payment_guide_state(booking_id)
        booking_manager.confirm_payment_state(booking_id, "1차 확인 메모")
        before_move = booking_manager.get_booking(booking_id)
        existing_note = before_move["payment_note"]

        moved_ok, _, moved = booking_manager.move_booking_to_session(
            booking_id,
            target_session_id,
            "2회차로 변경",
        )

        self.assertTrue(moved_ok)
        self.assertIn("[일정 이동] 2회차로 변경", moved["payment_note"])
        self.assertIn(existing_note, moved["payment_note"])

    def test_cancel_confirmed_paid_booking_preserves_existing_note(self):
        """입금확정 예약 취소 시 기존 payment_note가 유지되고 상태가 canceled로 변경되어야 한다."""
        session_id, booking_id = self._create_session_and_booking()
        booking_manager.send_payment_guide_state(booking_id)
        booking_manager.confirm_payment_state(booking_id, "운영자 수동 입금 확인")
        original = booking_manager.get_booking(booking_id)
        original_note = original["payment_note"]

        changed = booking_manager.set_booking_state(booking_id, status="canceled")
        booking = booking_manager.get_booking(booking_id)
        session = booking_manager.get_session(session_id)

        self.assertTrue(changed)
        self.assertEqual(booking["status"], "canceled")
        self.assertEqual(booking["payment_status"], "paid")
        self.assertEqual(booking["payment_note"], original_note)
        self.assertIsNotNone(booking["canceled_at"])
        self.assertEqual(session["active_booking_count"], 0)
        self.assertEqual(session["confirmed_booking_count"], 0)


    def test_move_booking_targets_exact_session_id_not_start_time(self):
        """동일 starts_at을 가진 두 세션이 있을 때, move_booking_to_session은
        세션 ID로 정확한 대상을 식별해야 한다."""
        now = datetime.now(timezone.utc)
        shared_start = (now + timedelta(days=14)).isoformat()
        shared_end = (now + timedelta(days=14, hours=2)).isoformat()

        source_session_id, booking_id = self._create_session_and_booking()
        booking_manager.send_payment_guide_state(booking_id)
        booking_manager.confirm_payment_state(booking_id, "운영자 수동 입금 확인")

        session_a_id = booking_manager.create_session(
            {
                "title": "TEST Same-Time A",
                "starts_at": shared_start,
                "ends_at": shared_end,
                "location": "장소 A",
                "status": "open",
                "capacity_max": 5,
                "price_krw": 50000,
            }
        )
        session_b_id = booking_manager.create_session(
            {
                "title": "TEST Same-Time B",
                "starts_at": shared_start,
                "ends_at": shared_end,
                "location": "장소 B",
                "status": "open",
                "capacity_max": 5,
                "price_krw": 50000,
            }
        )
        self.assertNotEqual(session_a_id, session_b_id)

        moved_ok, _, moved = booking_manager.move_booking_to_session(
            booking_id, session_a_id, "A 세션으로 이동"
        )
        session_a = booking_manager.get_session(session_a_id)
        session_b = booking_manager.get_session(session_b_id)

        self.assertTrue(moved_ok)
        self.assertEqual(moved["session_id"], session_a_id)
        self.assertNotEqual(moved["session_id"], session_b_id)
        self.assertEqual(session_a["active_booking_count"], 1)
        self.assertEqual(session_b["active_booking_count"], 0)
        self.assertEqual(moved["status"], "confirmed")
        self.assertEqual(moved["payment_status"], "paid")


if __name__ == "__main__":
    unittest.main()
