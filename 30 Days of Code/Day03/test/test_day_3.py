import pytest
from ..__main__ import day3

def test_odd_numbers():
    for n in range(-99,151,2):
        assert day3(n) == 'Weird'

def test_even_between_2_and_5():
    for n in range(2, 5+1, 2):
        assert day3(n) == 'Not Weird'

def test_even_greater_than_20():
    for n in range(22, 151, 2):
        assert day3(n) == 'Not Weird'

def test_even_between_6_and_20():
    for n in range(6, 20+1, 2):
        assert day3(n) == 'Weird'
