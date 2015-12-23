from __future__ import print_function
from collections import Counter
import sys

def find_room(k, arr):
    count = Counter(arr)
    for key in count:
        if count[key] == 1:
            return key

def main():
    lines = [[int(x) for x in line.strip().split()] for line in sys.stdin.readlines()[:2]]
    print(find_room(*lines))

if __name__ == '__main__':
    main()
