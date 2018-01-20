import pytest
from ..__main__ import reverse_game

def test_case_1():
    assert reverse_game(3, 1) == 2

def test_case_2():
    assert reverse_game(5, 2) == 4

def test_case_3():
    assert reverse_game(6, 4) == 2

def test_full_8():
    arr = [8,0,7,1,6,2,5,3,4]
    for i in range(len(arr)):
        assert reverse_game(len(arr), arr[i]) == i
