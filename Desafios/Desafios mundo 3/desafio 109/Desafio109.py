# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from time import sleep
import moeda


p = int(input('Digite o preço R$: '))
sleep(1)
print(f'A metada de de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(
    f'Aumentando em 10 % o valor de {p} fica em {(moeda.aumentar(p,10, True))}')
print(
    f'Diminuindo em 10 % o valor de {p} fica em {(moeda.diminuir(p,10, True))}')
