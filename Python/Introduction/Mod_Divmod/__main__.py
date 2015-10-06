from __future__ import print_function, division
import sys

def divmod(a, b):
    return (a//b, a%b)

def main():
    lines = [int(x) for x in sys.stdin.read().split()]
    a, b = divmod(*lines[:2])
    print(a)
    print(b)
    print((a,b))

if __name__ == '__main__':
    main()
