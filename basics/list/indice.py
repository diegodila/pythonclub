def input_numeros():
    l = []
    i = 0
    numero = 0
    while i < 3:
        l.append(int(input("digite a lista numero:")))
        i += 1
    
    numero = int(input("Digite o numero digitado: "))
    print(f'O numero que voce digitou é: {l[numero-1]}')


input_numeros()
    