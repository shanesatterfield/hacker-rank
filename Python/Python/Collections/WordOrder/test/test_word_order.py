import pytest
from ..__main__ import word_order

def test_case_1():
    input_data = [
        'bcdef',
        'abcdefg',
        'bcde',
        'bcdef',
    ]
    assert word_order(input_data) == [3,[2,1,1]]
