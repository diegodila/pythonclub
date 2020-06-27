#função input para receber dados int ou float e armazenar em variáveis

def input_numeric():
    anos = int(input("Digite quantos anos voce tem: "))
    dinheiro = float(input("Digite quanto de dinheiro tem na carteira: "))
    x = anos * dinheiro
    print(f'Se tivesse guardado esse dinheiro todos os anos da sua vida, voce teria: {x} reais')


input_numeric()