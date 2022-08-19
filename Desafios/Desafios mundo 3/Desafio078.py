#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
maior = 0
menor = 0
listanum = []
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a pocisão {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        elif listanum[c] < menor:
            menor = listanum[c] 
print('=-'*30)
print(f'Você adicionou os valores {listanum}')
print('Essa e sua lista ordenada {}'.format(sorted(listanum)))
print(f'O maior valor digitado foi {maior} nas pocisões ',end ='')
for i ,v in enumerate(listanum):
    if v == maior:
        print(f'{i}...',end ='')
print(f'O menor valor digitado foi {menor} nas pocisões ',end ='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...')