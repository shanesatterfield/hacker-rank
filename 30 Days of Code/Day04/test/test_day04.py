import pytest
from ..__main__ import Person

def test_initialize_pos_age():
    for age in range(0, 151):
        assert Person(age).getAge() == age

def test_initialize_neg_age(capsys):
    for age in range(-151, 0):
        assert Person(age).getAge() == 0
        # Check if proper message is printed to stdout.
        output, err = capsys.readouterr()
        assert output == 'This person is not valid, setting age to 0.\n'

def test_year_passes_pos_age():
    for age in range(0, 151):
        person = Person(age)
        person.yearPasses()
        assert person.getAge() == age + 1

def test_year_passes_neg_age():
    for age in range(-151, 0):
        person = Person(age)
        person.yearPasses()
        assert person.getAge() == 1

def helper_test_rangers(start, stop, message, capsys):
    for age in range(start, stop+1):
        Person(age).amIOld()
        out, err = capsys.readouterr()
        assert out == message

def test_too_young(capsys):
    helper_test_rangers(0, 12, 'You are young.\n', capsys)

def test_teenager(capsys):
    helper_test_rangers(13, 17, 'You are a teenager.\n', capsys)

def test_too_old(capsys):
    helper_test_rangers(18, 151, 'You are old.\n', capsys)
