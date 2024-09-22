#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado pelo usuário. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

def rentcar(*args):
    i = 0 
    custo = (args[i][i] * 0.15) + (args[i][i+1] * 60)
    print(f'O custo da locação será: {custo} reais')
    return custo

lista = []
lista.append(float(input('Digite a quantidade de km rodados: ')))
lista.append(int(input('Digite a quantidade de dias da locação: ')))
rentcar(lista)