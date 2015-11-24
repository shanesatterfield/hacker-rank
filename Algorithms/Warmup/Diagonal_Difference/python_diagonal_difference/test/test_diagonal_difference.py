import pytest
from ..__main__ import *

def test_case_1():
    assert diagonally([[11,2,4],[4,5,6],[10,8,-12]]) == 15
