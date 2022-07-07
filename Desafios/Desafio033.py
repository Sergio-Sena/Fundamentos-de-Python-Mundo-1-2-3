#Faça um progrma que leia 3 numeros e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 > n2 and n3:
    print( 'O maior número digitado foi: {}.'.format(n1))
if n2 > n1 and n2 > n3:
    print('O maior número digitado foi: {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior número digitado foi: {}'.format(n3))