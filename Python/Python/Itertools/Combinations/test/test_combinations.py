import pytest
from ..__main__ import *

def test_case_1():
    assert combs('HACK', 2) == ['A','C','H','K','AC','AH','AK','CH','CK','HK']
