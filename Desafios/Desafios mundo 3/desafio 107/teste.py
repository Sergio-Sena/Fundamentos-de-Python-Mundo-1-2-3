import moeda

p = float(input('Digite o preço R$: '))
print(f'A metadade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando em 10 % o valor de {p} fica em {moeda.aumentar(p,10)}')
print(f'Diminuindo em 10 % o valor de {p} fica em {moeda.diminuir(p,10)}')