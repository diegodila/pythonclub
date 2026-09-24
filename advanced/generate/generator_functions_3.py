"""Vemos o comportamento de uma funcao geradora."""


def generator(n: int = 0):
    """Vale ressaltar a chamada do generator."""
    while True:
        yield n
        n += 1
        if n >= 12:
            return "Acabou"


for i in generator():
    print(i)

# Aqui chamamos uma vez, é a execução da função que gera um obj generate
n = generator()
print(next(n))
print(next(n))
