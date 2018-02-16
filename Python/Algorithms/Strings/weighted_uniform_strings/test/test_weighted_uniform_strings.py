import pytest
from ..__main__ import calculate_weights, get_weight


def test_case_1():
    assert weight_in('abccddde', 1)


def test_case_2():
    assert weight_in('abccddde', 3)


def test_case_3():
    assert weight_in('abccddde', 12)


def test_case_4():
    assert weight_in('abccddde', 5)


def test_case_5():
    assert not weight_in('abccddde', 9)


def test_case_6():
    assert not weight_in('abccddde', 10)


def test_get_weight():
    assert get_weight('a') == 1
    assert get_weight('b') == 2
    assert get_weight('m') == 13
    assert get_weight('z') == 26


def weight_in(text: str, val: int) -> bool:
    return val in calculate_weights(text)
