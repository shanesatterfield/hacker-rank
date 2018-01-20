import pytest
from ..__main__ import *

def test_case_1():
    assert encryption('haveaniceday') == 'hae and via ecy'

def test_case_2():
    assert encryption('feedthedog') == 'fto ehg ee dd'

def test_case_3():
    assert encryption('chillout') == 'clu hlt io'

def test_case_4():
    assert encryption('ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots') == 'imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau'
