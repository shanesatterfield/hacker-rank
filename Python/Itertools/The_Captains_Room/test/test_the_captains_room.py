import pytest
from ..__main__ import find_room

def test_case_1():
    assert find_room(5, [1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2]) == 8
