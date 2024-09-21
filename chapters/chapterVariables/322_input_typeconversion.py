#Função que recebe entrada de dados de uma lista
def saldo(*args):
    i = 0
    print(f'Nome: {args[i][i]} idade: {args[i][i+1]} saldo: {args[i][i+2]}')

lista = []
lista.append(input('Digite o seu nome: '))
lista.append(int(input('Digite o sua idade: ')))
lista.append(float(input('Digite o saldo: ')))
saldo(lista)