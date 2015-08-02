import pytest
from ..__main__ import *

def test_case_1():
    assert cube_it(fib(5)) == [0, 1, 1, 8, 27]

def test_cubing():
    arr = [1,2,3,4,5]
    cubed_arr = []
    for n in arr:
        cubed_arr.append(int(math.pow(n, 3)))

    assert cube_it(arr) == cubed_arr

def test_fib_sequence():
    assert fib(10) == [0,1,1,2,3,5,8,13,21,34]

def test_fib_low_bounds():
    assert fib(1) == [0]

def test_fib_of_zero():
    assert fib(0) == []

def test_fib_negative():
    assert fib(-1) == []
    assert fib(-2) == []
    assert fib(-300) == []
    assert fib(-10000) == []

