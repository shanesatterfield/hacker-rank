from __future__ import print_function
import sys

def tarrs(K, a, b):
    a = list(sorted(a))
    b = list(reversed(sorted(b)))
    return all( (a[i] + b[i]) >= K for i in range(len(a)) )


def main():
    T = int(input())
    lines = [[int(b) for b in x.strip().split()] for x in sys.stdin.readlines()]
    for i in range(T):
        print("YES" if tarrs(lines[i*3][1], lines[i*3+1], lines[i*3+2]) else "NO")

if __name__ == '__main__':
    main()
