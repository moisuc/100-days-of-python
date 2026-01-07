from random import randint
import random
from turtle import Turtle,Screen

#A square
def draw_a_square():
    timmy_the_turle = Turtle()
    timmy_the_turle.shape('turtle')
    for _ in range(4):
        timmy_the_turle.right(90)
        timmy_the_turle.forward(100)

# DOTTED line
def draw_dotted_line():
    tim = Turtle()
    tim.shape('circle')
    tim.color('red')

    for i in range(100):
        tim.forward(5)
        if i%2 ==0:
            tim.penup()
        else:
            tim.pendown()

def draw_different_shapes():
    tim = Turtle()
    tim.shape('circle')
    tim.pensize(10)
    colors = ["indianred", "deepskyblue", "firebrick", "darkorchid", "forestgreen", 
          "gold", "mediumslateblue", "tomato", "turquoise", "salmon"]
    for i in range(3,10):
        angle = 360 / i
        tim.color(random.choice(colors))
        while True: 
            tim.right(angle)
            tim.forward(100)
            if abs(tim.pos()) < 1:
                break
def random_walk():
    tim = Turtle()
    tim.shape('arrow')
    tim.pensize(10)
    tim.speed(10)
    colors = ["indianred", "deepskyblue", "firebrick", "darkorchid", "forestgreen", 
          "gold", "mediumslateblue", "tomato", "turquoise", "salmon"]
    angles = [90,180,270,0]
    for _ in range(150):
        tim.setheading(random.choice(angles))
        tim.color(random.choice(colors))
        tim.forward(20)

def random_color():
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    random_color=(r,g,b)
    return random_color


def draw_a_spinograph():
    tim = Turtle()
    tim.shape('arrow')
    tim.speed('fastest')
    for i in range(500):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(i+10)


screen = Screen()
screen.colormode(255)

draw_a_spinograph()
screen.exitonclick()