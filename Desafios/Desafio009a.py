# Tabuada com range #
n = int(input('Digite a tubuada que quer ver :'))
print('-'*12)
for item in range(11):
    print('{} x  {:2}  = {}'.format(n,item,n*item))
print('-'*12)    