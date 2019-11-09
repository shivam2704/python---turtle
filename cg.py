import turtle
import math
from random import randint
import time
import random


turtle.up()
turtle.goto(-200,-150)
turtle.down()

turtle.fillcolor('#505050')
turtle.begin_fill()
for _ in range(2):
    turtle.fd(400)
    turtle.circle(100,90)
    turtle.fd(100)
    turtle.circle(100,90)
    
turtle.end_fill()

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
    
def stars():
    num_stars=0
    while num_stars <20:
        x = randint(-300,300)
        y = randint(-150,250)
        draw_star(1)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        num_stars +=1


stars()

turtle.color('white')
turtle.penup()
turtle.speed(0)

turtle.goto(-250,-50)
turtle.write('g', font=('Monotype Corsiva',100,'italic'))
turtle.goto(-120,0)
turtle.color('#F0F0F0')
turtle.begin_fill()
time.sleep(0)
turtle.speed(1)
turtle.circle(40)
turtle.end_fill()



turtle.color("white")
turtle.speed(2)


turtle.speed(1)
turtle.goto(10,-50)
turtle.write('g', font=('Monotype Corsiva',100,'italic'))
turtle.goto(90,-50)
turtle.write('l', font=('Monotype Corsiva',100,'italic'))
turtle.goto(160,-50)
turtle.write('e', font=('Monotype Corsiva',100,'italic'))
turtle.goto(-40,-20)
screen = turtle.Screen()
screen.addshape("copy1.gif")
turtle.shape("copy1.gif")

turtle.pendown()


turtlepower = []
turtle.tracer(0,0)
for i in range (1):
    t=turtle.Turtle()
    t.goto(random.random()*1, random.random()*1)
    turtlepower.append(t)


num_stars=0
while num_stars <80:
        x = randint(-300,300)
        y = randint(-150,250)
        draw_star(1)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        num_stars +=1
        
turtle.penup()
turtle.pendown()

