def remove_duplicates(items: list[str]) -> list[str]:
    # `dict.fromkeys` gera um dicionário a partir da lista.
    to_dict = dict.fromkeys(items)
    # to_dict = set(items) #nao mantem ordem igual ao dict
    # `list` converte o dict em lista, remove as duplicatas e mantém a ordem.
    return list(to_dict)

    # def remove_duplicates(items):
    # `dict.fromkeys` gera um dicionário a partir da lista.
    to_dict = dict.fromkeys(items)
    # `list` converte o dict em lista, remove as duplicatas e mantém a ordem.
    return list(to_dict)


# Será removido ❌:                       ❌        ❌        ❌
list_with_duplicates = ["luiz", "a", "b", "a", "c", "a", "d", "luiz"]
print(list_with_duplicates)
unique_items = remove_duplicates(list_with_duplicates)
print(unique_items)
