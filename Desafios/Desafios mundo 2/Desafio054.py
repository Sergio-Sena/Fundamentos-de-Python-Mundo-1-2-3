#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostra quantas pessoas não atingiram a maior idade e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Digite a {} data de nascimento: '.format(pess)))
    idade = atual-nasc
    if idade >= 21:
        print(idade)
        totmaior += 1
    else:
        print(idade)
        totmenor += 1
print('{} pessoas sao de menor idade.'.format(totmenor))
print('{} pessoas sao maior de idade.'.format(totmaior))