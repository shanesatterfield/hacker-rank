import pytest
from ..__main__ import *

def test_case_1():
    assert check_ss('hello', 'world') == True

def test_case_2():
    assert check_ss('hi', 'world') == False

def test_case_3():
    assert check_ss('dapkqnowwvdrknfvcmanjuroumppajrzklucroxvpfmcsclqa', 'ivtnjtgiogmwhqybjaxlktqbwsdhqrwovoavetymkpcco') == True

def test_case_4():
    assert check_ss('hrtybirxncuiailznohfawjwipdtupnxnisbwcplozwrzt', 'ngdmqotxkpnuhmpfmajthzdtnztrqyugendiublcwp') == True

def test_case_5():
    assert check_ss('rmpwlddwttapjzhdldjmuhmgruufltzszprzdcziigc', 'bbvvkeqkqekqqennyxqxkxnyxnyqnnybnbvnyqqe') == False

def test_case_6():
    assert check_ss('annbjookwtqkoivcgbqckqtvgvktobctktgkkjiac', 'zsspfhmzpurrrlurdsdlrfldzyldfhudfedrszdpmsudh') == False

def test_case_7():
    assert check_ss('yuuuydwovzawzamvydaaadkakukpynwfmpnmuaazokxkmjxawo', 'rqiqbhgscsetgihrrrgsqrlqgcbcbrettlehbeistbiqbisie') == False

def test_case_8():
    assert check_ss('ibvmfltfdvlmentbfdemebbnvllfneeefnaamtblt', 'gukzzrqruyxsrqhyuggkrjujkwjhqhqsrqgkrkqxpszrzk') == False

def test_case_9():
    assert check_ss('nakqzfroqouhgunxqvqbxwtibfodsvoilqrpvhtgzoholxd', 'bqluorjgkkrvmiptnxegxwlhrstiiafbfoxodzyguhdwi') == True

def test_case_10():
    assert check_ss('oyvgelovlyevhhedoeolyhdevcvhgceydcdehgvoc', 'wsqswjnjpiarszzzxpmptrquwbnbzqiqqtzqnbajnpsjfaxr') == False

def test_case_11():
    assert check_ss('hvkmgwawagozzabgmdmdvbbaxadawmbazvxohxzv', 'sfiltrslqepytjpfffqlrpejiueftrnisnnppnlpuficrjys') == False

def test_case_12():
    assert check_ss('nvsovybaljmzenkfgayfoxzcjantbdidxflbkhbixgzk', 'qdphnbrjmznztnphhutkdbwjzmjwugtxggxchzcidngplj') == True
