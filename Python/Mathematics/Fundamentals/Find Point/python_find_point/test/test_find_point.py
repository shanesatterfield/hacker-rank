import pytest
from ..__main__ import *

def test_case_1():
    assert find_point('0 0 1 1') == (2, 2)
