# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleiçõe

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        print(f' Com {idade}: Não Vota.') 
    elif 16 < idade < 18 or idade > 65:
        print(f'Com {idade}: O Voto é facultativo.')
    else:
        print(f'Com {idade} o voto é obrigatório') 

#Programa Principal
nasc = int(input('Em que ano você nasceu?: '))
print (voto(nasc))