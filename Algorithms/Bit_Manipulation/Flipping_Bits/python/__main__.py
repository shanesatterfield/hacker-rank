from __future__ import print_function
import sys

# The maximum size in bits.
max_bits = 32

# The calculated max value.
max_size = int(bin(pow(2, max_bits))[2:], 2)

# Flips the bits of a number.
def flip(num):
    return max_size - num - 1

def main():
    T = int(input())
    lines = [int(x.strip()) for x in sys.stdin.readlines()[:T]]

    for line in lines:
        print(flip(line))

if __name__ == '__main__':
    main()
