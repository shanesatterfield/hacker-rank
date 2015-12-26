import pytest
from ..__main__ import defaultdict

def test_case_1():
    assert defaultdict(['a','a','b','a','b'],['a','b','c']) == [[1,2,4],[3,5],[-1]]
