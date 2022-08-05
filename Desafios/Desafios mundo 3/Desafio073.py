#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.

lista = ( 'palmeiras','corinthians', 'Fluminense','Atlético','flamengo','Internacional','AtleticoMG','Bragantino','santos','São Paulo','Goias', 'Borafogo','AmericaMG','Ceará','Coritiba','Avai','Cuiaba','Fortaleza', 'AtleticoGo','juventude.')
print('-='*20)
print('{:-^30}'.format('Campeonato Brasileiro.'))
print('-='*20)
print('-='*30)
print(f'Os 5 primeiros colocados são {lista[0:5]}')
print(f'Os 4 Últimos colocados são {lista[-4:]}')
print('-='*30)
print('-='*30)
print(f'Times em ordem Alfabética {sorted(lista)}')