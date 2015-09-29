from __future__ import print_function
import sys

def simple_sum(lst):
    return sum(lst)

def main():
    T = int(input())
    arr = [int(x) for x in sys.stdin.read().strip().split()]
    print(simple_sum(arr))

if __name__ == '__main__':
    main()
