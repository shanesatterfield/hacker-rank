import pytest
from ..__main__ import *

def test_case_1():
    assert to_anagram('cde', 'abc') == 4
