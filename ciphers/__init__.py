from ciphers.caeser_cipher import CaeserCipher
from ciphers.vigenere_cipher import VigenereCipher
import argparse

VERSION = "0.0.0"


def caeser_cipher(args):
    if args.rotation:
        caeser = CaeserCipher(rotation=args.rotation)
    else:
        caeser = CaeserCipher()

    if args.action == "encrypt":
        print(caeser.encrypt(args.input))
    else:
        print(caeser.decrypt(args.input))


def vigenere_cipher():
    pass


operations = {"caeser": caeser_cipher, "vigenere": vigenere_cipher}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Determine which cipher, rotation, input string"
    )
    subparsers = parser.add_subparsers(dest="cipher")

    caeser = subparsers.add_parser("caeser", help="Use the Caeser Cipher")
    caeser.add_argument(
        "-r",
        "--rotation",
        help="Set the rotation for the cipher",
        type=int,
        action="store",
        required=True,
    )
    caeser.add_argument(
        "-i",
        "--input",
        help="Set the input string for the cipher",
        action="store",
        required=True,
    )
    caeser.add_argument(
        "-a" "--action",
        help="Set the action for the cipher",
        choices=["encrypt", "decrypt"],
        action="store",
        default="encrypt",
    )

    return parser.parse_args()


def main():
    args = parse_args()
    operations[args.cipher](args)
