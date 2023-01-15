"""Unit tests for validating Caesar encryption."""

import unittest

import cipher

class TestCanEncrypt(unittest.TestCase):
    def test_can_encrypt_true(self):
        """Test for valid encryptable data."""
        self.assertTrue(cipher.can_caesar_encrypt("Hello, world!"))
