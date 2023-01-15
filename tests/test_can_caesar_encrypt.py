"""Unit tests for validating Caesar encryption."""

import unittest

import cipher

class TestCanCaesarEncrypt(unittest.TestCase):
    def test_can_caesar_encrypt_valid_returns_true(self):
        self.assertTrue(cipher.can_caesar_encrypt("Hello, world!"))

    def test_can_encrypt_invalid_returns_false(self):
        self.assertFalse(cipher.can_caesar_encrypt("293847"))

    def test_can_encrypt_empty_returns_false(self):
        self.assertFalse(cipher.can_caesar_encrypt(""))

    def test_can_encrypt_control_returns_false(self):
        self.assertFalse(cipher.can_caesar_encrypt("\x01\x13\x07"))

    def test_can_encrypt_multi_returns_true(self):
        self.assertTrue(cipher.can_caesar_encrypt("Hello 02384029384"))
