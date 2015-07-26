import pytest

from ..__main__ import *

def test_case_1():
    assert mutate('abracadabra', 5, 'k') == 'abrackdabra'
