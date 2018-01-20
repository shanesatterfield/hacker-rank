from __future__ import print_function
import sys

def big_sum(lst):
    return sum(lst)

def main():
    T = int(input())
    nums = [int(x) for x in sys.stdin.read().strip().split()]
    print(big_sum(nums))

if __name__ == '__main__':
    main()
