import pytest
from ..__main__ import *

def test_case_1():
    assert restaurant(38,   751) == 28538
    assert restaurant(344,  734) == 63124
    assert restaurant(165,  635) == 4191
    assert restaurant(297,  667) == 198099
    assert restaurant(917,  264) == 242088
    assert restaurant(544,  642) == 87312
    assert restaurant(254,  914) == 58039
    assert restaurant(612,  50)  == 7650
    assert restaurant(94,   707) == 66458
    assert restaurant(564,  417) == 26132
    assert restaurant(145,  246) == 35670

def test_case_2():
    assert restaurant(309, 528) == 18128
    assert restaurant(577, 101) == 58277
    assert restaurant(371, 314) == 116494
    assert restaurant(207, 346) == 71622
    assert restaurant(284, 715) == 203060
    assert restaurant(178, 791) == 140798
    assert restaurant(725, 295) == 8555
    assert restaurant(796, 916) == 45571
    assert restaurant(667, 231) == 154077
    assert restaurant(282, 302) == 21291
    assert restaurant(984, 882) == 24108
    assert restaurant(718, 844) == 151498
    assert restaurant(372, 749) == 278628
    assert restaurant(735, 419) == 307965
    assert restaurant(979, 914) == 894806
    assert restaurant(444, 837) == 41292
    assert restaurant(715, 67)  == 47905
    assert restaurant(381, 22)  == 8382
    assert restaurant(367, 87)  == 31929
    assert restaurant(801, 365) == 292365
    assert restaurant(157, 429) == 67353
    assert restaurant(723, 756) == 60732
    assert restaurant(673, 882) == 593586
    assert restaurant(890, 520) == 4628
    assert restaurant(599, 342) == 204858

def test_case_3():
    assert restaurant(2, 2) == 1
    assert restaurant(6, 9) == 6

def test_gcd_sames():
    assert gcd(1, 1)   == 1
    assert gcd(20, 20) == 20
    assert gcd(3, 3)   == 3

def test_gcd_swappable():
    a, b = 32, 24
    assert gcd(a, b) == gcd(b, a)

def test_gcd_only_ones():
    assert gcd(5, 13)  == 1
    assert gcd(18, 25) == 1
    assert gcd(1, 3)   == 1
    assert gcd(2, 9)   == 1

def test_gcd_mults_of_5():
    assert gcd(25, 30) == 5
    assert gcd(40, 60) == 20
    assert gcd(45, 50) == 5

def test_gcd_random_test_cases():
    assert gcd(12341234, 4343214) == 2
    assert gcd(5628, 9056)        == 4
