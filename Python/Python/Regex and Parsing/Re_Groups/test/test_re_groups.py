import pytest
from ..__main__ import regroups

def test_case_1():
    assert regroups('..12345678910111213141516171820212223') == '1'

def test_case_2():
    assert regroups('__commit__') == 'm'

def test_case_3():
    assert regroups('__init__') == '-1'
