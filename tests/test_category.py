import pytest


def test_category_init(first_category, last_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство получения дополнительных функций для удобства жизни"

    assert last_category.name == "Телевизоры"
    assert last_category.description == "Современный телевизор станет вашим другом и помощником"

    assert len(first_category.product_in_list) == 2

    assert first_category.category_count == 2
    assert last_category.category_count == 2

    assert first_category.product_count == 3
    assert last_category.product_count == 3


def test_add_product_counter(first_category, product_3):
    assert len(first_category.product_in_list) == 2
    first_category.add_product(product_3)
    assert len(first_category.product_in_list) == 3


def test_products_property(first_category):
    product5 = "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" " Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    assert first_category.products == product5


def test_category_str(first_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 13 шт."


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy C23 Ultra"
    assert next(product_iterator).name == "Iphone 15"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_category_product_list_setter_smartphone(first_category, smartphone1):
    first_category.__products = smartphone1
    assert first_category.product_in_list[-1].name == "Iphone 15"
