import pytest
from ..__main__ import *

def test_letter_in_middle():
    assert isFloat('4.0O0') == False

def test_letter_in_middle_valid():
    assert isFloat('4.000') == True

def test_negative_sign():
    assert isFloat('-1.00') == True

def test_positive_sign():
    assert isFloat('+4.54') == True

def test_some_text():
    assert isFloat('SomeRandomStuff') == False

def test_starts_with_dot_valid():
    assert isFloat('.45') == True

def test_starts_with_dot_invalid():
    assert isFloat('.4u3') == False

def test_starts_with_dot_invalid_multiple_dots():
    assert isFloat('.4.3') == False

def test_leading_letter_then_dot():
    assert isFloat('u.45') == False

def test_plus_in_middle():
    assert isFloat('.4+5') == False

def test_negative_in_middle():
    assert isFloat('.4-5') == False

def test_ends_with_dot():
    assert isFloat('45.') == False
