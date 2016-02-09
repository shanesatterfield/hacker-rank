import pytest

from ..__main__ import *

def test_case_1():
    assert fizzbuzz(  10 ) == 23

def test_case_2():
    assert fizzbuzz( 100 ) == 2318

def test_edge_large():
    assert fizzbuzz( 1000000000 )

def test_edge_small():
    assert fizzbuzz( 1 ) == 0
