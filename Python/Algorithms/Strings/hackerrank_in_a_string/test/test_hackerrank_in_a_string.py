import pytest
from ..__main__ import contains_hackerrank


def test_case_1():
    assert contains_hackerrank('hereiamstackerrank')


def test_case_2():
    assert not contains_hackerrank('hackerworld')
