"""Criação de uma função generator."""

from pprint import pprint


def generator(n: int = 0):
    """Generator function."""
    yield 1  # pausa
    return "Acabou"  # levanta uma exceção StopIteration


gen = generator(n=0)
pprint(gen)
pprint(next(gen))
pprint(iter(gen))


def generator_2(n: int = 0):
    """Generator function."""
    yield 1  # pausa
    print("Continua")
    yield 2  # continua na proxima iteracao
    print("Continua")
    yield 3
    return "Acabou"


gen_2 = generator_2(n=0)
pprint(gen_2)
pprint(next(gen_2))
pprint(next(gen_2))
pprint(iter(gen_2))

gen3 = generator_2(n=0)
for n in gen3:
    pprint(n)
