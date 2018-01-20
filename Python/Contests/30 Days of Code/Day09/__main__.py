from __future__ import print_function
import sys

def day09(x, y):
    a, b = max(x,y), min(x,y)
    return gcd(a, b)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def main():
    x, y = [ int(n) for n in sys.stdin.read().strip().split() ]
    print(day09(x, y))

if __name__ == '__main__':
    main()
