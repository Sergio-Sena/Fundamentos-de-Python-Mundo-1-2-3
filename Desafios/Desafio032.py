#Faça um progrma de leia um ano de mostre se ele é BISSEXTO.
from datetime import date
a = int(input('Digite o ano para analisar com 4 digitos "XXXX".\nDigite 0 para verificar o ano atual:'))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a %100 != 0 or a % 400 == 0:
    print('O ano de {} é bissexto.'.format(a))
else:
    print('O ano {} não é bissexto.'.format(a))