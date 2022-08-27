#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

#entrada de lista
valores = []
#leitura de entrada
#leitura de resposta
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar?[S/N] '))
    if resp in 'Nn':
        break
print(f'Os valores digitados foram {valores}')