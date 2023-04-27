import os

from cryptography.fernet import Fernet


class FERNET: 

    def __init__(self, main):
        self.main = main

    def generate_key(self, args):
        print("Generating key for " + args.algorithm + " algorithm")
        # Fernet
        if (args.algorithm == 'fernet'):
            key = Fernet.generate_key()

            self.main.verboseLog("Key: \n" + key.decode('utf-8'))

            with open(args.key + '.key', 'wb') as key_file:
                key_file.write(key)
                print("Key saved to " + args.key)
    
    def encrypt(self, args):
        # Check if key exists
        if(not os.path.isfile(args.key + '.key')):
            print("Key file not found")
            exit(1)

        # Read key
        with open(args.key + '.key', 'rb') as key_file:
            key = key_file.read()

            # Load ferent with key
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

            # Load ferent with key
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