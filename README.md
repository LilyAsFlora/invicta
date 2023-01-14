# Invicta

A simple command line script for [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) encryption.

## Requirements

- [Python 3.11+](https://www.python.org/)

## Usage

```
invicta [-h] [-v] shift text
```
### Positional Arguments

`shift` —        The number of alphabet positions to shift letters by. This
                 value can be positive or negative, and will be rounded to the
                 nearest integer.
                 
`text` —         The plaintext to encrypt. Non-ASCII characters and whitespace
                 are preserved.

### Options
`-h, --help` — Show a help message and exit.

`-v, --version` —  Show the program's version number and exit.

## Examples

### Positive shift with spaces:

```
$ invicta 3 "Hello, world!"
Khoor, zruog!
```

### Negative shift with spaces:

```
$ invicta -2 "Hello, world!"
Fcjjm, umpjb!
```

### Shift greater than alphabet length:

```
$ invicta 28 "Hello, world!"
Jgnnq, yqtnf!
```

