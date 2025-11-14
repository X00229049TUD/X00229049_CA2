from calculator import multiply, divide


def test_multiply_two_positive_numbers() -> None:
    """
    Multiplying two positive numbers returns the product.
    """
    assert multiply(3, 4) == 12.0


def test_multiply_with_negative_number() -> None:
    """
    Multiplying by a negative number returns a negative product.
    """
    assert multiply(-2, 5) == -10.0


def test_multiply_with_floats() -> None:
    """
    Multiplying floats works as expected.
    """
    assert multiply(1.5, 2.0) == 3.0


def test_divide_two_positive_numbers() -> None:
    """
    Dividing two positive numbers returns the quotient.
    """
    assert divide(10, 2) == 5.0


def test_divide_result_fraction() -> None:
    """
    Division can produce a fractional result.
    """
    assert divide(7, 2) == 3.5


def test_divide_by_negative_number() -> None:
    """
    Dividing by a negative number returns a negative result.
    """
    assert divide(10, -2) == -5.0


def test_divide_by_zero_raises_value_error() -> None:
    """
    Division by zero raises ValueError.
    """
    try:
        divide(1, 0)
    except ValueError as exc:
        assert "Division by zero" in str(exc)
    else:
        raise AssertionError("Expected ValueError when dividing by zero")
