class ProductIterator:

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.product_in_list):
            product = self.category.product_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
