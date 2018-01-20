import pytest
from ..__main__ import resub

def test_and_switch():
    assert resub(' && ') == ' and '

def test_or_switch():
    assert resub(' || ') == ' or '

def test_and_statement():
    assert resub('if a + b > 0 && a - b < 0:') == 'if a + b > 0 and a - b < 0:'

def test_dont_change_threes():
    assert resub('#Note do not change &&& or ||| or & or |') == '#Note do not change &&& or ||| or & or |'

def test_dont_change_without_spaces():
    assert resub('#Only change those \'&&\' which have space on both sides.') == "#Only change those '&&' which have space on both sides."

def test_dont_change_with_only_one_space():
    assert resub("#Only change those '|| which have space on both sides.") == "#Only change those '|| which have space on both sides."

def test_case_1():
    assert resub("""x| ||&|& | & | &&  &&x
x& & |&||  || &&& & &x
x| &&||&& |  & |  |||x
x|&&& |&||  &|& |&|| x
x&& |   | ||&| |&|| &x
x|& &||& && &&&  &&| x
x|& &| | |&|& &  &| |x
x &&& |& & &||&|&&||&x
x  & &&| && ||  ||  |x
x&&& &&&  &|  || | ||x
x|&|& &&  |&   &|||&|x
x    &&&|&&| ||&&& &&x
x  & || |&&&&&|&&&&| x
x|&|&&&|&| || | &||& x
x&& |&|   |& &&&| && x
x &    &&&&& &|& &| |x
x|& & |   & |&  | |&|x
x&|&|&||||| &|&& || |x
x&|&  &&  |&|  &&&||&x
x || & | &&  &|&| |&|x""") == """x| ||&|& | & | and  &&x
x& & |&||  or &&& & &x
x| &&||&& |  & |  |||x
x|&&& |&||  &|& |&|| x
x&& |   | ||&| |&|| &x
x|& &||& and &&&  &&| x
x|& &| | |&|& &  &| |x
x &&& |& & &||&|&&||&x
x  & &&| and or  or  |x
x&&& &&&  &|  or | ||x
x|&|& and  |&   &|||&|x
x    &&&|&&| ||&&& &&x
x  & or |&&&&&|&&&&| x
x|&|&&&|&| or | &||& x
x&& |&|   |& &&&| and x
x &    &&&&& &|& &| |x
x|& & |   & |&  | |&|x
x&|&|&||||| &|&& or |x
x&|&  and  |&|  &&&||&x
x or & | and  &|&| |&|x"""
