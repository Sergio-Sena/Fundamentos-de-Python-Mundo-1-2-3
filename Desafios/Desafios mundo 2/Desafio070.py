total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Digite o preço R$: '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format('Fim do programa'))
print(f'O total da sua compra foi {total:.2f}.')
print(f'Temos {totmil} produtos acima de R$ 1000')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')

