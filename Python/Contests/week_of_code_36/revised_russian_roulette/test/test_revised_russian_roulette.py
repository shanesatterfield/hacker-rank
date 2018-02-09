import pytest
from ..__main__ import roulette


def test_case_1():
    assert (3, 6) == roulette([0, 1, 1, 0, 1, 1, 1, 1, 0, 0])


def test_case_2():
    assert (4, 7) == roulette([0, 1, 1, 0, 1, 1, 1, 1, 0, 1])
