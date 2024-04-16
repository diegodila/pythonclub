def foo(name, age, year, height, weight):
    your_year = your_age(age, year)
    your_imc = imc(height, weight)
    print(f'Seu nome é: {name} o ano que nasceu: {your_year} seu imc é: {your_imc:.2f} ')


def your_age(age, year):
    your = year - age
    return your

def imc(height, weight):
    imc = weight / (height * height)
    return imc

foo('diego', 29, 2020, 1.87, 102)