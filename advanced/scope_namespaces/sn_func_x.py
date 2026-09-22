"""Para fins de teste chamda dessa funcao."""


def func_global() -> None:
    """Funcao global definida nesse modulo a ser chamado por outro modulo."""
    print(f"Estou em: {__name__} - {__file__.split('/')[-1]}")
