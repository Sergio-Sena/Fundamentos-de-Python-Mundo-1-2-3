#Escreva um programa que faça um computador pensar em um  número entre 0 e 5 e peça para o usuario descobri qual foi o nuemro escolhido pelo computador. O computador deverá escrever na tela se o usuário ganhou ou perdeu! 
print('#====#'*25)
print('''#Escreva um programa que faça um computador pensar em um  número entre 0 e 5 e peça para o usuario descobri qual foi o número escolhido pelo computador.\n O computador deverá escrever na tela se o usuário ganhou ou perdeu! 
''')
print('#====#'*25)
print('Olá, Vamos fazer um pequeno joge de adivinhação. Eu vou pensar em un número e você diz qual nuemero eu pensei.\n ele será de 0 a 5. ')
n = int(input('Vamos lá digite o número que eu pensei: '))
import random
sorteado = random.randint(0,5)
if n == (sorteado):
    print('Parabens você ganhou')
else:
    print('Não foi dessa vez. Você perdeu')