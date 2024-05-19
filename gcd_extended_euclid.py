# Shitai Stanley Zhao
# May 16 2024
# gcd and extended euclid algorithm

import sys


# gcd(a, b) returns the greatest common divisor of a and b
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# the tuple returned is (x, y, d) where d = gcd(a, b) and d = ax + by
def extended_euclid(a, b) -> tuple:
    if b == 0:
        return (1, 0, a)
    else:
        (x, y, d) = extended_euclid(b, a % b)
        return (y, x - (a // b) * y, d)


def main(argv=sys.argv):

    # user input
    a = int(argv[1])
    b = int(argv[2])

    x, y, d = extended_euclid(a, b)

    while x < 0:
        x += b

    # print the results and the multiplicative inverse
    print(f"x = {x}, y = {y}, d = {d}")
    if d == 1:
        print(f"The multiplicative inverse of {a} mod {b} is {x % b}")
        print(f"d = {a}({x}) + {b}({y})")
    else:
        print(f"{a} and {b} are not coprime")

    return


if __name__ == "__main__":
    main(argv=sys.argv)
