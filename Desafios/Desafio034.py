#Faça em programa que leia um salario e calcule o valor de aumento de 10% para salarios acima de 1.250,00 e de 15% para salarios abaixo 1.250,00
sal = float(input('Digite a salário do funcionário R$: '))
if sal <= 1250:
    novo = sal + (sal*15/100)
    print('O novo salario do funcioanario sera R$ {:.2f}'.format(novo))
else:
    novo = sal + (sal*10/100)
    print('O novo salario do funcioanrio sera {:.2f}'.format(novo))