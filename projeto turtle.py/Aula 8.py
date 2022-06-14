# módulos python #
# import
# from modulo item

import math

import emoji
num = int(input('Digte um número :'))
raiz = math.sqrt(num)
print('A raiz quadrada de {} aredondada para cima é igual a {}'.format(num,math.ceil(raiz)))
print('A raiz quadrada de {} aredondada para baixo é {} '.format(num,math.floor(raiz)))
# import modulo randon #
import random
num = random.randint(1, 10)
print(num)
#===================#

import turtle
ninja = turtle.Turtle()
ninja.speed(500)

for i in range (180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.forward(30)

    ninja.penup()
    ninja.setposition(0 , 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()