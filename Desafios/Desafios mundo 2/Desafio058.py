#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
print('#=#'*30)
print('Olá, Vamos fazer um pequeno jogo de adivinhação.\nEu vou pensar em un número e você diz qual número eu pensei.\nEle será de 0 a 5. ')
print('#=#'*30)

from time import sleep
from random import randint

jogador = int(input('Digite o número que eu pensei: '))
cpu = randint(0,10)
print(cpu)

while jogador != cpu:
    print('Tente de novo.')
    jogador = int(input('Digite o número que eu pensei: '))
    if jogador == cpu:
        print('Parabens você ganhou.')