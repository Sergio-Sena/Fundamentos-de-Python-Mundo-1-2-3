#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('-='*25)
print('Gerador DE UMA PA')
print('-='*25)

primeiro = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer contar a mais?: '))
print('Fim')
print('Prograssão finalizada com {} termos mostrados.'.format(total))