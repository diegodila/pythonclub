from typing import Final

# Tipos primitivos implicitos abaixos
nome = "Diego"
x = 22
y = 22.33
c = 3 + 4j
is_valid = True
data = b"whatever"


# Tipos primitivos explicitos abaixo
x: int = 22
y: float = 23.33
c: complex = 3 + 4j
is_valid: bool = True
data: bytes = b"whatever"
nome_2: str = "Diego"
# nome_3: int = "Nao podemos atribuir um str ao inteiro"

# constante
CONSTANTE = "minha_constante"
# CONSTANTE = "convenção nao redefinir uma constante, podemos atribuir mais
# valores mas nao redefinir"

# Coleções
lista_numeros: list[int] = [1, 2, 3]
lista_numeros_2: list[int | str] = [1, 2, 3, "a"]

tupla_dois_valores: tuple[str, int] = ("Valor", 234)
tupla_varios: tuple[str, ...] = "a", "b", "c", "..."
tupla_imutavel: tuple[int, str] = (1, "Diego")

conjunto: set[int] = {1, 2, 3, 4}
conjunto_imutavel: frozenset[int] = frozenset([2, 3, 4, 5])

dicionario: dict[str, str] = {"chave": "valor", "chave2": "valor2"}
numeros: range = range(10)

# Outros tipos
nada: None = None  # Representa ausência de valor
qualquer_coisa: object = 123  # Pode ser qualquer objeto (tipo mais amplo)
tipo: type[str] = str  # Referência ao tipo 'str' em si (não uma string)

# Constantes novamente
CONSTANTE_DOIS: Final[list[str]] = ["a", "b"]
constante_tres: Final[dict[str, int]] = {"numero": 123, "outro_numero": 432}
