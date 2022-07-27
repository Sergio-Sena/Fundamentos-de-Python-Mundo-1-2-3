#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
from os import cpu_count


print('-='*25)
print('Gerador DE UMA PA')
print('-='*25)
primeiro = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')