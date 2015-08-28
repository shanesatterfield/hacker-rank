import pytest
from ..__main__ import *

def test_case_1():
    assert got('aaabbbb') == True

def test_case_2():
    assert got('cdefghmnopqrstuvw') == False

def test_case_3():
    assert got('cdcdcdcdeeeef') == True
