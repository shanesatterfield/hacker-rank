import pytest
from ..__main__ import tarrs

def test_case_1():
    assert tarrs(10,[2,1,3],[7,8,9]) == True

def test_case_2():
    assert tarrs(5,[1,2,2,1],[3,3,3,4]) == False
