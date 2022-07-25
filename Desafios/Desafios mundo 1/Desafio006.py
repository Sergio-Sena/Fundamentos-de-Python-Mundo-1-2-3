#Crie um programa que leia um número e mostre na tela o  Dobro,triplo, e raiz quadrada #

n = int(input('Digite um valor :'))
cores = {'limpa':'\033[m',
'branco':'\033[30m',
'vermelho':'\033[31m',
'verde':'\033[32m',
'amarelo':'\033[33m',
'azul':'\033[34m',
'magenta':'\033[035m',
'ciano':'\033[36m',
'cinza':'\033[37m',
'bold':'\033[1;33'}

print('O dobro do valor digitado vale {}{}{},\nO triplo vale {}{}{}\nE a raiz quadrada vale {}{:.2f}.'.format(cores['vermelho'], n*2, cores['limpa'], cores['magenta'], n*3, cores['limpa'], cores['ciano'],pow(n,(1/2))))