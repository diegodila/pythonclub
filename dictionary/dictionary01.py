cidade = {
    'Sao Paulo' : {
        'rua' : 'faria lima',
        'bairro' : 'itaim'
    },
    'Los Angeles': {
        'rua' : 'bervely hills',
        'bairro' : 'hollywood'
    },
    'Berlim': {
        'rua' : 'kors',
        'bairro' : 'derkou'
    }
}

for cidade_chave, cidade_valor in cidade.items(): 
    print(f'Exibindo {cidade_chave}')
    for rua_chave, rua_valor in cidade_valor.items():
        print(f'\t{rua_chave}',rua_valor)

print('Aqui deletamos são paulo!!!')

del cidade['Sao Paulo']

for cidade_chave, cidade_valor in cidade.items(): 
    print(f'Exibindo {cidade_chave}')
    for rua_chave, rua_valor in cidade_valor.items():
        print(f'\t{rua_chave}',rua_valor)