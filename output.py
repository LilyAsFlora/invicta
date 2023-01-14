"""Functions for handling command line output."""

import cipher

def output_encryption(args):
    result = cipher.caesar_encrypt_text(args.text, args.shift)
    print(result)

def output_decryption(args):
    result = cipher.caesar_decrypt_text(args.text)

    for string in result:
        print(string)
