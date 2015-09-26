from __future__ import print_function, division
import sys, math

def ashish(candies):
    # return ashish_naive(candies)
    i = 0
    while True:
        if sqrs_seq(i+1) > candies:
            break
        i += 1
    return i

def sqrs_seq(x):
    return int((x/6) * (x+1) * (2*x + 1))

def ashish_naive(candies):
    i    = 0
    curr = None
    while True:
        curr = int(math.pow(i+1, 2))
        if curr > candies:
            break

        candies -= curr
        i += 1
    return i


def main():
    T = int(input())
    lines = [int(x.strip()) for x in sys.stdin.readlines()[:T]]

    for line in lines:
        print(ashish(line))

if __name__ == '__main__':
    main()
