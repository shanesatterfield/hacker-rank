from ..__main__ import max_array_sum
from random import randint


def test_case_0():
    assert max_array_sum([3, 7, 4, 6, 5]) == 13


def test_case_1():
    assert max_array_sum([2, 1, 5, 8, 4]) == 11


def test_case_2():
    assert max_array_sum([3, 5, -7, 8, 10]) == 15


def test_case_3():
    assert max_array_sum([8, 9, 8]) == 16


def test_case_4():
    assert max_array_sum([3, 5, -7, 8, 10, 5, -3]) == 18


def test_sequential():
    assert max_array_sum(list(reversed(range(4, 11)))) == 28


def test_high_load():
    arr = [randint(-10, 10) for n in range(10**2)]
    max_array_sum(arr)


def test_max_load():
    arr = [randint(-10**4, 10*4) for n in range(10**5)]
    max_array_sum(arr)
