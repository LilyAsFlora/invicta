"""Command line argument processing for Invicta."""

import argparse

import _version

def process_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Encrypt text with the Caesar cipher."
    )

    parser.add_argument(
        "-v", "--version", action="version", 
        version=f"%(prog)s {_version.__version__}"
    )

    parser.add_argument(
        "shift", type=int, 
        help="The number of alphabet positions to shift letters by. This value \
              can be positive or negative, and will be rounded to the nearest \
              integer."
    )

    parser.add_argument(
        "text", type=str, 
        help="The plaintext to encrypt. Non-ASCII characters and whitespace \
              are preserved."
    )

    return parser.parse_args()
