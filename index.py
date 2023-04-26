import argparse

from algos.aes import AES
from algos.fernet import FERNET
from algos.gpg import GPG
from algos.rsa import RSA

parser = argparse.ArgumentParser()

# Add mutually exclusive groups for commands
commands = parser.add_mutually_exclusive_group(required=True)
commands.add_argument('-encrypt', '-en', action='store_true', help='Encrypt the given input')
commands.add_argument('-decrypt', '-de', action='store_true', help='Decrypt the given input')
commands.add_argument('-generate', '-gen', action='store_true', help='Generate a key for the given algorithm')

# Add algorithm options and verbose option
parser.add_argument('-algorithm', '-alg', action='store', help='Define the algorithm used', default='fernet', choices=['fernet', 'rsa', 'aes', 'gpg'])
parser.add_argument('-verbose', '-v', action='store_true', help='Gain additional information')

# Add mutually exclusive groups for input and output
inputOption = parser.add_mutually_exclusive_group(required=False)
inputOption.add_argument('--input', '-i', ction='store', help='An input string')
inputOption.add_argument('--inputFile', '--if', action='store', help='Path to an input file')

outputOption = parser.add_mutually_exclusive_group(required=False)
outputOption.add_argument('--output', '-o', action='store_true', help='Output to console')
outputOption.add_argument('--outputFile', '-of', action='store', help='Path to an output file')

# Add key, passphrase and keyRing options
parser.add_argument('--key', '-k', action='store', help='The key file to use/save as (ignoring file extensions)', default='key')
parser.add_argument('--passphrase', '-p', action='store', help='The passphrase to use (if required), if not provided you will be prompted for one.')
parser.add_argument('--keyRing', '-kr', action='store', help='Path to the key ring to use (for GPG only)')

# Parse arguments
args = parser.parse_args()

class Main: 

    def __init__(self):
        self.FERNET = FERNET(self)
        self.RSA = RSA(self)
        self.AES = AES(self)
        self.GPG = GPG(self)

    def verboseLog(self, message):
        if (args.verbose):
            print("(VERBOSE) " + message)
    
    def run(self, args):
        if (args.generate):
            if (args.algorithm == 'fernet'):
                self.FERNET.generate_key(args)
            elif (args.algorithm == 'rsa'):
                self.RSA.generate_key(args)
            elif (args.algorithm == 'aes'):
                self.AES.generate_key(args)
            elif (args.algorithm == 'gpg'):
                self.GPG.generate_key(args)
        
        elif (args.encrypt):
            if (args.algorithm == 'fernet'):
                self.FERNET.encrypt(args)
            elif (args.algorithm == 'rsa'):
                self.RSA.encrypt(args)
            elif (args.algorithm == 'aes'):
                self.AES.encrypt(args)
            elif (args.algorithm == 'gpg'):
                self.GPG.encrypt(args)

        elif (args.decrypt):
            if (args.algorithm == 'fernet'):
                self.FERNET.decrypt(args)
            elif (args.algorithm == 'rsa'):
                self.RSA.decrypt(args)
            elif (args.algorithm == 'aes'):
                self.AES.decrypt(args)
            elif (args.algorithm == 'gpg'):
                self.GPG.decrypt(args)

# Run the program
if __name__ == '__main__':
    main = Main()
    main.run(args)