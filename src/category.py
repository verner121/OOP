from src.product import Product


class Category:
    name: int
    description: int
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        total_product = 0
        for product in self.__products:
            total_product += product.quantity
        return f"{self.name}, количество продуктов: {total_product} шт."

    def avg_quantity_products(self):
        try:
            return round(
                sum(product.price for product in self.product_in_list)
                / sum(product.quantity for product in self.product_in_list)
            )
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        return " ".join(str(prod) for prod in self.__products)

    def add_product(self, new_product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            self.product_count += 1
            print("Задача добавлена успешно")
        else:
            raise TypeError

    @property
    def product_in_list(self):
        return self.__products
