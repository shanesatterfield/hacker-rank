import pytest
from ..__main__ import day09

def test_case_1():
    assert day09(1, 5) == 1

def test_case_2():
    assert day09(2, 3) == 1

def test_gcd_is_factor():
    assert day09(9, 21) == 3

def test_gcd_is_self():
    assert day09(25, 100) == 25
