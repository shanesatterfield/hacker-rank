import pytest
from ..__main__ import is_strict

def test_case_1():
    assert is_strict([1,2,3,4,5,6,7,8,9,10,11,12,23,45,84,78],[[1,2,3,4,5], [100,11,12]]) == False
