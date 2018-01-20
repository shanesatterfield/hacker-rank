import pytest
from ..__main__ import *

def test_case_1():
    assert big_sum([1000000001,1000000002,1000000003,1000000004,1000000005]) == 5000000015
