import pytest
from ..__main__ import caesar

def test_case_1():
    assert caesar('middle-Outz', 2) == 'okffng-Qwvb'
