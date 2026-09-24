"""Uso do generate interable e interator."""

from pprint import pprint

interable = ["Eu", "Tenho", "__inter__"]
interator = interable.__iter__()
interator2 = iter(interable)
pprint(next(interator))
pprint(interator)


pprint(interator2)
pprint(next(interator2))
pprint(next(interator2))
pprint(next(interator2))
pprint(next(interator2))
# Levanta uma exceção StopIteration
