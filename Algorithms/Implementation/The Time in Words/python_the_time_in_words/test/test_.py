import pytest
from ..__main__ import *

def test_o_clock():
    assert word_time(5, 0) == "five o'clock"

def test_1_past_five():
    assert word_time(6, 1) == 'one minute past six'

def test_10_past_five():
    assert word_time(7, 10) == 'ten minutes past seven'

def test_half_past():
    assert word_time(8, 30) == 'half past eight'

def test_twenty_to():
    assert word_time(9, 40) == 'twenty minutes to ten'

def test_quarter():
    assert word_time(10, 45) == 'quarter to eleven'

def test_13_to():
    assert word_time(5, 47) == 'thirteen minutes to six'

def test_28_to():
    assert word_time(5, 28) == 'twenty eight minutes past five'
