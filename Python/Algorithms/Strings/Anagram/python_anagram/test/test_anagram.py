import pytest
from ..__main__ import *

def test_case_1():
    assert anagram('aaabbb') == 3

def test_case_2():
    assert anagram('ab') == 1

def test_case_3():
    assert anagram('abc') == -1

def test_case_4():
    assert anagram('mnop') == 2

def test_case_5():
    assert anagram('xyyx') == 0

def test_case_6():
    assert anagram('xaxbbbxx') == 1
