import pytest, random
from ..__main__ import sherlock

# Shuffles a string in place and returns the value.
def shuffle(string):
    temp = list(string)
    random.shuffle(temp)
    return ''.join(temp)

def test_shuffler():
    test_string = 'asdfasdf'
    assert sorted(shuffle(test_string)) == sorted(test_string)

def test_one_at_end():
    assert sherlock(shuffle('aaabbbc')) == True

def test_one_at_beginning():
    assert sherlock(shuffle('abbcc')) == True

def test_two_at_end():
    assert sherlock(shuffle('aabbcd')) == False

def test_two_at_beginning():
    assert sherlock(shuffle('cdaabb')) == False

def test_one_at_middle():
    assert sherlock(shuffle('aabdbcc')) == True

def test_two_at_middle():
    assert sherlock(shuffle('aabdebcc')) == False

def test_works_with_space_valid():
    assert sherlock(shuffle('a abdbcc ')) == True

def test_works_with_spaces_invalid():
    assert sherlock(shuffle('aabdbcc ')) == False

def test_remove_additional_ones():
    assert sherlock(shuffle('aaabbbcccc')) == True
