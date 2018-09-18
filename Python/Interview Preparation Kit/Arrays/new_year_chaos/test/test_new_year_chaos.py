import pytest
from ..__main__ import minimum_bribes

params = [
    ([2, 1, 5, 3, 4], 3),
    ([2, 5, 1, 3, 4], None),
    ([5, 1, 2, 3, 7, 8, 6, 4], None),
    ([1, 2, 5, 3, 7, 8, 6, 4], 7),
    ([1, 2, 5, 3, 4, 7, 8, 6], 4),
    (list(range(10**5)), 0)
]


@pytest.fixture(params=params)
def params(request):
    return request.param


def test_new_year_chaos(params):
    assert minimum_bribes(params[0]) is params[1]
