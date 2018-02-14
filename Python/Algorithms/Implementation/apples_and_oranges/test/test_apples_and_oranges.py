import pytest
from ..__main__ import Interval, count_inside


def test_case_1():
    assert count_inside(Interval(7, 11), 5, [-2, 2, 1]) == 1


def test_case_2():
    assert count_inside(Interval(7, 11), 15, [5, -6]) == 1
