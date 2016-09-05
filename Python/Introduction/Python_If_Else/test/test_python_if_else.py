import pytest
from ..__main__ import *

def test_odd():
    for n in range(1, 1000, 2):
        assert weird(n) == 'Weird'

def test_2_through_5():
    for n in range(2, 5, 2):
        assert weird(n) == 'Not Weird'

def test_greater_than_20():
    for n in range(22, 1000, 2):
        assert weird(n) == 'Not Weird'

def test_6_through_20():
    for n in range(6, 20 + 1, 2):
        assert weird(n) == 'Weird'
