from random import randint
print('-='*30)
print('Vamos jogar par ou impar?')
print('-='*30)

v = 0
while True:
    jogador= int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você digitou {jogador} e o computador {computador}. Total {total}.')
    print('Deu Par' if total % 2 == 0 else 'Deu Impar')                                                                                     
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu.')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v+= 1
        else:
            print('Você perdeu!')
        break
print('Vamos jogar novamente....')
print(f'GAME OVER!!!!Você teve {v} vitórias.')