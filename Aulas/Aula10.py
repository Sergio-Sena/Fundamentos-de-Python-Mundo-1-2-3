# condições em python
#Anunciado: 

nome = str(input('Qual o seu nome ? '))
nomem = nome.upper()
if nomem == "SERGIO":
    print('Que nome lindo você tem')
print('Bom dia {}.'.format(nome))
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua nota foi {:.1f}'.format(m))
if m >=6.0:
    print('Sua média foi boa.PARABENS.')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')