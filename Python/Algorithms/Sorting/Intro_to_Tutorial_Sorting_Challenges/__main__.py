from __future__ import print_function
import sys

def intro(v, arr):
    """Searches through the array and finds the position of the v element."""
    return arr.index(v)

def main():
    lines = [[int(x) for x in line.strip().split()] for line in sys.stdin.readlines()[:3]]
    print(intro(lines[0][0], lines[2]))

if __name__ == '__main__':
    main()
