#Crie um programa que leia um nome de uma pessoa e se ela tem 'silva' no nome #
nome = str(input('Digite um nome: ')).strip()
print('Seu nome tem Silva ? {}'.format('silva' in nome.lower()))