import pytest

from ..__main__ import *

def test_case_1():
    assert is_pangram('We promptly judged antique ivory buckles for the next prize') == True

def test_case_2():
    assert is_pangram('We promptly judged antique ivory buckles for the prize') == False

def test_icase():
    assert is_pangram('We promptly judged antique ivory buckles for the next prize') == True
    assert is_pangram('We promptLy judGed Antique ivory buckles for the next prize') == True
    assert is_pangram('WE PROMPTLY JUDGED ANTIQUE IVORY BUCKLES FOR THE NEXT PRIZE') == True

    assert is_pangram('We promptly judged antique ivory buckles for the prize') == False
    assert is_pangram('WE PROMPTLY JUDGED ANTIQUE IVORY BUCKLES FOR THE PRIZE') == False
