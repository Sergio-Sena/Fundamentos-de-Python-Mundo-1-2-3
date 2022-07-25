#Elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal e a forma de pagamento>
# A vista ou cheque 10% off
# A vista 5% off
# Em até 2x no cartao preço normal
# Acima de 3x no cartao 20%

print('{:=^40}'.format('Lojas Sena'))

preço = float(input('Digite o valor da compra: '))

print ('''Formas de pagamento: 
[1] Para pagamento a vista ou cheque.
[2] Para pagamento a vista no cartão
[3] Em ate 2X no cartão
[4] Acima de 3X no cartao''')
opção = int(input('Qual a opção? '))
if opção == 1:
    total = preço -(preço * 10 / 100)
    print ('Sua compra de R$ {} com desconto de 10% ficou por R$ {}.'.format(preço,total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print ('Sua compra de R$ {} com desconto de 5% ficou R$ {}.'.format(preço,total))
elif opção == 3:
    total = preço/2
    print ('Sua compra de R$ {} em 2x ficou R$ {} cada percela sem juros.'.format(preço,total))
elif opção == 4:
    totpar = (int(input('Qual o total de parcelas? ')))
    total = preço +(preço * 20  / 100)
    parcela = total / totpar
    print('Sua compra de R$ {} ficou {}x de {} com acrécimo,totalizando R${} no final.'.format(preço,totpar,parcela,total))
else:
    total =0
    print('Opção Inválida. Tente novamente.')
