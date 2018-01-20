from __future__ import print_function
import sys

def seta(arr):
    result = set()
    for n in arr:
        result.add(n)
    return len(result)

def main():
    T = int(input())
    lines = [x.strip() for x in sys.stdin.readlines()[:T]]
    print(seta(lines))

if __name__ == '__main__':
    main()
