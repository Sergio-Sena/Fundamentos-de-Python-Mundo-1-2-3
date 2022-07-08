#Crie um programa que Leia o dia, mes e ano do usuario e mostre na tela as respectivas datas.
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[4;33m',
        'pretoebranco':'\033[7;30m'}

d = int(input('Digite o dia do seu nascimento :'))
m = input('Digite o mes do seu nascimento :')
a = int(input('Digite o ano do seu nascimento :'))
print('Voce nasceu no dia {}{} do {} de {}{}. Correto ?'.format(cores['amarelo'], d, m, a, cores['limpa']))
