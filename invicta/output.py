"""Functions for handling command line output."""

import argparse

import spellchecker

from . import cipher, english


def output_encryption(args: argparse.Namespace) -> None:
    """Handles encryption output for the given arguments."""
    result = cipher.caesar_encrypt_text(args.text, args.shift)

    print(result)


def output_decryption(args: argparse.Namespace) -> None:
    """Handles decryption output for the given arguments."""
    if not cipher.can_caesar_encrypt(args.text):
        return

    plaintexts = cipher.caesar_decrypt_text(args.text)

    # -o, --output-shifts
    if args.output_shifts:
        for position, plaintext in enumerate(plaintexts, 1):
            pos_shift_to_encrypt = cipher.ALPHABET_LENGTH - position
            neg_shift_to_encrypt = -position

            plaintexts[position - 1] = f"{pos_shift_to_encrypt} {neg_shift_to_encrypt} {plaintext}"

    # -e, --english
    if args.english:
        spell_checker = spellchecker.SpellChecker()

        plaintexts = [
            string for string in plaintexts if english.contains_english(
                string, spell_checker
            )
        ]

    for string in plaintexts:
        print(string)


