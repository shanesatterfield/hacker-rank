import pytest
from ..__main__ import zippy

def test_case_1():
    assert zippy([
        [89, 90, 78, 93, 80],
        [90, 91, 85, 88, 86],
        [91, 92, 83, 89, 90.5]
    ]) == [90.0, 91.0, 82.0, 90.0, 85.5 ]
