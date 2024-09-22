#Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distancia a percorrer e a velocidade média esperada para a viagem.
def speed_average(*args):
    i = 0 
    tempo = 60 * (args[i][i] / args[i][i+1])
    if(tempo >= 60):
        print(f'O tempo de viagem será: {tempo/60:.2f} hora(s)')
    else:
        print(f'O tempo de viagem será: {tempo:.2f} minuto(s)')

    return tempo 

lista = []
lista.append(float(input('Digite a distancia percorrida: ')))
lista.append(float(input('Digite a velocidade média: ')))
speed_average(lista)

