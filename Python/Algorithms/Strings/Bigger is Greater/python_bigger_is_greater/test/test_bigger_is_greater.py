import pytest

from ..__main__ import *

def test_case_1():
    assert greater('ab') == 'ba'

def test_case_2():
    assert greater('bb') == 'no answer'

def test_case_3():
    assert greater('hefg') == 'hegf'

def test_case_4():
    assert greater('dhck') == 'dhkc'

def test_case_5():
    assert greater('dkhc') == 'hcdk'
