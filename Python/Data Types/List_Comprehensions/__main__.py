from __future__ import print_function
import sys

def listcomp(X, Y, Z, N):
    return [ [x, y, z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x+y+z != N ]

def main():
    lst = [ int(x) for x in sys.stdin.read().strip().split() ]
    print(listcomp(*lst[:4]))

if __name__ == '__main__':
    main()
