from turtle import Turtle,Screen

t = Turtle()
t.speed('fast')
screen = Screen()
def move_forward():
    t.forward(10)

def move_backwards():
    t.backward(10)

def move_left():
    t.left(10)

def move_right():
    t.right(10)

screen.listen()
screen.onkeypress(move_forward,'w')
screen.onkeypress(move_backwards,'s')
screen.onkeypress(move_left,'a')
screen.onkeypress(move_right,'d')


screen.colormode(255)

screen.exitonclick()