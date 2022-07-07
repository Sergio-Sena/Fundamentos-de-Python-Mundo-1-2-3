#Escreva um programa que faça um computador pensar em um  número entre 0 e 5 e peça para o usuario descobri qual foi o número escolhido pelo computador.\n O computador deverá escrever na tela se o usuário ganhou ou perdeu! 

print('#=#'*30)
print('Olá, Vamos fazer um pequeno jogo de adivinhação.\nEu vou pensar em un número e você diz qual número eu pensei.\nEle será de 0 a 5. ')
print('#=#'*30)

jogador = int(input('Digite o número que eu pensei: '))
from time import sleep
from random import randint
cpu = randint(0,5)
print('PROCESSANDO....')
sleep(2)
if jogador == (cpu):
    print('Parabens você ganhou.')
else:
    print('GANHEI.Eu pensei no número {} e não no {}.'.format(cpu,jogador))