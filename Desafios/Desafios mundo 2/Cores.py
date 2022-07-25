from distutils import core


cores = {'limpa':'\033[m',
'branco':'\033[30m',
'vermelho':'\033[31m',
'verde':'\033[32m',
'amarelo':'\033[1;33m',
'azul':'\033[34m',
'magenta':'\033[35m',
'ciano':'\033[36m',
'cinza':'\033[37m',}
print(cores['vermelho'],'cores',cores['verde'],'cores',cores['amarelo'],'cores',cores['azul'],'cores',cores['magenta'],'cores',cores['ciano'],'cores', cores['cinza'],'cores')
print('codigo padrão ANSI (\033[m)->codigo scape (0;33;44m)-> Style;cor de fonte,backgound\n -> Códigos mais usados de Style\n ->0-Nenhum\n ->1-BOLD\n ->4-UNDERLINE\n ->7-Negative ')
print('=+='*25)
print('# codigos mais usados Texto\n #30-branco\n #31-vermelho\n #32-verde\n #33-amarelo\n #34-azul\n #35-magenta\n #36-ciano\n #37-cinza')
print('=+='*25)
print('# codigos mais usados Backgroud\n #40-branco\n #41-vermelho\n #42-verde\n #43-amarelo\n #44-azul\n #45-magenta\n #46-ciano\n #47-cinza')
print('=+='*25)




