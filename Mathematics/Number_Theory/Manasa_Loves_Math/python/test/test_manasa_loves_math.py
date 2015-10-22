import pytest
from ..__main__ import *

def test_case_1():
    assert manasa(61) == True

def test_case_2():
    assert manasa(75) == False

def test_case_3():
    assert manasa(8) == True

def test_case_4():
    assert manasa(86) == False

def test_case_5():
    assert manasa(656411992834780769) == True

def test_case_6():
    assert manasa(16) == True

def test_case_7():
    assert manasa(797428283417050169664035301) == True

def test_case_8():
    assert manasa(291980408812221272653210455978306606766749171310795237202791534316) == True

def test_case_9():
    assert manasa(43868777129190746666867112574182580480192224310976772496745185534692813255607614584953) == True

def test_case_10():
    assert manasa(83) == False

def test_case_11():
    assert manasa(73) == False

def test_case_12():
    assert manasa(18) == False

def test_case_13():
    assert manasa(8448486719387376743582010404904250098991820779343623144397709446477366668838892354781310) == True

def test_case_14():
    assert manasa(82) == False

def test_case_15():
    assert manasa(66779474231821129045812825048181651718431715857074577769465473851122988251046944391087145) == True

def test_case_16():
    assert manasa(8507918459233853433898) == True

def test_case_17():
    assert manasa(50920389229) == True

def test_case_18():
    assert manasa(55) == False

def test_case_19():
    assert manasa(89700340094344533824048032524) == True

def test_case_20():
    assert manasa(2674899409564019369510192517978637237199245848875) == True

def test_case_21():
    assert manasa(7796743832620192685579958636585267033346528850018868773558319155051) == True

def test_case_22():
    assert manasa(289590340650638323102631988931438487643620883718048413701624967827783165153747741) == True

def test_case_23():
    assert manasa(750873417676425329696060907660575764025) == True

def test_case_24():
    assert manasa(7554628914084603) == True

def test_case_25():
    assert manasa(70) == False

def test_case_26():
    assert manasa(406465225674529102995695275874146004547104578799108880439119843445809) == True

def test_case_27():
    assert manasa(74) == False

def test_case_28():
    assert manasa(73) == False

def test_case_29():
    assert manasa(6372102293456569445900412585925055285626161740884687648808591218738511139523514) == True

def test_case_30():
    assert manasa(78) == False

def test_case_31():
    assert manasa(69) == True

def test_case_32():
    assert manasa(6958729040045897120392645284681596368385589160804034210040409658) == True

def test_case_33():
    assert manasa(1754401212012072517) == True
