#faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem de aumento. Exiba o valor do aumento
def salary_increase(*args):
    i = 0
    novo_salario = args[0][i] * ((args[0][i+1] / 100) + 1)
    format(novo_salario, '5')
    return novo_salario

lista = []
lista.append(float(input("Digite o valor do salário: ")))
lista.append(float(input("Digite a porcentagem de aumento: ")))

print(salary_increase(lista))

