# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

resp = 'S'
cont = 1
toth = 0
idadeM = 0
idade = 0
while resp not in 'Nn':
    idade = int(input('Digite a idade :'))
    sexo = str(input('Digite o sexo: [M/F] ')).upper().strip()
    print(f'idade {idade} sexo {sexo}')
    resp = str(input('Quer continunar [S/N]? ')).upper().strip()[0]
    if resp == 'S':
        cont += 1
    if idade > 18:
        idade += 1
    if sexo =='M':
        toth += 1
    if sexo == 'F' and sexo == 'F':
        idadeM += 1 
    if resp == 'N':
        break
print (f'Total de {cont} pessoas sendo {idadeM} maior de 18 anos, {toth} homens e {idadeM} mulheres menor de 20.' )
