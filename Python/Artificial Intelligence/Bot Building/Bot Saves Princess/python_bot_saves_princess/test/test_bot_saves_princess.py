import pytest
from ..__main__ import *

def test_case_bottom_left():
    assert sorted(save_princess("---\n-m-\np--")) == sorted(['DOWN', 'LEFT'])

def test_case_bottom_right():
    assert sorted(save_princess("---\n-m-\n--p")) == sorted(['DOWN', 'RIGHT'])

def test_case_top_left():
    assert sorted(save_princess("p--\n-m-\n---")) == sorted(['UP', 'LEFT'])

def test_case_top_right():
    assert sorted(save_princess("--p\n-m-\n---")) == sorted(['UP', 'RIGHT'])

def test_list_or_string():
    input_string = "---\n-m-\np--"
    assert sorted(save_princess(input_string.split('\n'))) == sorted(save_princess(input_string))
