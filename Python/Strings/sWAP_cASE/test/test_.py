import pytest
from ..__main__ import *

def test_case_1():
    assert swap_case('HackerRank.com presents "Pythonist 2".') == 'hACKERrANK.COM PRESENTS "pYTHONIST 2".'
