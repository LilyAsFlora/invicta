"""Command line argument processing for Invicta."""

import argparse

import _version

def process_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Encrypt text with the Caesar cipher."
    )

    subparsers = parser.add_subparsers(help="Sub-command help")

    encrypt = subparsers.add_parser("encrypt", help="Caesar encryption.")
    decrypt = subparsers.add_parser("decrypt", help="Caesar decryption.")

    parser.add_argument(
        "-v", "--version", action="version", 
        version=f"%(prog)s {_version.__version__}"
    )

    encrypt.add_argument(
        "shift", type=int, 
        help="The number of alphabet positions to shift letters by. This value \
              can be positive or negative, and will be rounded to the nearest \
              integer."
    )

    encrypt.add_argument(
        "text", type=str, 
        help="The plaintext to encrypt. Non-ASCII characters and whitespace \
              are preserved."
    )

    decrypt.add_argument(
        "text", type=str,
        help="The ciphertext to decrypt. Will output all possible solutions."
    )

    return parser.parse_args()
