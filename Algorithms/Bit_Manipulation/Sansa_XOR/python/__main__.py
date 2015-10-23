from __future__ import print_function
from functools import reduce
import sys

def sansa(lst):
    result = 0
    for j in range(len(lst)):
        for i in range(len(lst)):
            if i + j >= len(lst):
                break
            result ^= reduce(lambda x,y: x^y, lst[i:i+j+1])
    return result

def main():
    T = int(input())
    lines = [[int(b) for b in x.strip().split()] for x in sys.stdin.readlines()]
    for line in lines[1::2]:
        print(sansa(line))

if __name__ == '__main__':
    main()
