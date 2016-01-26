import pytest
from ..__main__ import ordered_insert

def test_case_1():
    input_data = [
        ('BANANA FRIES', 12),
        ('POTATO CHIPS', 30),
        ('APPLE JUICE', 10),
        ('CANDY', 5),
        ('APPLE JUICE', 10),
        ('CANDY', 5),
        ('CANDY', 5),
        ('CANDY', 5),
        ('POTATO CHIPS', 30),
    ]

    expected = [('BANANA FRIES', 12),('POTATO CHIPS', 60),('APPLE JUICE', 20),('CANDY', 20)]
    assert ordered_insert(input_data) == expected
