"""pii_masker 단위 테스트.

근거 spec: /Users/yoon/ai-tools/docs/reports/work_bus/2026-05-09_member_applicant_pii_masking_preimplementation_check_autoplan_164.md §4
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from agents.pii_masker import (  # noqa: E402
    mask_email,
    mask_location_to_grade,
    mask_name,
    mask_phone,
    sanitize_payment_note,
)


class MaskNameTest(unittest.TestCase):
    def test_korean_three_chars(self):
        self.assertEqual(mask_name("홍길동"), "홍**")

    def test_korean_one_char_preserved(self):
        self.assertEqual(mask_name("홍"), "홍")

    def test_korean_two_chars(self):
        self.assertEqual(mask_name("홍길"), "홍*")

    def test_korean_four_chars(self):
        self.assertEqual(mask_name("홍길동영"), "홍***")

    def test_english_with_space(self):
        self.assertEqual(mask_name("John Doe"), "J*** D**")

    def test_email_lookalike_input(self):
        self.assertEqual(mask_name("john@email.com"), "j*************")

    def test_empty_input(self):
        self.assertEqual(mask_name(""), "")
        self.assertEqual(mask_name(None), "")

    def test_strip_whitespace(self):
        self.assertEqual(mask_name("  홍길동  "), "홍**")


class MaskPhoneTest(unittest.TestCase):
    def test_dashed_canonical(self):
        self.assertEqual(mask_phone("010-1234-5678"), "010-****-5678")

    def test_no_dash_eleven_digits(self):
        self.assertEqual(mask_phone("01012345678"), "010-****-5678")

    def test_intl_with_country_code(self):
        self.assertEqual(mask_phone("+82-10-1234-5678"), "+82-10-****-5678")

    def test_space_separated(self):
        self.assertEqual(mask_phone("010 1234 5678"), "010-****-5678")

    def test_empty_input(self):
        self.assertEqual(mask_phone(""), "")
        self.assertEqual(mask_phone(None), "")

    def test_short_input_fallback(self):
        self.assertEqual(mask_phone("123"), "***-****-****")

    def test_partial_digits_keep_last_four(self):
        self.assertEqual(mask_phone("xy 5678"), "***-****-5678")


class MaskEmailTest(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(mask_email("holong@example.com"), "h*****@e******.com")

    def test_short_local_and_host(self):
        self.assertEqual(mask_email("a@b.com"), "a@b.com")

    def test_lowercase_normalization(self):
        self.assertEqual(mask_email("Holong@Example.COM"), "h*****@e******.com")

    def test_invalid_no_at(self):
        self.assertEqual(mask_email("not_an_email"), "")

    def test_empty_input(self):
        self.assertEqual(mask_email(""), "")
        self.assertEqual(mask_email(None), "")

    def test_subdomain_tld_preserved(self):
        self.assertEqual(mask_email("user@mail.co.kr"), "u***@m******.kr")


class SanitizePaymentNoteTest(unittest.TestCase):
    def test_account_number_dashed(self):
        self.assertIn("<ACCT>", sanitize_payment_note("계좌 1002-123-456789 송금"))

    def test_account_number_long_digit_run(self):
        self.assertIn("<ACCT>", sanitize_payment_note("123456789012345 ok"))

    def test_email_replaced(self):
        self.assertIn("<EMAIL>", sanitize_payment_note("hello@x.com 입금"))

    def test_phone_replaced(self):
        self.assertIn("<PHONE>", sanitize_payment_note("010-1234-5678 송금"))

    def test_token_bearer(self):
        self.assertIn("<TOKEN>", sanitize_payment_note("Bearer abcdef1234567890"))

    def test_token_sk_prefix(self):
        out = sanitize_payment_note("sk-1234567890abcdef0123 송금")
        self.assertIn("<TOKEN>", out)

    def test_length_truncation(self):
        text = "가" * 250
        out = sanitize_payment_note(text, max_len=200)
        self.assertTrue(out.endswith("..."))
        self.assertEqual(len(out), 203)

    def test_passthrough_clean_text(self):
        self.assertEqual(sanitize_payment_note("홍길동"), "홍길동")

    def test_empty_input(self):
        self.assertEqual(sanitize_payment_note(""), "")
        self.assertEqual(sanitize_payment_note(None), "")


class MaskLocationToGradeTest(unittest.TestCase):
    def test_district_extracted(self):
        self.assertEqual(mask_location_to_grade("서울 강남구 역삼동 12-3"), "강남")

    def test_dong_only(self):
        self.assertEqual(mask_location_to_grade("어쩌고동 1번 출구"), "어쩌고")

    def test_city(self):
        self.assertEqual(mask_location_to_grade("부산시 해운대 어딘가"), "부산")

    def test_empty_input(self):
        self.assertEqual(mask_location_to_grade(""), "")
        self.assertEqual(mask_location_to_grade(None), "")

    def test_no_match_returns_empty(self):
        self.assertEqual(mask_location_to_grade("Online Zoom Link"), "")


if __name__ == "__main__":
    unittest.main()
