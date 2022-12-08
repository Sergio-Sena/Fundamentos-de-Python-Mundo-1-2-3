#Calcule o Seno Coseno a Tangente de um ângulo
from math import sin,cos,tan,radians

ângulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno)) 
cosseno = cos(radians(ângulo))
print('o ângulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a tangente de {:.2f} '.format(ângulo, tangente))