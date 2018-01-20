import pytest
from ..__main__ import all_or_nothing

def test_case_1():
    assert all_or_nothing([12,9,61,5,14]) == True
