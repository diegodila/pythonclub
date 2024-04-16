def sala_cinema():
    sala = [10,4,3,2,0]
    while True:
        digito = int(input('Digite o numero da sala de cinema do 1 ao 5, (0 sair): \n'))
        if digito == 0:
            print('Sessão encerrada!!!!\n')
            break
        elif digito > len(sala) or digito < 1:
            print('Sala inválida!!!\n')
        elif sala[digito-1] == 0:
            print('Não há lugares na sala escolhida!!!\n')
        else:
            lugares = int(input(f'Digite a quantidade de lugares (disponíveis:{sala[digito-1]}): \n'))
            if lugares > sala[digito-1]:
                print('Não há essa quantidade de lugares!!\n')
            elif lugares < 1:
                print('lugar inválido, digite a quantidade de lugares\n')
            else:
                sala[digito-1]-=lugares
                print(f'Vendido {lugares} lugares, agora a sala tem {sala[digito-1]} lugares\n')
    print('Utilização das salas')
    for i,j in enumerate(sala):
        print(f'sala: {i+1} lugares: {j}')


sala_cinema()