from calculator import add, subtract


def test_add_two_positive_numbers() -> None:
    """
    Adding two positive numbers returns their sum.
    """
    assert add(2, 3) == 5


def test_add_with_negative_number() -> None:
    """
    Adding a negative number is equivalent to subtraction.
    """
    assert add(10, -4) == 6


def test_add_with_floats() -> None:
    """
    Adding floating point values works as expected.
    """
    assert add(1.5, 2.5) == 4.0


def test_subtract_two_positive_numbers() -> None:
    """
    Subtracting two positive numbers returns the difference.
    """
    assert subtract(10, 3) == 7


def test_subtract_resulting_in_negative() -> None:
    """
    Subtraction can produce a negative result.
    """
    assert subtract(3, 10) == -7


def test_subtract_with_floats() -> None:
    """
    Subtracting floating point values works as expected.
    """
    assert subtract(5.5, 2.0) == 3.5