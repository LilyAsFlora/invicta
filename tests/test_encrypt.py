"""Unit testing for encryption functionality."""

import unittest

import cipher

class TestEncrypt(unittest.TestCase):
    def test_encrypt_char_pos(self):
        """Positive single character encryption."""
        self.assertEqual(cipher.caesar_encrypt_char("a", 1), "b")

    def test_encrypt_char_neg(self):
        """Negative single character encryption."""
        self.assertEqual(cipher.caesar_encrypt_char("a", -1), "z")

    def test_encrypt_char_upper(self):
        """Uppercase character encryption."""
        self.assertEqual(cipher.caesar_encrypt_char("G", 3), "J")

    def test_encrypt_text_pos(self):
        """Positive text encryption."""
        self.assertEqual(cipher.caesar_encrypt_text("abc", 1), "bcd")

    def test_encrypt_test_neg(self):
        """Negative text encryption."""
        self.assertEqual(cipher.caesar_encrypt_text("abc", -1), "zab")

    def test_encrypt_text_upper(self):
        """Uppercase text encryption."""
        self.assertEqual(cipher.caesar_encrypt_text("FOO", 4), "JSS")

    def test_encrypt_text_round(self):
        """Test shift rounding."""
        self.assertEqual(cipher.caesar_encrypt_text("a", 1.2), "b")
