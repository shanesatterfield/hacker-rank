import pytest
from ..__main__ import *

def test_case_1():
    assert vemail('lara@hackerrank.com') == True

def test_case_2():
    assert vemail('brian-23@hackerrank.com') == True

def test_case_3():
    assert vemail('britts_54@hackerrank.com') == True

def test_case_4_list():
    assert val_emails([
        'lara@hackerrank.com',
        'brian-23@hackerrank.com',
        'britts_54@hackerrank.com'
    ]) == ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
