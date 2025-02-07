def test_category_init(first_category, last_category):
    assert first_category.name == "Смартфоны"
    assert (
            first_category.description
            == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )

    assert last_category.name == "Телевизоры"
    assert (
            last_category.description
            == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )

    assert len(first_category.products) == 2

    assert first_category.category_count == 2
    assert last_category.category_count == 2

    assert first_category.product_count == 2
    assert last_category.product_count == 1
