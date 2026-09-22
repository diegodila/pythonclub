"""Chamada da funcao sn_func_x e utilizacao da funcao."""

from pprint import pprint

import sn_func_x


def func_global() -> None:
    """Func_global definida nesse modulo para ver o comportamento."""
    pprint(f"Estou em: {__name__} - {__file__.split('/')[-1]}")


sn_func_x.func_global()
pprint("-----")
func_global()
print()
pprint(globals())
