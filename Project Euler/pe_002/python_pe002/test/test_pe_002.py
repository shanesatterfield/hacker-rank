from __future__ import print_function, division, generators

import pytest

from ..__main__ import *
import math

def test_case_1():
    assert fib( 10 ) == 10

def test_case_2():
    assert fib( 100 ) == 44

# Test for runtime errors for largest input
def test_edge_large_n():
    assert fib( 4 * math.pow(10, 6) )
