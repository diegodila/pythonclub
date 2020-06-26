#composição de strings com multiplos valores, string, inteiro, decimal 
nome = 'Diego'
idade = 29
valor = 100.25
print('Nome:%s idade:%03d valor na carteira:%5.2f'%(nome,idade,valor))
print('Nome:%10s idade:%3d valor na carteira:%f'%(nome,idade,valor))
print('Nome:%-10s idade:%-3d valor na carteira:[%-5.2f]'%(nome,idade,valor))