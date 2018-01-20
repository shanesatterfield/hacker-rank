import pytest, math

from ..__main__ import *

def test_case_1():
    assert astr('AAAA') == 3

def test_case_2():
    assert astr('BBBBB') == 4

def test_case_3():
    assert astr('ABABABAB') == 0

def test_case_4():
    assert astr('BABABA') == 0

def test_case_5():
    assert astr('AAABBB') == 4

def test_edge_case_large():
    assert astr('A' * int(math.pow(10, 5)))
