# Виджет для электронной торговли
## Описание:
Мы не будем реализовывать систему платежей, однако подготовим всё для того, чтобы у нас появилось ядро для интернет-магазина. В дальнейшем для этого ядра возможно будет реализовать любой интерфейс — от сайта до телеграм-бота.
## Установка и использование:
1. Откройте [GitHub](https://github.com/) в вашем браузере

2. 2.Клонируйте репозиторий:
```
git clone git@github.com:verner121/Homework.git
```
3.Установите зависимости:
```
pip install -r requirements.txt
flake8 = "^7.1.1"
black = "^24.10.0"
isort = "^5.13.2"
mypy = "^1.13.0"
python = "^3.13"
```
## Тестирование
1. в папке `tests` проводятся тестирования функций с различными сценариями и подставлением данных
2. тестирование по работе с классами
3. для проведения тестрирования необходимо ввести команду `poetry run pytest --cov`
4. были созданы тесты по каждому модулю и отдельной функции различными вариантами
5. были созданы фикстуры
6. поркытие тестов составляет 100%

## 00П
1. Были созданы два класса (Products, Category) и каждому классу были прописаны их свойства и атрибуты
2. Была произведена инициализация этих классов 
3. Были изменены некоторые атрибуты на приватные и реализованы к ним геттеры и сеттеры
4. создан новый класс-метод 
new_product
, который принимает на вход параметры товара в словаре и возвращает созданный объект класса 
Product.
