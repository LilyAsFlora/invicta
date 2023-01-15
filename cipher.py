"""Caesar encryption."""

import string

import exceptions

ZERO_SHIFT = 65
ALPHABET_LENGTH = 26

def can_caesar_encrypt(text: str) -> bool:
    """Checks whether the given string can be modified with a Caesar cipher."""
    return any([(char in string.ascii_letters) for char in text]) \
        and text != ""

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
    """

    # Remember whether the input is lower or upper, so we can
    # return it this way.
    return_lower = True if char == char.lower() else False

    # Convert it to uppercase, as this corresponds with our zero shift.
    # For instance, 'A' here becomes 0.
    zero_shifted = ord(char.upper()) - ZERO_SHIFT

    # Apply the Caesar Cipher formula to find the desired ASCII code,
    # then convert it back to a character.
    encrypted_ascii = (zero_shifted + round(shift)) % ALPHABET_LENGTH
    encrypted_char = chr(encrypted_ascii + ZERO_SHIFT)

    if return_lower:
        return encrypted_char.lower()
    else:
        return encrypted_char

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

    for char in text:
        if char in string.ascii_letters:
            result += caesar_encrypt_char(char, shift)
        else:
            result += char

    return result

def caesar_decrypt_text(text: str) -> list[str]:
    """Decrypts the given Caesar ciphertext with brute force.

    Args:
        text (str): The text to decrypt.

    Returns:
        list[str]: A list of all possible plaintexts from the given cipher.
    """
    if not can_caesar_encrypt(text):
        raise exceptions.CannotCaesarEncryptException(
            f"String '{text}' could not have been encrypted with Caesar cipher."
        )

    result = []

    for i in range(1, ALPHABET_LENGTH):
        result.append(caesar_encrypt_text(text, i))

    return result
