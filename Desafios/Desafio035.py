#Desenvolva um programa que peça tres valores de retas e diga se o  usuário se pode ou não formar um triangulo.
n1 = float(input('Digite o valor da primeira reta: '))
n2 = float(input('Digite o valor da segunda reta: '))
n3 = float(input('Digite o valor da terceira: '))
if n1 < n2+n3 and n2 < n1+n3 and n3 < n1 + n2: 
    print( 'Com Os valores digitados {},{},{}  é possivel fazer um triângulo.'.format(n1,n2,n3))
else:
    print('Com os valores digitados {},{},{} não é possivel formar um triângulo.'.format(n1,n2,n3))
