import pytest
from ..__main__ import capitalize

def test_case_1():
    assert capitalize('hello world') == 'Hello World'
