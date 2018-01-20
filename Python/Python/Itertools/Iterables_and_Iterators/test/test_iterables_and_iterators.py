import pytest
from ..__main__ import iterab

def test_case_1():
    assert iterab(['a', 'a', 'c', 'd'], 2) == 0.8333
