import pytest
from ..__main__ import *

def test_case_1():
    assert sorted(kaprekar_range(1, 100)) == [1, 9, 45, 55, 99]

def test_case_2():
    assert sorted(kaprekar_range(100, 300)) == [297]

def test_invalid_range():
    assert sorted(kaprekar_range(400, 700)) == []

def test_inclusive():
    assert sorted(kaprekar_range(1, 99999)) == [1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728, 4950, 5050, 7272, 7777, 9999, 17344, 22222, 77778, 82656, 95121, 99999]
