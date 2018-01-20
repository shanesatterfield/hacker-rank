import pytest
from ..__main__ import *

def test_case_1():
    assert count_gems(['abcdde', 'baccd', 'eeabg']) == 2
