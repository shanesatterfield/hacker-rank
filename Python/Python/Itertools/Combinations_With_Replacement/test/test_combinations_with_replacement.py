import pytest
from ..__main__ import *

def test_case_1():
    assert list(combs('HACK', 2)) == ['AA','AC','AH','AK','CC','CH','CK','HH','HK','KK']
