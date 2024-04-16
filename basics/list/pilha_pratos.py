def pilha():
    prato = 5
    pilha = list(range(1,prato+1))
    while True:
        print(f'Existem {len(pilha)} na pilha de pratos')
        print(f'A pilha de pratos é: {pilha}')
        digito = input('Digite D para desimpilhar, E para empilhar ou S para sair (D, E ou S: ')
        if digito == 'D':
            if len(pilha) > 0:
                saiu = pilha.pop(-1) 
                print(f'O prato {saiu} saiu')
            else:
                print('Pilha de pratos vazia!!!!')
        elif digito == 'E':
            prato += 1
            pilha.append(prato)
        elif digito == 'S':
            break
        else:
            print("Digito inválido!!!(D, E ou S")
pilha()