# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',' dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resp =''
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    resp = str(input('Quer continuar?[S/N] ')).upper().strip()
    if 0 <= num <= 20 and resp == 'N':
        break
    print(f'Você digitou o número {cont[num]}')
    print('Tente novamente. ',end ='')
print(f'Você digitou o número {cont[num]}')
