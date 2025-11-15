"""
core module
"""

from typing import Union
Number = Union[int, float]


def add(a: float, b: float) -> float:
    """
    Return the sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Return the result of a minus b.
    """
    return a - b

def multiply(a: Number, b: Number) -> float:
    """
    Return the product of two numbers.
    """
    return float(a * b)


def divide(a: Number, b: Number) -> float:
    """
    Return the result of dividing a by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return float(a / b)

def power(base, exponent):
    """
    Raise base to exponent.
    """
    return base ** exponent
