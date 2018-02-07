import pytest
from ..__main__ import count_camel_words


def test_case_1():
    assert 5 == count_camel_words('saveChangesInTheEditor')
