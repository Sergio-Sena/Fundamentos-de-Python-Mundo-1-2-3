#Faça em programa que leia um salario e calcule o valor de aumento de 10% para salarios acima de 1.250,00 e de 15% para salarios abaixo 1.250,00
sal = float(input('Digite a salario do funcionário: '))
salm = 1.250
if sal >= salm:
    print('O novo salário desse funcionário é de R$ : {:.3f}'.format(sal+(sal*0.10)))
else:
    print('O novo salário do funcinário é de R$ {:.3f}.'.format(sal+(sal*0.15)))