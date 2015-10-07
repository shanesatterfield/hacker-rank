import pytest
from ..__main__ import *

def test_case_1():
    assert mod_power(3,4,5) == (81, 1)
