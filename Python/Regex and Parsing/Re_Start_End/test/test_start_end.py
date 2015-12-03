import pytest
from ..__main__ import restart

def test_case_1():
    assert restart('aaadaa', 'aa') == [(0, 1),(1, 2),(4, 5)]

def test_no_matches():
    assert restart('abcdef', 'zz') == [(-1,-1)]

def test_one_match_found():
    assert restart('12345', '4') == [(3,3)]
