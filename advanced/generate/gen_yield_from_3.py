"""Utilização do yield from."""

from collections.abc import Generator


def gen1() -> Generator[int, None, None]:
    """Primeiro generate."""
    print("Comecou gen 1")
    yield 1
    yield 2
    yield 3
    print("Acabou o gen 1")


def gen2(gen: Generator[int, None, None]) -> Generator[int, None, None]:
    """Segundo generate."""
    print("Comecou o gen 2")
    yield from gen
    yield 4
    yield 5
    yield 6
    print("Acabou o gen 2")


g = gen2(gen1())
for numero in g:
    print(numero)
