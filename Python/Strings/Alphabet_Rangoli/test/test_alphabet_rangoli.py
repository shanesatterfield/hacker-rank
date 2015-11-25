import pytest, random
from ..__main__ import rangoli

def test_iteration_negative():
    for n in range(100):
        assert rangoli(random.randint(-1000000, -1)) == []

def test_iteration_0():
    assert rangoli(0) == []

def test_iteration_1():
    assert rangoli(1) == ['a']

def test_iteration_2():
    assert rangoli(2) == [
        "--b--",
        "b-a-b",
        "--b--"
    ]

def test_iteration_3():
    assert rangoli(3) == [
        "----c----",
        "--c-b-c--",
        "c-b-a-b-c",
        "--c-b-c--",
        "----c----"
    ]

def test_iteration_5():
    assert rangoli(5) == [
        "--------e--------",
        "------e-d-e------",
        "----e-d-c-d-e----",
        "--e-d-c-b-c-d-e--",
        "e-d-c-b-a-b-c-d-e",
        "--e-d-c-b-c-d-e--",
        "----e-d-c-d-e----",
        "------e-d-e------",
        "--------e--------",
    ]

def test_iteration_10():
    assert rangoli(10) == [
        "------------------j------------------",
        "----------------j-i-j----------------",
        "--------------j-i-h-i-j--------------",
        "------------j-i-h-g-h-i-j------------",
        "----------j-i-h-g-f-g-h-i-j----------",
        "--------j-i-h-g-f-e-f-g-h-i-j--------",
        "------j-i-h-g-f-e-d-e-f-g-h-i-j------",
        "----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----",
        "--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--",
        "j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j",
        "--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--",
        "----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----",
        "------j-i-h-g-f-e-d-e-f-g-h-i-j------",
        "--------j-i-h-g-f-e-f-g-h-i-j--------",
        "----------j-i-h-g-f-g-h-i-j----------",
        "------------j-i-h-g-h-i-j------------",
        "--------------j-i-h-i-j--------------",
        "----------------j-i-j----------------",
        "------------------j------------------",
    ]
