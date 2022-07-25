#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior

#– O segundo valor é maior

#– Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print('o primeiro valor é maior, {} .'.format(n1))
elif n2> n1:
    print('O segundo valor é maior, {}.'.format(n2))
else:
    print('Não existe valor maior, os valores são iguias.')
