def salary(salary):
    aumento = [1.05, 1.10, 1.20, 1.30, 1.40, 1.50]
    return salary * aumento[0]


print(salary(1000))