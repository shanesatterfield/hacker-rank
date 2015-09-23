import pytest
from ..__main__ import *

def test_case_1():
    assert most_common('aabbbccde') == [('b', 3), ('a', 2), ('c',2)]

def test_case_2():
    assert most_common('qwertyuiopasdfghjklzxcvbnm') == [('a',1),('b',1),('c',1)]
