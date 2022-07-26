#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Importar biblioteca randon
from random import randint
from socket import inet_pton
#Randomizar um nuemro de 0,10
computador = randint(0,10)
print('=-'*30)
print('Sou seu computador....Acabei de pensar um número entre 0 e 10 .')
print('Será que você consegue acertar? ')
print('=-'*30)
acertou = False
palpites = 0
while not acertou:
    jogador =int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        else:
            print('Menos...tente mais uma vez.')
print('Acertou com {} palpites.Eu pensei no número {}. Parabéns.'.format(palpites,computador))