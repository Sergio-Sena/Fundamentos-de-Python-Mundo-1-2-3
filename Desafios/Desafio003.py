#Crie um programa queleia 2 números e mostre a soma deles na tela.
cores = {'limpa':'\033[m',
'azul':'\033[34m',
'verde':'\033[32m',
'ciano':'\033[36m'}

n1 = int(input('Digite um número :'))
n2 = int(input('Digite outro número:'))
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}'.format(cores['azul'], n1,cores['limpa'], cores['verde'],n2,cores['limpa'], cores['ciano'],n1+n2, cores['limpa']))