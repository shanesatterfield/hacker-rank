import pytest
from ..__main__ import *

def test_case_1():
    assert product([1,2], [3,4]) == [(1, 3),(1, 4),(2, 3),(2, 4)]
