"""Functions for handling command line output."""

import argparse

import cipher

def output_encryption(args: argparse.Namespace) -> None:
    """Handles encryption output for the given arguments."""
    result = cipher.caesar_encrypt_text(args.text, args.shift)
    print(result)

def output_decryption(args: argparse.Namespace) -> None:
    """Handles decryption output for the given arguments."""
    result = cipher.caesar_decrypt_text(args.text)

    if not cipher.can_caesar_encrypt(args.text):
        return

    if args.output_shifts:
        for index, string in enumerate(result, 1):
            result[index - 1] = \
                f"{cipher.ALPHABET_LENGTH - index} {-index} {string}"

    for string in result:
        print(string)
