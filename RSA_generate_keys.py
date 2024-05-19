# Shitai Stanley Zhao
# May 16 2024
# Using the RSA algorithm to encrypt and decrypt messages
# Based on the gcd.py and the primality.py modules

from gcd_extended_euclid import gcd, extended_euclid
from primality import is_prime
import random


# generate two random three digit primes p and q
def generate_primes():
    p = random.randint(100, 1000)
    q = random.randint(100, 1000)
    while not is_prime(p, 10):
        p = random.randint(100, 1000)
    while not is_prime(q, 10):
        q = random.randint(100, 1000)
    print(f"p: {p}, q: {q}")
    return p, q


# generate the public and private keys
# n is the first public key, e is the second public key, x is the private key
def generate_keys():
    p, q = generate_primes()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # d is the multiplicative inverse of e mod phi i.e. e * d ≡ 1 (mod phi)
    d, _, g = extended_euclid(e, phi)

    # ensure d is positive
    d = d % phi
    if d < 0:
        d += phi

    # return the public and private keys
    return n, e, d


def main():
    # generate the public and private keys
    n, e, d = generate_keys()

    # print the public and private keys
    print(f"Public key: ({n}, {e})")
    print(f"Private key: ({d})")

    return


if __name__ == "__main__":
    main()
