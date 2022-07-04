#Faça um programa que leia o nome da cidade e verifique se o nome da cidade começa com 'santo'#

cid = str(input('Digite o nome da sua cidade: ')).strip()
print(cid[:5].lower() == 'santo')