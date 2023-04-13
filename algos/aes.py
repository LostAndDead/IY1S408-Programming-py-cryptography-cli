import base64
import getpass
import os
import random
import string

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class AES:

    def __init__(self, main):
        self.main = main

    def generate_key(self, args):
        if (args.passphrase):
            password = args.passphrase.encode('utf-8')
        else:
            print("RSA key generation requires a passphrase. This passphrase is not needed to decrypt or encrypt, but is required to generate the key.")
            randomize = input("Randomize passphrase? (y/n): ")
            if (randomize == 'y'):
                characters = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(characters) for i in range(8)).encode('utf-8')
            else:
                password = getpass.getpass("Key: ").encode('utf-8')

        salt = os.urandom(16)

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )

        key = base64.urlsafe_b64encode(kdf.derive(password))

        self.main.verboseLog("Random Key: \n" + key.decode('utf-8'))

        with open(args.key + '.key', 'wb') as key_file:
            key_file.write(key)
            print("Key saved to " + args.key)
    
    def encrypt(self, args):
        # Check if key exists
        if (not os.path.isfile(args.key + '.key')):
            print("Key file not found")
            exit(1)

        # Read key
        with open(args.key + '.key', 'rb') as key_file:
            key = key_file.read()

            # Load aes with key
            fernet = Fernet(key)
            if (args.input):
                print("Encrypting " + args.input + " with " + args.algorithm + " algorithm")
                encrypted = fernet.encrypt(args.input.encode('utf-8'))
                self.main.verboseLog("Encrypted: \n" + encrypted.decode('utf-8'))
                if (args.outputFile):
                    with open(args.outputFile, 'wb') as output_file:
                        output_file.write(encrypted)
                        print("Encrypted saved to " + args.outputFile)
                else:
                    print(encrypted.decode('utf-8'))
            elif (args.inputFile):

                # Check if input file exists
                if (not os.path.isfile(args.inputFile)):
                    print("Input file not found")
                    exit(1)
                print("Encrypting " + args.inputFile + " with " + args.algorithm + " algorithm")

                # Read input file
                with open(args.inputFile, 'rb') as input_file:
                    input = input_file.read()
                    encrypted = fernet.encrypt(input)
                    self.main.verboseLog("Encrypted: \n" + encrypted.decode('utf-8'))
                    if (args.outputFile):
                        with open(args.outputFile, 'wb') as output_file:
                            output_file.write(encrypted)
                            print("Encrypted saved to " + args.outputFile)
                    else:
                        print(encrypted.decode('utf-8'))
    
    def decrypt(self, args):
        # Check if key exists
        if (not os.path.isfile(args.key + '.key')):
            print("Key file not found")
            exit(1)

        # Read key
        with open(args.key + '.key', 'rb') as key_file:
            key = key_file.read()

            # Load aes with key
            fernet = Fernet(key)
            if (args.input):
                print("Decrypting " + args.input + " with " + args.algorithm + " algorithm")
                # Decrypt input
                decrypted = fernet.decrypt(args.input.encode('utf-8'))
                self.main.verboseLog("Decrypted: \n" + decrypted.decode('utf-8'))
                # Save decrypted to file
                if (args.outputFile):
                    with open(args.outputFile, 'wb') as output_file:
                        output_file.write(decrypted)
                        print("Decrypted saved to " + args.outputFile)
                # Print decrypted
                else:
                    print(decrypted.decode('utf-8'))
            elif (args.inputFile):
                # Check if input file exists
                if (not os.path.isfile(args.inputFile)):
                    print("Input file not found")
                    exit(1)
                print("Decrypting " + args.inputFile + " with " + args.algorithm + " algorithm")

                # Read input file
                with open(args.inputFile, 'rb') as input_file:
                    input = input_file.read()
                    # Decrypt input
                    decrypted = fernet.decrypt(input)
                    self.main.verboseLog("Decrypted: \n" + decrypted.decode('utf-8'))
                    # Save decrypted to file
                    if (args.outputFile):
                        with open(args.outputFile, 'wb') as output_file:
                            output_file.write(decrypted)
                            print("Decrypted saved to " + args.outputFile)
                    # Print decrypted
                    else:
                        print(decrypted.decode('utf-8'))