import pytest

from ..__main__ import get_decent

def test_get_decent():
    assert get_decent(  1 ) == -1
    assert get_decent(  3 ) == 555
    assert get_decent(  5 ) == 33333
    assert get_decent( 11 ) == 55555533333
    assert get_decent( 14 ) == 55555555533333
    assert get_decent( 16 ) == 5555553333333333
