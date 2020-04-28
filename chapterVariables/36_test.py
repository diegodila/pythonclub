def test(*args):
    i = 0
    soma = 0
    resultado = 0
    while args[i] < args:
        soma += args[i]
        i += i 
    
    resultado = soma / i
    if(resultado >= 7):
        print("Voce foi aprovado!!!")
    else:
        print("Voce foi reprovado!!!")
    

test([7,8,9])