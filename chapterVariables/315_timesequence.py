def divida():
    divida = 0
    digito = 1
    while digito > 0:
        compra = int(input('Digite o valor da compra: '))
        divida += compra
        digito = int(input('Se deseja sair e somar sua dívida digite 0 ou digite 1 para continuar somando compras: '))
    print(f'Sua divida é de: {divida} reais')

divida()