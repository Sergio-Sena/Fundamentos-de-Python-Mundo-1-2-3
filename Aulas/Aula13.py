#laço com variável de controle.
from tkinter import N


s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n
print('A soma de todos os números é {}.'.format(s))
print('fim') 