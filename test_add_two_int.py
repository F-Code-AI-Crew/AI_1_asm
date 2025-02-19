import pytest
from add_two_int import add_two_int

def test_add_positive_numbers():
    assert add_two_int(2, 3) == 5

def test_add_negative_numbers():
    assert add_two_int(-1, -1) == -2

def test_add_mixed_numbers():
    assert add_two_int(-1, 1) == 0

def test_add_zero():
    assert add_two_int(0, 0) == 0