import pytest
from ..__main__ import *

def test_case_1():
    assert nested([
        ['Harry', 37.21],
        ['Berry', 37.21],
        ['Tina', 37.2],
        ['Akriti', 41],
        ['Harsh', 39]
    ]) == ['Berry', 'Harry']

def test_case_2():
    assert nested([
        ['Prashant', 32],
        ['Pallavi', 36],
        ['Dheeraj', 39],
        ['Shivam', 40]
    ]) == ['Pallavi']
