# Create cars that are 20px high by 40px wide
# that are randomly generated along the y-axis
# and move to the left edge of the screen.
# No cars should be generated in the top and bottom 50px
# of the screen (think of it as a safe zone for our little turtle).
# Hint: generate a new car only every 6th time the game loop runs.
# If you get stuck, check the video walkthrough in Step 4.

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_speed = MOVE_INCREMENT

    def add_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car_x = 300
        car_y = random.randint(-250, 250)
        car.goto(car_x, car_y)
        self.cars.append(car)

    def move(self):
        for i_car in self.cars:
            new_x = i_car.xcor() - self.move_speed
            i_car.goto(new_x, i_car.ycor())

    def level_up(self):
        self.move_speed += MOVE_INCREMENT

