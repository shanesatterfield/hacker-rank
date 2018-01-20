from __future__ import print_function
import sys

def bigint(a, b, c, d):
    return int(pow(a, b) + pow(c, d))

def main():
    data = [int(x.strip()) for x in sys.stdin.readlines()]
    print(bigint(*data))

if __name__ == '__main__':
    main()
