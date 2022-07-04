print('''#Desafio#
#crie um programa que leia o nome completo de uma pessoa e mostre:
# 1-todas as letras maiúsculas
# 2-todas as letras minusculas 
# 3-quantas letras ao todo sem considerar espaços
# 4-quantas letras tem o primeiro nome #''')

nome = input('Digite seu nome completo: ')
print('1- todas as letras maiúsculas:', (nome.upper()))
print('2- todas as letras minusculas:', (nome.lower()))
print('3- quantas letras ao todo sem considerar espaços:', (len(nome)))
pn = nome.split()
print('4- Primeiro nome:',pn[0],(len(pn[0])),'Letras')