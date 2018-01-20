import pytest
from ..__main__ import sort_data

arr = [
    [10,  2,  5],
    [ 7,  1,  0],
    [ 9,  9,  9],
    [ 1, 23, 12],
    [ 6,  5, 91],
]

def test_sort_row_0():
    assert sort_data(arr, 0) == [
        [ 1, 23, 12],
        [ 6,  5, 91],
        [ 7,  1,  0],
        [ 9,  9,  9],
        [10,  2,  5],
    ]

def test_sort_row_1():
    assert sort_data(arr, 1) == [
        [ 7,  1,  0],
        [10,  2,  5],
        [ 6,  5, 91],
        [ 9,  9,  9],
        [ 1, 23, 12],
    ]

def test_sort_row_2():
    assert sort_data(arr, 2) == [
        [ 7,  1,  0],
        [10,  2,  5],
        [ 9,  9,  9],
        [ 1, 23, 12],
        [ 6,  5, 91],
    ]
