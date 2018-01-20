from __future__ import print_function, division
import sys, math

def closest(a, b, x):
    return int(round(math.pow(a, b) / x)) * x

def main():
    T = int(input())
    lines = [[int(b) for b in x.strip().split()] for x in sys.stdin.readlines()[:T]]

    for line in lines:
        print(closest(*line))

if __name__ == '__main__':
    main()
