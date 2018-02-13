import pytest
from ..__main__ import kangaroo


def test_case_1():
    assert kangaroo(0, 3, 4, 2)


def test_case_2():
    assert not kangaroo(0, 2, 5, 3)
