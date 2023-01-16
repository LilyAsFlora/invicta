"""This module contains functions for English checks in Invicta."""

from spellchecker import SpellChecker

def is_english_word(word: str, checker: SpellChecker) -> bool:
    """Returns `True` if the given word exists in the English dictionary.
    
    Note that a 'word' is defined here as a sequence of whitespace-separated 
    ASCII characters; this includes alphanumerics. Thus, if `word` contains
    several words, this will return `False`.
    
    Args:
        word: A string to test. This does not have to be pre-sanitised.
        checker: An instance of pyspellchecker.Spellchecker
    """
    return word.lower().strip() in checker.known([word.lower().strip()])

def contains_english(string: str, checker: SpellChecker) -> bool:
    """Returns `True` if the given string contains a word that exists in the
    English dictionary.
    
    See `is_english_word` for the definition of a `word`.

    Args:
        word: A string to test. This does not have to be pre-sanitised.
        checker: An instance of pyspellchecker.Spellchecker
    """
    return any(
        [is_english_word(word.strip(), checker) for word in string.split(" ")]
    )
