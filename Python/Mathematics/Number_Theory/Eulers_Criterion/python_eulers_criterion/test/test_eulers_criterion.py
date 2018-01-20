import pytest
from ..__main__ import *

def test_case_1():
    assert eulers_criterion(5, 7) == False

def test_case_2():
    assert eulers_criterion(4, 7) == True

def test_case_3():
    assert eulers_criterion(83715323, 118299443) == False

def test_case_4():
    assert eulers_criterion(556588044, 646429061) == True

def test_case_5():
    assert eulers_criterion(0, 41) == True

def test_case_6():
    assert eulers_criterion(193548814, 722391517) == True
