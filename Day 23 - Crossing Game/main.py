import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, "Up")
screen.onkeypress(player.move_backward, "Down")

game_is_on = True
car_list = []
while game_is_on:
    scoreboard.display()
    # Generate car and make it move
    generate = random.randint(1, 10)
    if generate > 6:
        car = CarManager(scoreboard.level)
        car_list.append(car)

    # Move car & Check if the turtle collide with the car
    for c in car_list:
        if player.distance(c) < 35:
            game_is_on = False
            scoreboard.game_over()
            break
        c.move()

    # Check if player pass this level
    if player.ycor() > 280:
        scoreboard.level += 1
        player.reset()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
