from __future__ import print_function
import sys, itertools

def is_strict(sup, arr):
    sup = set(sup)
    arr = [ set(x) for x in arr ]
    return all(map(lambda x: sup.issuperset(x) and len(sup) > len(arr), arr))

def main():
    lines = [[int(x) for x in line.strip().split()] for line in sys.stdin.readlines()]
    print(is_strict(lines[0], lines[2:]))

if __name__ == '__main__':
    main()
