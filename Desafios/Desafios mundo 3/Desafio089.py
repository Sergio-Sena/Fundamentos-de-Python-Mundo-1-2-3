# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
boletin = [[],[],[],[]]
media = []
boletin[0].append(str(input("Digite o nome do Aluno: ")))
boletin[1].append(float(input("Digite a 1° nota: ")))
boletin[2].append(float(input("Digite a 2° nota: ")))
print(f'O Aluno {boletin[0]} teve as notas {boletin[1]} e {boletin[2]}')