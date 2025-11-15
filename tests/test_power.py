import pytest
from calculator import power


def test_power_positive_integers():
    assert power(2, 3) == 8
    assert power(5, 0) == 1


def test_power_fractional_exponent():
    result = power(9, 0.5)
    assert pytest.approx(result, rel=1e-9) == 3.0


def test_power_negative_exponent():
    result = power(2, -1)
    assert pytest.approx(result, rel=1e-9) == 0.5
