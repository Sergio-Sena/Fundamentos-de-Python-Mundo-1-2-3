#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

media = maior = menor =0
r = 'n'
while r == 's':
    n =int(input('digite um número: '))
    if n > maior:
        maior = n
        print(maior)
    elif n < maior:
        menor = n
        print(menor)
    r = str(input('Digitar outro número?: '))