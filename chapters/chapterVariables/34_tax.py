def tax(tax):
    if tax >= 1200:
        print("Taxado!!!")


tax(1200)

#outra forma, usando lambda 
tax_lambda = lambda x: print("Taxadoo!!!") if x>=1200 else print('Não foi taxado!')
tax_lambda(1330)

#lambda não imprime, temos que usar a function print
tax_lambda1 = lambda x: 'Taxado' if x >= 1200 else 'Not tax'
print(tax_lambda1(1222))