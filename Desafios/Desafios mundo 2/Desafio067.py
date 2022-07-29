#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
from time import sleep

cont=0
while True:
    print('-='*30)
    n = int(input('Digite a Tabuado que você quer ver: '))
    print('-='*30)
    if n < 0:
        break
    for cont in range(0,11):
        print(f'{n} x {cont} = {n*cont}')
    print('Digite um valor negativo para finalizar.')
    print('-='*30)
sleep(1)
print('Finalizando.....')
print('Fim do pragrama. Volte Sempre!!!')
print('-='*30)