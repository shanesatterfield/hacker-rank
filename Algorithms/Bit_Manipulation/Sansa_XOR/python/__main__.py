from __future__ import print_function
from functools import reduce
import sys

def sansa(lst):
    result = 0
    starting = int(len(lst)%2==0)
    for n in range(starting, len(lst), 2):
        result ^= lst[n]
    return result

def main():
    T = int(input())
    lines = [[int(b) for b in x.strip().split()] for x in sys.stdin.readlines()]
    for line in lines[1::2]:
        print(sansa(line))

if __name__ == '__main__':
    main()
