class MixinLog:
    """Миксин для вывода информации о продукте"""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        """Метод для вывода информации о продукте"""
        return f"{self.__class__.__name__}('{self.name}','{self.description}','{self.price}','{self.quantity}')"
