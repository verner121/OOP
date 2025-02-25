from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, "Apple A16 Bionic", "Apple", 512, "White")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    LawnGrass('55" QLED 4K', "Фоновая подсветка", 123000.0, 7, "Russia", 7, "White")
    message = capsys.readouterr()
    assert message.out.strip() == 'LawnGrass(55" QLED 4K, Фоновая подсветка, 123000.0, 7)'
