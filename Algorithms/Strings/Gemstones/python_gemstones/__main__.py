from __future__ import print_function, division
from functools import reduce
import sys

def count_gems( gems ):
    gems = [ set(list(x)) for x in gems ]
    return len(reduce(lambda a,b: a.intersection(b), gems))

def main():
    T = int(input())
    gems = [ x.strip() for x in sys.stdin.readlines()[:T] ]
    print(count_gems(gems))

if __name__ == '__main__':
    main()
