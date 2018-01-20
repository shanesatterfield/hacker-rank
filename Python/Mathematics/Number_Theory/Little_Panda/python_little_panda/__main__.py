from __future__ import print_function, division
import sys, math

def extended_euclidean(a, b, x):
    if b >= 0:
        return modulo_exponentiation(a, b, x)

    # Note: C = Current, P = Previous
    rp, rc = x, a
    tp, tc = 0, 1
    sp, sc = 1, 0
    next_iter = None
    quotient = None

    while rc != 0:
        quotient = rp // rc
        next_iter = euclid_iter(rp, rc, quotient)
        rp, rc = euclid_iter(rp, rc, quotient)
        sp, sc = euclid_iter(sp, sc, quotient)
        tp, tc = euclid_iter(tp, tc, quotient)

    ans = modulo_exponentiation(tp, abs(b), x)
    # If negative, turn it into the lowest positive answer.
    return ans if ans > 0 else -(ans // x) * x + ans

# Returns a tuple of xi, xi+1.
def euclid_iter(prev, curr, quotient):
    return curr, prev - (quotient * curr)

def modulo_exponentiation(base, exponent, mod):
    result = 1
    base = base % mod

    while exponent > 0:
        if exponent & 1:
            result = (result * base) % mod
        exponent = exponent >> 1
        base = (base * base) % mod
    return int(result)

def main():
    T = int(input())
    lines = [[int(b) for b in x.strip().split()] for x in sys.stdin.readlines()[:T]]

    for line in lines:
        print(extended_euclidean(*line))

if __name__ == '__main__':
    main()
