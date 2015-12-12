import pytest
from ..__main__ import noidea

def test_case_1():
    assert noidea([1,5,3], [3,1], [5,7]) == 1
