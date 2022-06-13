# Pintar paredes #

alt = float(input('Entre com a altura :'))
lar = float(input('Entre com a largura :'))
a = (alt*lar)
print('Sua parede de {} x {} tem uma área de {} m² e precisará de {:.2f} litros de tinta para pinta-la'.format(alt,lar,a,a/2))
