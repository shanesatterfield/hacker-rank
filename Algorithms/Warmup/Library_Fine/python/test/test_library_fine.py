import pytest
from ..__main__ import *

def test_case_1():
    assert fine([9,6,2015], [6,6,2015]) == 45

def test_case_2():
    assert fine([1,1,2016], [9,6,2015]) == 10000

def test_case_3():
    assert fine([1,1,2016], [9,6,2015]) == 10000

def test_case_4():
    assert fine([2,5,2015],[30,5,2015]) == 0

def test_case_5():
    assert fine([6,6,2015],[9,6,2016]) == 0
