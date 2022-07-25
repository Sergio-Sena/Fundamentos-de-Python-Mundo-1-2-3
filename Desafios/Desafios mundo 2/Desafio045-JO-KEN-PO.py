#Crie um programa que faça o computador jogar jokenpô com você.
from random import randint 
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)

print('''Suas Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada?: '))
print ('-='*11)
print('jo')
sleep(1)
print('Ken')
sleep(1)
print('Po!!!')
sleep(1)
print ('-='*11)
print ('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print ('-='*11)
if computador == 0: #computador joga pedra
    if jogador == 0:
        print('Empate.')        
    elif jogador == 1:
        print('Jogador ganhou.')
    elif jogador == 2:
        print('Computador venceu.')
    else:
        print('jogada inválida')
elif computador == 1: #computador joga papel
    if jogador == 0:
        ('computador venceu.')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('jogador venceu.')
    else:
        print('jogada inválida.')
elif computador == 2: #computador Tesoura
    if jogador == 0:
        print('jogador venceu.')
    elif jogador == 1:
        print('computador venceu.')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('jogada inválida.')
