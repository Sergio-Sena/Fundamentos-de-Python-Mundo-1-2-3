# Aula Dicionário
#Declarando dicionarios
from typing import KeysView


pessoas = {'nome': "Gustavo", "Idade": "29","Sexo":"M"}
# mostrar dicioanrio
print(pessoas)
# mostrar chaves
print('-=' * 30)
print(pessoas.keys())
# mostrar valores dentro do dicionário
print('-=' * 30)
print(pessoas.values())
# mostrar itens dentro do dicionário
print('-=' * 30)
print(pessoas.items())
print('-=' * 30)
for k in pessoas.keys():
    print(k)
print('-=' * 30)    
for k in pessoas.values():  
    print(k)    
print('-=' * 30)
for k,v in pessoas.items():   
    print(f'{k} = {v}')
print('-=' * 30)
del pessoas["Sexo"]
print(pessoas)
print('-=' * 30)
pessoas['nome'] = "leandro"
print(pessoas)
print('-=' * 30)
# Dicionario dentro de lista
brasil = []
estado1 = {'uf':'Rio de janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
# Cópia de dados
print("-=" * 30)
estado = dict()
brasil = list()
for c in range(0,3):
    estado['UF'] = str(input("Unidade federativa: "))
    estado['Sigla'] = str(input('Sigla do estado'))
    brasil.append(estado.copy()) 
for e in brasil:
      for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')