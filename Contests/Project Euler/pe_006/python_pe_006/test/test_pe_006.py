import pytest
from ..__main__ import pe_006

class TestPe006:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.differ = pe_006()

    def test_case_1(self):
        assert self.differ.find_diff(3) == 22

    def test_case_2(self):
        assert self.differ.find_diff(10) == 2640
