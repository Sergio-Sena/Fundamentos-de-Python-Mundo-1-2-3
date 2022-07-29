#Vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código. É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.Além disso, vamos aprender como trabalhar com as novas fstrings do Python.
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n ==999:
        break
    s += n
print(f'A soma vale {s}.')
nome = 'jose'
idade = 33 
print(f'O {nome} tem {idade} anos')