from __future__ import print_function
import sys

def tuple_to_hash( lst ):
    return hash(tuple(lst))



def main():
    # Retrieve the number of inputs
    T = int(input())
    # ans = tuple([ int(x) for x in sys.stdin.read().split()[:T] ])
    print(tuple_to_hash([ int(x) for x in sys.stdin.read().split()[:T] ]))


if __name__ == '__main__':
    main()

    # One-liner
    # print(hash(tuple([int(x) for x in sys.stdin.read().split()[1:]])))
