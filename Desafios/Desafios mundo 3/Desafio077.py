# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
resp = ''
while True:
    palavras = str(input('Dgite as palavras: '))
    resp = str(input('Mais palavras? [S/N]')).upper().strip()
    if resp == 'N':
        break
    print(palavras)