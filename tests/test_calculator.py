
from src.calculator import add, subtract, product


def test_add():
    assert add(6, 6) == 12
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(6, 6) == 0
    assert subtract(-1, 1) == -2


def test_product():
    assert product(6, 6) == 36
    assert product(-1, 1) == -1
