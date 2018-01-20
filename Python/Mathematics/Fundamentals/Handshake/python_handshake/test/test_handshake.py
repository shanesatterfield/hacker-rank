import pytest
from ..__main__ import handshakes

def test_negative():
    assert handshakes(-1) == 0

def test_zero():
    assert handshakes(0) == 0

def test_1():
    assert handshakes(1) == 0

def test_2():
    assert handshakes(2) == 1

def test_3():
    assert handshakes(3) == 3

def test_4():
    assert handshakes(4) == 6
