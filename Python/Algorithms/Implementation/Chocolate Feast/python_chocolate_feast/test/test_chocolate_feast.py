import py.test

from ..__main__ import feast

def test_case_1():
    assert feast( 10, 2, 5 ) == 6
    assert feast( 12, 4, 4 ) == 3
    assert feast(  6, 2, 2 ) == 5
