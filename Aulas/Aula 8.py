# módulos python #
# import
# from modulo item

import math
num = int(input('Digte um número :'))
raiz = math.sqrt(num)
print('A raiz quadrada de {} aredondada para cima é igual a {}'.format(num,math.ceil(raiz)))
print('A raiz quadrada de {} aredondada para baixo é {} '.format(num,math.floor(raiz)))
