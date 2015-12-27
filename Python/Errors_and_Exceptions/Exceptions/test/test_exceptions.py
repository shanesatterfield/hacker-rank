import pytest
from ..__main__ import excerpt

zero_message = 'Error Code: integer division or modulo by zero'
value_message = "Error Code: invalid literal for int() with base 10: '$'"

def test_case_1():
    assert excerpt(1,0) == zero_message

def test_case_2():
    assert excerpt(2,'$') == value_message

def test_case_3():
    assert excerpt(3,1) == 3
