from time import sleep
#---------------------------------------#
print('Antecessor e sucessor')
#---------------------------------------#
cores ={'limpa':'\033[m',
'verde':'\033[32m',
 'amarelo':'\033[33m',
 'azul':'\033[034m'}
n = int(input('Digite um número :'))
print('Analisando...')
sleep(1)
print('Número digitado  {}{}{}\nNúmero antecessor {}{}{}\nNúmero sucessor é {}{}'.format(cores['amarelo'],n,cores['limpa'],cores['verde'],n-1,cores['limpa'],cores['azul'],n+1))