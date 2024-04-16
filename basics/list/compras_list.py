def compras():
    lista_compras = []
    while True:
        produto = input('Digite o produto: \n')
        if produto == 'fim':
            print('Saindo...')
            break
        quantidade = int(input('Digite a quantidade: \n'))
        valor = float(input('Digite o valor: \n'))
        lista_compras.append([produto,quantidade,valor])
    soma = 0.0    
    for i in lista_compras:
        soma += i[1] * i[2] 
        print(f'Foram comprados {i[1]} {i[0]}(s) a {i[2]} reais cada, no valor total de {soma} reais')
        soma = 0.0

compras() 