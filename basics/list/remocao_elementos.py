def remove():
    l = ['a','b','c']
    del l[0]
    print(l)

def remove_fatia():
    l = list(range(101))
    del l [1:99]
    print(f'A remoção da fatia entre 1 e 98 é: {l} ')

remove()
remove_fatia()