# Shitai Zhao Stanley
# May 16 2024
# Randomized primality test that gives a probability of (0.5)^k of being wrong
# and generates a list of prime numbers of three digits

import random


# Randomized primality test that has a false positive probability of <(0.5)^k
def is_prime(p, k):
    # easy cases and even numbers
    if p == 2 or p == 3:
        return True
    if p % 2 == 0:
        return False

    # Loop through k times to lower the probability of being wrong
    for _ in range(k):
        a = random.randint(2, p - 1)
        if a ** (p - 1) % p != 1:
            return False
    return True


def generate_three_digit_primes():
    primes = []
    for i in range(100, 1000):
        # loop 10 times as an arbitrary number
        if is_prime(i, 10):
            primes.append(i)
    return primes


def main():
    primes = []
    primes = generate_three_digit_primes()
    print(len(primes), 'prime numbers from 100 to 1000')
    print(primes)


if __name__ == "__main__":
    main()
