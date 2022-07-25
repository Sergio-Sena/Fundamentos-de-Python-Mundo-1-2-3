#Faça um progrma que leia 3 numeros e mostre qual é o maior e qual é o menor.
from re import A


a = int(input('Digite o Primeiro número: '))
b = int(input('Digite o Segundo número: '))
c = int(input('Digite o Terceiro numero: '))

'''if a > b and c:
    print( 'O maior número digitado foi: {}.'.format(a))
if c > a and b > c:
    print('O maior número digitado foi: {}'.format(b))
if c > a and c > b:
    print('O maior número digitado foi: {}'.format(n3))'''
#Resolução Simplificada
#Verificando quem é menor:
menor = a
if b < a and  b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é maior:
maior = a
if b> a and b>c:
    maior = b
if c> a and c< b:
    maior = c
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))