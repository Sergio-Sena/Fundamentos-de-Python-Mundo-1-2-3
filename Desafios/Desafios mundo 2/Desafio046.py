#Faça um programa que mostre na tela uma contagem regressiva para os fogos de artificio, indo de 10 ate 0 com pausa de 1 segundo entre eles.
from time import sleep

for c in range(10,-1,-1):
    print(c)
    sleep(1) 
print('Feliz ano novooooooooo!!!!!!!!')