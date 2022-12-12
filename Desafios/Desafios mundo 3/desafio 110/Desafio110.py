# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda

p = int(input('Digite o preço R$: '))
print(f'A metada de de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando em 10 % o valor de {p} fica em {(moeda.aumentar(p,10, True))}')
print(f'Diminuindo em 10 % o valor de {p} fica em {(moeda.diminuir(p,10, True))}')