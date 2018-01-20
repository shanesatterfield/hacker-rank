from __future__ import print_function
import sys

def get_minimum_socks( socks ):
    return socks+1

def main():
    T = int(input())
    for n in sys.stdin.readlines()[:T]:
        print(int(n)+1)

if __name__ == '__main__':
    main()

    # One-liner
    #[ print(int(x)+1) for x in sys.stdin.readlines()[1:] ]
