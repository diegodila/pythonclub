def fila():
    ultimo = 10
    fila = list(range(0,ultimo))
    while True:
        print(f'Contem {len(fila)} clientes na fila')
        print(f'A fila é: {fila}')
        digito = input('Digite F para entrar na fila ou A para ser atendido ou S para sair:(F, A ou S)')
        if digito == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f'O cliente {atendido} está sendo atendido')
            else:
                print('A fila está vazia!!!')
        elif digito == 'F':
            ultimo += 1
            fila.append(ultimo)
        elif digito == 'S':
            break
        else:
            print("*******Digito incorreto tente novamente!!!(F, A e S********")

fila()