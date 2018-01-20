import pytest
from ..__main__ import day06

def test_negative():
    assert day06(-1) == []

def test_zero_height():
    assert day06(0) == []

def test_height_1():
    assert day06(1) == ['#']

def test_height_2():
    assert day06(2) == [' #', '##']

def test_height_6():
    assert day06(6) == [
         '     #',
         '    ##',
         '   ###',
         '  ####',
         ' #####',
         '######'
    ]
