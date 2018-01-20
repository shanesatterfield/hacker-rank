import pytest
from ..__main__ import *

def test_case_1():
    percentage_store([['Krishna','67','68','69'],['Arjun','70','98','63'],['Malika','52','56','60']])
    assert finding('Malika') == '56.00'
