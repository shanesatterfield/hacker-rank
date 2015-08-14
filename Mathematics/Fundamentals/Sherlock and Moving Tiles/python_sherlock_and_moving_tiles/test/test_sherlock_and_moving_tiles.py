import pytest
from ..__main__ import *

delta = 0.0001

def test_case_1():
    expected = 4.1421
    actual = get_time( 10, 1, 2, 50 )
    assert actual >= expected - delta or actual <= expected + delta

def test_case_2():
    expected = 0.0
    actual = get_time( 10, 1, 2, 100 )
    assert actual >= expected - delta or actual <= expected + delta

