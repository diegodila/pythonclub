#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total em dias

def smoking(*args):
    i = 0
    minutos = (args[i][i] * 10) * (args[i][i+1] * 365)
    horas = ((minutos / 60) // 1)
    hora_minuto = ((minutos / 60) % horas) * 60
    print(f'O tempo perdido de vida em total de minutos: {minutos} ')
    print(f'O tempo perdido de vida é: {horas:.0f} horas e {hora_minuto:.0f} minutos ')
    return f'minutos{minutos} horas:{horas} minutos:{hora_minuto}'


lista = []
lista.append(int(input('Quantos cigarros você fuma por dia: ')))
lista.append(int(input('Quantos anos fumando? ')))
smoking(lista)