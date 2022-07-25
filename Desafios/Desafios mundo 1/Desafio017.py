# Anunciado: Crie um programa que leia um numero Real e mostres a sua porção inteira.

from math import trunc
num = float(input('Digite um número: '))
print('Numero digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))