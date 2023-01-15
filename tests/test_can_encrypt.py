"""Unit tests for validating Caesar encryption."""

import unittest

import cipher

class TestCanEncrypt(unittest.TestCase):
    def test_can_encrypt_valid(self):
        """Test for valid data."""
        self.assertTrue(cipher.can_caesar_encrypt("Hello, world!"))
