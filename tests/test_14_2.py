from src.classes import Product


def test_new_product(product_test_fixture):
    product = Product.new_product(product_test_fixture)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_getter(sample_product):
    assert sample_product.price == 100.0


def test_new_prise(sample_product):
    sample_product.price = 50.50
    assert sample_product.price == 50.50


def test_new_prise_error(sample_product, capsys):
    sample_product.price = 0
    pr, _ = capsys.readouterr()
    assert pr == 'Цена не должна быть нулевая или отрицательная\n'
