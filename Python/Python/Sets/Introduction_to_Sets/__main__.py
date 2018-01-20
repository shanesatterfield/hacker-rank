from __future__ import print_function, division
import sys

def introd(arr):
    arr = set(arr)
    return sum(arr) / len(arr)

def main():
    lines = sys.stdin.readlines()
    print(introd([int(x) for x in lines[1].split()]))

if __name__ == '__main__':
    main()
