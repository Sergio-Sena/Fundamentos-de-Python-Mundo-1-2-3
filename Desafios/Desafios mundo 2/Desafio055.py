#Faça um programa que leia o peso de 5 pessoas e mostre qual foi o maoir e o menor peso lido

pesado = 0
leve = 0
for cont in range(1,6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(cont))
    )
    if cont == 1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso 
        if peso < leve:
            leve = peso
    
print ('Maior peso lido foi {} KG:'.format(pesado)) 
print('Menor peso lido foi:',leve)