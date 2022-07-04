print('''#Desafio#
#crie um programa que leia o nome completo de uma pessoa e mostre:
# 1-todas as letras maiúsculas
# 2-todas as letras minusculas 
# 3-quantas letras ao todo sem considerar espaços
# 4-quantas letras tem o primeiro nome #''')

nome = input('Digite seu nome completo: ')
print('Analisando seu nome.....')
print('Seu nome em maiúsculas:', (nome.upper()))
print('Seu nome em maiúsculas:', (nome.lower()))
print('Letras ao todo sem considerar espaços:', (len(nome)))
pn = nome.split()
print('Seu Primeiro nome é :',pn[0],'e contém',(len(pn[0])),'letras.')