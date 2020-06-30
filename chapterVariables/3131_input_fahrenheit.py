def fahrenheit(*args):
    i = 0 
    fahrenheit = ((args[i][i] * 9) / 5) + 32
    print(f'A temperatura em fahrenheit é: {fahrenheit}')
    return fahrenheit

lista = []
lista.append(float(input('Digite graus em celsius: ')))
fahrenheit(lista)