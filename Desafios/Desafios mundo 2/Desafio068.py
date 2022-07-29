#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
print('-='*30)
print('Vamos jogar par ou impar?')
print('-='*30)
from random import randint
pontocpu = pontos = cont = 0 



while True:
    resp = int(input('Escolha 0 para par ou 1 para impar:  '))
    n = int(input('Digite um valor:'))
    cpu = (randint(0,10))
    if resp == 0 :
        if n % 2 == 0:
            print('jogador ganhou!')
            pontos = cont + 1
            print('-='*30)
        else:
            print('Ganhei!')
            pontocpu += 1
    if resp == 1:
        if n % 2 == 1:
            print('Jogador ganhou.')
            pontos += 1
            print('-='*30)
        else:
            print('Ganhei!')
            pontocpu += 1
    if pontocpu == 1:
        break
print(f'{n}')
print(f'{cpu:.0f}')
print(f'Computador fez {pontocpu}')
print(f'Parabéns você fez {pontos} pontos.')