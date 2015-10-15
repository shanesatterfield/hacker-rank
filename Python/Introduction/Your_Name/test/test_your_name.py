import pytest
from ..__main__ import *

def test_case_1():
    assert greet('Guido', 'Rossum') == 'Hello Guido Rossum! You just delved into python.'
