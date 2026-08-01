import pytest
from app.calculator import *

def test_add():
    assert add(5, 4) == 9

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(20, 4) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)