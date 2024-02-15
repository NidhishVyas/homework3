""" Tests for the operations and Calculation class """
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("n1, n2, operation, expected", [
    (Decimal('8'), Decimal('2'), add, Decimal('10')),
    (Decimal('8'), Decimal('2'), subtract, Decimal('6')),
    (Decimal('8'), Decimal('2'), multiply, Decimal('16')),
    (Decimal('8'), Decimal('2'), divide, Decimal('4')),
    (Decimal('8.8'), Decimal('0.2'), add, Decimal('9.0')),
    (Decimal('8.8'), Decimal('0.2'), subtract, Decimal('8.6')),
    (Decimal('8.8'), Decimal('0.2'), multiply, Decimal('1.76')),
    (Decimal('8.8'), Decimal('0.2'), divide, Decimal('44.0')),
])

def test_calculation_operations(n1, n2, operation, expected):
    """" Test cases """
    calc = Calculation(n1, n2, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {n1} and {n2}"

def test_calculation_repr():
    """ Test the string representation (__repr__) of the Calculation class """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert calc.__repr__() == expected_repr, "__repr__ method output doesn't match expected string"

def test_divide_by_zero():
    """ Test case when diivided by zero """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Can't divide by zero"):
        calc.perform()
