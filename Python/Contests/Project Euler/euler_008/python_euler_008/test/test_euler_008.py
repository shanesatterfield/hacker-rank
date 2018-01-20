import pytest
from ..__main__ import euler_008

def test_case_1():
    assert euler_008(5, "3675356291") == 3150

def test_case_2():
    assert euler_008(5, "2709360626") == 0

def test_one_of_two():
    assert euler_008(1, "12") == 2

def test_two_of_two():
    assert euler_008(2, "34") == 12

def test_zero_items():
    assert euler_008(0, "123123") == 0

def test_7_of_8():
    assert euler_008(7, "12345678") == 40320
