#Desafio 15 #
# Aluguel de carros #
km = float(input('Quantos km foram rodados ?:'))
dias =int(input('Qauntos dias foram alugados ?'))
pago = (dias*60)+(km*0.15)
print('O tal a pagar é de R${:.2f}'.format(pago))