import pytest


def test_lawn_grass_init(lawn_grass1):
    assert lawn_grass1.name == '55" QLED 4K'
    assert lawn_grass1.description == "Фоновая подсветка"
    assert lawn_grass1.price == 123000.0
    assert lawn_grass1.quantity == 7
    assert lawn_grass1.country == "Russia"
    assert lawn_grass1.germination_period == 7
    assert lawn_grass1.color == "White"


def test_lawn_grass_add(lawn_grass1, lawn_grass2):
    assert lawn_grass1 + lawn_grass2 == 1295000


def test_lawn_grass_add_error(lawn_grass2):
    with pytest.raises(TypeError):
        assert lawn_grass2 + 1
