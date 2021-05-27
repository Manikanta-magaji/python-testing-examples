from app.calculator import Calculator
import pytest


def test_add():
    calculator = Calculator()
    res = calculator.add(2, 3)
    assert res == 5


def test_add_wierd():
    calculator = Calculator()

    with pytest.raises(TypeError):
        res = calculator.add('two', 3)


def test_subtract():
    calculator = Calculator()
    res = calculator.subtract(9, 3)
    assert res == 6


def test_multiply():
    calculator = Calculator()
    res = calculator.multiply(9, 3)
    assert res == 27


def test_divide():
    calculator = Calculator()
    res = calculator.divide(9, 3)
    assert res == 3


def test_divide_zero():
    calculator = Calculator()
    with pytest.raises(ValueError):
        res = calculator.divide(9, 0)