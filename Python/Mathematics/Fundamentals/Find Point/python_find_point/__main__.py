from __future__ import print_function, division
import sys

def find_point( line ):
    px, py, qx, qy = [ int(x) for x in line.strip().split() ]
    return 2 * qx - px, 2 * qy - py

def main():
    T = int(input())
    lines = sys.stdin.readlines()[:T]

    for line in lines:
        print(*find_point(line))

if __name__ == '__main__':
    main()
