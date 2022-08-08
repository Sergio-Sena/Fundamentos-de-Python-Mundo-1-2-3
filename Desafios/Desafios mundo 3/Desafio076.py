#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('lapis',1.75,
'barracha',2,
'caderno',15.90,
'estojo',25.00,
'traferidor',4.20,
'compasso',4.99,
'mochila',120.00,
'canetas',22.30,
'livros',34.90)

print('-~' *20)
print(f'{"Listagem de preço":^30}')
print('-~' *20)

for item in range(0,len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<20}', end = '')
    else:
        print(f'R${listagem[item]:>7.2f}')
print('-~' *20)