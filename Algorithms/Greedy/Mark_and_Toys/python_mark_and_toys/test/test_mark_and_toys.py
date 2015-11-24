import pytest
from ..__main__ import max_toys

def test_case_1():
    assert max_toys(50, [1,12,5,111,200,1000,10]) == 4
