import pytest
from ..__main__ import introd

def test_case_1():
    assert introd([161,182,161,154,176,170,167,171,170,174]) == 169.375
