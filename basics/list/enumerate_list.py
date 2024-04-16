def lista_for():
    l = [1,2,3,4,5]
    x = 0 
    for i in l:
        print(i, sep=' ', end=' ')
        print(x)
        x += 1

def lista_enumerate():
    l = [1,2,3,4,5,6]
    for i,e in enumerate(l):
        print(f'indice: {i} e elemento: {e}', end=' - ') 
    print()


def lista_tupla():
    l = [1,2,3,4,5,6]
    for z in enumerate(l):
        i, e = z
        print(f'indice: {i} e elemento: {e}', end=' - ')
        print(z)


lista_for()
lista_enumerate()
lista_tupla()