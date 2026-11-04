#!/usr/bin/env python3
"""Unit tests for ARSEN Meta Multi-LLM Publisher & Ledger (scripts/meta_publisher.py)."""

import os
import shutil
import tempfile
import unittest

from scripts.meta_publisher import (
    AntigravityGuard,
    ClaudeCopywriter,
    CodexPublisher,
    FormattedPost,
    MetaLedger,
    MetaPublisherConfig,
    OrcaMetaOrchestrator,
    Platform,
    PublishReceipt,
    PublishRequest,
    PublishStatus,
)


class TestMetaPublisher(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.test_dir, "test_meta_ledger.db")
        self.config = MetaPublisherConfig(
            db_path=self.db_path,
            daily_ig_limit=2,
            daily_threads_limit=5,
            dry_run=True,
        )
        self.ledger = MetaLedger(self.db_path)

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_ledger_initialization_and_recording(self):
        """SQLite 원장 초기화 및 발행 기록/카운트 검증."""
        self.assertEqual(self.ledger.get_daily_count(Platform.INSTAGRAM), 0)
        self.assertEqual(self.ledger.get_daily_count(Platform.THREADS), 0)

        # 1건 기록
        row_id = self.ledger.record_publication(
            platform=Platform.THREADS,
            post_type="TEXT",
            text="테스트 포스트",
            media_url=None,
            post_id="post_123",
            container_id="cnt_123",
            status=PublishStatus.PUBLISHED,
        )
        self.assertGreater(row_id, 0)
        self.assertEqual(self.ledger.get_daily_count(Platform.THREADS), 1)
        self.assertEqual(self.ledger.get_daily_count(Platform.INSTAGRAM), 0)

    def test_claude_copywriter_formatting(self):
        """클로드 플랫폼별 카피라이팅 및 훅 생성 검증."""
        copywriter = ClaudeCopywriter()

        # 인스타그램 포맷 검증
        ig_req = PublishRequest(
            platform=Platform.INSTAGRAM,
            raw_content="AI 에이전트 자동화의 미래\n실전 엔터프라이즈 파이프라인 구축법",
            tags=["AI", "개발일지"],
        )
        ig_post = copywriter.format_for_platform(ig_req)
        self.assertIn("📌", ig_post.formatted_text)
        self.assertIn("#AI", ig_post.formatted_text)
        self.assertEqual(ig_post.hook_summary, "AI 에이전트 자동화의 미래")

        # 쓰레드 포맷 검증
        th_req = PublishRequest(
            platform=Platform.THREADS,
            raw_content="오늘 오르카 멀티에이전트 오케스트레이션을 배포했습니다.\n코덱스, 클로드, 안티그래비티 3개 모델이 완벽히 분업합니다.",
        )
        th_post = copywriter.format_for_platform(th_req)
        self.assertIn("여러분의 파이프라인 구성 방식은 어떤가요?", th_post.formatted_text)
        self.assertEqual(th_post.media_type, "TEXT")

    def test_antigravity_guard_secret_and_pii_detection(self):
        """안티그래비티 보안 가드: 시크릿 및 PII 차단 검증."""
        guard = AntigravityGuard(self.ledger, self.config)

        # 정상 게시물
        clean_post = FormattedPost(
            platform=Platform.THREADS,
            formatted_text="정상적인 개발 일지 본문입니다.",
            hook_summary="정상",
        )
        is_safe, violations = guard.audit_and_protect(clean_post)
        self.assertTrue(is_safe)
        self.assertEqual(len(violations), 0)

        # 슬랙 토큰 유출 시도 (테스트용 합성 토큰)
        dummy_slack_token = "xoxb-" + "9" * 11 + "-" + "8" * 11 + "-" + "z" * 24
        leaked_post = FormattedPost(
            platform=Platform.THREADS,
            formatted_text=f"여기 슬랙 토큰 {dummy_slack_token} 입니다.",
            hook_summary="유출",
        )
        is_safe, violations = guard.audit_and_protect(leaked_post)
        self.assertFalse(is_safe)
        self.assertTrue(any("Slack Token" in v for v in violations))

        # 전화번호 PII 유출 시도
        pii_post = FormattedPost(
            platform=Platform.INSTAGRAM,
            formatted_text="문의는 010-1234-5678 로 연락주세요.",
            hook_summary="전화번호",
        )
        is_safe, violations = guard.audit_and_protect(pii_post)
        self.assertFalse(is_safe)
        self.assertTrue(any("휴대폰 번호 PII" in v for v in violations))

    def test_circuit_breaker_enforcement(self):
        """서킷브레이커: 일일 안전 상한(IG: 2건, Threads: 5건) 초과 시 차단 검증."""
        guard = AntigravityGuard(self.ledger, self.config)

        # 인스타그램 2건 발행 기록 (상한 도달)
        for i in range(2):
            self.ledger.record_publication(
                platform=Platform.INSTAGRAM,
                post_type="IMAGE",
                text=f"게시물 {i}",
                media_url="http://img.com",
                post_id=f"p_{i}",
                container_id=f"c_{i}",
                status=PublishStatus.PUBLISHED,
            )

        post = FormattedPost(
            platform=Platform.INSTAGRAM,
            formatted_text="3번째 인스타 게시 시도",
            hook_summary="3번째",
        )
        is_safe, violations = guard.audit_and_protect(post)
        self.assertFalse(is_safe)
        self.assertTrue(any("서킷브레이커" in v for v in violations))

    def test_orca_orchestrator_pipeline_e2e_dry_run(self):
        """오르카 오케스트레이터 전체 파이프라인 E2E 모의 실행 검증."""
        orchestrator = OrcaMetaOrchestrator(self.config)

        # 1. 쓰레드 발행 요청
        req = PublishRequest(
            platform=Platform.THREADS,
            raw_content="오르카 오케스트레이션 기반 쓰레드 자동화 1호 포스팅입니다.",
        )
        receipt = orchestrator.execute_pipeline(req)

        self.assertEqual(receipt.status, PublishStatus.PUBLISHED)
        self.assertIsNotNone(receipt.post_id)
        self.assertIn("mock_post_threads", receipt.post_id)
        self.assertEqual(orchestrator.ledger.get_daily_count(Platform.THREADS), 1)

        # 2. 인스타그램 발행 요청
        ig_req = PublishRequest(
            platform=Platform.INSTAGRAM,
            raw_content="오르카 오케스트레이션 기반 인스타그램 카드뉴스 1호",
            media_url="https://arsen.ai/assets/cardnews_01.jpg",
        )
        ig_receipt = orchestrator.execute_pipeline(ig_req)

        self.assertEqual(ig_receipt.status, PublishStatus.PUBLISHED)
        self.assertIsNotNone(ig_receipt.post_id)
        self.assertEqual(orchestrator.ledger.get_daily_count(Platform.INSTAGRAM), 1)


if __name__ == "__main__":
    unittest.main()
