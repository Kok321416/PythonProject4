import pytest

from src.classes import Product


def test_print_mixing(capsys):
    """Тестирование вывода класса Mixins"""
    # Создание экземпляров класса Product
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    captured = capsys.readouterr()
    assert captured.out.strip() == (
        "Product('Samsung Galaxy S23 Ultra','256GB, Серый цвет, 200MP "
        "камера','180000.0','5')"
    )

    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    captured = capsys.readouterr()
    assert (
        captured.out.strip()
        == "Product('Iphone 15','512GB, Gray space','210000.0','8')"
    )

    Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    captured = capsys.readouterr()
    assert (
        captured.out.strip()
        == "Product('Xiaomi Redmi Note 11','1024GB, Синий','31000.0','14')"
    )


def test_value_error():
    with pytest.raises(
        ValueError,
        match="Товар с нулевым количеством не может быть добавлен",
    ):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
