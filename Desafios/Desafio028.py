#Faça um programa que leia o nome completo de uma pessoa, mostre em seguida o primeiro e o último nome dela
# Ex.:Ana maria de souza
# Primeiro = Ana
# último = Souza #
n = str(input('Digite um nome completo: ')).strip()
nome = n.split()
print('Prazer em conhcece-lo ',nome[0])
print('Primeiro nome {}.'.format(nome[0]))
print('Ultimo nome {}.'.format(nome[len(nome)-1]))
