from __future__ import print_function, division
import sys

# Basic modular exponentiation
def mod_power(a, b, m):
    base = a
    exponent = b
    result = 1

    base = base % m
    while exponent > 0:
        if exponent & 1 == 1:
            result = (result * base) % m
        exponent = exponent >> 1
        base = (base*base) % m
    return (pow(a,b), result)

def main():
    lines = [int(x) for x in sys.stdin.read().strip().split()]

    for line in mod_power(*lines):
        print(line)

if __name__ == '__main__':
    main()
