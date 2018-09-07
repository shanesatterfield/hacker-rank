from ..__main__ import process_input_line
from ..__main__ import find_largest_hourglass
from ..__main__ import calc_hourglass_sum
from ..__main__ import Pos

matrix = [
    [-9, -9, -9,  1, 1, 1],
    [ 0, -9,  0,  4, 3, 2],
    [-9, -9, -9,  1, 2, 3],
    [ 0,  0,  8,  6, 6, 0],
    [ 0,  0,  0, -2, 0, 0],
    [ 0,  0,  1,  2, 4, 0]
]


def test_process_input_line_with_extra_whitespace():
    assert process_input_line(' 0  1   0\n') == [0, 1, 0]


def test_process_input_line_without_extra_whitespace():
    assert process_input_line('0 1 0') == [0, 1, 0]


def test_find_largest_hour_glass():
    assert find_largest_hourglass(matrix) == 28


def test_calc_hourglass_sum():
    assert calc_hourglass_sum(matrix, Pos(1, 0)) == -34
