"""This module contains functions for English checks in Invicta."""

import string

from spellchecker import SpellChecker

def strip_to_ascii_letters(initial_string: str) -> str:
    """Removes all non-ASCII-letter characters in a string.

    More precisely, this function returns a new `str` stripped of any
    characters that do not occur in `string.ascii_letters`. All whitespace
    is preserved.
    """
    result = ""

    for char in initial_string:
        if (char in string.ascii_letters) or (char.isspace()):
            result += char

    return result

def is_english_word(word: str, checker: SpellChecker) -> bool:
    """Returns `True` if the given word exists in the English dictionary.
    
    Note that a 'word' is defined here as a sequence of whitespace-separated 
    ASCII characters; this includes alphanumerics. Thus, if `word` contains
    several words, this will return `False`.
    
    Args:
        word: A string to test. 
        checker: An instance of pyspellchecker.Spellchecker
    """
    sanitised_word = word.lower().strip()

    return sanitised_word in checker.known([sanitised_word])

def contains_english(string: str, checker: SpellChecker) -> bool:
    """Returns `True` if the given string contains a word that exists in the
    English dictionary.
    
    See `is_english_word` for the definition of a `word`.

    Args:
        word: A string to test. This does not have to be pre-sanitised.
        checker: An instance of pyspellchecker.Spellchecker
    """
    words = string.split(" ")

    return any([is_english_word(word.strip()) for word in words])
