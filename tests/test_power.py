import pytest
from calculator import power


def test_power_integers():
    assert power(2, 3) == 8
    assert power(5, 0) == 1


def test_power_fractional():
    assert pytest.approx(power(9, 0.5), rel=1e-9) == 3.0


def test_power_negative_exponent():
    assert pytest.approx(power(2, -1), rel=1e-9) == 0.5

