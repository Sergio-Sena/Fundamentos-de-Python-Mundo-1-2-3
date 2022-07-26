#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

#[ 1 ] somar

#[ 2 ] multiplicar

#[ 3 ] maior

#[ 4 ] novos números

#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso

# Ler números

from time import sleep

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
print('-='*30)
opcao = 0
while opcao != 5:
    print('-='*30)
    print('''
    Escolha uma das opções:
    [ 1 ] - Somar
    [ 2 ] - multiplicar
    [ 3 ] - maior
    [ 4 ] - novos números
    [ 5 ] - sair so programa''')
    print('-='*30)
    opcao = int(input('Qual é a sua escolha? : '))
    print('-='*30)
    if opcao == 1:
        soma = n1+n2
        print('A soma entre {} e {} vale {}.'.format(n1,n2,soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} vale {}.'.format(n1,n2,mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior valor é {}.'.format(n1,n2,maior))
    elif opcao == 4:
        print('Digite os números novamente.')
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente novamente.')
print('-='*30)
sleep(2)
print('Fim do programa! Volte sempre.')