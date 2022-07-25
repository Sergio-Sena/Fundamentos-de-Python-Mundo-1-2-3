#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão.
print('-='*25)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('-='*25)
primeiro = int(input('Digite um número: '))
razao = int(input('Digite um número: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro,decimo+ razao,razao):
    print('{} '.format(c), end='-> ')
print('Acabou')
