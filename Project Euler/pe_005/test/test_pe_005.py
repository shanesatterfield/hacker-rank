import pytest
from ..__main__ import pe_005

class TestPe005:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.mype = pe_005()

    def test_case_1(self):
        assert self.mype.find_multiple(3) == 6

    def test_case_2(self):
        assert self.mype.find_multiple(10) == 2520

    def test_case_3(self):
        assert self.mype.find_multiple(1) == 1
