from src.classes import Category


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


# тесты 14.2
