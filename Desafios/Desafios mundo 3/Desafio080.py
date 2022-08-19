#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

from tkinter import INSERT


n = list()
for c in range(0,5):
    n = 0
    if n == 0:
        n.append(int(input('Digite um valor: ')))
print(n)