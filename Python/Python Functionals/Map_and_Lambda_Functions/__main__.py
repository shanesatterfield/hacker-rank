from __future__ import print_function, division
import sys, math

def fib( N ):
    fib_list = [0, 1]
    while len( fib_list ) < N:
        fib_list.append( fib_list[-1] + fib_list[-2] )

    if N <= 0:
        fib_list = []

    elif N == 1:
        fib_list = fib_list[:N]


    return fib_list

def cube_it( fib_list ):
    return list(map(lambda x: int(math.pow(x, 3)), fib_list))

def main():
    # Get the number of test cases.
    T = int(input())

    fib_list = fib( T )
    fib_list = cube_it( fib_list )

    print( fib_list )

if __name__ == '__main__':
    main()
