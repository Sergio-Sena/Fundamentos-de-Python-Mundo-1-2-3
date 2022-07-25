# Crie um program que converta a medida digitada em centimetros e milímetros

m = float(input('Entre com a metragem a converter :'))
print('{} metros convertidos em centimetos vale {:.0f} centimetros\n e convertidos em mm vale {:.0f} milímetros '.format(m,100*m,1000*m))