# Detect when the turtle player collides with a car
# and stop the game if this happens.
# If you get stuck, check the video walkthrough in Step 5.

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.up, "Up")

car_manager = CarManager()

scoreboard = Scoreboard()

game_counter = 1

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()

    # generate a car every 6
    if game_counter == 6:
        car_manager.add_car()
        game_counter = 1
    game_counter += 1

    # detect collision with cars
    for every_car in car_manager.cars:
        if player.distance(every_car) < 20:
            game_is_on = False
            # show game over
            scoreboard.game_over()

    # reach top
    if player.reach_top():
        # level up cars
        car_manager.level_up()
        scoreboard.level_up()


screen.exitonclick()
