import pytest
from ..__main__ import *

def test_case_1():
    assert text_wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4) == [
        'ABCD',
        'EFGH',
        'IJKL',
        'IMNO',
        'QRST',
        'UVWX',
        'YZ']
