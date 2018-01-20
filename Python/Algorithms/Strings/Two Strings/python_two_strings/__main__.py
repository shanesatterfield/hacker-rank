from __future__ import print_function
import sys

def check_ss( a, b ):
    a = set(a)
    b = set(b)
    return len(a.intersection(b)) > 0

def main():
    T = int(input())
    lines = [ x.strip() for x in sys.stdin.readlines()[:T*2] ]

    for n in range(0, T*2, 2):
        result = check_ss( lines[n], lines[n+1] )
        print('YES' if result else 'NO')

if __name__ == '__main__':
    main()
