import pytest
from ..__main__ import get_record_breaks


def test_zeroes_on_null_inputs():
    a, b = get_record_breaks(None)
    assert a == 0
    assert b == 0


def test_zeroes_on_empty_scores_list():
    a, b = get_record_breaks([])
    assert a == 0
    assert b == 0


def test_zeroes_on_first_score():
    a, b = get_record_breaks([100])
    assert a == 0
    assert b == 0


def test_new_max_twice():
    new_max, _ = get_record_breaks(list(range(3)))
    assert new_max == 2


def test_new_min_twice():
    _, new_min = get_record_breaks([x for x in range(3)][::-1])
    assert new_min == 2


def test_calculates_record_breaks():
    scores = [10, 11, 12, 13, 23, 15, 9, 8, 7]
    new_max, new_min = get_record_breaks(scores)
    assert new_max == 4
    assert new_min == 3
