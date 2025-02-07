import json
import os

from src.category import Category
from src.product import Product


def read_json(path):
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_by_json(data):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    raw_categories = read_json("../data/products.json")
    categories_data = create_objects_by_json(raw_categories)
    print(categories_data)
