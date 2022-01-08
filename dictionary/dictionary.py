pessoas = {
    'jose' : {
        'rua' : 'faria lima',
        'cep' : '01045-370'
    },
    'pedro': {
        'rua' : 'peixoto galeao',
        'cep' : '09034-423'
    }
}

for i, j in pessoas.items(): 
    print(f'Exibindo {i}')
    for k, l in j.items():
        print(f'\t{k}',l)