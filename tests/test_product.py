import pytest

from src.product import Product


def test_product_1_init(product_1):
    assert product_1.name == "Samsung Galaxy C23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_product_2_init(product_2):
    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8


def test_product_3_init(product_3):
    assert product_3.name == "Xiaomi Redmi Note 11"
    assert product_3.description == "1024GB, Синий"
    assert product_3.price == 31000.0
    assert product_3.quantity == 14


def test_product_4_init(product_4):
    assert product_4.name == '55" QLED 4K'
    assert product_4.description == "Фоновая подсветка"
    assert product_4.price == 123000.0
    assert product_4.quantity == 7


def test_new_product():
    from src.product import Product

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5
    assert new_product.description == "256GB, Серый цвет, 200MP камера"


def test_new_price(capsys, product_1):
    product_1.price = 0
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    product_1.price = 30
    assert product_1.price == 30


def test_product_str(product_1):
    assert str(product_1) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"


def test_product_add(product_2, product_3):
    assert product_2 + product_3 == 2114000


def test_not_quantity_product():
    with pytest.raises(ValueError) as e:
        Product("Iphone 15", "512GB, Gray space", 210000.0, 0)
        assert str(e.value) == "Товар с нулевым количеством не может быть добавлен"
