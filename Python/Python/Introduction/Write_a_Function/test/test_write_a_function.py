import pytest
from ..__main__ import *

def test_not_by_four():
    assert is_leap(1990) == False

def test_by_4():
    assert is_leap(1992) == True

def test_hundred():
    assert is_leap(2100) == False
    assert is_leap(2200) == False
    assert is_leap(2300) == False

def test_four_hundred():
    assert is_leap(2400) == True
