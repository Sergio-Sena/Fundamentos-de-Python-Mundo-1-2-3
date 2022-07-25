#Desenvolva um programa que leia seis numeros inteiros e mostra a soma apenas daqueles que forem pares.Se o valor for impar descarte-o. 
print('#-#'*25)
soma = 0
for c in range(0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0: 
        soma = soma+n
print('A soma dos numeros pares vale {}.'.format(soma))
print('#-#'*25)