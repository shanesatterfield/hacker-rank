import pytest
from ..__main__ import *

def test_case_1():
    assert perms('HACK', 2) == sorted(['AC','AH','AK','CA','CH','CK','HA','HC','HK','KA','KC','KH'])
