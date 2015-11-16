import pytest
from ..__main__ import *

def test_case_1():
    assert sherlock([1,2,3]) == False

def test_case_2():
    assert sherlock([1,2,3,3]) == True
