#Crie um progrma que leia um número e mostre na tela se ele é PAR ou IMPAR.
n = int(input('Digite um número: '))
v = n % 2
if v == 0:
    print('{} É um número par.'.format(n))
else:
    print('{} É um número impar.'.format(n))



