num = [2, 5, 9, 1]
num[2]=3
num.append(7)
num.sort()
num.sort(reverse=True)
print(num)
num.insert(2,0)
num.pop(2)
print(f'Essa lista tem {len(num)} elementos.')

from random import randint

valores =[]
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print(f'Essa lista tem {len(valores)} valores')
print('Cheguei ao final da lista.')