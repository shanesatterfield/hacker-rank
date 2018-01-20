import pytest
from ..__main__ import *

def test_case_1():
    expected = ['AB', 'CA', 'AD']
    assert merger('AABCAAADA', 3) == expected
