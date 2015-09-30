import pytest
from ..__main__ import *

def test_case_1():
    assert manasa(1) == 5

def test_case_2():
    assert manasa(2) == 10

def test_case_3():
    assert manasa(3) == 15
