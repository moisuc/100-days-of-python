from turtle import Turtle,Screen


screen = Screen()
WIDTH = 500
HEIGHT = 400
screen.setup(width=WIDTH,height=HEIGHT)

user_bet = screen.textinput("Make your bet","Wich turtle will win the race? Choose a color: ")


tim = Turtle()

screen.exitonclick()