"""Unit tests for English checks."""

import unittest

import spellchecker

import english

class TestEnglish(unittest.TestCase):
    def setUp(self):
        self.spell_checker = spellchecker.SpellChecker()

    def test_is_english_word_true_for_english(self):
        test_word = "the"
        result = english.is_english_word(test_word, self.spell_checker)

        self.assertTrue(result)

    def test_is_english_word_false_for_non_english(self):
        test_word="q"
        result = english.is_english_word(test_word, self.spell_checker)

        self.assertFalse(result)

    def test_is_english_word_false_for_empty(self):
        empty_string = ""
        result = english.is_english_word(empty_string, self.spell_checker)

        self.assertFalse(result)