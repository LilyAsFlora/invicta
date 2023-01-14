"""Unit tests for Caesar decryption."""

import unittest

import cipher

class TestDecrypt(unittest.TestCase):
    def test_decrypt_single(self):
        """Test for a single word."""
        encrypted = cipher.caesar_encrypt_text("foo", 16)

        self.assertIn("foo", cipher.caesar_decrypt_text(encrypted))

    def test_decrypt_multi(self):
        """Test for multiple words."""
        encrypted = cipher.caesar_encrypt_text("Hello, world!", 25)

        self.assertIn("Hello, world!", cipher.caesar_decrypt_text(encrypted))
