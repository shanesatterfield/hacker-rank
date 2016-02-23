from __future__ import print_function, division

import sys, math

def fizzbuzz( num ):
    num -= 1
    return 3*fast_sum(num//3) + 5*fast_sum(num//5) - 15*fast_sum(num//15)

def fast_sum( N ):
    total = N // 2 * (N+1)
    if N % 2 != 0:
        total += (N+1) // 2
    return total

def main():
    T = int(input())
    for line in sys.stdin.readlines()[:T]:
        print(fizzbuzz( int(line) ))

if __name__ == '__main__':
    main()
