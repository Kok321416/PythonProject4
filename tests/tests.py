import pytest

from src.classes import Category, Smartphone


# Тесты для Product
def test_product_initialization(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Description"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 5


# Тесты для Category
def test_empty_category_initialization(empty_category):
    assert empty_category.name == "Empty Category"
    assert empty_category.description == "Description"
    assert len(empty_category.products) == 0


def test_category_with_products(category_with_products, sample_products):
    assert len(category_with_products.products) == 2
    assert category_with_products.products[0].name == "Product 1"
    assert category_with_products.products[1].price == 200


def test_category_count():
    initial_count = Category.category_count
    Category("New Category", "Desc")
    assert Category.category_count == initial_count + 1


def test_product_count(sample_products):
    initial_count = Category.product_count
    Category("New Category", "Desc", sample_products)
    assert Category.product_count == initial_count + len(sample_products)


def test_product_str(product1):
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб., Остаток: 5 шт."


def test_product_add(product1, product2):
    assert (product1.price * product1.quantity) + (
        product2.price * product2.quantity
    ) == 1920000.0


def test_add(sample_grass1, sample_smartphones, capsys):
    """Тест попытки сложить смартфон и траву"""
    with pytest.raises(TypeError) as excinfo:
        add_smartphone_and_grass = sample_smartphones + sample_grass1
    assert "Нельзя складывать товары разных классов" in str(excinfo.value)


def test_subintase(empty_category):
    """проверяет Теперь защитим метод так, чтобы, кроме смартфонов, травы газонной или других продуктов, в список нельзя было добавлять ничего другого."""

    class NotAProduct:
        pass

    not_a_product = NotAProduct()
    initial_count = Category.product_count
    with pytest.raises(TypeError):
        empty_category.add_product(not_a_product)

    assert Category.product_count == initial_count
    assert len(empty_category.products) == 0


import pytest


def test_smartphone_initialization(sample_smartphones):
    """Тест корректности инициализации смартфона"""
    assert sample_smartphones.name == "Samsung Galaxy S23 Ultra"
    assert sample_smartphones.description == "256GB, Серый цвет, 200MP камера"
    assert sample_smartphones.price == 180000.0
    assert sample_smartphones.quantity == 5
    assert sample_smartphones.efficiency == 95.5
    assert sample_smartphones.model == "S23 Ultra"
    assert sample_smartphones.memory == 256
    assert sample_smartphones.color == "Серый"


def test_lawn_grass_initialization(sample_grass1):
    """Тест корректности инициализации газонной травы"""
    assert sample_grass1.name == "Газонная трава"
    assert sample_grass1.description == "Элитная трава для газона"
    assert sample_grass1.price == 500.0
    assert sample_grass1.quantity == 20
    assert sample_grass1.country == "Россия"
    assert sample_grass1.germination_period == "7 дней"
    assert sample_grass1.color == "Зеленый"
