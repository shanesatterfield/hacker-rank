import pytest
from ..__main__ import *

round_amount = 5

def rounder(num):
    return round(num, round_amount)

def test_case_1_r():
    assert rounder(get_r(1, 2)) == rounder(2.23606797749979)

def test_case_1_phi():
    assert rounder(get_phi(1, 2)) == rounder(1.1071487177940904)

def test_case_2_r():
    assert rounder(get_r(-1, -5)) == rounder(5.09901951359)

def test_case_2_phi():
    assert rounder(get_phi(-1, -5)) == rounder(-1.76819188664)
