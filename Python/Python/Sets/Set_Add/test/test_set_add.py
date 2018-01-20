import pytest
from ..__main__ import seta

def test_case_1():
    assert seta(['UK','China','USA','France','New Zealand','UK','France']) == 5
