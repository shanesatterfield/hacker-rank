import pytest
from ..__main__ import birthday_cake_candles


def test_case_1():
    result = birthday_cake_candles(4, [3, 2, 1, 3])
    assert result == 2


def test_more_age():
    result = birthday_cake_candles(2, [3, 3, 3, 3, 3])
    assert result == 2


def test_not_as_many_as_age():
    result = birthday_cake_candles(10, [3, 3, 3, 3, 3])
    assert result == 5
