import os

import rsa


class RSA: 

    def __init__(self, main):
        self.main = main
    
    def generate_key(self, args):
        (pubkey, privkey) = rsa.newkeys(512)

        self.main.verboseLog("Public key: \n" + pubkey.save_pkcs1().decode('utf-8'))
        self.main.verboseLog("Private key: \n" + privkey.save_pkcs1().decode('utf-8'))

        with open(args.key + '.private', 'wb') as priv_file:
            priv_file.write(privkey.save_pkcs1())
            print("Private key saved to " + args.key + '.private')

        with open(args.key + '.public', 'wb') as pub_file:
            pub_file.write(pubkey.save_pkcs1())
            print("Public key saved to " + args.key + '.public')
    
    def encrypt(self, args):
        # Check if key exists
        if (not os.path.isfile(args.key + '.public')):
            print("Key file not found")
            exit(1)

        # Read key
        with open(args.key + '.public', 'rb') as key_file:
            key = key_file.read()

            # Load rsa with key
            pubkey = rsa.PublicKey.load_pkcs1(key)
            if (args.input):
                print("Encrypting " + args.input + " with " + args.algorithm + " algorithm")
                encrypted = rsa.encrypt(args.input.encode('utf-8'), pubkey)
                self.main.verboseLog("Encrypted: \n" + str(encrypted, errors='ignore'))
                if (args.outputFile):
                    with open(args.outputFile, 'wb') as output_file:
                        output_file.write(encrypted)
                        print("Encrypted saved to " + args.outputFile)
                else:
                    print('RSA stores data outside of the normal UTF-8 encodable range, so it cannot be printed to the console. Please use the --outputFile option to save the encrypted data to a file.')
            elif (args.inputFile):

                # Check if input file exists
                if (not os.path.isfile(args.inputFile)):
                    print("Input file not found")
                    exit(1)
                print("Encrypting " + args.inputFile + " with " + args.algorithm + " algorithm")

                # Read input file
                with open(args.inputFile, 'rb') as input_file:
                    input = input_file.read()
                    encrypted = rsa.encrypt(input, pubkey)
                    self.main.verboseLog("Encrypted: \n" + input.decode('utf-8'))
                    if (args.outputFile):
                        with open(args.outputFile, 'wb') as output_file:
                            output_file.write(encrypted)
                            print("Encrypted saved to " + args.outputFile)
                    else:
                        print(encrypted.decode('utf-8'))
        
    def decrypt(self, args):
        # Check if key exists
        if (not os.path.isfile(args.key + '.private')):
            print("Key file not found")
            exit(1)

        # Read key
        with open(args.key + '.private', 'rb') as key_file:
            key = key_file.read()

            # Load rsa with key
            privkey = rsa.PrivateKey.load_pkcs1(key)
            if (args.input):
                print ("String decryption not supported for RSA. Please use the --inputFile option to specify an input file.")
                exit(1)
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
                    decrypted = rsa.decrypt(input, privkey)
                    self.main.verboseLog("Decrypted: \n" + decrypted.decode('utf-8'))
                    # Save decrypted to file
                    if (args.outputFile):
                        with open(args.outputFile, 'wb') as output_file:
                            output_file.write(decrypted)
                            print("Decrypted saved to " + args.outputFile)
                    # Print decrypted
                    else:
                        print(decrypted.decode('utf-8'))