import pytest
from ..__main__ import compress

def test_case_1():
    assert compress('1222311') == [(1, 1), (3, 2), (1, 3), (2, 1)]
