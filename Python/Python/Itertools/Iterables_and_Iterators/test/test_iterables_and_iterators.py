import pytest
from ..__main__ import iterab

def test_case_1():
    result = iterab(['a', 'a', 'c', 'd'], 2)
    assert round(result, 4) == 0.8333
