#Deselvolva um programa que leia o nome,idade e sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo
#Qual é o nome do homen mais velho.
#Quantas mulheres tem menos de 20 anos
somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for p in range(1,5):
    print('------{}° PESSOA------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in   'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
media = somaidade / 4
print('A media de idade do grupo é {} anos'.format(media))
print('O homen mais velho tem {} e se chama {}.'.format(maioridadehomem, nomevelho))
print('O total de mulheres no grupo menor de 20 anos são {}.'.format(totmulher))