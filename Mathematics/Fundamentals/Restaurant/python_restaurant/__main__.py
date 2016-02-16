from __future__ import print_function
import sys

def restaurant(a, b):
    return a * b // gcd(a, b)**2

def gcd(a, b):
    a, b = min(a,b), max(a,b)
    if a == b:
        return a
    return gcd(a, b - a)


def main():
    T = int(input())
    input_data = [[int(x) for x in line.strip().split()] for line in sys.stdin.readlines()[:T]]

    for line in input_data:
        print(restaurant(line[0], line[1]))

if __name__ == '__main__':
    main()
