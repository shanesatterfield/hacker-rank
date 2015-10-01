import pytest
from ..__main__ import *

def test_case_1():
    assert pm([-4,3,-9,0,4,1]) == [0.500,0.333,0.167]
