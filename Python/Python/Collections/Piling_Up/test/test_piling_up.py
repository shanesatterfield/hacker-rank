import pytest
from ..__main__ import piling_up

def test_case_1():
    assert piling_up([4,3,2,1,3,4]) == True

def test_case_2():
    assert piling_up([1,3,2]) == False
