"""Closures em python."""

from collections.abc import Callable


def externa(a: str) -> Callable[[str], str]:
    """Funcao externa para comportamento de closure."""

    def interna(b: str):
        """Funcao interna para comportamento clousure."""
        return f"{a} {b}"

    return interna
