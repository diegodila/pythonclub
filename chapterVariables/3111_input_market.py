#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar 
def market(*args):
    i = 0
    print(f'Pecerntual de desconto é: {args[0][1]}')
    preco = args[0][i] * ((100 - args[0][i+1]) / 100)
    print(f"Preço a pagar pela mercadoria é: {preco} reais")
    return preco

lista = []
lista.append(float(input("Informe o valor da compra: ")))
lista.append(float(input("Informe o percentual de desconto: ")))
market(lista)