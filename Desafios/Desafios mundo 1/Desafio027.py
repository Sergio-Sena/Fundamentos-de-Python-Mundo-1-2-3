#Faça um programa que leia uma frase pelo teclado e mostre
# Quantas vezes aparece a letra'a'
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece pela última vez#
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na pocisão {}.'.format(frase.find('A')+1))
print('A ultima letra A apareceu na pocisão {}.'.format(frase.rfind('A')+1))