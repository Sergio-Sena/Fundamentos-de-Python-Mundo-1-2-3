#Escreva um programa que leia a velocidade de um carro.
#se ele ultrapassar a delocidade de 80km/h mostre uma mensagem que ele foi multado.
# Multa custará R$ 7,00 por cada Km acima da velocidade.
km = float(input('Qual foi a velocidade medida? '))
vel = 80
multa = 7
if km <=(vel):
    print('Bom dia. Dirija com segurança!')
else:
    print('Você foi multado por excesso de velocidade que é de 80km/h. A multa gerada foi de R${:.2f}.'.format((km-80)*7))