#Escreva um programa que leia o valor em metros e o exiba convertido em milimetros
def milimetros_centimetros():
    metros = float(input('Digite o valor em metros: '))
    print(f'A conversão de metros em centimetros é: {metros*100} centimetros')
    print(f'A conversão de metros em milimetros é: {metros*1000} milimetros')

milimetros_centimetros()