"""Unit tests for validating Caesar encryption."""

import unittest

import cipher

class TestCanEncrypt(unittest.TestCase):
    def test_can_encrypt_true(self):
        """Test for valid encryptable data."""
        self.assertTrue(cipher.can_caesar_encrypt("Hello, world!"))

    def test_can_encrypt_false(self):
        """Test for valid non-encryptable data."""
        self.assertFalse(cipher.can_caesar_encrypt("293847"))

    def test_can_encrypt_empty(self):
        """Test for an empty string."""
        self.assertFalse(cipher.can_caesar_encrypt(""))

    def test_can_encrypt_control(self):
        """Test for a string containing control characters."""
        self.assertFalse(cipher.can_caesar_encrypt("\x01\x13\x07"))

    def test_can_encrypt_multi(self):
        """Test on a string containing encryptable and non-encryptable 
        characters."""
        self.assertTrue(cipher.can_caesar_encrypt("Hello 02384029384"))
