import pytest
from ..__main__ import pyeval

def test_case_1(capsys):
    pyeval('print(2 + 3)')
    output, err = capsys.readouterr()
    assert output == '5\n'
