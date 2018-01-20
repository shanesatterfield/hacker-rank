import pytest
from ..__main__ import *

def test_case_1():
    assert taum(10, 10, 1, 1, 1) == 20

def test_case_2():
    assert taum(5, 9, 2, 3, 4) == 37

def test_case_3():
    assert taum(3, 6, 9, 1, 1) == 12

def test_case_4():
    assert taum(7, 7, 4, 2, 1) == 35

def test_case_5():
    assert taum(3, 3, 1, 9, 2) == 12
