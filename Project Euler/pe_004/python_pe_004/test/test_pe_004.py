import pytest
from ..__main__ import pe_004

def test_case_1():
    assert pe_004(101110) == 101101

def test_case_2():
    assert pe_004(800000) == 793397
