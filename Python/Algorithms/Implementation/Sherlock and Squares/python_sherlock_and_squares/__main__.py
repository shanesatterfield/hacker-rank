from __future__ import print_function, division

import sys, math

def main():
    T = int(input())
    for line in sys.stdin.readlines()[:T]:
        interval = [ int(x) for x in line.split() ]
        print( squares_interval( interval[0], interval[1] ) )

def squares_interval( a, b ):
    count = 0
    interval = [ a, b ]
    if is_square( a ):
        count = 1

    count += int(math.sqrt( b )) - int(math.sqrt( a ))
    return count

def is_square( num ):
    return math.pow( int(math.sqrt(num)), 2 ) == num

if __name__ == '__main__':
    main()
