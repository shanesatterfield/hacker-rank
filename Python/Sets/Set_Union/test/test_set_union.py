import pytest
from ..__main__ import setunion

def test_case_1():
    assert setunion([1,2,3,4,5,6,7,8,9], [10,1,2,3,11,21,55,6,8]) == 13
