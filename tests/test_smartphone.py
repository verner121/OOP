import pytest


def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Samsung Galaxy C23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == "Qualcomm"
    assert smartphone1.model == "Samsung"
    assert smartphone1.memory == 1024
    assert smartphone1.color == "Black"


def test_smartphone_add(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 2580000


def test_smartphone_add_error(smartphone1):
    with pytest.raises(TypeError):
        assert smartphone1 + 1
