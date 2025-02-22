from src.product import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        self.__price = price

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError
