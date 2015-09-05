import pytest
from ..__main__ import *

def test_case_1():
    assert validate('qA1') == [True, True, True, True, True]
