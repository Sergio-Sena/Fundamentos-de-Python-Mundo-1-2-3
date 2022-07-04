#faça um progrma que leia um numero de 0 a 9999 e mostre na tela casa um dos números separados
# EX.: 1834
# unidades 4
# dezenas 3
# centenas 8
# milhar 1#

from re import U


num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade {}'.format(u))
print('Dezenas {}'.format(d))
print('Centenas {}'.format(c))
print('Milhar {}'.format(m))