import pytest
from calculator import Calculator


def test_add():
    c = Calculator()
    assert c.add(2, 3) == 5


def test_divide_by_zero():
    c = Calculator()
    with pytest.raises(ZeroDivisionError):
        c.divide(1, 0)


def test_evaluate_basic():
    c = Calculator()
    assert c.evaluate("2 + 3 * 4") == 14


def test_evaluate_disallowed_code():
    c = Calculator()
    with pytest.raises(ValueError):
        c.evaluate("__import__('os').system('echo hi')")


def test_factorial_non_integer():
    c = Calculator()
    with pytest.raises(ValueError):
        c.factorial(5.5)
