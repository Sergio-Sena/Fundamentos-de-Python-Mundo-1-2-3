# Media de aluno #
cores = {'limpa':'\033[m',
'azul':'\033[34m',
'ciano':'\033[36m',
'media':'0;33;45'}

nome = input('Digite o nome do aluno :')
n1 = float(input('Digite a primeira nota :'))
n2 = float(input('Digite a segunda nota :'))
print('A média do aluno {}{}{} foi {:.1f}'.format(cores['ciano'],nome,cores['limpa'], (n1+n2)/2))