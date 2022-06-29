# o mesmo professor do dedafio antarior quer sortear a ordem de apresentação dos alunos.Faça um programa que leia o nome o nome dos alunos e mostra a ordem sorteada. 
from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem de aoresentação é {} '.format(lista))