import pytest

from ..__main__ import *

def test_case_1():
    assert is_pi_song('Can I have a large container of coffee right now') == True
    assert is_pi_song('Can I have a large container of tea right now') == False
    assert is_pi_song('Now I wish I could recollect pi Eureka cried the great inventor Christmas Pudding Christmas Pie Is the problems very center') == True

def test_case_2():
    assert is_pi_song("How I need a drink alcoholic in nature after the tough chapters involving quantum mechanics") == True
    assert is_pi_song("How I wish I could recollect pi easily today") == True
    assert is_pi_song("Hello world") == False
    assert is_pi_song("May I have a large container of coffee cream and sugar") == True
    assert is_pi_song("May I have a large container of coffee cream and sugar and cake") == False
