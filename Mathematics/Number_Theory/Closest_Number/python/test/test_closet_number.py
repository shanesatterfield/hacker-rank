import pytest
from ..__main__ import *

def test_case_1():
    assert closest(349, 1, 4) == 348

def test_case_2():
    assert closest(395, 1, 7) == 392

def test_case_3():
    assert closest(4, -2, 2) == 0
