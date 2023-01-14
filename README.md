
# Invicta

A fun little command line utility for [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) encryption and decryption.

## Requirements

- [Python 3.11+](https://www.python.org/)

## Usage
```
invicta [-h] [-v] {encrypt,decrypt} ...
```

#### Global Options
`-h, --help` — Show a help message and exit.

`-v, --version` —  Show the program's version number and exit.

### Encryption
```
invicta encrypt [-h] shift text
```

#### Positional Arguments

`shift` —        The number of alphabet positions to shift letters by. This
                 value can be positive or negative, and will be rounded to the
                 nearest integer.
                 
`text` —         The plaintext to encrypt. Non-ASCII characters and whitespace
                 are preserved.

### Decryption

Here, decryption is done with a brute-force approach, leaving it up to the user to interpret the results.

```
invicta decrypt [-h] text
```
#### Positional Arguments
`text` — The ciphertext to decrypt. Will output all possible solutions.

#### Options
  `-h, --help`  Show a help message and exit.

## Encryption Examples

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

## Decryption Examples

### Multi-word decryption:
```
$ invicta decrypt "Zwddg, ogjdv!"
Axeeh, phkew!
Byffi, qilfx!
Czggj, rjmgy!
Dahhk, sknhz!
Ebiil, tloia!
Fcjjm, umpjb!
Gdkkn, vnqkc!
Hello, world! ← This one works!
Ifmmp, xpsme!
Jgnnq, yqtnf!
Khoor, zruog!
Lipps, asvph!
Mjqqt, btwqi!
Nkrru, cuxrj!
Olssv, dvysk!
Pmttw, ewztl!
Qnuux, fxaum!
Rovvy, gybvn!
Spwwz, hzcwo!
Tqxxa, iadxp!
Uryyb, jbeyq!
Vszzc, kcfzr!
Wtaad, ldgas!
Xubbe, mehbt!
Yvccf, nficu!
```

