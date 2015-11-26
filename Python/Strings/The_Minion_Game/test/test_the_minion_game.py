import pytest
from ..__main__ import *

def test_case_1():
    assert minion('BANANA') == [player[1], 12]

def test_case_2():
    assert minion('naan') == ['Draw']

def test_case_3():
    assert minion('BANANANAAAS') == ['Draw']

def test_case_4():
    with open('./input2.txt', 'r') as f:
        assert minion(f.read().rstrip()) == ['Stuart', 7501500]
