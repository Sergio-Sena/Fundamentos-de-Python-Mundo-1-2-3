#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
from turtle import clear


cont = 0
print('Digite 999 para parar.')
n = int(input('Digite um valor: '))
while n != 999:
    n = int(input('Digite um valor: '))
    if n <= 999:
        n1 = n
        cont +=1
print(cont)  
print('Fim')