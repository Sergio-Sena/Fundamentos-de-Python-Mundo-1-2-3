#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = (float(input('Qual o o valor da Casa R$?: ')))
sal = (float(input('Qual o valor do salário mensal?: ')))
prazo = (int(input('Em quantos anos a dívida será quitada?: ')))
mensal = ((valor/prazo)/12)
if mensal <= ((sal*30)/100):
    print('Finaciamento aprovado.Serão prestações de {:.3f} mensais por {} anos.'.format(mensal,prazo))
else:
    print('Financiamento Recusado.Prestação de {} é maoir do que 30% da renda mensal informada que é de {:.2f}.'.format(mensal,sal))