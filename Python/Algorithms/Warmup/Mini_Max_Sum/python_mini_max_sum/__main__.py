"""
Algorithms -> Warmup -> Mini-Max Sum
"""

from os import sys
from typing import List, Tuple


def main():
    inputs = [int(x) for x in sys.stdin.readline().split()]
    print(*find_mini_max(inputs))


def find_mini_max(lst: List[int]) -> Tuple[int, int]:
    sorted_lst = sorted(lst)
    return sum(sorted_lst[0:4]), sum(sorted_lst[1:5])


if __name__ == '__main__':
    main()
