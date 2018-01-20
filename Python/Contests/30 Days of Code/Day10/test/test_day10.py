import pytest
from ..__main__ import day10

def test_case_1():
    assert day10(4) == '100'

def test_case_2():
    assert day10(5) == '101'

def test_check_against_bin_builtin():
    for n in range(1, 128):
        assert day10(n) == get_binary_string(n)

def test_edge_case_low():
    assert day10(1) == '1'

def test_edge_case_high():
    num = pow(2, 32)
    assert day10(num) == get_binary_string(num)

def get_binary_string(num):
    return bin(num).split('b')[1]
