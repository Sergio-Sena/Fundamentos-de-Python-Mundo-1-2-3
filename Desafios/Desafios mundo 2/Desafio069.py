# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

resp = 'S'
cont = 1
Maioridade = tothomen = menoridade = 0

while resp not in 'Nn':
    print('-='*25)
    idade = int(input('Digite a idade :'))
    sexo = str(input('Digite o sexo: [M/F] ')).upper().strip()
    print('-='*25)
    resp = str(input('Quer continunar [S/N]? ')).upper().strip()[0]
    if resp == 'S':
        cont += 1
    if idade > 18:
        Maioridade += 1
    if sexo == 'M':
        tothomen += 1
    if sexo == 'F' and idade < 20:
        menoridade += 1
    if resp == 'N':
        break
print('-='*25)    
print (f'Total de {cont} pessoas.')
print(f'Sendo {Maioridade} maior de 18 anos.')
print(f'{tothomen} homens.')
print(f'{menoridade} mulheres menor de 20.')
