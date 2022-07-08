#Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.


print('codigo padrão ANSI (\033[m)->codigo scape (0;33;44m)-> Style;cor de fonte,backgound\n -> Códigos mais usados de Style\n ->0-Nenhum\n ->1-BOLD\n ->4-UNDERLINE\n ->7-Negative')
print('=+='*25)
print('# codigos mais usados Texto\n #30-branco\n #31-vermelho\n #32-verde\n #33-amarelo\n #34-azul\n #35-magenta\n #36-ciano\n #37-cinza')
print('=+='*25)
print('# codigos mais usados Backgroud\n #40-branco\n #41-vermelho\n #42-verde\n #43-amarelo\n #44-azul\n #45-magenta\n #46-ciano\n #47-cinza')
print('=+='*25)
print('\033[4;34m Ola mundo\033[m') 
#Método cores
nome = 'Sérgio'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[4;33m',
        'pretoebranco':'\033[7;30m'}
print('Olá muito prazer em te conhecer,{}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))