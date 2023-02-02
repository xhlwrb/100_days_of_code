# Create a scoreboard that keeps track of which level the user is on.
# Every time the turtle player does a successful crossing,
# the level should increase. When the turtle hits a car,
# GAME OVER should be displayed in the centre. If you get stuck,
# check the video walkthrough in Step 7.
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.show_level()

    def show_level(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.show_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
