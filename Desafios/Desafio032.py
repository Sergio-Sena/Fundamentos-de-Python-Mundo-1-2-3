#Faça um progrma de leia um ano de mostre se ele é BISSEXTO.
a = int(input('Digite o ano letivo com 4 digitos "XXXX":'))
if a % 4 == 0:
    print('O ano de {} é bissexto.'.format(a))
else:
    print('O ano {} não é bissexto.'.format(a))