import pytest
from ..__main__ import delta

def test_case_1():
    assert delta('Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 +0000') == 25200

def test_case_2():
    assert delta('Sat 02 May 2015 19:54:36 +0530', 'Fri 01 May 2015 13:54:36 +0000') == 88200
