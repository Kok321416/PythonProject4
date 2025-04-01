import pytest

from src.classes import Product, Category


@pytest.fixture
def product():
    return Product(name="Товар 1", description="Описание товара", price=100.50, quantity=10)

@pytest.fixture
def category(product):
    return Category(name="Категория 1", description="Описание категории", products=[product])
