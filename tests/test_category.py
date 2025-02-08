def test_category_init(first_category, last_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == 'Смартфоны, как средство получения дополнительных функций для удобства жизни'

    assert last_category.name == "Телевизоры"
    assert last_category.description == "Современный телевизор станет вашим другом и помощником"

    assert len(first_category.products) == 2

    assert first_category.category_count == 2
    assert last_category.category_count == 2

    assert first_category.product_count == 3
    assert last_category.product_count == 3
