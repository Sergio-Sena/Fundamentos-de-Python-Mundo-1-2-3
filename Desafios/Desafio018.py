#crie um programa que calcule a hiponusa de um cateto e o cateto
from math import hypot
sen = float(input('Digite o valor de seno: '))
cos = float(input('Digite o valor de coseno: '))
print('O valor da Hipotenusa de {} e {} é igual a {:.2f}'.format(sen, cos, hypot(sen,cos)))