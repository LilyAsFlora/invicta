"""Unit testing for encryption functionality."""

import unittest

import cipher

class TestCaesarEncrypt(unittest.TestCase):
    def test_caesar_encrypt_positive_char(self):
        self.assertEqual(cipher.caesar_encrypt_char("a", 1), "b")

    def test_caesar_encrypt_negative_char(self):
        self.assertEqual(cipher.caesar_encrypt_char("a", -1), "z")

    def test_caesar_encrypt_char_upper_preserves_case(self):
        self.assertEqual(cipher.caesar_encrypt_char("G", 3), "J")

    def test_caesar_encrypt_positive_text(self):
        self.assertEqual(cipher.caesar_encrypt_text("abc", 1), "bcd")

    def test_caesar_encrypt_negative_text(self):
        self.assertEqual(cipher.caesar_encrypt_text("abc", -1), "zab")

    def test_caesar_encrypt_text_upper_preserves_case(self):
        self.assertEqual(cipher.caesar_encrypt_text("FOO", 4), "JSS")

    def test_caesar_encrypt_fractional_shift_is_rounded(self):
        self.assertEqual(cipher.caesar_encrypt_text("a", 1.2), "b")

    def test_caesar_encrypt_empty_string_returns_empty(self):
        self.assertEqual(cipher.caesar_encrypt_text("", 17), "")

    def def_test_caesar_encrypt_non_ascii_chars_preserved(self):
        test_data = "→⁷∴°"

        self.assertEqual(cipher.caesar_encrypt_text(test_data, 14), test_data)

    def test_caesar_encrypt_control_chars_preserved(self):
        test_data = "\x16\x1E\x7F"

        self.assertEqual(cipher.caesar_encrypt_text(test_data, 15), test_data)
