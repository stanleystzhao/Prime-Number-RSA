# Shitai Zhao
# May 16 2024
# RSA encoder

import sys


def main(argv=sys.argv):

    # If arguments are not provided, print the usage
    if len(argv) != 4:
        print("Usage: python RSA_encoder.py public key 1 public key 2 message")
        return

    # Take in the public keys and message
    n = int(argv[1])
    e = int(argv[2])
    message = int(argv[3])

    # encrypt the messages
    ciphertext = pow(message, e, n)

    # print the message and the ciphertext
    print(f"Message: {message}")
    print(f"Encrypted message: {ciphertext}")

    return


if __name__ == "__main__":
    main()
