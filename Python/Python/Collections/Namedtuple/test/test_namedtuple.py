import pytest
from ..__main__ import ntup

def test_case_1():
    input_data = [
        ['5'],
        ['ID', 'MARKS', 'NAME', 'CLASS'],
        ['1', '97', 'Raymond', '7'],
        ['2', '50', 'Steven',  '4'],
        ['3', '91', 'Adrian',  '9'],
        ['4', '72', 'Stewart', '5'],
        ['5', '80', 'Peter',   '6'],
    ]
    assert ntup(input_data) == '78.00'

def test_case_2():
    input_data = [
        ['5'],
        ['MARKS', 'CLASS', 'NAME', 'ID'],
        ['92', '2', 'Calum',  '1'],
        ['82', '5', 'Scott',  '2'],
        ['94', '2', 'Jason',  '3'],
        ['55', '8', 'Glenn',  '4'],
        ['82', '2', 'Fergus', '5'],
    ]
    assert ntup(input_data) == '81.00'
