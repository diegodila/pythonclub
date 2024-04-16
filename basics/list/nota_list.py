# Atenção na iteração dos numeros 

def nota(*args):
    soma = 0
    i = 0
    # contador = 0
    for i in args[i]:
        # args[i] = float(input(f'Digite a nota {contador+1}: ')) tupla não podemos alterar valor 
        soma += i
        i += 1
        print(soma)

nota([6, 7, 4, 4, 4])

