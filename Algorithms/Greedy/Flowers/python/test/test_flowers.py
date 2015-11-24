import pytest
from ..__main__ import flowers

def test_case_1():
    assert flowers(3, [2,5,6]) == 13

def test_case_2():
    assert flowers(2, [2,5,6]) == 15
