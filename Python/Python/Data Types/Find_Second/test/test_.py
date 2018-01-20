import pytest
from ..__main__ import *

def test_case_1():
    assert second_largest([2,3,6,6,5]) == 5
