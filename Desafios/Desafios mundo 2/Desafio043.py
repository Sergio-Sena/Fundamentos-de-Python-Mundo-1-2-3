#-Desenvolva um programa que leia o peso e a altura de uma pessoa e calcule seu imc e mostre seu status, de acordo com a tabela abaixo:
#-Abaixo de 18.5: Abaixo do peso.
#-Entre 18.5 e 24.9: Peso ideal.
#Entre 25 até 29.9 :sobre peso.
# Entre 30 e 39.9:Obesidade.
# Acima dos 40: Obesidade mórbida.
# peso/altura*2

cores = {'limpa':'\033[m',
'vermelho':'\033[31m'}

peso = float(input('Digite o seu peso? (kg): '))
alt = (float(input('Digite a sua altura? (m): '))) 
imc = peso / (alt**2)

#verificando faixa etária do IMC

if imc < 18.5:
    print('Seu IMC é {:.1f} e está abaixo do ideal.'.format(imc))
elif imc >= 18.5 <=imc < 25:
    print('Seu IMC é {:.1f} e esta no peso ideal. Continue assim.'.format(imc))
elif 25 <= imc <= 30:
    print('Seu IMC é {:.1f} e esta em sobrepeso. Cuidado.'.format( imc )) 
elif 30 <= imc <= 40:
    print('Seu IMC é {:.1f}, Alerta de Obesidade.'.format(imc))
else:
    print('Seu IMC é {:.1f}, ALERTA DE OBESIDADE MORBIDA, procure um médico imediatamente.'.format(imc))