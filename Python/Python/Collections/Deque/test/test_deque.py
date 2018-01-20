import pytest, collections
from ..__main__ import deq

def test_case_1():
    commands = [
        ['append',     [1]],
        ['append',     [2]],
        ['append',     [3]],
        ['appendleft', [4]],
        ['pop',        []],
        ['popleft',    []],
    ]
    assert deq(commands) == collections.deque([1,2])
