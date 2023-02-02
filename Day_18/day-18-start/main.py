# from turtle import Turtle, Screen
#
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
#
#
# screen = Screen()
# screen.exitonclick()
#
# import heroes
#
# print(heroes.gen())
#
# from turtle import Turtle, Screen
#
# tim = Turtle()
#
# for i in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# screen = Screen()
# screen.exitonclick()
#
# from turtle import Turtle, Screen
# import random
#
# tim = Turtle()
# screen = Screen()
# screen.colormode(255)
#
# # draw 8 shapes, 3 to 10 edges
# for edges in range(3, 11):
#     degree = 360 / edges
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tim.pencolor(r, g, b)
#     for edge in range(edges):
#         tim.forward(50)
#         tim.right(degree)
#
#
# screen.exitonclick()
#
# from turtle import Turtle, Screen
# import random
#
# tim = Turtle()
# screen = Screen()
# screen.colormode(255)
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     angle = random.randint(0, 360)
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tim.pencolor(r, g, b)
#     tim.forward(30)
#     tim.setheading(angle)
#
#
# screen.exitonclick()

from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)

draw_spirograph(5)

screen.exitonclick()