import pytest
from ..__main__ import minimax

def test_case_1():
    assert minimax(4, 9, [5,8,14]) == 4

def test_case_2():
    assert minimax(23, 69, [38,50,60,30,48]) == 69

def test_case_3():
    assert minimax(43, 110, [114,48,86,180,176,66,126,194,50,198,140,192,186,4,136,138,130,178,36,14]) == 100
