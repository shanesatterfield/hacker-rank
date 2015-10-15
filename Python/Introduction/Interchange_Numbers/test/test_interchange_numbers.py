import pytest
from ..__main__ import *

def test_case_1():
    assert interchange(2, 1) == (1, 2)
