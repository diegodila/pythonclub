import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    print([Fruit("banana").__dict__, my_fruit.__dict__])
    return [Fruit("banana"), my_fruit]

@pytest.mark.meu_teste
def test_my_fruit_in_basket(my_fruit, fruit_basket):
    print(f'{my_fruit.__dict__}, {fruit_basket[0].__dict__}, {fruit_basket[1].__dict__}')
    assert my_fruit in fruit_basket