# Aula 21 Função parte 2

#Interactive help (ajuda interativa)
help(print) 
print(__doc__)
# Docstrings
def contador(i, f, p):
    """
    -> FAZ UMA COMTAGEM O MOSTRA NA TELA
    :param I Inicio da contagem
    :param F Fim da contagem
    :param P Passo da contagem
    :return Sem retorno
    """    
    c = i
    while c <= f:   
        print(f'{c} ',end ='')
        c += p
    print('FIM!')

contador(0,100,5)

help(contador)

# Parametros opcionais

def somar(a, b, c=0):
    """
    -> FAZ UMA COMTAGEM O MOSTRA NA TELA
    :param I Inicio da contagem
    :param F Fim da contagem
    :param P Passo da contagem
    :return Sem retorno
    """    
    s = a + b + c
    print(f'A soma vale {s}')
somar(3,2,5)
somar(3,2)
# Escopo de variaveis
n1 = 2
print(f'Fora n1 vale {n1}')
# Retorno valores(Return)
def somar(a,b,c):
    s = a + b + c
    return s 
resp = somar(3,2,5)
print(resp)
# Pratica de exercicio

def fatorial(num = 1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f
#programa pricipal
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados valem {f1}, {f2} e {f3}')



