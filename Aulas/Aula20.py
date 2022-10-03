# Funções em Python
#Rotina - (DEF)

def Lin():
    print('-='*30)

# Programa Principal
Lin()
print('Olá mundo')
Lin()
print('Curos em video')
Lin()   
print('gsutavo Guanabara')
Lin()
print('Aprenda Python')
Lin()
# Parâmetros

def titulo(txt):
    print('-='*30)
    print(txt)
    print('-='*30)

titulo('    Olá mundo   ')
titulo('    Curos em video  ')   
titulo('    Gustavo Guanabara   ')
titulo('    Aprenda Python  ')
titulo('    Python é muito bom  ')

# Parte Pratica

# Programa Principal

a = 5
b = 4
s = a+b
print(s) 

a = 8
b = 9
s = a+b
print(s)

a = 2
b = 1
s = a+b
print(s)
# Criando def para o mesmo programa
def soma(a, b):
    s = a+b
    print(s)

Lin()
soma(4,5)
soma(8,9)
soma(2,1)

# Empacotamento
def contador(*num):
    print(num)
    print()
Lin()
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
Lin()
def dobra(lst):
    pos=0
    while pos < len(lst):
        lst[pos] *= 2
        pos+=1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
Lin()
 