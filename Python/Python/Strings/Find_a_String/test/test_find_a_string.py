import pytest
from ..__main__ import *

def test_case_1():
    assert count_subs('ABCDCDC', 'CDC') == 2
