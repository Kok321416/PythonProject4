
class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0
    product_count = 0
    name: str
    description: str
    products: list

    def __init__(self, name, description,products=None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1  # Увеличиваем счетчик категорий
        Category.product_count += len(self.products)  # Увеличиваем счетчик товаров
