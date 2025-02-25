from src.product import Product


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
        self.__price = price

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError
