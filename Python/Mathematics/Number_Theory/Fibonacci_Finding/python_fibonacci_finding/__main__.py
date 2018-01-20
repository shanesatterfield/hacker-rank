from __future__ import print_function
import sys, math

M = int(math.pow(10, 9)) + 7

def fib(A, B, N):
    if N <= 0:
        return A
    if N == 1:
        return B

    a = 1
    b = 1
    N -= 1
    index = 1

    # This goes through the bits, but skips the most significant bit.
    for bit_num in reversed(range(N.bit_length()-1)):
        # Doubles and crazy modulo distribution.
        c = int((a%M * ((b<<1)%M - a%M)%M)%M)
        d = int(((a%M * a%M)%M + (b%M * b%M)%M)%M)

        a = c
        b = d

        index = index << 1

        # Jumps up by 1 in reverse.
        if (N >> bit_num) & 1:
            temp = a
            a = b
            b = int((temp + b)%M)
            index += 1

    return int(((A%M * a%M)%M + (B%M * b%M)%M)%M)

def main():
    T = int(input())
    lines = [ [int(b) for b in x.strip().split()] for x in sys.stdin.readlines() ]

    for line in lines:
        print(fib(*line[:3]))

if __name__ == '__main__':
    main()
