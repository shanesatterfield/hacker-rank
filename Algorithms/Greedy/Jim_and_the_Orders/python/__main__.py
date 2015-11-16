from __future__ import print_function
import sys

def jim(lst):
    lst = sorted([ (i+1, sum(lst[i])) for i in range(len(lst)) ], key=lambda x: x[1])
    return [ x[0] for x in lst ]

def main():
    T = int(input())
    lines = [[int(b) for b in x.strip().split()] for x in sys.stdin.readlines()][:T]
    print(*jim(lines))

if __name__ == '__main__':
    main()
