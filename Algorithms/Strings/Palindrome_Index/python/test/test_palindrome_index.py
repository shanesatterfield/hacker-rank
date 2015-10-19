import pytest
from ..__main__ import *

def test_case_1():
    assert mkpal('aaab') == 3

def test_case_2():
    assert mkpal('baa') == 0

def test_case_3():
    assert mkpal('aaa') == -1

def test_case_4():
    assert mkpal('hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh') == 44

def test_already_palindrome_even():
    assert mkpal('abcddcba') == -1

def test_already_palindrome_odd():
    assert mkpal('abcdcba') == -1

def test_first_wrong():
    assert mkpal('zabcddcba') == 0

def test_last_wrong():
    assert mkpal('abcddcbaz') == 8

def test_middle_wrong_left():
    assert mkpal('abzcddcba') == 2

def test_middle_wrong_right():
    assert mkpal('abcddczba') == 6

def test_edge_case_large():
    string = 'l'*100005
    index = 12345
    string = string[:index] + 'z' + string[index+1:]
    assert mkpal(string) == index
