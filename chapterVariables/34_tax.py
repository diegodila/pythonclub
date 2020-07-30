def tax(tax):
    if tax >= 1200:
        print("Taxado!!!")


tax(1200)

#outra forma, usando lambda 
tax_lambda = lambda x: print("Taxadoo!!!") if x>=1200 else print('Não foi taxado!')
tax_lambda(1330)