import pytest
from ..__main__ import day08

class TestDay08:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.diction          = dict()
        self.diction["sam"]   = 99912222
        self.diction["tom"]   = 11122222
        self.diction["harry"] = 12299933

    def test_case_1(self):
        assert day08(self.diction, 'sam')    == 'sam=99912222'

    def test_case_2(self):
        assert day08(self.diction, 'edward') == 'Not found'

    def test_case_3(self):
        assert day08(self.diction, 'harry')  == 'harry=12299933'
