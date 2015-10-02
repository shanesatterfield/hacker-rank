import pytest
from ..__main__ import *

def test_case_1():
    assert time_convert('07:05:45PM') == '19:05:45'

def test_case_2():
    assert time_convert('12:40:22AM') == '00:40:22'

def test_case_3():
    assert time_convert('12:45:54PM') == '12:45:54'
