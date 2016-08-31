from __future__ import print_function, division
from itertools import *
import sys

def merger(string, K):
    return [ ''.join(uniquify(group)) for group in splitting(string, int(K)) ]

def uniquify(arr):
    seen = set()
    result = []
    for x in arr:
        if not x in seen:
            seen.add(x)
            result.append(x)
    return result

def splitting(arr, k):
    result = []
    while len(arr) > 0:
        result.append(arr[:k])
        arr = arr[k:]
    return result

def main():
    lines = [ line.strip() for line in sys.stdin.readlines()[:2] ]

    for chunk in merger(*lines):
        print(chunk)

if __name__ == '__main__':
    main()
