import pytest
from ..__main__ import *

def test_case_1():
    assert get_minimum_socks( 1 ) == 2

def test_case_2():
    assert get_minimum_socks( 2 ) == 3
