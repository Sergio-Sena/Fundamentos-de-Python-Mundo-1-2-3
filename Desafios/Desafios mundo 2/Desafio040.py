#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

cores = {'limpa':'\033[m',
'branco':'\033[30m',
'vermelho':'\033[31m',
'verde':'\033[32m',
'amarelo':'\033[1;33m',
'azul':'\033[34m',
'magenta':'\033[35m',
'ciano':'\033[36m',
'cinza':'\033[37m',}

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
media = (nota1+nota2)/2

if media < 5:
    print('Estude mais sua media foi {}{}{}. Aluno Reprovado.'.format(cores['vermelho'],media,cores['limpa']))
elif media >= 5 and media <= 6.9:
    print('Aluno em recuperação. Faltou só um pouquinho. Sua media foi {}{}{}.'.format(cores['amarelo'],media,cores['limpa']))
else:
    print('Aluno aprovado. PARABÉNS pequeno gafanhoto.Sua média foi {}{}{}.'.format(cores['verde'],media,cores['limpa']))