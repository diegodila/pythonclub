'''
1 - receber um numero inteiro
2 - saber se o numero é multiplo de 3 e 5:
    bacon com ovos
3 - saber se o numero é multiplo de 3
    bacon
4 - saber se o numero é multiplo somente de 5:
    ovos
5 - saber se o numero não é multiplo de 3 e 5:
    passa fome
'''

def nobaconeggs(n):
    assert isinstance(n, (float, int)), 'n deve ser int ou float'

    if n % 3 == 0 and n % 5 == 0:
        return 'alface com ovos'

    if n % 3 == 0:
        return 'Algas'

    if n % 5 == 0:
        return 'Ovos'

    return 'Passar fome'