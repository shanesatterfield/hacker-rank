import pytest
from ..__main__ import *

def test_case_1():
    assert simple_sum([1,2,3,4,10,11]) == 31
