import pytest
from ..__main__ import *

def test_case_1():
    assert sym(set([2,4,5,9]), set([2,4,11,12])) == [5, 9, 11, 12]
