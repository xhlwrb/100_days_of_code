from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def t_forward():
    tim.forward(10)


def t_backward():
    tim.backward(10)


def t_clockwise():
    tim.right(15)


def t_counterclock():
    tim.left(15)


def t_clear():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
for i in range(20):
    screen.onkey(t_forward, "w")
    screen.onkey(t_backward, "s")
    screen.onkey(t_clockwise, "d")
    screen.onkey(t_counterclock, "a")
    screen.onkey(t_clear, "c")

screen.exitonclick()
