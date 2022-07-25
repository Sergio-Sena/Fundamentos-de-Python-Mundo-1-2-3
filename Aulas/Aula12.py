#condições aninhadas
# IF,ELIF,ELSE
nome = str(input('Qual e seu nome:? '))
nome =nome.lower()
if nome == ('sergio'):
    print('Que lindo nome vc tem {}.'.format(nome))
elif nome =="paulo" or nome == 'pedro' or nome == 'maria':
    print('Seu nome é bem popular no brasil {}.'.format(nome))
elif nome in 'Ana Claudia Juliana jéssica':
    print('Belo nome feminino.'.format(nome))
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}.'.format(nome))

