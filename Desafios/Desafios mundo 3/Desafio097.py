# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  Ex:                                                                                                                 escreva(‘Olá, Mundo!’) 
# Saída:                                                                                                              ~~~~~~~~~                                                                                                           Olá, Mundo!                                                                                                              ~~~~~~~~~                    


def escreva(msg) :
    tam = len(msg)+2
    print('~'*tam )
    print(f' {msg}')
    print('~'*tam )
while True:
    escreva(str(input('digite a frase: ')))
    resp =(str(input('Quer continuar?[S/N]? '))).upper().strip()
    if resp in 'Nn':
        break 
print('<<< O programa foi Finalizado volte sempre..>>>')