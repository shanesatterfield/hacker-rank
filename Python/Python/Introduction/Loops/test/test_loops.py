import pytest
from ..__main__ import *

def test_case_1():
    assert loops(5) == [0,1,4,9,16]
