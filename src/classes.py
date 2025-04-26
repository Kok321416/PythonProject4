from abc import ABC, abstractmethod

# class BaseProduct(ABC):
#     @abstractmethod
#     def __init__(self):
#         pass
#
#
# class MixinLog:
#     pass


class Product:
    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> object:
        # super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        """Класс-метод для создания нового продукта из словаря с данными"""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб., Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return (self.__price * self.quantity) + (other.price * other.quantity)


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
        if not isinstance(product, Product):
            raise TypeError
        else:
            self.__products.append(product)
            Category.product_count += 1  # Увеличиваем счетчик товаров

    @property
    def products(self):
        """Геттер для вывода списка товаров в заданном формате, только показываем"""
        products_list = []
        for product in self.__products:
            products_list.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )
        return products_list

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return (self.price * self.quantity) + (other.price * other.quantity)


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
