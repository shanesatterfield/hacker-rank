import pytest
from ..__main__ import *

def test_case_1():
    assert flip(2147483647) == 2147483648

def test_case_2():
    assert flip(1) == 4294967294

def test_case_3():
    assert flip(0) == 4294967295
