import pytest

from ..__main__ import *

def test_case_1():
    assert squares_interval(  3,  9 ) == 2
    assert squares_interval( 17, 24 ) == 0

def test_same_interval_inclusive():
    assert squares_interval( 2, 2 ) == 0
    assert squares_interval( 3, 3 ) == 0
    assert squares_interval( 4, 4 ) == 1
    assert squares_interval( 9, 9 ) == 1

def test_between_two_squares():
    assert squares_interval( 4,  9 ) == 2
    assert squares_interval( 4, 16 ) == 3

def test_is_square():
    assert is_square(  2 ) == False
    assert is_square(  3 ) == False
    assert is_square(  4 ) == True
    assert is_square(  5 ) == False
    assert is_square(  9 ) == True
    assert is_square( 10 ) == False
    assert is_square( 11 ) == False
    assert is_square( 12 ) == False
    assert is_square( 16 ) == True
