import pytest
from ..__main__ import *

def test_case_1():
    assert sorted(manasa(3, 1, 2)) == sorted([2, 3, 4])

def test_case_2():
    assert sorted(manasa(4, 10, 100)) == sorted([30, 120, 210, 300])

def test_edge_case_n():
    assert sorted(manasa(1000, 10, 100))
