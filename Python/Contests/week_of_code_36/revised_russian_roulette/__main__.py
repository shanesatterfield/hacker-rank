import sys
from typing import List, Tuple


def roulette(arr: List[int]) -> Tuple[int, int]:
    maxi = sum(arr)
    mini = maxi
    index = 0

    while index + 1 < len(arr):
        if arr[index] == 1 and arr[index+1] == 1:
            mini -= 1
            index += 1
        index += 1

    return mini, maxi


def main():
    line = sys.stdin.readlines()[1].strip().split()
    print(*roulette([int(x) for x in line]))


if __name__ == '__main__':
    main()
