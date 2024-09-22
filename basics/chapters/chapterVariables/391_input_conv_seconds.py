#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total de segundos
def converter_seconds(*args):
    i = 0
    while(i < len(args)):
        segundos = args[0][i] * 24 * 60 * 60
        i += 1
        segundos += args[0][i] * 60 * 60
        i += 1
        segundos += args[0][i] * 60
        i += 1
    return segundos
    
lista = []
lista.append(int(input("Digite o valor de dias a converter para segundos: ")))
lista.append(int(input("Digite o valor de horas a converter para segundos: ")))
lista.append(int(input("Digite o valor de minutos a converter para segundos: ")))

print(converter_seconds(lista))
