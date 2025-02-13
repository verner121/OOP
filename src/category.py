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

    @property
    def products(self):
        return "\n ".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]
        )

    def add_product(self, new_product):
        self.__products.append(new_product)
        self.product_count += 1

    @property
    def product_in_list(self):
        return self.__products
