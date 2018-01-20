import pytest
from ..__main__ import *

def test_insert():
    lst = MyList()
    inputs = ['insert 0 5', 'insert 1 10', 'insert 0 6']
    for n in inputs:
        lst.run_cmd(n)

    assert lst.lst == [6, 5, 10]

def test_remove():
    lst = MyList()
    inputs = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'remove 6']
    for n in inputs:
        lst.run_cmd(n)

    assert lst.lst == [5, 10]

def test_append():
    lst = MyList()
    inputs = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'remove 6', 'append 9', 'append 1']
    for n in inputs:
        lst.run_cmd(n)

    assert lst.lst == [5, 10, 9, 1]

def test_sort():
    lst = MyList()
    inputs = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'remove 6', 'append 9', 'append 1', 'sort']
    for n in inputs:
        lst.run_cmd(n)

    assert lst.lst == [1, 5, 9, 10]

def test_pop():
    lst = MyList()
    inputs = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'remove 6', 'append 9', 'append 1', 'sort', 'pop']
    for n in inputs:
        lst.run_cmd(n)

    assert lst.lst == [1, 5, 9]

def test_reverse():
    lst = MyList()
    inputs = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'remove 6', 'append 9', 'append 1', 'sort', 'pop', 'reverse']
    for n in inputs:
        lst.run_cmd(n)

    assert lst.lst == [9, 5, 1]

def test_print( capsys ):
    lst = MyList()
    inputs = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'remove 6', 'append 9', 'append 1', 'sort', 'pop', 'reverse', 'print']
    for n in inputs:
        lst.run_cmd(n)

    out, err = capsys.readouterr()
    assert out == '[9, 5, 1]\n'

def test_case_1( capsys ):
    lst = MyList()
    inputs = [
        'insert 0 5',
        'insert 1 10',
        'insert 0 6',
        'print',
        'remove 6',
        'append 9',
        'append 1',
        'sort',
        'print',
        'pop',
        'reverse',
        'print'
    ]

    for n in inputs: lst.run_cmd(n)
    out, err = capsys.readouterr()
    assert out == '[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]\n'
