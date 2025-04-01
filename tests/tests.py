from src.classes import Category


def test_product_initialization(product):
    assert product.name == "Товар 1"
    assert product.description == "Описание товара"
    assert product.price == 100.50
    assert product.quantity == 10

def test_category_initialization(category):
    assert category.name == "Категория 1"
    assert category.description == "Описание категории"
    assert len(category.products) == 1

def test_total_categories_and_products(category):
    assert Category.category_count == 1
    assert Category.product_count == 1