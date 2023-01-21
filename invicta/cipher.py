"""Caesar encryption."""

import string

ALPHABET_LENGTH = 26

def can_caesar_encrypt(text: str) -> bool:
    """Checks whether the given string can be modified with a Caesar cipher.
    
    Returns `True` if any character in `text` is present in 
    `string.ascii_letters`."""
    for char in text:
        if char in string.ascii_letters:
            return True

    return False

def caesar_encrypt_char(char: str, shift: int) -> str:
    """
    Applies case-preserving Caesar cipher to the given character.

    Args:
        char (str): A string of length 1.
        shift (int): The number of alphabet positions to shift by. This value
        can be negative, and will be rounded to the nearest 
        integer.

    Returns:
        str: The resulting ciphertext.

    See the equation described in https://en.wikipedia.org/wiki/Caesar_cipher#Example.
    """

    ZERO_SHIFT = 65

    if not can_caesar_encrypt(char):
        return char

    # In this algorithm, we will use the following scheme:
    # A → 0, B → 1, C → 2, ...

    # Convert the plaintext to uppercase, as this corresponds with our scheme.
    char_upper = char.upper()

    # Subtract a fixed "zero shift" value from the char's ASCII value, to
    # enumerate it according to our scheme. For instance, "A" → 0.
    zero_shifted = ord(char_upper) - ZERO_SHIFT

    # Apply the Caesar Cipher formula to find the post-encryption ASCII value.
    # The modulo operation ensures no overflow occurs (i.e. a value over 26),
    # and allows a loop-back sort of encryption, such as Z forward to B by 
    # a shift of +3.
    zero_shifted_encrypted = (zero_shifted + round(shift)) % ALPHABET_LENGTH
    char_encrypted = chr(zero_shifted_encrypted + ZERO_SHIFT)

    if char.islower():
        return char_encrypted.lower()

    return char_encrypted

def caesar_encrypt_text(text: str, shift: int) -> str:
    """
    Applies Caesar cipher to the given string. Non-ascii characters and case
    are preserved.

    Args:
        text (str): The plaintext to encrypt.
        shift (int): The number of alphabet positions to shift by. This value
        can be negative.

    Returns:
        str: The resulting ciphertext.
    """
    result = ""

    # Yes, a map() or list comprehension is appropriate here, but I consider
    # this more readable.
    for char in text:
        result += caesar_encrypt_char(char, shift)

    return result

def caesar_decrypt_text(text: str) -> list[str]:
    """Decrypts the given Caesar ciphertext with brute force.

    Args:
        text (str): The text to decrypt.

    Returns:
        list[str]: A list of all possible plaintexts from the given cipher.
    """
    result = []

    # We only need 1 shift for each letter in the alphabet, as duplicates
    # will occur after this.
    for i in range(1, ALPHABET_LENGTH):
        result.append(caesar_encrypt_text(text, i))

    return result
