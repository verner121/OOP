import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


@pytest.fixture
def product_1():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def first_category():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство получения дополнительных функций для удобства жизни",
        [
            Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )


@pytest.fixture
def last_category():
    return Category(
        "Телевизоры",
        "Современный телевизор станет вашим другом и помощником",
        [Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def product_2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def product_4():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def product_iterator(first_category):
    return ProductIterator(first_category)


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy C23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        "Qualcomm",
        "Samsung",
        1024,
        "Black",
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, "Apple A16 Bionic", "Apple", 512, "White")


@pytest.fixture
def lawn_grass1():
    return LawnGrass('55" QLED 4K', "Фоновая подсветка", 123000.0, 7, "Russia", 7, "White")


@pytest.fixture
def lawn_grass2():
    return LawnGrass("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, "China", 3, "Red")


@pytest.fixture
def new_category():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство получения дополнительных функций для удобства жизни",
        [],
    )
