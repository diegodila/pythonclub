class Pessoa:

    def __init__(self,nome='Diego',sobrenome=''):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('GF','GF3')
p2 = Pessoa('fc', 'df')
lista = [vars(p1), vars(p2)]

import json 
PATH_TO_JSON = './work/pythonclub/f5_POO/json/salva_classe.json'
def salvar_json():
    with open(PATH_TO_JSON, 'w') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=2)
        
salvar_json()