#Desenvolva um programa que pergunte a distancia da viagem em km. Calcule o preço da passagem cobrando R$ 0,50 por km para viagens ate 200km e 0,45 para viagem mais longas.
km = float(input('Digite o kilometragem da sua viagem: '))
if km <= 200:
    print('A sua viagem custará R${:.2f}.'.format(km*0.50))
else:
    print('Sua viagem custará R${:.2f}.'.format(km*0.45))