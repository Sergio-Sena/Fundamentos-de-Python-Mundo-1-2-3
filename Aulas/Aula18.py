# Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

print("-=" *30)
# Estrutura lista dentro de listas
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = "maria"  
teste[1] = "22"
galera.append(teste[:])
print(galera)
print("-=" *30)
#Estrutura lista dentro de listas
galera = [['joão',19],['Ana',33],['joaquin',13],['Maria',45]]
print(galera)
for p in galera:
    print(f"{p[0]} tem {p[1]} anos de idade")
print("-=" *30)
#Exemplo mais completo
galera = list()
dados = list()

totmai = totmen = 0
for c in range(0,3):
    dados.append(str(input("nome: ")))
    dados.append(int(input("Idade: ")))
    galera.append(dados[:])
    dados.clear()
print(galera)
# maior de idade dentro dos dados:
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totmen += 1
print(f"Temos {totmai} maior de idade e {totmen} de menor idade .")