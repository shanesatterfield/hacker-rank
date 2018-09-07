import sys
from typing import List


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def within(self, bounds) -> bool:
        return 0 <= self.x < bounds.x and 0 <= self.y < bounds.y


hourglass_shape = [
    Pos(0, 0), Pos(1, 0), Pos(2, 0),
               Pos(1, 1),
    Pos(0, 2), Pos(1, 2), Pos(2, 2),
]


def main():
    matrix = [process_input_line(line) for line in sys.stdin.readlines()]
    print(find_largest_hourglass(matrix))


def process_input_line(line: str) -> List[int]:
    # Trim extra whitespace and parse to 2D integer array
    return [int(x) for x in line.strip().split()]


def find_largest_hourglass(matrix: List[List[int]]) -> int:
    largest = float('-inf')
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            total = calc_hourglass_sum(matrix, Pos(x, y))
            if total and total > largest:
                largest = total

    return largest


def calc_hourglass_sum(matrix: List[List[int]], start: Pos) -> int:
    hourglass_positions = calc_hourglass_positions(start)

    # Validate that hourglass is within bounds
    bounds = Pos(len(matrix[0]), len(matrix))
    if not is_shape_in_bounds(bounds, hourglass_positions):
        return None

    # Calculate the sum of the hourglass
    return sum(matrix[pos.y][pos.x] for pos in hourglass_positions)


def calc_hourglass_positions(start: Pos) -> List[Pos]:
    return [start + offset for offset in hourglass_shape]


def is_shape_in_bounds(bounds: Pos, positions: List[Pos]) -> bool:
    return all(pos.within(bounds) for pos in positions)


if __name__ == '__main__':
    main()
