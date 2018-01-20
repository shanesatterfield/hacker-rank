import pytest
from ..__main__ import mutate

def test_intersection_update():
    a = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,24,52}
    b = {2,3,5,6,8,9,1,4,7,11}
    c = a & b
    assert mutate('intersection_update', a, b) == c
    assert a == c

def test_update():
    a = {10, 12, 13, 14, 52, 24}
    b = {55, 66}
    c = a | b
    assert mutate('update', a, b) == c
    assert a == c

def test_symmetric_difference_update():
    a = {66, 52, 55, 24, 10, 12, 13, 14}
    b = {22, 7, 35, 62, 58}
    c = a ^ b
    assert mutate('symmetric_difference_update', a, b) == c
    assert a == c

def test_difference_update():
    a = {66, 35, 7, 10, 12, 13, 14, 52, 22, 55, 24, 58, 62}
    b = {11, 22, 35, 55, 58, 62, 66}
    c = a - b
    assert mutate('difference_update', a, b) == c
    assert a == c
