import pytest
from ..__main__ import *

def test_case_1():
    assert resplit('100,000,000.000') == ['100','000','000','000']

def test_multiple_delimiters():
    assert resplit('.172..16.52.207,172.16.52.117') == ['172','16','52','207','172','16','52','117']
