import pytest
from src.classes import Product, Category


# Фикстуры
@pytest.fixture
def sample_product():
    return Product("Test Product", "Description", 100.0, 5)


@pytest.fixture
def sample_products():
    return [
        Product("Product 1", "Desc 1", 100, 2),
        Product("Product 2", "Desc 2", 200, 3),
    ]


@pytest.fixture
def empty_category():
    return Category("Empty Category", "Description")


@pytest.fixture
def category_with_products(sample_products):
    return Category("Test Category", "Description", sample_products)


@pytest.fixture
def product_test_fixture():
    return {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0, "quantity": 5}
