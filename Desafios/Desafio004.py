#crie um programa que leia um nome e mostre na tela.

nome = input('Digite seu nome : ')
cores = {'limpa':'\033[m',
        'vermelho':'\033[7;31;40m',}
        
print('Olá {}{}{}, é um prazer conhece-lo'.format(cores['vermelho'], nome ,cores['limpa']))