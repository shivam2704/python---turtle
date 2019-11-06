import turtle
import math
from random import randint
import random

turtle.up()
turtle.goto(-200,-150)
turtle.down()
turtle.hideturtle()
turtle.fillcolor('#505050')
turtle.begin_fill()
for _ in range(2):
    turtle.fd(400)
    turtle.circle(100,90)
    turtle.fd(100)
    turtle.circle(100,90)
    

  
turtle.end_fill()

turtle.color('white')
turtle.penup()
turtle.speed(0)

turtle.goto(-250,-50)
turtle.write('g', font=('Monotype Corsiva',100,'italic'))
turtle.goto(-120,0)
turtle.color('#F0F0F0')
turtle.begin_fill()

turtle.circle(40)
turtle.end_fill()

turtle.color('white')
turtle.goto(-70,-50)
turtle.write('o', font=('Monotype Corsiva',100,'italic'))
turtle.goto(10,-50)
turtle.write('g', font=('Monotype Corsiva',100,'italic'))
turtle.goto(90,-50)
turtle.write('l', font=('Monotype Corsiva',100,'italic'))
turtle.goto(160,-50)
turtle.write('e', font=('Monotype Corsiva',100,'italic'))
turtle.pendown()


turtle.speed(0)

turtle.color("white")
def draw_star(size):
    count = 0
    angle = 144
    turtle.begin_fill()
    while count <= 5:
        turtle.forward(size)
        turtle.right(angle)
        count += 1
    turtle.end_fill()
    return
num_stars=0
while num_stars <200:
    x = randint(-300,300)
    y = randint(-150,250)
    draw_star(1)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    num_stars +=1
    


