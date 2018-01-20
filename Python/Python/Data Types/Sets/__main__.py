from __future__ import print_function
import sys

def sym( a, b ):
    return sorted(list(a.symmetric_difference(b)))

def main():
    lines = sys.stdin.readlines()[:4]
    
    M = int(lines[0].strip())
    N = int(lines[2].strip())

    a = set([ int(x) for x in lines[1].strip().split() ])
    b = set([ int(x) for x in lines[3].strip().split() ])

    for n in sym( a, b ):
        print( n )

if __name__ == '__main__':
    main()
