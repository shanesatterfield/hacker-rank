from __future__ import print_function
import sys, itertools
from collections import Counter

def noidea(arr, a, b):
    count   = Counter(arr)
    result  = add_from_both(arr, a, count)
    result -= add_from_both(arr, b, count)
    return result

def add_from_both(arr, s, count):
    return sum([ count[x] for x in set(s).intersection(arr) ])

def main():
    lines = [[int(x) for x in line.strip().split()] for line in sys.stdin.readlines()[:4]]
    print(noidea(*lines[1:4]))

if __name__ == '__main__':
    main()
