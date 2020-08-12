x = ['Python wins, Pythonico', 'Pisco, Pateta', 'Ps , SP']
a = [y.replace('P', '*') for y in x]
print(a)

split = [y.split() for y in x]
print(split)

z = [i.replace(' ,', ',') for i in x]
print(z)
