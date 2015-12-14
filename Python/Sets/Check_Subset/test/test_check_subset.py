import pytest
from ..__main__ import issub

def test_case_1():
    assert issub([1,2,3,5,6], [9,8,5,6,3,2,1,4,7]) == True

def test_case_2():
    assert issub([2], [3,6,5,4,1]) == False

def test_case_3():
    assert issub([1,2,3,5,6,8,9], [9,8,2]) == False
