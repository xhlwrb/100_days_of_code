from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800, 600)
screen.tracer(0)

scoreboard = Scoreboard()

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)

screen.listen()


screen.onkey(r_paddle.go_up,  "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor()< -320:
        ball.bounce_x()

    # miss r
    if ball.xcor() > 380:
        # reset the ball
        ball.reset_position()
        scoreboard.l_point()

    # miss l
    if ball.xcor() < -380:
        # reset the ball
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()
