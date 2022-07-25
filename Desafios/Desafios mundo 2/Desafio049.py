#Refaça o exercício 009 mostrando a tabuada que o usuario escolher, so que agora utilizando o laço for.
from time import sleep
print('-='*25)
n =(int(input('Qual a tabuada devo mostrar?: ')))
for cont in range(0,11):
    sleep(0.5)
    print(n,'x',cont,'=',n*cont)
print('-='*25)
