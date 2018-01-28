import pytest
from ..__main__ import *

def test_case_1():
    assert intro(4, [1,4,5,7,9,12]) == 1
