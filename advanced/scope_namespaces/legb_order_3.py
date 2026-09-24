"""Utilização da LEGB order e seus conceitos."""

nome_global = "nome_global"


def func_global() -> None:
    """Função global para utilização de enclosing."""
    nome_enclosing = "nome_enclosing"  # Enclosing (Local)

    def func_interna() -> None:
        print("IMPRIMINDO", nome_enclosing)

        # nome_enclosing = "CRIAR UMA NOVA VARIÁVEL NESSE ESCOPO"

        def func_mais_interna() -> None:
            nome_local = "nome_local"  # Local

            print(
                "LOCAL:",
                nome_local,
                nome_enclosing,
                "funcao_interna",
                nome_global,
                "+builtins",
            )

        func_mais_interna()

    func_interna()
    print(
        "ENCLOSING:",
        nome_enclosing,
        "funcao_interna",
        "funcao_global",
        nome_global,
        "+builtins",
    )


func_global()
print("GLOBAL:", nome_global, "func_global", "+builtins")
