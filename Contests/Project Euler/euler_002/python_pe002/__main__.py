from __future__ import print_function
import sys

def fib( N ):
    N = int( N )
    total = 0
    curr = 1
    prev = 1

    while curr <= N:
        if curr % 2 == 0:
            total += curr

        curr += prev
        prev = curr - prev

    return total

def main():
    T = int(input())
    for n in sys.stdin.readlines()[:T]:
        print(fib( n ))

if __name__ == '__main__':
    main()
