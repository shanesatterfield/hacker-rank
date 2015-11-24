from __future__ import print_function, division
import sys, itertools

def flowers(K, prices):
    prices = list(reversed(sorted(prices)))
    result = 0
    for i in range(len(prices) // K + 1):
        result += sum(prices[i*K:i*K+K]) * (i+1)
    return result

def main():
    lines = [[int(b) for b in x.strip().split()] for x in sys.stdin.readlines()][:2]
    print(flowers(lines[0][1], lines[1]))

if __name__ == '__main__':
    main()
