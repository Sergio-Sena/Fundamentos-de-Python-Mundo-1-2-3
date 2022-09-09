# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expr = str(input("Digite uma expressão: "))
pilha = []
for sím in expr:
    if sím == "(":
        pilha.append("(")
    elif sím == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha)== 0:
    print("A sua expressão esta correta.")
else:
    print("A sua expressçao ensta inválida")