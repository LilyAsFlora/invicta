"""Functions for handling command line output."""

import cipher

def output_encryption(args):
    """Handles encryption output for the given arguments."""
    result = cipher.caesar_encrypt_text(args.text, args.shift)
    print(result)

def output_decryption(args):
    """Handles decryption output for the given arguments."""
    result = cipher.caesar_decrypt_text(args.text)

    for string in result:
        print(string)
