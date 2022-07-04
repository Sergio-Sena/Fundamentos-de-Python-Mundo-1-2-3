#Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

#Aula#
frase = ('Curso em Vídeo python')
print(frase,('Imprimir na tela'))
#Fatiamento#
print(frase[3:13:],('Imprime a terceira letra da frase começando do 0 ate o 13 pulando de 2 em 2 '))
#Função Count#
print(frase.count('o'),('Conta quantos O tem dentro da frase'))
#Função Upper#
print(frase.upper(),('Coloca tudo em maiusculo'))
#Função Lower#
print(frase.lower(),('Coloca tudo em minúsculo'))
#Função Len#
print(len(frase),('Mostra a quantidade de itens na frase'))
#Função replace #
print(frase.replace('python', 'Android'),('Substitui uma palavra por outra na frase, porém não grava, sera necessario criar uma variavel para receber a substituição como feito abaixo'))
dividido = frase.split()
print(dividido[0],('Mostra a posição 0 da frase dividido'))
print(dividido[2][3],('Mostra a posição 2 letra 3 da variavel dividido'))

#Função In#
print(('Curso' in frase),('Procura palavra Curso na frase e verifica se é verdadeiro iu falso pela funcão IN'))
#Função find#
print(frase.find('Vídeo'),('procura a partir de qual posição existe a palavra Vídeo'))

#Função split#
print(frase.split(),('Retira os espaços no começo e no fim'))

