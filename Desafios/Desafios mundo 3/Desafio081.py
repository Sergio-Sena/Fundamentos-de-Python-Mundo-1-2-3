#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:                                                                           
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Continuar?[S/N] '))
    if resp in 'Nn':
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem reserva são {lista}')
if 5 in lista:
    print('O valor 5 esnta na lista.')
else:
    print('O valor 5 não faz parte da lista')