import pytest
from ..__main__ import day05

def test_case_1():
    assert list(day05(5, 3, 5)) == [8, 14, 26, 50, 98]

def test_case_2():
    assert list(day05(0, 2, 10)) == [2, 6, 14, 30, 62, 126, 254, 510, 1022, 2046]

def test_case_3():
    assert list(day05(3, 3, 3)) == [6, 12, 24]

def test_case_4():
    assert list(day05(0, 0, 5)) == [0, 0, 0, 0, 0]

def test_case_5():
    assert list(day05(6, 6, 10)) == [12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144]
