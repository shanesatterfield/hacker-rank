import pytest
from ..__main__ import *

def get_printed(num):
    return "The final price of the meal is $" + str(num) + ".\n"

def test_case_1(capsys):
    day_2(12.00, 20, 8)
    output, err = capsys.readouterr()
    assert output == get_printed(15)
