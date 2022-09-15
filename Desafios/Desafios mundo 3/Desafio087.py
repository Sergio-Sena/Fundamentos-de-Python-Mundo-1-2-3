# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:

# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

from threading import main_thread


matrix = [[0,0,0],[0,0,0],[0,0,0]]
spar = scol = mai = 0
for l in range(0,3):
    for c in range(0,3):
        matrix[l][c] = (int(input(f"Digite o valor de {[l],[c]}")))
print('-='*30)
for l in range(0,3):    
    for c in range(0,3):
        print(f'[{matrix[l][c]:^5}]',end ='')
        if matrix[l][c] % 2 == 0:
            spar += matrix[l][c]
    print()
print("-="*30)
print(f'A soma dos valores pares vale {spar}.')
for l in range(0,3):
    scol += matrix[l][2]
print(f"A soma dos valores da terceira coluna vale {scol}.")
for c in range(0,3):
    if c == 0:
        mai = matrix[1][c]
    elif matrix[1][c] > mai: 
        mai = matrix[1][c]
print(f'A maior valor da segunda coluna é {mai}.')