from __future__ import print_function, division
import sys, math

def get_time( L, S1, S2, Q ):
    return math.sqrt(2) * (L - math.sqrt(Q)) / abs(S2 - S1)

def main():
    lines = sys.stdin.readlines()

    L, S1, S2 = [ int(x.strip()) for x in lines[0].split() ]
    T         = int(lines[1])
    queries   = [ int(x) for x in lines[2:2+T] ]

    for Q in queries:
        print(get_time(L, S1, S2, Q))

if __name__ == '__main__':
    main()
