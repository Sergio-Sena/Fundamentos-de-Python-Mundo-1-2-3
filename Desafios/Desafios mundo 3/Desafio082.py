#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

#entrada de lista
num = list()
pares = list()
impar = list()
#leitura de entrada
#leitura de resposta
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar?[S/N] '))
    if resp in 'Nn':
        break
for i ,v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-='*30)
print(f"Os valores digitados foram {num}")
print(f"Os valores pares foram {pares}")
print(f"Os valores ìmpares foram {impar}")