# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleiçõe

from datetime import date

def voto():
    if idade > 18:
        return ('Voto Negado' )
    elif idade < 18 and idade > 70:
        return ('Voto Obrigatorio')
    else:
        return( 'Voto facultativo')  


hoje = date.today().year
nasc = int(input('Digite a date de Nasc.: '))
idade = hoje - nasc
voto(idade)
print (f'Seu voto é {voto(idade)}')