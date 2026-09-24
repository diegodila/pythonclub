"""Uso do generate."""

import sys
from pprint import pprint

interable = ["Eu", "Tenho", "__inter__"]
interator = interable.__iter__()
interator2 = iter(interable)
pprint(next(interator))
pprint(interator)

lista = [n for n in range(10)]
pprint(lista)
generator = (n for n in range(10))
pprint(generator)
pprint(sys.getsizeof(lista))
print(sys.getsizeof(generator))
