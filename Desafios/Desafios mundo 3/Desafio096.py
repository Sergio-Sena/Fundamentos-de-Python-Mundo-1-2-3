# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terrenoretangular (largura e comprimento) e mostre a área do terreno.
from time import time


from time import sleep

def lin():
    print('-'*30)
    print('Controle de Terrenos')
    print('-'*30)

def área() :
    l = float(input('Qual e largura do Terreno ?: '))
    c = float(input('Qual o cumprimento do Terreno ?: ')) 
    a = l*c
    sleep(1)
    print(f'A área do seu terreno de de {a:2.2f} m².')    

lin()
área()
print('-=' * 30)
print('<<<Finalizando....>>>')
sleep(2)
print('<<<Fim....>>>')