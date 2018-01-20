from __future__ import print_function, division
import sys, math

def kaprekar_range( p, q ):
    return sorted(list(filter(is_kaprekar, list(range(p, q+1)))))

def is_kaprekar( num ):
    squared = str(int(math.pow(num, 2)))
    l       = squared[:len(squared)//2] or '0'
    r       = squared[len(squared)//2:] or '0'
    return (int(l) + int(r)) == num

def main():
    p, q = [ int(x.strip()) for x in sys.stdin.readlines() ]
    result = kaprekar_range( p, q )
    if len(result) == 0:
        print('INVALID RANGE')
    else:
        print(*result)

if __name__ == '__main__':
    main()
