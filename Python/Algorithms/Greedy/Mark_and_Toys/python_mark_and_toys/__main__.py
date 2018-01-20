from __future__ import print_function
import sys

def max_toys(K, prices):
    count = 0
    for n in sorted(prices):
        if n > K:
            break
        K -= n
        count += 1
    return count

def main():
    lines = [[int(b) for b in x.strip().split()] for x in sys.stdin.readlines()]
    print(max_toys(lines[0][1], lines[1]))

if __name__ == '__main__':
    main()
