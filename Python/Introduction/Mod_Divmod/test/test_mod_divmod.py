import pytest
from ..__main__ import *

def test_case_1():
    assert divmod(177, 10) == (17, 7)
