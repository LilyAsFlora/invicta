
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
  `-h, --help` — Show a help message and exit.
  `-o, --output-shifts` — Shows the shift keys needed to get from each plaintext to the ciphertext.

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

### Multi-word decryption with shift keys:
```
$ invicta decrypt --output-shifts "Zwddg, ogjdv!"
25 Axeeh, phkew!
24 Byffi, qilfx!
23 Czggj, rjmgy!
22 Dahhk, sknhz!
21 Ebiil, tloia!
20 Fcjjm, umpjb!
19 Gdkkn, vnqkc!
18 Hello, world! ← This one works!
17 Ifmmp, xpsme!
16 Jgnnq, yqtnf!
15 Khoor, zruog!
14 Lipps, asvph!
13 Mjqqt, btwqi!
12 Nkrru, cuxrj!
11 Olssv, dvysk!
10 Pmttw, ewztl!
9 Qnuux, fxaum!
8 Rovvy, gybvn!
7 Spwwz, hzcwo!
6 Tqxxa, iadxp!
5 Uryyb, jbeyq!
4 Vszzc, kcfzr!
3 Wtaad, ldgas!
2 Xubbe, mehbt!
1 Yvccf, nficu!
```

From thesee results, we can conclude the string "Hello, world!" was shifted by 18 characters to produce "Zwddg, ogjdv!".

