import pytest
from src.classes import Product, Category, LawnGrass, Smartphone


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
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture
def test_pr_str_pr():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


PRODUCT1_DATA = {
    "name": "Samsung Galaxy S23 Ultra",
    "description": "256GB, Серый цвет, 200MP камера",
    "price": 180000.0,
    "quantity": 5,
}


@pytest.fixture
def product1():
    """Фикстура для создания первого продукта."""
    return Product(**PRODUCT1_DATA)


PRODUCT2_DATA = {
    "name": "Samsung Galaxy S23 Ultra",
    "description": "256GB, Серый цвет, 200MP камера",
    "price": 170000.0,
    "quantity": 6,
}


@pytest.fixture
def product2():
    """Фикстура для создания первого продукта."""
    return Product(**PRODUCT2_DATA)


# Фикстуры для тестовых данных
@pytest.fixture
def sample_smartphone1():
    return Smartphone(
        name="iPhone 13",
        description="Флагман Apple",
        price=80000,
        quantity=10,
        efficiency="Высокая",
        model="13 Pro",
        memory="128GB",
        color="Graphite",
    )


@pytest.fixture
def sample_smartphone2():
    return Smartphone(
        name="Samsung Galaxy S21",
        description="Флагман Samsung",
        price=70000,
        quantity=15,
        efficiency="Высокая",
        model="S21 Ultra",
        memory="256GB",
        color="Phantom Black",
    )


@pytest.fixture
def sample_grass1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def sample_grass2():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )


@pytest.fixture
def sample_smartphones():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def sample_smartphones2():
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )


@pytest.fixture
def empty_category():
    """Фикстура для пустой категории"""
    return Category("Тестовая категория", "Описание тестовой категории")
