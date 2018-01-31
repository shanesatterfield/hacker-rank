import pytest

from ..__main__ import *

def test_case_1():
    inputs = [1, 2, 3, 4, 5]
    mini, maxi = find_mini_max(inputs)
    assert mini == 10
    assert maxi == 14