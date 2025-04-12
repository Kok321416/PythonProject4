class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        """Класс-метод для создания нового продукта из словаря с данными"""
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    @property
    def price(self):
       return self.__price

    @price.setter
    def price(self, new_prise):
        if new_prise <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = new_prise


class Category:
    category_count = 0
    product_count = 0
    name: str
    description: str
    __products: list

    def __init__(self, name, description, products=None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1  # Увеличиваем счетчик категорий
        Category.product_count += len(self.__products)  # Увеличиваем счетчик товаров

    def add_product(self, product: Product):
        """Метод для добавления товара в категорию"""
        self.__products.append(product)
        Category.product_count += 1  # Увеличиваем счетчик товаров

    @property
    def products(self):
        """Геттер для вывода списка товаров в заданном формате, только показываем"""
        products_list = []
        for product in self.__products:
            products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return products_list
