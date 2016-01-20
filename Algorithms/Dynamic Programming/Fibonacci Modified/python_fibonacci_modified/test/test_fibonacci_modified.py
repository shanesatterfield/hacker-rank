import pytest
from ..__main__ import fib_mod

def test_case_1():
    assert fib_mod(0, 1, 5) == 5

def test_case_2():
    assert fib_mod(0, 1, 10) == 84266613096281243382112
