import pytest
from ..__main__ import is_valid

def test_case_1():
    assert is_valid(".*\+") == True

def test_case_2():
    assert is_valid(".*+") == False
