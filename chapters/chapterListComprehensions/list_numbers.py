lista = [1,2,3,4,5,6,7,8,9,10]
x = [x*2 for x in lista]
print(x)

#function 
def lista_(y):
    return [x*3 for x in y]

print(lista_(lista))

#lambda
list_ = lambda y: [x*3 for x in y]
print(list_(lista))