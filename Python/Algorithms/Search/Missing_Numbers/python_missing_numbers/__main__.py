from __future__ import print_function
from collections import Counter
import sys

def missing(a, b):
    count = Counter(b)
    count.subtract(Counter(a))
    return sorted(list(filter(lambda x: count[x] > 0, count)))

def main():
    lines = [ [int(b) for b in x.strip().split()] for x in sys.stdin.readlines()[1::2] ][:2]
    print(*missing(*lines))

if __name__ == '__main__':
    main()
