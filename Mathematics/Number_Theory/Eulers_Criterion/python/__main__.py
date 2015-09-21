from __future__ import print_function
import sys, math

# Efficient solution using the Right-to-left binary method of modular exponentiation.
# You can find this here https://en.wikipedia.org/wiki/Modular_exponentiation
def eulers_criterion(A, M):
    if A == 0:
        return True

    exponent = (M-1)//2
    result   = 1
    base     = A % M

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % M
        exponent = exponent >> 1
        base = (base * base) % M

    # Final modulated answer.
    return result % M == 1

# Naive solution
# You can find the formula here https://en.wikipedia.org/wiki/Euler%27s_criterion
# def eulers_criterion(A, M):
#     return math.pow(A, (M-1)//2) % M == 1

def main():
    T = int(input())

    # Takes the stdin lines and converts them into pairs of integers for processing.
    lines = [ [ int(b) for b in x.strip().split() ] for x in sys.stdin.readlines() ]

    for line in lines:
        print("YES" if eulers_criterion(*line[:2]) else "NO")

if __name__ == '__main__':
    main()
