import pytest
from ..__main__ import day_0

def test_case_1(capsys):
    day_0()
    output, err = capsys.readouterr()
    assert output == "Hello World.\nWelcome to 30 Days of Code.\n"
