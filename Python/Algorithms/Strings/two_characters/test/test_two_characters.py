import pytest
from ..__main__ import reduce_to_two


def test_case_1():
    return 5 == reduce_to_two('beabeefeab')
