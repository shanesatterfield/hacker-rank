import sys
from typing import List


class Interval:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    def is_inside(self, x: int):
        return self.start <= x and x <= self.stop


def count_inside(house: Interval, start_point: int, items: List[int]) -> int:
    items = map(lambda item: start_point + item, items)
    items = map(house.is_inside, items)
    items = map(int, items)
    return sum(items)


def main():
    lines = sys.stdin.readlines()
    lines = [list(map(int, line.strip().split())) for line in lines]
    house = Interval(*lines[0])
    apples_start, oranges_start = lines[1]
    apples = lines[3]
    oranges = lines[4]
    print(count_inside(house, apples_start, apples))
    print(count_inside(house, oranges_start, oranges))


if __name__ == '__main__':
    main()
