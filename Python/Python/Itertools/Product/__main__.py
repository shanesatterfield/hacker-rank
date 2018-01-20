from __future__ import print_function
import sys, itertools

def product(a, b):
    return list(itertools.product(sorted(a), sorted(b)))

def main():
    lines = [[int(b) for b in x.strip().split()] for x in sys.stdin.readlines()[:2]]
    print(*product(*lines))

if __name__ == '__main__':
    main()
