#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e se encontram no intervalo entre 1 até 500.
v = 0
cont = 0
for c in range (1,501, 2):
    if c % 3 == 0:
        cont = cont+1
        v = v + c
print('A soma de todos os números impares e multiplos de 3 no intervalo de 1 a 500 vale {} e são  {} números.'.format(v,cont))