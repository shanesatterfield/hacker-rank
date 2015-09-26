import pytest
from ..__main__ import *

def test_case_1():
    assert extended_euclidean(1, 2, 3) == 1

def test_case_2():
    assert extended_euclidean(3, 4, 2) == 1

def test_case_3():
    assert extended_euclidean(4, -1, 5) == 4

def test_case_4():
    assert extended_euclidean(984877, 309, 328453) == 252015
