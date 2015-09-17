from __future__ import print_function
import sys

def second_largest( nums ):
    return sorted(list(set(nums)))[-2]

def main():
    T = int(input())
    print(second_largest([ int(x) for x in sys.stdin.read().strip().split() ]))

if __name__ == '__main__':
    main()
