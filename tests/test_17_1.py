import pytest

from src.classes import Product


def test_value_error():
    with pytest.raises(
        ValueError,
        match="Товар с нулевым количеством не может быть добавлен",
    ):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_zero_quantity():
    with pytest.raises(
        ValueError,
        match="Товар с нулевым количеством не может быть добавлен",
    ):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
