import pytest
from ..__main__ import stand

def test_case_1():
    assert stand(['07895462130','919875641230','9195969878']) == ['+91 78954 62130','+91 91959 69878','+91 98756 41230']
