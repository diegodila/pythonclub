#Programa que recebe notas e verifica se está aprovado ou não
def nota(*args):
    i = 0
    soma = 0
    resultado = 0
    print(len(args))
    while i < len(args):
        soma += args[i]
        i += 1
    

    resultado = soma / i
    if(resultado >= 7):
        print("Voce foi aprovado!!!")
    else:
        print("Voce foi reprovado!!!")
    

nota(7,8,9)