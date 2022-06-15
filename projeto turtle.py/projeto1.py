#===================#

import turtle
ninja = turtle.Turtle()
ninja.speed(15)

for i in range (90):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.forward(50)
    ninja.left(60)
    ninja.forward(30)

    ninja.penup()
    ninja.setposition(0 , 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()



