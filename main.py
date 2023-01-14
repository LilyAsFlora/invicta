#!/usr/bin/env python3

import arguments
import cipher

def main():
    args = arguments.process_args()

    result = cipher.caesar_encrypt_text(args.text, args.shift)
    print(result)

if __name__ == "__main__":
	main()
