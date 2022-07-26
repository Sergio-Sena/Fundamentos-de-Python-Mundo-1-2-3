#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
print('#=#'*30)
print('Olá, Vamos fazer um pequeno jogo de adivinhação.')
print ('Eu vou pensar em un número e você diz qual número eu pensei.\nEle será de 0 a 10. ')
print('#=#'*30)
#importação de biblioteca
from time import sleep
from random import randint
#variável
cont = 1
jogador = int(input('Digite o número que eu pensei: '))
cpu = randint(0,10)
#laço de repetição
while jogador != cpu:
    print('Tente de novo.')
    jogador = int(input('Digite o número que eu pensei: '))
    cont +=1    
    if jogador == cpu:
        print('Parabens você ganhou.')
print('Mas precisou de {} chances para acertar.'.format(cont))        