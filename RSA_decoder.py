# Shitai Zhao
# May 16 2024
# RSA decoder

import sys


def main(argv=sys.argv):
    # if arguments are not provided, print the usage
    if len(argv) != 4:
        print("Usage: python RSA_decoder.py public key 1 private key text")
        return

    # Take in the first public key, the private key, and the ciphertext
    n = int(argv[1])
    d = int(argv[2])
    ciphertext = int(argv[3])

    # decrypt the ciphertext
    message = pow(ciphertext, d, n)

    # print the ciphertext and the message
    print(f"Ciphertext (Encrypted message): {ciphertext}")
    print(f"Message: {message}")

    return


if __name__ == "__main__":
    main()
