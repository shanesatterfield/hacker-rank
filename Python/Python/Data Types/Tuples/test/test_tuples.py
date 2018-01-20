import pytest
from ..__main__ import *

def test_case_1():
    assert tuple_to_hash([1, 2]) == 3713081631934410656
