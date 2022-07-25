# Conversor de temperatura
from re import M


temperatura = float(input('Digite a temperatura C°:'))
print('A temperatura {:.0f} C° corresponde a {:.0f} F°'.format(temperatura,(temperatura*9/5+32)))
