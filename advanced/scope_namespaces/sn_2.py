namespace_global = globals()
um_nome = "um_nome (GLOBAL)"

print(id(um_nome), id(namespace_global["um_nome"]))
print(f"Namespace global: {namespace_global}")  # retorna um dict
# print(dir(__builtins__))
print()
print(__builtins__.locals())
print()


def func_global(sou_local: str) -> None:
    um_nome: str = "um_nome (LOCAL)"
    outro_nome: str = "outro_nome (LOCAL)"
    print("LOCALS (namespace da função)")
    print("dir: ", dir())
    print("vars: ", vars())
    print(locals())
    print()


func_global("arg (local)")
print()

# print("GLOBALS (namespace do módulo)")
print(
    globals()
)  # a funcao func_global entra apenas depois, porque foi definida depois
