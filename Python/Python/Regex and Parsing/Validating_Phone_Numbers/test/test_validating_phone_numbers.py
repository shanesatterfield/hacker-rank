import pytest
from ..__main__ import valphone

def test_case_1():
    assert valphone('9587456281') == True

def test_case_2():
    assert valphone('1252478965') == False
