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

    def test_encrypt_text_neg(self):
        """Negative text encryption."""
        self.assertEqual(cipher.caesar_encrypt_text("abc", -1), "zab")

    def test_encrypt_text_upper(self):
        """Uppercase text encryption."""
        self.assertEqual(cipher.caesar_encrypt_text("FOO", 4), "JSS")

    def test_encrypt_text_round(self):
        """Test shift rounding."""
        self.assertEqual(cipher.caesar_encrypt_text("a", 1.2), "b")

    def test_encrypt_empty(self):
        """Test encryption for an empty string."""
        self.assertEqual(cipher.caesar_encrypt_text("", 17), "")

    def test_encrypt_non_ascii(self):
        """Test encryption for non-ASCII characters."""
        test_data = "→⁷∴°"

        self.assertEqual(cipher.caesar_encrypt_text(test_data, 14), test_data)

    def test_encrypt_control(self):
        """Test encryption for control characters."""
        test_data = "\x16\x1E\x7F"

        self.assertEqual(cipher.caesar_encrypt_text(test_data, 15), test_data)