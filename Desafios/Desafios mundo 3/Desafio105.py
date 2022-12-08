# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma 
# – A situação (opcional)

#programa principal

def notas(*n, sit=False):
    """
    paran n (uma ou mais notas aceita varias) 
    paran sit (valor opcional indica se deve ou não adicionar a situação)
    return (dicionario com varias informações fa turma)
   
    """
    
    r =dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] > 7:
            r['situação'] = "BOA"
        elif r['media'] >= 5:
            r['situação'] = "regular"
        else:
            r['situação'] = "RUIM"


    return r

resp = notas(5.2,8.5,9, sit=True)

print(resp)
help(notas)