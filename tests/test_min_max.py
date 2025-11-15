from calculator import maximum, minimum


def test_maximum_basic():
    assert maximum(10, 3) == 10
    assert maximum(-1, -5) == -1


def test_minimum_basic():
    assert minimum(10, 3) == 3
    assert minimum(-1, -5) == -5


def test_maximum_equal_values():
    assert maximum(4, 4) == 4


def test_minimum_equal_values():
    assert minimum(4, 4) == 4
    