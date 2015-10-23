from __future__ import print_function
from functools import reduce
import sys

def sansa(lst):
    result = 0
    for j in range(len(lst)):
        temp = 0
        for i in range(j, len(lst)):
            temp ^= lst[i]
            result ^= temp
    return result

def main():
    T = int(input())
    lines = [[int(b) for b in x.strip().split()] for x in sys.stdin.readlines()]
    for line in lines[1::2]:
        print(sansa(line))

if __name__ == '__main__':
    main()
