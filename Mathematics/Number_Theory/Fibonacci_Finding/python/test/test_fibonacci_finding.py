import pytest
from ..__main__ import fib

def test_case_1():
    assert fib(2,3,1) == 3

def test_case_2():
    assert fib(9,1,7) == 85

def test_case_3():
    assert fib(9,8,3) == 25

def test_case_4():
    assert fib(2,4,9) == 178

def test_case_5():
    assert fib(1,7,2) == 8

def test_case_6():
    assert fib(1,8,1) == 8

def test_case_7():
    assert fib(4,3,1) == 3

def test_case_8():
    assert fib(3,7,5) == 44

def test_case_9():
    assert fib(509618737, 460201239, 229176339) == 945141656
