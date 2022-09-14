# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

# Entrada de dados

num = [[],[]]
valor = 0
for i in range(1,8):
    valor = (int(input(f"Digie o {i}º numero: ")))
    if valor % 2 == 0:
            num[0].append(valor)
    if valor % 2 == 1:
            num[1].append(valor)      
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram {num[0]}')
print(f"Os valores impares digitados foram {num[1]}") 
