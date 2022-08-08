#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.

núm = (int(input('Digite um valor: ')),
int(input('Digite o segundo valor: ')),
int(input('Digite o terceiro valor: ')),
int(input('Digite o quarto valor: ')))
print(f'você digitou os valores: {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes.')
if 3 in núm:
    print(f'O valor 3 aparece na posicisão {núm.index(3)+1}º')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram ', end = '')
for n in núm:
    if n % 2 == 0:
        print(n, end='')