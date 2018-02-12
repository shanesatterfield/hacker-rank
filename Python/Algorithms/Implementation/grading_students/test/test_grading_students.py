import pytest
from ..__main__ import grade_student


def test_case_1():
    assert 75 == grade_student(73)


def test_case_2():
    assert 67 == grade_student(67)


def test_case_3():
    assert 40 == grade_student(38)


def test_case_4():
    assert 33 == grade_student(33)
