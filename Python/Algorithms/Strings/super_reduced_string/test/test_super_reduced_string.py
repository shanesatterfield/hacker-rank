import pytest
from ..__main__ import super_reduce_string


def test_case_1():
    assert "abd" == super_reduce_string("aaabccddd")


def test_case_3():
    assert "Empty String" == super_reduce_string('baab')


def test_strip_2_of_3():
    assert 'a' == super_reduce_string('aaaaa')


def test_strip_to_empty():
    assert 'Empty String' == super_reduce_string('aabb')