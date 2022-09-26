# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
from time import sleep

ficha = list()
while True:
    nome = str(input('Digite o nome do aluno: '))
    n1 = float(input('Digite a Nota 1: '))
    n2 = float(input('Digite a Nota 2: '))
    media = (n1 + n2)/2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N] )'))
    if resp in "Nn":
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print("-" * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar a nota de qual aluno? (999 interrompe): ' ))   
    if opc == 999:
        print('Finalizando....')
        sleep(2)
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('-=' *30)
print('<<<Volte sempre>>>')