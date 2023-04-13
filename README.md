# Python Crytography CLI

A simple CLI tool for encrypting and decrypting files and strings using python cryptography.

## Installation

### Requirements

- Python 3.6 or higher
- Pip
- Git
- GNUPG (for GPG)

### Install

```console
$ git clone https://github.com/LostAndDead/python-cryptography-cli.git
$ cd python-cryptography-cli
$ pip install -r requirements.txt
```

## Usage
```console
index.py [-h] (-encrypt | -decrypt | -generate) [-algorithm {fernet,rsa,aes,gpg}] [-verbose] [--input INPUT | --inputFile INPUTFILE] [--output | --outputFile OUTPUTFILE] [--key KEY] [--passphrase PASSPHRASE]

options:
  -h, --help            show this help message and exit
  -encrypt, -en         Encrypt the given input
  -decrypt, -de         Decrypt the given input
  -generate, -gen       Generate a key for the given algorithm
  -algorithm {fernet,rsa,aes,gpg}, -alg {fernet,rsa,aes,gpg}
                        Define the algorithm used
  -verbose, -v          Gain additional information
  --input INPUT, --i INPUT
                        An input string
  --inputFile INPUTFILE, --if INPUTFILE
                        Path to an input file
  --output, --o         Output to console
  --outputFile OUTPUTFILE, --of OUTPUTFILE
                        Path to an output file
  --key KEY, --k KEY    The key file to use/save as (ignoring file extensions)
  --passphrase PASSPHRASE, --p PASSPHRASE
                        The passphrase to use (if required), if not provided you will be prompted for one.
  --keyRing KEYRING, --kr KEYRING
                        Path to the key ring to use (for GPG only)
```

## Algorithms
The following algorithms are supported:

- Fernet
- RSA (see below)
- AES
- GPG (see below)

## RSA
Due to how RSA stores data and bytes outside of the normal UTF-8 encodable range many of the values cant be displayed as a string. This means that when using RSA you cant output the encrypted data to the console or enter it via the command line. You must use files for these operations.

## GPG
GPG is a little different to the other algorithms as it uses a keyring instead of a single key file. The keyring must be managed by a GPG agent such as GPGTools for Mac or GPG4Win for Windows. (https://gnupg.org/download/) You must download one of these agents and install it before GPG will work. The program should be able to find the keyring automatically, but if it can't you can specify the path to the keyring location using the `--keyring` argument.

## Example commands
Bellow are several example commands showcasing how you can use each of the different algorithums and IO methods.

For this example we have a `io` folder for the files and an `keys` folder for the keys

### Generate a Fernet Key
```console
$ py .\index.py -gen -algo 'fernet' --key '.\keys\fernetKey'
```

### Encrypt a file using Fernet
```console
$ py .\index.py -en -algo 'fernet' --inputFile '.\io\secret.txt' --outputFile '.\io\fernetOut.txt' --key '.\keys\fernetKey'
```

### Decrypt a file using Fernet
```console
$ py .\index.py -de -algo 'fernet' --inputFile '.\io\fernetOut.txt' --outputFile '.\io\fernetDecrypt.txt' --key '.\keys\fernetKey'
```

### Encrypt a string using RSA
```console
$ py .\index.py -en -algo 'rsa' --input 'super secret message' --output --key '.\keys\rsaKey'
```

### Decrypt a string using AES
```console
$ py .\index.py -de -v -algo 'aes' --inputFile '.\io\aesOut.txt' --outputFile '.\io\aesDecrypt.txt' --key '.\keys\aesKey'
```