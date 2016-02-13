import pytest
from ..__main__ import PE_007

class TestPE007:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.primer = PE_007()

    def test_case_1(self):
        assert self.primer.find_prime(3) == 5

    def test_case_2(self):
        assert self.primer.find_prime(6) == 13
