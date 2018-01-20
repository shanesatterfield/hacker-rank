import pytest
from ..__main__ import *

def test_case_1():
    assert score([5,6,7], [3,6,10]) == [1,1]

def test_all_the_same():
    assert score([1,1,1], [1,1,1]) == [0,0]

def test_all_alice():
    assert score([2,2,2], [1,1,1]) == [3,0]

def test_all_bob():
    assert score([1,1,1], [2,2,2]) == [0,3]

def test_negative():
    assert score([-5,-6,7], [3,6,10]) == [0,3]
