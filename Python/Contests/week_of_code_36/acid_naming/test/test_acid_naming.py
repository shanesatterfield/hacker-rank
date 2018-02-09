import pytest
from ..__main__ import Acid, name_acid


def test_case_1():
    assert Acid.NON_METAL == name_acid('hydrochloric')


def test_case_2():
    assert Acid.POLYATOMIC == name_acid('rainbowic')


def test_case_3():
    assert Acid.NOT_ACID == name_acid('idontevenknow')
