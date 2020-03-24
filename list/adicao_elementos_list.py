def adicionando_elementos():
    l = ['a']
    l.append('b')
    print(f'Iniciando com a e usando append: {l}')
    l.extend(['c'])
    print(f'A função extend só aceita paramentros de lista []: {l}')
    l.append(['d','e'])
    print(f'A função append podemos passar outra lista [], lista dentro de lista: {l}')
    l.extend(['f','g'])
    print(f'Continuando a lista com uma lista dentro dela: {l}')
    return l


adicionando_elementos()