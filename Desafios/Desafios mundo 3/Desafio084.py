# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. 
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


# importar lib de tempo
from time import sleep
# Ler nome e peso
temp = []
princ = []
mai = men = 0
# Alimentar e validar dados
while True:
    temp.append(str(input("Digite o nome: ")))
    temp.append(float(input("Digite o peso: ")))
    if len(princ) == 0: 
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:   
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input("Quer contnuar?[S/N]: "))
# Quebra de Loop
    if resp in "Nn":
        break
print("-=" *30)
# Impressão de dados
print(f"Você cadastrou {len(princ)} pessoas")
# Validação de maoir peso
print(f"O maior peso foi {mai} kg. Peso de",end ='')
for p in princ:
    if p[1] == mai:
        print(f"{[p[0]]}")
print('-=' *30)
# Validação de menor peso
print(f'O menor peso foi {men} kg. Peso de ',end ='')
for p in princ:
    if p[1] == men:
        print(f"{[p[0]]}")
print("-=" *30)
print('Finalizando.....')
sleep(2)