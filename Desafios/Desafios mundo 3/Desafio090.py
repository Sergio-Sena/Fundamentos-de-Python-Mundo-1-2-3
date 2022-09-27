# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
aluno['nome'] = str(input("Nome do aluno: "))
aluno['média'] = float(input(f'Média do aluno {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['Situação'] = 'Aprovado.'
elif 5 <= aluno['média'] < 7:
    aluno['Situação'] = 'Recuperação.'
else:
    aluno['Situação'] = 'Reprovado.'
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
