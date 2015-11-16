import pytest
from ..__main__ import jim

def test_case_1():
    assert jim([[1,3],[2,3],[3,3]]) == [1,2,3]

def test_case_2():
    assert jim([[8,1],[4,2],[5,6],[3,1],[4,3]]) == [4,2,5,1,3]
