def tax(salary):
    if (salary > 4900):
        salary *= 0.80
        print('Você foi taxado!!! seu novo sálario é:',salary, sep=' --> ')
    else:
        print('Você não foi taxado!!!')



tax(10000)