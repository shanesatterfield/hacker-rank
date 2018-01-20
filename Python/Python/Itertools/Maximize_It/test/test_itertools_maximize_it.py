import pytest
from ..__main__ import *

def test_case_1():
    assert find_largest([
        [5, 4],
        [7, 8, 9],
        [5, 7, 8, 9, 10]
    ], 1000) == 206

def test_sum_of_zero():
    assert get_sum([], 1) == 0

def test_sum_of_case_1():
    assert get_sum([5, 7, 5], 7) == (99 % 7)
