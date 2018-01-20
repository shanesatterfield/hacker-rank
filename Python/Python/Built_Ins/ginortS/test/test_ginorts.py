import pytest
from ..__main__ import ginorts

def test_case_1():
    assert ginorts('Sorting1234') == 'ginortS1324'

def test_sorting_even_and_odd_numbers():
    assert ginorts('0123456789') == '1357902468'

def test_sorting_lower_case_letters_same():
    arr = [chr(x) for x in range(ord('a'), ord('z')+1)]
    assert ginorts(arr) == ''.join(arr)

def test_sorting_upper_case_letters_same():
    arr = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    assert ginorts(arr) == ''.join(arr)

def test_lower_before_upper():
    arr = [chr(x) for x in range(ord('a'), ord('z')+1)]
    arr.extend([chr(x) for x in range(ord('A'), ord('Z')+1)])
    assert ginorts(arr) == ''.join(arr)

def test_upper_before_digits():
    arr = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    arr.extend('0123456789')
    assert ginorts(arr) == ''.join([chr(x) for x in range(ord('A'), ord('Z')+1)] + list('1357902468'))
