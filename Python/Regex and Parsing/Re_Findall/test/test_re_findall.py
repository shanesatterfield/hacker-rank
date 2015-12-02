import pytest
from ..__main__ import refindall

def test_case_1():
    assert refindall('rabcdeefgyYhFjkIoomnpOeorteeeeet') == ['ee','Ioo','Oeo','eeeee']

def test_no_answer():
    assert refindall('match a single character not present in the list below') == ['-1']
