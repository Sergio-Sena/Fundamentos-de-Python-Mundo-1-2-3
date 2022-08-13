# A confederação Nacional precisa de um programa que leia o ano de nascimento do atelta e de acordo com sua idade classifque:
#- Até 9 anos: mirim
#- Até 14 anos:infantil
#- Ate 19 anos:junior
#-Ate 20 anos:Senior
#-Acima master
from datetime import date

cores = {'limpa':'\033[m',
'branco':'\033[30m',
'vermelho':'\033[31m',
'verde':'\033[32m',
'amarelo':'\033[1;33m',
'azul':'\033[34m',
'magenta':'\033[35m',
'ciano':'\033[36m',
'cinza':'\033[37m',}
nasc = int(input('Digite a data do seu nascimento com 4 digitos XXXX: '))
idade = date.today().year - nasc
if idade  <=9:
    print(f'O atelata tem {idade} anos.Sua categoria é mirin.')
elif idade <= 14:
    print(f'O atleta tem {idade} anos. Sua classe é Infantil')
elif idade <= 19:
    print(f'O atleta tem {idade} anos. Sua categoria é junior.')
elif idade <= 20:
    print(f'O atleta tem {idade} anos. Sua categoria é Senior.')
else:
    print(f'O atleta tem {idade} anos. Sua categoria de master.')

